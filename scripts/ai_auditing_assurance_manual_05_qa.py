#!/usr/bin/env python3
"""Fail-closed intake QA for Manual 05 — AI Auditing and Assurance."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / ".compliance" / "ai-auditing-assurance-manual-05-baseline.json"
AAIA = ROOT / ".compliance" / "isaca-aaia-source.json"
CATALOG = ROOT / ".compliance" / "manual-catalog.json"
REGISTRY = ROOT / ".compliance" / "authoritative-sources.json"
MANUAL = ROOT / "03-assurance-and-audit" / "AI_Auditing_and_Assurance"
ENTRY = MANUAL / "MANUAL_05_IMPLEMENTATION_PATHS.md"
README = MANUAL / "README.md"
WORKFLOW = ROOT / ".github" / "workflows" / "13-ai-auditing-assurance-manual-05-qa.yml"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def roots(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.casefold())
    return {word[:-1] if len(word) > 4 and word.endswith("s") else word for word in words}


def concept_present(concept: str, document_roots: set[str]) -> bool:
    needed = roots(concept)
    return bool(needed) and needed.issubset(document_roots)


def main() -> int:
    errors: list[str] = []
    try:
        baseline = load(BASELINE)
        aaia = load(AAIA)
        catalog = load(CATALOG)
        registry = load(REGISTRY)
    except Exception as exc:
        print(f"FAIL: required controlled file could not be loaded: {exc}")
        return 1

    if baseline.get("manual_id") != "ai-auditing-assurance-manual-05":
        errors.append("unexpected Manual 05 id")
    if baseline.get("planned_publication_languages") != ["en", "es-419", "pt-BR"]:
        errors.append("Manual 05 must retain en, es-419, pt-BR publication languages")
    if baseline.get("implementation_paths") != ["essential", "structured", "enhanced"]:
        errors.append("Manual 05 must retain Essential/Structured/Enhanced paths")

    required_registry_ids = {
        "iso-19011-2026", "iso-iec-42006-2025", "iso-iec-42001-2023",
        "nist-ai-rmf-1-0", "nist-ai-600-1", "nist-sp-800-53a-r5",
    }
    registry_ids = {x.get("id") for x in registry.get("sources", []) if isinstance(x, dict)}
    for source_id in sorted(required_registry_ids - registry_ids):
        errors.append(f"required authoritative source missing: {source_id}")

    if aaia.get("source_id") != "isaca-aaia" or aaia.get("publisher") != "ISACA":
        errors.append("controlled ISACA AAIA source record is invalid")
    for field in ("official_url", "exam_content_outline_url"):
        parsed = urlparse(str(aaia.get(field, "")))
        if parsed.scheme != "https" or parsed.hostname not in {"www.isaca.org", "isaca.org"}:
            errors.append(f"AAIA {field} must remain on official isaca.org")
    expected_domains = ["AI Governance and Risk", "AI Operations", "AI Auditing Tools and Techniques"]
    if aaia.get("controlled_domains") != expected_domains:
        errors.append("AAIA controlled domains changed unexpectedly")

    readme = README.read_text(encoding="utf-8") if README.is_file() else ""
    entry = ENTRY.read_text(encoding="utf-8") if ENTRY.is_file() else ""
    if len(readme) < 3000:
        errors.append("Manual 05 README is missing or unexpectedly small")
    if len(entry) < 7000:
        errors.append("Manual 05 implementation entry is missing or unexpectedly small")
    combined = readme + "\n" + entry
    combined_roots = roots(combined)
    for domain in expected_domains:
        if domain not in combined:
            errors.append(f"Manual 05 missing AAIA domain: {domain}")
    for topic in baseline.get("required_topics", []):
        if not concept_present(str(topic), combined_roots):
            errors.append(f"Manual 05 missing required concept: {topic}")
    if len(re.findall(r"(?ms)^```mermaid\s*\n.*?^```\s*$", entry)) != 3:
        errors.append("Manual 05 implementation entry must contain exactly three Mermaid graphics")
    if entry.count("**Accessible explanation:**") != 3:
        errors.append("each Manual 05 graphic must have an accessible explanation")

    matches = [x for x in catalog.get("manuals", []) if x.get("id") == "ai-auditing-assurance"]
    if len(matches) != 1:
        errors.append("catalog must contain exactly one ai-auditing-assurance entry")
    else:
        item = matches[0]
        if item.get("status") != "development" or item.get("layout") != "controlled-build" or item.get("series_order") != 5:
            errors.append("Manual 05 catalog entry must be development/controlled-build/series_order 5")

    if not WORKFLOW.is_file():
        errors.append("Manual 05 dedicated QA workflow is missing")
    else:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        if "permissions:\n  contents: read" not in workflow:
            errors.append("Manual 05 workflow must be read-only")
        if re.search(r"(?m)^\s*push:\s*$", workflow):
            errors.append("Manual 05 workflow must not push changes")

    print("Manual 05 — AI Auditing and Assurance QA")
    print("  ISACA AAIA domains checked: 3")
    print("  implementation paths checked: 3")
    print(f"  authoritative registry sources checked: {len(required_registry_ids)}")
    for error in errors:
        print(f"  ERROR: {error}")
    if errors:
        print("FAIL: Manual 05 controlled intake gate did not pass")
        return 1
    print("PASS: Manual 05 controlled intake gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
