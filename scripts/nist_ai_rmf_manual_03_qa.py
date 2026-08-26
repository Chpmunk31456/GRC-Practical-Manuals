#!/usr/bin/env python3
"""Fail-closed integrity gate for NIST AI RMF Manual 03.

The gate validates the controlled version-aware implementation intake. Passing
it does not establish trustworthy-AI achievement, legal compliance,
certification, or an audit opinion.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / ".compliance" / "nist-ai-rmf-manual-03-baseline.json"
SOURCE_REGISTRY_PATH = ROOT / ".compliance" / "authoritative-sources.json"
CATALOG_PATH = ROOT / ".compliance" / "manual-catalog.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "10-nist-ai-rmf-manual-03-qa.yml"
APPROVED_NIST_DOMAINS = {"www.nist.gov", "airc.nist.gov", "nvlpubs.nist.gov"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"required file is missing: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def main() -> int:
    errors: list[str] = []

    try:
        baseline = load_json(BASELINE_PATH)
        registry = load_json(SOURCE_REGISTRY_PATH)
        catalog = load_json(CATALOG_PATH)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    if baseline.get("schema_version") != "1.0":
        errors.append("baseline schema_version must be 1.0")
    if baseline.get("manual_id") != "nist-ai-rmf-manual-03":
        errors.append("unexpected Manual 03 id")
    if baseline.get("development_phase") != "controlled-english-source-build":
        errors.append("Manual 03 development phase must remain controlled-english-source-build")
    if baseline.get("controlled_language") != "en":
        errors.append("English must remain the controlled source language during this phase")
    if baseline.get("planned_publication_languages") != ["en", "es-419", "pt-BR"]:
        errors.append("planned publication languages must be en, es-419, and pt-BR")

    current = baseline.get("current_framework")
    if not isinstance(current, dict):
        errors.append("current_framework must be an object")
        current = {}
    expected_current = {
        "source_id": "nist-ai-rmf-1-0",
        "publication": "NIST AI 100-1",
        "version": "AI RMF 1.0",
        "publication_date": "2023-01-26",
        "registry_status": "final-under-revision",
        "revision_state": "revision-in-progress",
        "revision_notice_required": True,
    }
    for field, expected in expected_current.items():
        if current.get(field) != expected:
            errors.append(f"current_framework.{field} must remain {expected!r}")

    genai = baseline.get("generative_ai_profile")
    if not isinstance(genai, dict):
        errors.append("generative_ai_profile must be an object")
        genai = {}
    if genai.get("source_id") != "nist-ai-600-1" or genai.get("status") != "final":
        errors.append("NIST AI 600-1 must remain the controlled final GenAI profile")
    if genai.get("applies_when") != "generative-ai-in-scope":
        errors.append("GenAI profile applicability boundary is missing")

    manual_relative = baseline.get("manual_path")
    if not isinstance(manual_relative, str) or not manual_relative:
        errors.append("manual_path must be a non-empty repository-relative path")
        manual_root = ROOT
    else:
        manual_root = ROOT / manual_relative
        if ".." in Path(manual_relative).parts or not manual_root.resolve().is_relative_to(ROOT):
            errors.append("manual_path must remain inside the repository")
            manual_root = ROOT
    if not manual_root.is_dir():
        errors.append("Manual 03 directory is missing")

    readme_path = manual_root / "README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    if len(readme) < 5_000:
        errors.append("Manual 03 README is missing or unexpectedly small")

    entry_relative = baseline.get("implementation_entry")
    entry_path = manual_root / str(entry_relative)
    entry = entry_path.read_text(encoding="utf-8") if entry_path.is_file() else ""
    if len(entry) < 10_000:
        errors.append("Manual 03 implementation entry is missing or unexpectedly small")

    combined = readme + "\n" + entry
    combined_normalized = normalize(combined)

    for path_name in baseline.get("implementation_paths", []):
        if normalize(str(path_name)) not in combined_normalized:
            errors.append(f"implementation entry is missing proportional path: {path_name}")

    core_functions = baseline.get("core_functions")
    if core_functions != ["GOVERN", "MAP", "MEASURE", "MANAGE"]:
        errors.append("Core functions must be GOVERN, MAP, MEASURE, MANAGE in controlled order")
    else:
        for function in core_functions:
            if function not in entry:
                errors.append(f"implementation entry is missing Core function: {function}")

    expected_source_parts = [
        "English/source/01_PRELIMINARIES_CHAPTERS_01_08.md",
        "English/source/02_MAP_CHAPTERS_09_16.md",
        "English/source/03_MEASURE_CHAPTERS_17_24.md",
        "English/source/04_MANAGE_CHAPTERS_25_32.md",
    ]
    if baseline.get("english_source_parts") != expected_source_parts:
        errors.append("controlled English source must contain the four ordered chapter parts")
    source_texts: list[str] = []
    for relative in expected_source_parts:
        source_path = manual_root / relative
        if not source_path.is_file():
            errors.append(f"controlled English source part is missing: {relative}")
            source_texts.append("")
            continue
        source_text = source_path.read_text(encoding="utf-8")
        source_texts.append(source_text)
        if len(source_text) < 15_000:
            errors.append(f"controlled English source part is unexpectedly small: {relative}")

    source_combined = "\n".join(source_texts)
    chapter_numbers = [
        int(number)
        for number in re.findall(r"(?m)^# ([0-9]+)\. ", source_combined)
    ]
    expected_chapters = list(range(1, 33))
    if baseline.get("english_chapter_count") != 32:
        errors.append("controlled English chapter count must remain 32")
    if chapter_numbers != expected_chapters:
        errors.append(
            "controlled English chapters must appear exactly once in order 1-32; "
            f"found {chapter_numbers}"
        )
    for function in core_functions:
        if function not in source_combined:
            errors.append(f"controlled English source is missing Core function: {function}")

    required_source_visuals = baseline.get("required_source_visuals")
    if required_source_visuals != 12:
        errors.append("controlled English source must require exactly 12 memory graphics")
        required_source_visuals = 12
    source_mermaid_blocks = re.findall(
        r"(?ms)^```mermaid\s*\n(.*?)^```\s*$", source_combined
    )
    if len(source_mermaid_blocks) != required_source_visuals:
        errors.append(
            f"controlled English source has {len(source_mermaid_blocks)} closed Mermaid blocks; "
            f"expected {required_source_visuals}"
        )
    if source_combined.count("**Accessible explanation:**") != required_source_visuals:
        errors.append("each controlled English source graphic must have an accessible explanation")
    for index, block in enumerate(source_mermaid_blocks, start=1):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines or lines[0] != "flowchart TD":
            errors.append(f"controlled source visual {index} must be a top-down flowchart")
        if "-->" not in block:
            errors.append(f"controlled source visual {index} lacks a relationship arrow")
        if "click " in block or "%%{" in block:
            errors.append(f"controlled source visual {index} contains disallowed directives")

    if baseline.get("english_source_status") != "controlled-draft-source-review-required":
        errors.append("English source status must remain controlled-draft-source-review-required")
    human_control = baseline.get("human_review_control")
    expected_decision_fields = [
        "reviewer", "date", "decision", "evidence", "findings", "remediation"
    ]
    if not isinstance(human_control, dict):
        errors.append("human_review_control must be an object")
    else:
        if human_control.get("required") is not True:
            errors.append("Manual 03 must require human review")
        if human_control.get("gate_status") != "open":
            errors.append("Manual 03 human-review gate must remain open during controlled source build")
        if human_control.get("fail_closed") is not True:
            errors.append("Manual 03 human-review control must fail closed")
        if human_control.get("final_release_approval_required") is not True:
            errors.append("Manual 03 must require final human release approval")
        if human_control.get("required_decision_fields") != expected_decision_fields:
            errors.append("Manual 03 human decisions must record all controlled evidence fields")

    for topic in baseline.get("required_topics", []):
        if normalize(str(topic)) not in combined_normalized:
            errors.append(f"Manual 03 is missing required topic: {topic}")

    for marker in baseline.get("required_version_markers", []):
        if str(marker) not in combined:
            errors.append(f"Manual 03 is missing version-awareness marker: {marker}")

    for boundary in baseline.get("required_assurance_boundaries", []):
        if normalize(str(boundary)) not in combined_normalized:
            errors.append(f"Manual 03 is missing assurance boundary: {boundary}")

    try:
        required_visuals = int(baseline.get("required_visuals_in_implementation_entry"))
    except (TypeError, ValueError):
        required_visuals = -1
    if required_visuals != 3:
        errors.append("Manual 03 must require exactly three implementation-entry memory graphics")
        required_visuals = 3

    mermaid_blocks = re.findall(r"(?ms)^```mermaid\s*\n(.*?)^```\s*$", entry)
    if len(mermaid_blocks) != required_visuals:
        errors.append(f"implementation entry has {len(mermaid_blocks)} closed Mermaid blocks; expected {required_visuals}")
    for index, block in enumerate(mermaid_blocks, start=1):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines or lines[0] != "flowchart TD":
            errors.append(f"Mermaid visual {index} must be a top-down flowchart")
        if "-->" not in block:
            errors.append(f"Mermaid visual {index} lacks a relationship arrow")
        if block.count('"') % 2:
            errors.append(f"Mermaid visual {index} has unbalanced quoted labels")
        if "click " in block or "%%{" in block:
            errors.append(f"Mermaid visual {index} contains disallowed directives")

    accessibility_label = baseline.get("visual_accessibility_label")
    if accessibility_label != "Accessible explanation:":
        errors.append("controlled visual accessibility label changed unexpectedly")
    if entry.count("**Accessible explanation:**") != required_visuals:
        errors.append("each Manual 03 memory graphic must have one accessible explanation")

    source_by_id = {
        source.get("id"): source
        for source in registry.get("sources", [])
        if isinstance(source, dict) and source.get("id")
    }
    required_source_ids = baseline.get("required_source_ids")
    if required_source_ids != ["nist-ai-rmf-1-0", "nist-ai-600-1"]:
        errors.append("required source ids must be nist-ai-rmf-1-0 and nist-ai-600-1")
        required_source_ids = ["nist-ai-rmf-1-0", "nist-ai-600-1"]

    expected_status = {
        "nist-ai-rmf-1-0": "final-under-revision",
        "nist-ai-600-1": "final",
    }
    max_days = baseline.get("source_watch", {}).get("maximum_review_interval_days", 30)
    try:
        max_days = int(max_days)
    except (TypeError, ValueError):
        errors.append("source_watch.maximum_review_interval_days must be an integer")
        max_days = 30

    for source_id in required_source_ids:
        source = source_by_id.get(source_id)
        if source is None:
            errors.append(f"required NIST source is absent from registry: {source_id}")
            continue
        if source.get("status") != expected_status[source_id]:
            errors.append(
                f"{source_id} registry status is {source.get('status')!r}; "
                f"controlled baseline expects {expected_status[source_id]!r}; perform impact analysis before adoption"
            )
        parsed = urlparse(str(source.get("url", "")))
        if parsed.scheme != "https" or parsed.hostname not in APPROVED_NIST_DOMAINS:
            errors.append(f"required source is not on an approved official NIST domain: {source_id}")
        if source_id not in readme:
            errors.append(f"Manual 03 README is missing controlled source id: {source_id}")
        try:
            last_verified = dt.date.fromisoformat(str(source.get("last_verified")))
            interval = int(source.get("review_interval_days"))
            if interval > max_days:
                errors.append(f"required source review interval exceeds Manual 03 maximum: {source_id}")
            if dt.date.today() > last_verified + dt.timedelta(days=interval):
                errors.append(f"required NIST source review is overdue: {source_id}")
        except (TypeError, ValueError):
            errors.append(f"required NIST source has invalid verification metadata: {source_id}")

    catalog_matches = [
        item for item in catalog.get("manuals", [])
        if isinstance(item, dict) and item.get("id") == "nist-ai-rmf-1-0"
    ]
    if len(catalog_matches) != 1:
        errors.append("manual catalog must contain exactly one nist-ai-rmf-1-0 entry")
    else:
        item = catalog_matches[0]
        if item.get("path") != baseline.get("manual_path"):
            errors.append("Manual 03 catalog path does not match baseline")
        if item.get("status") != "development":
            errors.append("Manual 03 catalog status must be development")
        if item.get("layout") != "controlled-build" or item.get("series_order") != 3:
            errors.append("Manual 03 catalog must use controlled-build layout and series_order 3")
        if not str(item.get("title", "")).startswith("Manual 03"):
            errors.append("Manual 03 catalog title must identify series order")

    source_watch = baseline.get("source_watch")
    if not isinstance(source_watch, dict):
        errors.append("source_watch must be an object")
    else:
        if source_watch.get("enabled") is not True:
            errors.append("Manual 03 source watch must remain enabled")
        if source_watch.get("fail_on_missing_source") is not True:
            errors.append("Manual 03 must fail on missing controlled sources")
        if source_watch.get("fail_on_status_mismatch") is not True:
            errors.append("Manual 03 must fail on source-status mismatch")
        if source_watch.get("adoption_mode") != "impact-analysis-before-baseline-change":
            errors.append("Manual 03 must require impact analysis before baseline adoption")

    if not WORKFLOW_PATH.is_file():
        errors.append("dedicated Manual 03 QA workflow is missing")
    else:
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        for control in (
            "permissions:\n  contents: read",
            "pull_request:",
            "python3 scripts/nist_ai_rmf_manual_03_qa.py",
            "python3 scripts/compliance_qa.py sources",
            "python3 scripts/compliance_qa.py catalog",
        ):
            if control not in workflow:
                errors.append(f"Manual 03 workflow is missing control: {control!r}")
        if re.search(r"(?m)^\s*push:\s*$", workflow):
            errors.append("Manual 03 QA workflow must not push changes")

    print("NIST AI RMF Manual 03 QA")
    print(f"  implementation paths checked: {len(baseline.get('implementation_paths', []))}")
    print(f"  Core functions checked: {len(baseline.get('core_functions', []))}")
    print(f"  memory graphics checked: {required_visuals}")
    print(f"  controlled NIST sources checked: {len(required_source_ids)}")
    print(f"  controlled English chapter parts checked: {len(expected_source_parts)}")
    print(f"  controlled English chapters checked: {len(chapter_numbers)}")
    print(f"  controlled source memory graphics checked: {required_source_visuals}")
    print("  AI RMF revision state expected: revision-in-progress")
    for error in errors:
        print(f"  ERROR: {error}")
    if errors:
        print("FAIL: Manual 03 integrity gate did not pass")
        return 1
    print("PASS: Manual 03 version-aware implementation gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
