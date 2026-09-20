#!/usr/bin/env python3
"""Multilingual, local-first writing QA for controlled professional documents.

The checker is intentionally diagnostic. It never rewrites source files.
LanguageTool is local-only unless --allow-remote is explicitly supplied.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLICY = ROOT / "config" / "document_writing_policy.json"
WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def load_policy(path: Path = DEFAULT_POLICY) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def is_local_endpoint(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host in {"127.0.0.1", "localhost", "::1"}


def normalized_repo_path(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        rel = path
    return "/" + rel.as_posix().lower().lstrip("/")


def is_supported(path: Path, policy: dict) -> bool:
    return path.suffix.lower() in set(policy["supported_source_extensions"])


def is_excluded(path: Path, policy: dict, include_generated: bool = False) -> bool:
    norm = normalized_repo_path(path)
    for marker in policy["repository_scan"].get("exclude_path_parts", []):
        if marker.lower() in norm:
            return True
    if not include_generated:
        for marker in policy["repository_scan"].get("generated_path_markers", []):
            if marker.lower() in norm:
                return True
    return False


def read_text_for_detection(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        blocks = extract_docx_blocks(path)
        return "\n".join(block["text"] for block in blocks[:50])
    return path.read_text(encoding="utf-8", errors="replace")


def detect_language(path: Path, text: str, policy: dict) -> str:
    norm = normalized_repo_path(path)

    markers = policy.get("mixed_language_markers", [])
    if len(markers) >= 2 and sum(1 for marker in markers if marker in text) >= 2:
        return "mixed"

    lower_text = text[:5000].lower()
    if "controlled language:** english" in lower_text or "controlled language: english" in lower_text:
        return "en-US"

    for language, config in policy["languages"].items():
        for marker in config.get("path_markers", []):
            if marker.lower() in norm:
                return language

    return policy["default_language"]


def clean_markup_line(line: str) -> str:
    value = line.strip()
    value = re.sub(r"^#{1,6}\s+", "", value)
    value = re.sub(r"^>\s*", "", value)
    value = re.sub(r"^(?:[-*+] |\d+[.)]\s+)", "", value)
    value = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"`[^`]+`", " ", value)
    value = value.replace("**", "").replace("__", "")
    value = re.sub(r"(?<!\*)\*(?!\*)", "", value)
    value = re.sub(r"<https?://[^>]+>", " ", value)
    value = re.sub(r"https?://\S+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def extract_markdown_blocks(text: str) -> list[dict]:
    blocks: list[dict] = []
    current: list[str] = []
    start_line = 1
    in_fence = False

    def flush() -> None:
        nonlocal current, start_line
        if current:
            cleaned = " ".join(item for item in current if item).strip()
            if cleaned:
                blocks.append({"text": cleaned, "location": f"line {start_line}", "line": start_line})
        current = []

    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if not stripped:
            flush()
            continue

        if stripped.startswith("<!--") or stripped.startswith("-->"):
            flush()
            continue

        if stripped.startswith("|"):
            flush()
            continue

        if re.fullmatch(r"[:|\- ]{3,}", stripped):
            flush()
            continue

        cleaned = clean_markup_line(raw)
        if not cleaned:
            flush()
            continue

        if not current:
            start_line = number
        current.append(cleaned)

    flush()
    return blocks


def extract_plain_blocks(text: str) -> list[dict]:
    blocks: list[dict] = []
    current: list[str] = []
    start_line = 1

    def flush() -> None:
        nonlocal current, start_line
        if current:
            value = " ".join(current).strip()
            if value:
                blocks.append({"text": value, "location": f"line {start_line}", "line": start_line})
        current = []

    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            flush()
            continue
        if stripped.startswith(".. "):
            flush()
            continue
        if not current:
            start_line = number
        current.append(stripped)
    flush()
    return blocks


def extract_docx_blocks(path: Path) -> list[dict]:
    blocks: list[dict] = []
    with zipfile.ZipFile(path) as archive:
        raw = archive.read("word/document.xml")
    root = ET.fromstring(raw)
    number = 0
    for paragraph in root.iter(WORD_NS + "p"):
        text = "".join(node.text or "" for node in paragraph.iter(WORD_NS + "t")).strip()
        if text:
            number += 1
            blocks.append({"text": text, "location": f"paragraph {number}", "line": number})
    return blocks


def extract_blocks(path: Path) -> list[dict]:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_docx_blocks(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".md":
        return extract_markdown_blocks(text)
    return extract_plain_blocks(text)


def local_findings(blocks: list[dict], policy: dict) -> list[dict]:
    findings: list[dict] = []
    style = policy["human_style"]
    duplicate_pattern = re.compile(
        r"\b([\wÀ-ÖØ-öø-ÿ][\wÀ-ÖØ-öø-ÿ'’-]*)\s+\1\b",
        re.IGNORECASE | re.UNICODE,
    )

    if style.get("flag_consecutive_duplicate_words", True):
        for block in blocks:
            for match in duplicate_pattern.finditer(block["text"]):
                findings.append({
                    "source": "local",
                    "severity": "error",
                    "code": "duplicate_word",
                    "message": f"Repeated word: {match.group(1)!r}",
                    "location": block["location"],
                    "text": match.group(0),
                })

    for phrase in style.get("avoid_phrases", []):
        pattern = re.compile(r"(?i)(?<!\w)" + re.escape(phrase) + r"(?!\w)")
        for block in blocks:
            for match in pattern.finditer(block["text"]):
                findings.append({
                    "source": "local",
                    "severity": "warning",
                    "code": "generic_phrase",
                    "message": f"Replace generic wording with specific, evidence-based prose: {phrase!r}",
                    "location": block["location"],
                    "text": match.group(0),
                })

    max_words = int(style.get("max_sentence_words", 55))
    sentence_pattern = re.compile(r"[^.!?]+[.!?]?")
    for block in blocks:
        for match in sentence_pattern.finditer(block["text"]):
            sentence = match.group(0).strip()
            if not sentence:
                continue
            words = re.findall(r"\b[\wÀ-ÖØ-öø-ÿ&/+.-]+\b", sentence, re.UNICODE)
            if len(words) > max_words:
                findings.append({
                    "source": "local",
                    "severity": "warning",
                    "code": "long_sentence",
                    "message": f"Sentence has {len(words)} words; review for clarity without changing technical meaning.",
                    "location": block["location"],
                    "text": sentence[:180],
                })

    return findings


def chunks_from_blocks(blocks: list[dict], limit: int = 12000) -> list[dict]:
    chunks: list[dict] = []
    text_parts: list[str] = []
    spans: list[dict] = []
    length = 0

    def flush() -> None:
        nonlocal text_parts, spans, length
        if text_parts:
            chunks.append({"text": "\n\n".join(text_parts), "spans": spans})
        text_parts = []
        spans = []
        length = 0

    for block in blocks:
        value = block["text"]
        extra = len(value) + (2 if text_parts else 0)
        if text_parts and length + extra > limit:
            flush()
        start = length + (2 if text_parts else 0)
        if text_parts:
            length += 2
        text_parts.append(value)
        spans.append({
            "start": start,
            "end": start + len(value),
            "location": block["location"],
        })
        length += len(value)
    flush()
    return chunks


def location_for_offset(spans: list[dict], offset: int) -> str:
    for span in spans:
        if span["start"] <= offset <= span["end"]:
            return span["location"]
    return spans[-1]["location"] if spans else "unknown"


def languagetool_findings(
    blocks: list[dict],
    language: str,
    endpoint: str,
    policy: dict,
    *,
    allow_remote: bool = False,
    timeout: int = 45,
) -> list[dict]:
    if not allow_remote and not is_local_endpoint(endpoint):
        raise ValueError("Remote LanguageTool endpoint blocked; use local LanguageTool or --allow-remote.")

    blocking = set(policy["languagetool"].get("blocking_issue_types", []))
    disabled = ",".join(policy["languagetool"].get("disabled_rule_ids", []))
    findings: list[dict] = []

    for chunk in chunks_from_blocks(blocks):
        payload = {"text": chunk["text"], "language": language}
        if disabled:
            payload["disabledRules"] = disabled
        request = urllib.request.Request(
            endpoint,
            data=urllib.parse.urlencode(payload).encode("utf-8"),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))

        for match in data.get("matches", []):
            rule = match.get("rule", {})
            issue_type = rule.get("issueType", "uncategorized")
            offset = int(match.get("offset", 0))
            context = match.get("context", {})
            findings.append({
                "source": "languagetool",
                "severity": "error" if issue_type in blocking else "warning",
                "code": rule.get("id", "LANGUAGETOOL"),
                "issue_type": issue_type,
                "message": match.get("message", "LanguageTool finding"),
                "location": location_for_offset(chunk["spans"], offset),
                "text": context.get("text", ""),
                "replacements": [item.get("value") for item in match.get("replacements", [])[:5]],
            })
    return findings


def collect_all(policy: dict, include_generated: bool = False) -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and is_supported(path, policy) and not is_excluded(path, policy, include_generated):
            files.append(path)
    return sorted(files)


def collect_changed(base: str, policy: dict, include_generated: bool = False) -> list[Path]:
    command = ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD"]
    result = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    files: list[Path] = []
    for item in result.stdout.splitlines():
        path = ROOT / item
        if path.is_file() and is_supported(path, policy) and not is_excluded(path, policy, include_generated):
            files.append(path)
    return sorted(set(files))


def analyze_file(
    path: Path,
    policy: dict,
    *,
    endpoint: str | None = None,
    require_languagetool: bool = False,
    allow_remote: bool = False,
) -> dict:
    detection_text = read_text_for_detection(path)
    language = detect_language(path, detection_text, policy)
    blocks = extract_blocks(path)
    findings = local_findings(blocks, policy)
    lt_status = "not_requested"

    if language == "mixed":
        lt_status = "skipped_mixed_language"
    elif endpoint:
        try:
            findings.extend(
                languagetool_findings(
                    blocks,
                    language,
                    endpoint,
                    policy,
                    allow_remote=allow_remote,
                )
            )
            lt_status = "ok"
        except (URLError, HTTPError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as exc:
            if require_languagetool:
                raise RuntimeError(f"{path}: LanguageTool unavailable or invalid: {exc}") from exc
            lt_status = f"unavailable: {exc}"

    return {
        "path": path.relative_to(ROOT).as_posix(),
        "language": language,
        "blocks_checked": len(blocks),
        "languagetool_status": lt_status,
        "counts": {
            "errors": sum(1 for finding in findings if finding["severity"] == "error"),
            "warnings": sum(1 for finding in findings if finding["severity"] == "warning"),
        },
        "findings": findings,
    }


def should_fail(result: dict, fail_level: str) -> bool:
    if fail_level == "none":
        return False
    if fail_level == "warning":
        return bool(result["counts"]["errors"] or result["counts"]["warnings"])
    return bool(result["counts"]["errors"])


def render_text(results: list[dict]) -> str:
    lines: list[str] = []
    total_errors = 0
    total_warnings = 0
    for result in results:
        total_errors += result["counts"]["errors"]
        total_warnings += result["counts"]["warnings"]
        lines.append(
            f"{result['path']} [{result['language']}]: "
            f"{result['counts']['errors']} error(s), "
            f"{result['counts']['warnings']} warning(s); "
            f"LanguageTool={result['languagetool_status']}"
        )
        for finding in result["findings"]:
            lines.append(
                f"  {finding['severity'].upper():7} {finding['location']:>14} "
                f"{finding['source']}:{finding['code']} - {finding['message']}"
            )
    lines.append(f"TOTAL: {total_errors} error(s), {total_warnings} warning(s)")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", help="Specific source documents to review")
    parser.add_argument("--all", action="store_true", help="Review all supported controlled-source files")
    parser.add_argument("--changed-from", help="Review supported files changed since this Git commit/ref")
    parser.add_argument("--policy", default=str(DEFAULT_POLICY))
    parser.add_argument("--languagetool-url", default=None)
    parser.add_argument("--require-languagetool", action="store_true")
    parser.add_argument("--allow-remote", action="store_true")
    parser.add_argument("--include-generated", action="store_true")
    parser.add_argument("--fail-level", choices=["none", "warning", "error"], default="error")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--output")
    parser.add_argument("--list-only", action="store_true")
    parser.add_argument("--vale-files-only", action="store_true")
    args = parser.parse_args()

    policy = load_policy(Path(args.policy))

    selectors = sum(bool(item) for item in (args.files, args.all, args.changed_from))
    if selectors != 1:
        parser.error("Choose exactly one input mode: files, --all, or --changed-from.")

    if args.all:
        paths = collect_all(policy, args.include_generated)
    elif args.changed_from:
        paths = collect_changed(args.changed_from, policy, args.include_generated)
    else:
        paths = [Path(item) if Path(item).is_absolute() else ROOT / item for item in args.files]
        paths = [
            path for path in paths
            if path.is_file() and is_supported(path, policy)
            and not is_excluded(path, policy, args.include_generated)
        ]

    if args.vale_files_only:
        paths = [path for path in paths if path.suffix.lower() in {".md", ".txt", ".rst"}]

    if args.list_only:
        payload = [path.relative_to(ROOT).as_posix() for path in paths]
        output = json.dumps(payload, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(output + "\n", encoding="utf-8")
        print(output)
        return 0

    endpoint = args.languagetool_url
    if endpoint is None and args.require_languagetool:
        endpoint = policy["privacy"]["default_endpoint"]

    results: list[dict] = []
    exit_code = 0
    try:
        for path in paths:
            result = analyze_file(
                path,
                policy,
                endpoint=endpoint,
                require_languagetool=args.require_languagetool,
                allow_remote=args.allow_remote,
            )
            results.append(result)
            if should_fail(result, args.fail_level):
                exit_code = 1
    except (RuntimeError, OSError, ValueError, zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.format == "json":
        output = json.dumps(
            {
                "schema_version": 1,
                "files_checked": len(results),
                "results": results,
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n"
    else:
        output = render_text(results)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    print(output, end="")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
