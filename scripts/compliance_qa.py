#!/usr/bin/env python3
"""Fail-closed repository QA for the GRC Practical Manuals collection.

The checks intentionally validate project-owned structure, metadata, evidence, and
workflow safety. They do not claim that passing CI establishes legal compliance,
certification, or audit assurance.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / ".compliance" / "manual-catalog.json"
SOURCES_PATH = REPO_ROOT / ".compliance" / "authoritative-sources.json"
ALLOWED_SOURCE_DOMAINS = {
    "airc.nist.gov",
    "csrc.nist.gov",
    "digital-strategy.ec.europa.eu",
    "eur-lex.europa.eu",
    "hhs.gov",
    "nvlpubs.nist.gov",
    "www.hhs.gov",
    "www.iso.org",
    "www.nist.gov",
}
ALLOWED_SOURCE_STATUSES = {
    "final",
    "final-under-revision",
    "official-guidance-non-binding",
    "proposed-not-current-law",
    "under-development",
    "voluntary-code-non-binding",
}
PUBLISHED_FORMATS = (".md", ".docx", ".pdf")


@dataclass
class CheckResult:
    name: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    details: dict[str, object] = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return not self.errors

    def emit(self) -> None:
        state = "PASS" if self.passed else "FAIL"
        print(f"[{state}] {self.name}")
        for warning in self.warnings:
            print(f"  WARNING: {warning}")
        for error in self.errors:
            print(f"  ERROR: {error}")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"required file is missing: {path.relative_to(REPO_ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}") from exc


def is_relative_repo_path(value: str) -> bool:
    path = Path(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def check_catalog() -> CheckResult:
    result = CheckResult("manual catalog")
    try:
        catalog = load_json(CATALOG_PATH)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result

    if catalog.get("schema_version") != "1.0":
        result.errors.append("schema_version must be 1.0")
    if catalog.get("languages") != ["en", "es-419", "pt-BR"]:
        result.errors.append("languages must be exactly en, es-419, and pt-BR")

    manuals = catalog.get("manuals")
    if not isinstance(manuals, list) or not manuals:
        result.errors.append("manuals must be a non-empty list")
        return result

    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    allowed_statuses = {"published", "development", "planned", "retired"}
    allowed_layouts = {"standard", "language-directories", "controlled-build", "toolkit"}
    for index, manual in enumerate(manuals):
        label = f"manuals[{index}]"
        if not isinstance(manual, dict):
            result.errors.append(f"{label} must be an object")
            continue
        manual_id = manual.get("id")
        path = manual.get("path")
        if not isinstance(manual_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", manual_id):
            result.errors.append(f"{label}.id must be lowercase kebab-case")
        elif manual_id in seen_ids:
            result.errors.append(f"duplicate manual id: {manual_id}")
        else:
            seen_ids.add(manual_id)
        if not isinstance(path, str) or not is_relative_repo_path(path):
            result.errors.append(f"{label}.path must be a safe repository-relative path")
        elif path in seen_paths:
            result.errors.append(f"duplicate manual path: {path}")
        else:
            seen_paths.add(path)
        if manual.get("status") not in allowed_statuses:
            result.errors.append(f"{label}.status is invalid")
        if manual.get("layout") not in allowed_layouts:
            result.errors.append(f"{label}.layout is invalid")
        if not isinstance(manual.get("title"), str) or not manual["title"].strip():
            result.errors.append(f"{label}.title is required")

    result.details = {
        "manual_count": len(manuals),
        "published_count": sum(m.get("status") == "published" for m in manuals if isinstance(m, dict)),
        "planned_count": sum(m.get("status") == "planned" for m in manuals if isinstance(m, dict)),
    }
    return result


def files_with_extensions(directory: Path, extensions: Iterable[str]) -> dict[str, list[Path]]:
    return {
        extension: sorted(path for path in directory.rglob(f"*{extension}") if path.is_file())
        for extension in extensions
    }


def check_structure() -> CheckResult:
    result = CheckResult("manual structure")
    required_root = ["README.md", "LICENSE", ".zenodo.json"]
    required_sections = [
        "01-foundations",
        "02-management-systems",
        "03-assurance-and-audit",
        "04-regulatory-compliance",
        "05-operational-resilience",
        "06-cloud-and-technology-risk",
        "07-third-party-risk",
        "08-templates-and-tools",
    ]
    for relative in required_root:
        if not (REPO_ROOT / relative).is_file():
            result.errors.append(f"missing required root file: {relative}")
    for relative in required_sections:
        section = REPO_ROOT / relative
        if not section.is_dir():
            result.errors.append(f"missing required section: {relative}")
        elif not (section / "README.md").is_file():
            result.errors.append(f"missing section README: {relative}/README.md")

    try:
        catalog = load_json(CATALOG_PATH)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result

    checked = 0
    for manual in catalog.get("manuals", []):
        if manual.get("status") not in {"published", "development"}:
            continue
        relative = manual.get("path", "")
        directory = REPO_ROOT / relative
        checked += 1
        if not directory.is_dir():
            result.errors.append(f"cataloged {manual['status']} path is missing: {relative}")
            continue
        if not (directory / "README.md").is_file():
            result.errors.append(f"missing manual README: {relative}/README.md")
        if manual.get("status") != "published":
            continue
        artifacts = files_with_extensions(directory, PUBLISHED_FORMATS)
        for extension, matches in artifacts.items():
            if not matches:
                result.errors.append(f"published manual lacks {extension} artifact: {relative}")
        if not any(path.name.startswith("English_Source_") for path in artifacts[".md"]):
            english_dir = directory / "English"
            if not english_dir.is_dir() or not list(english_dir.glob("*.md")):
                result.errors.append(f"published manual lacks an identifiable English source: {relative}")

    result.details = {"active_manual_paths_checked": checked}
    return result


def require_language_artifacts(result: CheckResult, directory: Path, label: str) -> None:
    if not directory.is_dir():
        result.errors.append(f"missing {label} directory: {directory.relative_to(REPO_ROOT)}")
        return
    for extension in PUBLISHED_FORMATS:
        if not any(path.is_file() for path in directory.rglob(f"*{extension}")):
            result.errors.append(
                f"{label} package lacks {extension}: {directory.relative_to(REPO_ROOT)}"
            )


def check_translations() -> CheckResult:
    result = CheckResult("trilingual publication parity")
    try:
        catalog = load_json(CATALOG_PATH)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result

    checked = 0
    for manual in catalog.get("manuals", []):
        if manual.get("status") != "published":
            continue
        directory = REPO_ROOT / manual["path"]
        layout = manual.get("layout")
        checked += 1
        if layout == "standard":
            require_language_artifacts(result, directory, "English/root")
            require_language_artifacts(result, directory / "Espanol", "es-419")
            require_language_artifacts(result, directory / "Portugues_BR", "pt-BR")
        elif layout == "language-directories":
            require_language_artifacts(result, directory / "English", "English")
            require_language_artifacts(result, directory / "Espanol", "es-419")
            require_language_artifacts(result, directory / "Portugues_BR", "pt-BR")
        else:
            result.errors.append(
                f"published manual uses a non-publication layout: {manual['id']} ({layout})"
            )

    result.details = {"published_manuals_checked": checked}
    return result


def check_sources(network: bool = False) -> CheckResult:
    result = CheckResult("authoritative source registry")
    try:
        registry = load_json(SOURCES_PATH)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result

    sources = registry.get("sources")
    if registry.get("schema_version") != "1.0":
        result.errors.append("source registry schema_version must be 1.0")
    if not isinstance(sources, list) or not sources:
        result.errors.append("sources must be a non-empty list")
        return result

    seen: set[str] = set()
    today = dt.date.today()
    live_checked = 0
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            result.errors.append(f"{label} must be an object")
            continue
        required = {
            "id",
            "family",
            "title",
            "version",
            "status",
            "url",
            "last_verified",
            "review_interval_days",
        }
        missing = sorted(required - source.keys())
        if missing:
            result.errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue
        source_id = source["id"]
        if source_id in seen:
            result.errors.append(f"duplicate source id: {source_id}")
        seen.add(source_id)
        if source["status"] not in ALLOWED_SOURCE_STATUSES:
            result.errors.append(f"invalid source status for {source_id}: {source['status']}")
        parsed = urlparse(source["url"])
        if parsed.scheme != "https" or parsed.hostname not in ALLOWED_SOURCE_DOMAINS:
            result.errors.append(f"source is not on an approved authoritative domain: {source_id}")
        try:
            verified = dt.date.fromisoformat(source["last_verified"])
            interval = int(source["review_interval_days"])
            if interval < 1 or interval > 365:
                raise ValueError
            due = verified + dt.timedelta(days=interval)
            if today > due:
                result.errors.append(
                    f"source review is overdue: {source_id} (due {due.isoformat()})"
                )
        except (TypeError, ValueError):
            result.errors.append(f"invalid review date or interval for {source_id}")

        if network and parsed.scheme == "https" and parsed.hostname in ALLOWED_SOURCE_DOMAINS:
            request = urllib.request.Request(
                source["url"],
                headers={"User-Agent": "GRC-Practical-Manuals-source-watch/1.0"},
                method="GET",
            )
            try:
                with urllib.request.urlopen(request, timeout=20) as response:
                    if not 200 <= response.status < 400:
                        result.warnings.append(f"unexpected HTTP {response.status}: {source_id}")
                    response.read(512)
                live_checked += 1
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                result.warnings.append(f"live check unavailable for {source_id}: {exc}")

    result.details = {"source_count": len(sources), "live_checked": live_checked}
    return result


CROSSWALK_REQUIREMENTS = {
    "Control_Mapping_Register.csv": {
        "Mapping_ID",
        "Source_Framework",
        "Source_Requirement_ID",
        "Target_Framework",
        "Target_Requirement_ID",
        "Relationship_Type",
        "Coverage_Rationale",
        "Source_URL_or_Repository",
    },
    "Gap_Overlap_and_Conflict_Register.csv": {
        "Analysis_ID",
        "Record_Type",
        "Description",
        "Risk_or_Impact",
        "Owner",
        "Status",
    },
    "Mapping_Review_Checklist.csv": {
        "Review_ID",
        "Mapping_ID",
        "Reviewer",
        "No_Unsupported_Compliance_Claim",
        "Decision",
    },
    "Requirement_Decomposition_Worksheet.csv": {
        "Decomposition_ID",
        "Source_Framework",
        "Source_Requirement_ID",
        "Official_Source_Location",
        "Normalized_Control_Objective",
        "Review_Status",
    },
}


def check_crosswalks() -> CheckResult:
    result = CheckResult("control mapping and crosswalk data")
    tools_dir = (
        REPO_ROOT
        / "08-templates-and-tools"
        / "Control_Mapping_and_Crosswalk"
        / "tools"
    )
    checked_rows = 0
    for filename, required_headers in CROSSWALK_REQUIREMENTS.items():
        path = tools_dir / filename
        if not path.is_file():
            result.errors.append(f"missing crosswalk tool: {path.relative_to(REPO_ROOT)}")
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = reader.fieldnames or []
            if len(headers) != len(set(headers)):
                result.errors.append(f"duplicate CSV headers: {filename}")
            missing = sorted(required_headers - set(headers))
            if missing:
                result.errors.append(f"{filename} missing headers: {', '.join(missing)}")
            first_header = headers[0] if headers else None
            seen_ids: set[str] = set()
            for row_number, row in enumerate(reader, start=2):
                checked_rows += 1
                record_id = (row.get(first_header, "") if first_header else "").strip()
                if not record_id:
                    result.errors.append(f"{filename}:{row_number} has no record identifier")
                elif record_id in seen_ids:
                    result.errors.append(f"{filename}:{row_number} duplicates id {record_id}")
                seen_ids.add(record_id)
                if any(value is None for value in row.values()):
                    result.errors.append(f"{filename}:{row_number} has more values than headers")

    result.details = {"csv_templates_checked": len(CROSSWALK_REQUIREMENTS), "data_rows_checked": checked_rows}
    return result


def check_workflow_security() -> CheckResult:
    result = CheckResult("GitHub Actions workflow security")
    workflow_dir = REPO_ROOT / ".github" / "workflows"
    workflows = sorted(list(workflow_dir.glob("*.yml")) + list(workflow_dir.glob("*.yaml")))
    if not workflows:
        result.errors.append("no GitHub Actions workflows were found")
        return result

    uses_pattern = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
    immutable_action = re.compile(r"^[^@]+@[0-9a-f]{40}$")
    for path in workflows:
        relative = path.relative_to(REPO_ROOT)
        text = path.read_text(encoding="utf-8")
        if "pull_request_target:" in text:
            result.errors.append(f"unsafe pull_request_target trigger: {relative}")
        if re.search(r"permissions:\s*write-all", text):
            result.errors.append(f"write-all permissions are forbidden: {relative}")
        if re.search(r"contents:\s*write", text):
            result.errors.append(f"contents: write is forbidden in QA workflows: {relative}")
        if not re.search(r"^permissions:\s*\n\s+contents:\s*read\s*$", text, re.MULTILINE):
            result.errors.append(f"workflow must declare top-level contents: read: {relative}")
        if re.search(r"\bgit\s+push\b", text, re.IGNORECASE):
            result.errors.append(f"workflow must not push repository changes: {relative}")
        if re.search(r"\b(curl|wget)\b[^\n|]*\|\s*(ba)?sh\b", text, re.IGNORECASE):
            result.errors.append(f"piped remote shell execution is forbidden: {relative}")
        for action in uses_pattern.findall(text):
            if action.startswith("./") or action.startswith("docker://"):
                continue
            if not immutable_action.fullmatch(action):
                result.errors.append(f"action is not pinned to a full commit SHA in {relative}: {action}")

    result.details = {"workflow_count": len(workflows)}
    return result


def check_zenodo() -> CheckResult:
    result = CheckResult("Zenodo release metadata")
    path = REPO_ROOT / ".zenodo.json"
    try:
        metadata = load_json(path)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result
    required = {"creators", "title", "access_right", "upload_type", "license", "description"}
    missing = sorted(required - metadata.keys())
    if missing:
        result.errors.append(f".zenodo.json missing fields: {', '.join(missing)}")
    creators = metadata.get("creators")
    if not isinstance(creators, list) or not creators or not all(c.get("name") for c in creators if isinstance(c, dict)):
        result.errors.append(".zenodo.json must contain at least one named human creator")
    if metadata.get("license") != "cc-by-nc-sa-4.0":
        result.errors.append("Zenodo license must remain cc-by-nc-sa-4.0")
    return result


def write_release_report(results: list[CheckResult], output: Path) -> None:
    artifacts: list[dict[str, object]] = []
    for catalog_entry in load_json(CATALOG_PATH).get("manuals", []):
        if catalog_entry.get("status") != "published":
            continue
        directory = REPO_ROOT / catalog_entry["path"]
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.suffix.lower() in PUBLISHED_FORMATS:
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                artifacts.append(
                    {
                        "path": path.relative_to(REPO_ROOT).as_posix(),
                        "bytes": path.stat().st_size,
                        "sha256": digest,
                    }
                )
    report = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "overall_pass": all(item.passed for item in results),
        "checks": [
            {
                "name": item.name,
                "passed": item.passed,
                "errors": item.errors,
                "warnings": item.warnings,
                "details": item.details,
            }
            for item in results
        ],
        "published_artifacts": artifacts,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_results(results: list[CheckResult], output: Path | None = None) -> int:
    for result in results:
        result.emit()
    if output is not None:
        write_release_report(results, output)
        print(f"Release QA report written to {output}")
    return 0 if all(result.passed for result in results) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("catalog", "structure", "translations", "crosswalks", "workflow-security"):
        subparsers.add_parser(name)
    sources = subparsers.add_parser("sources")
    sources.add_argument("--network", action="store_true", help="also test live authoritative URLs")
    release = subparsers.add_parser("release")
    release.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    commands = {
        "catalog": [check_catalog],
        "structure": [check_structure],
        "translations": [check_translations],
        "crosswalks": [check_crosswalks],
        "workflow-security": [check_workflow_security],
    }
    if args.command == "sources":
        return run_results([check_sources(network=args.network)])
    if args.command == "release":
        checks = [
            check_catalog(),
            check_structure(),
            check_sources(network=False),
            check_translations(),
            check_crosswalks(),
            check_workflow_security(),
            check_zenodo(),
        ]
        return run_results(checks, output=args.output)
    return run_results([function() for function in commands[args.command]])


if __name__ == "__main__":
    sys.exit(main())
