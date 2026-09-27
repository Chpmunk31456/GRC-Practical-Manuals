#!/usr/bin/env python3
"""End-to-end integrity gate for Manual 03.

Validates controlled sources, multilingual parity signals, generated DOCX/PDF
artifacts, publication-report hashes, and release-control records. The gate is
diagnostic only: it never rewrites source or generated artifacts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLICY = ROOT / "config" / "manual03_e2e_policy.json"
WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_policy(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_sources(manual_root: Path, patterns: list[str]) -> list[Path]:
    found: set[Path] = set()
    for pattern in patterns:
        found.update(path for path in manual_root.glob(pattern) if path.is_file())
    return sorted(found)


def combined_text(paths: list[Path]) -> str:
    return "\n\n".join(path.read_text(encoding="utf-8", errors="replace") for path in paths)


def chapter_numbers(text: str, pattern: str) -> list[int]:
    return sorted({int(value) for value in re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)})


def check_docx(path: Path) -> tuple[bool, str]:
    try:
        with zipfile.ZipFile(path) as archive:
            required = {"[Content_Types].xml", "word/document.xml"}
            names = set(archive.namelist())
            missing = sorted(required - names)
            if missing:
                return False, f"missing DOCX members: {', '.join(missing)}"
            root = ET.fromstring(archive.read("word/document.xml"))
            paragraphs = sum(1 for _ in root.iter(WORD_NS + "p"))
            if paragraphs == 0:
                return False, "DOCX contains no Word paragraphs"
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        return False, f"invalid DOCX: {exc}"
    return True, "valid DOCX package"


def check_pdf(path: Path) -> tuple[bool, str]:
    with path.open("rb") as handle:
        prefix = handle.read(8)
    if not prefix.startswith(b"%PDF-"):
        return False, "missing PDF file signature"
    if path.stat().st_size < 1024:
        return False, "PDF is implausibly small"
    return True, "valid PDF signature"


def report_hashes(report: dict, manual_root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for edition in report.get("editions", {}).values():
        artifacts = edition.get("artifacts", {})
        for kind in ("docx", "pdf"):
            item = artifacts.get(kind, {})
            name = item.get("file")
            digest = item.get("sha256")
            if name and digest:
                result[(manual_root / "publication" / name).as_posix()] = digest.lower()
    return result


def parse_checksum_manifest(path: Path, manual_root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^([0-9a-fA-F]{64})\s+[* ]?(.+)$", line)
        if not match:
            continue
        digest, name = match.groups()
        candidate = Path(name)
        if not candidate.is_absolute():
            candidate = manual_root / "publication" / candidate.name
        result[candidate.as_posix()] = digest.lower()
    return result


def run(policy: dict) -> dict:
    manual_root = ROOT / policy["manual_root"]
    failures: list[str] = []
    warnings: list[str] = []
    evidence: dict = {"languages": {}, "artifacts": {}}

    expected_chapters = int(policy["expected_chapters"])
    expected_numbers = list(range(1, expected_chapters + 1))

    for locale, cfg in policy["languages"].items():
        sources = collect_sources(manual_root, cfg["source_globs"])
        if not sources:
            failures.append(f"{locale}: no controlled source files found")
            continue
        text = combined_text(sources)
        numbers = chapter_numbers(text, cfg["chapter_heading_pattern"])
        if numbers != expected_numbers:
            failures.append(
                f"{locale}: chapter inventory mismatch; expected 1-{expected_chapters}, got {numbers}"
            )
        missing_terms = [term for term in cfg["required_terms"] if term.lower() not in text.lower()]
        if missing_terms:
            failures.append(f"{locale}: missing controlled terms: {', '.join(missing_terms)}")
        evidence["languages"][locale] = {
            "source_files": [path.relative_to(ROOT).as_posix() for path in sources],
            "chapter_count": len(numbers),
            "chapters": numbers,
            "required_terms_present": not missing_terms,
        }

    translation_review = manual_root / policy["translation_review"]
    if not translation_review.is_file():
        failures.append("controlled translation review record is missing")
    else:
        review_text = translation_review.read_text(encoding="utf-8", errors="replace")
        if policy["maintenance"].get("require_translation_review_pass") and "PASS AFTER REMEDIATION" not in review_text:
            failures.append("controlled translation review does not record PASS AFTER REMEDIATION")

    publication_readme = manual_root / policy["publication_readme"]
    if not publication_readme.is_file():
        failures.append("publication README is missing")
    elif policy["maintenance"].get("require_fail_closed_publication_language"):
        readme_text = publication_readme.read_text(encoding="utf-8", errors="replace").lower()
        if "fail-closed" not in readme_text and "fail closed" not in readme_text:
            failures.append("publication README does not preserve fail-closed release language")

    report_path = manual_root / policy["publication_report"]
    if not report_path.is_file():
        failures.append("publication report is missing")
        report = {}
    else:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        editions = report.get("editions", {})
        for locale in policy["languages"]:
            if locale not in editions:
                failures.append(f"publication report missing edition: {locale}")
            elif int(editions[locale].get("chapter_count", -1)) != expected_chapters:
                failures.append(f"publication report chapter count mismatch for {locale}")

    expected_report_hashes = report_hashes(report, manual_root)
    checksum_path = manual_root / policy["checksum_manifest"]
    checksum_hashes = parse_checksum_manifest(checksum_path, manual_root) if checksum_path.is_file() else {}
    if not checksum_path.is_file():
        failures.append("publication checksum manifest is missing")

    for locale, relative_paths in policy["required_publication_artifacts"].items():
        evidence["artifacts"][locale] = []
        for relative in relative_paths:
            path = manual_root / relative
            record = {"path": path.relative_to(ROOT).as_posix()}
            if not path.is_file():
                failures.append(f"{locale}: missing publication artifact {relative}")
                record["status"] = "missing"
                evidence["artifacts"][locale].append(record)
                continue

            digest = sha256(path)
            record["sha256"] = digest
            record["bytes"] = path.stat().st_size

            report_digest = expected_report_hashes.get(path.as_posix())
            if policy["maintenance"].get("require_report_hash_match"):
                if not report_digest:
                    failures.append(f"{locale}: no publication-report hash for {path.name}")
                elif report_digest != digest:
                    failures.append(f"{locale}: publication-report hash mismatch for {path.name}")

            manifest_digest = checksum_hashes.get(path.as_posix())
            if manifest_digest and manifest_digest != digest:
                failures.append(f"{locale}: checksum manifest mismatch for {path.name}")
            elif checksum_hashes and not manifest_digest:
                warnings.append(f"{locale}: artifact absent from checksum manifest: {path.name}")

            if path.suffix.lower() == ".docx" and policy["maintenance"].get("require_docx_integrity"):
                ok, detail = check_docx(path)
                if not ok:
                    failures.append(f"{locale}: {path.name}: {detail}")
                record["container_check"] = detail
            if path.suffix.lower() == ".pdf" and policy["maintenance"].get("require_pdf_signature"):
                ok, detail = check_pdf(path)
                if not ok:
                    failures.append(f"{locale}: {path.name}: {detail}")
                record["container_check"] = detail

            record["status"] = "pass"
            evidence["artifacts"][locale].append(record)

    source_chapter_counts = {
        locale: data["chapter_count"] for locale, data in evidence["languages"].items()
    }
    if source_chapter_counts and len(set(source_chapter_counts.values())) != 1:
        failures.append(f"multilingual chapter-count parity failure: {source_chapter_counts}")

    return {
        "schema_version": 1,
        "manual": policy["manual_root"],
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "warnings": warnings,
        "evidence": evidence,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", default=str(DEFAULT_POLICY))
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--output")
    args = parser.parse_args()

    try:
        result = run(load_policy(Path(args.policy)))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"Manual 03 E2E gate error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    else:
        lines = [f"Manual 03 end-to-end validation: {result['status']}"]
        for item in result["failures"]:
            lines.append(f"ERROR: {item}")
        for item in result["warnings"]:
            lines.append(f"WARN: {item}")
        rendered = "\n".join(lines) + "\n"

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
