#!/usr/bin/env python3
"""Fail-closed integrity gate for NIST AI 600-1 Manual 04.

Passing this gate validates a controlled version-aware implementation intake.
It does not establish trustworthy-AI achievement, legal compliance,
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
BASELINE_PATH = ROOT / ".compliance" / "nist-ai-600-1-manual-04-baseline.json"
SOURCE_REGISTRY_PATH = ROOT / ".compliance" / "authoritative-sources.json"
CATALOG_PATH = ROOT / ".compliance" / "manual-catalog.json"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "12-nist-ai-600-1-manual-04-qa.yml"
APPROVED_NIST_DOMAINS = {"www.nist.gov", "airc.nist.gov", "nvlpubs.nist.gov", "doi.org"}

EXPECTED_RISK_FAMILIES = [
    "CBRN Information or Capabilities",
    "Confabulation",
    "Dangerous, Violent, or Hateful Content",
    "Data Privacy",
    "Environmental Impacts",
    "Harmful Bias and Homogenization",
    "Human-AI Configuration",
    "Information Integrity",
    "Information Security",
    "Intellectual Property",
    "Obscene, Degrading, and/or Abusive Content",
    "Value Chain and Component Integration",
]

EXPECTED_CONSIDERATIONS = [
    "Governance",
    "Content Provenance",
    "Pre-deployment Testing",
    "Incident Disclosure",
]


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

    expected_envelope = {
        "schema_version": "1.0",
        "manual_id": "nist-ai-600-1-manual-04",
        "development_phase": "version-aware-implementation-intake",
        "controlled_language": "en",
    }
    for field, expected in expected_envelope.items():
        if baseline.get(field) != expected:
            errors.append(f"{field} must remain {expected!r}")
    if baseline.get("planned_publication_languages") != ["en", "es-419", "pt-BR"]:
        errors.append("planned publication languages must be en, es-419, and pt-BR")

    profile = baseline.get("current_profile")
    if not isinstance(profile, dict):
        errors.append("current_profile must be an object")
        profile = {}
    expected_profile = {
        "source_id": "nist-ai-600-1",
        "publication": "NIST AI 600-1",
        "version": "Generative Artificial Intelligence Profile",
        "publication_date": "2024-07-26",
        "registry_status": "final",
        "relationship": "cross-sectoral-profile-and-companion-to-ai-rmf-1-0",
    }
    for field, expected in expected_profile.items():
        if profile.get(field) != expected:
            errors.append(f"current_profile.{field} must remain {expected!r}")

    parent = baseline.get("parent_framework")
    if not isinstance(parent, dict):
        errors.append("parent_framework must be an object")
        parent = {}
    if parent.get("source_id") != "nist-ai-rmf-1-0":
        errors.append("AI RMF 1.0 must remain the controlled parent framework")
    if parent.get("registry_status") != "final-under-revision":
        errors.append("AI RMF 1.0 registry status must remain final-under-revision")
    if parent.get("revision_state") != "revision-in-progress":
        errors.append("AI RMF revision state must remain explicit")
    if parent.get("impact_analysis_required_on_change") is not True:
        errors.append("parent-framework change must require impact analysis")

    if baseline.get("risk_families") != EXPECTED_RISK_FAMILIES:
        errors.append("Manual 04 must preserve the twelve controlled GAI risk families in order")
    if baseline.get("primary_considerations") != EXPECTED_CONSIDERATIONS:
        errors.append("Manual 04 must preserve the four primary GAI considerations in order")
    if baseline.get("core_functions") != ["GOVERN", "MAP", "MEASURE", "MANAGE"]:
        errors.append("Core functions must remain GOVERN, MAP, MEASURE, MANAGE")

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
        errors.append("Manual 04 directory is missing")

    readme_path = manual_root / "README.md"
    readme = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    if len(readme) < 6_000:
        errors.append("Manual 04 README is missing or unexpectedly small")

    entry_relative = baseline.get("implementation_entry")
    entry_path = manual_root / str(entry_relative)
    entry = entry_path.read_text(encoding="utf-8") if entry_path.is_file() else ""
    if len(entry) < 12_000:
        errors.append("Manual 04 implementation entry is missing or unexpectedly small")

    combined = readme + "\n" + entry
    combined_normalized = normalize(combined)
    for path_name in baseline.get("implementation_paths", []):
        if normalize(str(path_name)) not in combined_normalized:
            errors.append(f"implementation entry is missing proportional path: {path_name}")
    for topic in baseline.get("required_topics", []):
        if normalize(str(topic)) not in combined_normalized:
            errors.append(f"Manual 04 is missing required topic: {topic}")
    for boundary in baseline.get("required_assurance_boundaries", []):
        if normalize(str(boundary)) not in combined_normalized:
            errors.append(f"Manual 04 is missing assurance boundary: {boundary}")
    for family in EXPECTED_RISK_FAMILIES:
        if family not in combined:
            errors.append(f"Manual 04 is missing controlled risk family: {family}")
    for consideration in EXPECTED_CONSIDERATIONS:
        if consideration not in combined:
            errors.append(f"Manual 04 is missing primary consideration: {consideration}")

    try:
        required_visuals = int(baseline.get("required_visuals_in_implementation_entry"))
    except (TypeError, ValueError):
        required_visuals = -1
    if required_visuals != 3:
        errors.append("Manual 04 must require exactly three implementation-entry memory graphics")
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
    if baseline.get("visual_accessibility_label") != "Accessible explanation:":
        errors.append("controlled visual accessibility label changed unexpectedly")
    if entry.count("**Accessible explanation:**") != required_visuals:
        errors.append("each Manual 04 memory graphic must have one accessible explanation")

    source_by_id = {
        source.get("id"): source
        for source in registry.get("sources", [])
        if isinstance(source, dict) and source.get("id")
    }
    required_source_ids = baseline.get("required_source_ids")
    if required_source_ids != ["nist-ai-600-1", "nist-ai-rmf-1-0"]:
        errors.append("required source ids must be nist-ai-600-1 and nist-ai-rmf-1-0")
        required_source_ids = ["nist-ai-600-1", "nist-ai-rmf-1-0"]
    expected_status = {"nist-ai-600-1": "final", "nist-ai-rmf-1-0": "final-under-revision"}
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
            errors.append(f"{source_id} status mismatch; perform impact analysis before adoption")
        parsed = urlparse(str(source.get("url", "")))
        if parsed.scheme != "https" or parsed.hostname not in APPROVED_NIST_DOMAINS:
            errors.append(f"required source is not on an approved official NIST/DOI domain: {source_id}")
        if source_id not in readme:
            errors.append(f"Manual 04 README is missing controlled source id: {source_id}")
        try:
            verified = dt.date.fromisoformat(str(source.get("last_verified")))
            interval = int(source.get("review_interval_days"))
            if interval > max_days:
                errors.append(f"required source review interval exceeds Manual 04 maximum: {source_id}")
            if dt.date.today() > verified + dt.timedelta(days=interval):
                errors.append(f"required NIST source review is overdue: {source_id}")
        except (TypeError, ValueError):
            errors.append(f"required NIST source has invalid verification metadata: {source_id}")

    catalog_matches = [
        item for item in catalog.get("manuals", [])
        if isinstance(item, dict) and item.get("id") == "nist-ai-600-1"
    ]
    if len(catalog_matches) != 1:
        errors.append("manual catalog must contain exactly one nist-ai-600-1 entry")
    else:
        item = catalog_matches[0]
        if item.get("path") != baseline.get("manual_path"):
            errors.append("Manual 04 catalog path does not match baseline")
        if item.get("status") != "development":
            errors.append("Manual 04 catalog status must be development")
        if item.get("layout") != "controlled-build" or item.get("series_order") != 4:
            errors.append("Manual 04 catalog must use controlled-build layout and series_order 4")
        if not str(item.get("title", "")).startswith("Manual 04"):
            errors.append("Manual 04 catalog title must identify series order")

    source_watch = baseline.get("source_watch")
    if not isinstance(source_watch, dict):
        errors.append("source_watch must be an object")
    else:
        if source_watch.get("enabled") is not True:
            errors.append("Manual 04 source watch must remain enabled")
        if source_watch.get("fail_on_missing_source") is not True:
            errors.append("Manual 04 must fail on missing controlled sources")
        if source_watch.get("fail_on_status_mismatch") is not True:
            errors.append("Manual 04 must fail on source-status mismatch")
        if source_watch.get("adoption_mode") != "impact-analysis-before-baseline-change":
            errors.append("Manual 04 must require impact analysis before baseline adoption")

    if not WORKFLOW_PATH.is_file():
        errors.append("dedicated Manual 04 QA workflow is missing")
    else:
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        for control in (
            "permissions:\n  contents: read",
            "pull_request:",
            "python3 scripts/nist_ai_600_1_manual_04_qa.py",
            "python3 scripts/compliance_qa.py sources",
            "python3 scripts/compliance_qa.py catalog",
        ):
            if control not in workflow:
                errors.append(f"Manual 04 workflow is missing control: {control!r}")
        if re.search(r"(?m)^\s*push:\s*$", workflow):
            errors.append("Manual 04 QA workflow must not push changes")

    print("NIST AI 600-1 Manual 04 QA")
    print(f"  implementation paths checked: {len(baseline.get('implementation_paths', []))}")
    print(f"  Core functions checked: {len(baseline.get('core_functions', []))}")
    print(f"  primary considerations checked: {len(baseline.get('primary_considerations', []))}")
    print(f"  GAI risk families checked: {len(baseline.get('risk_families', []))}")
    print(f"  memory graphics checked: {required_visuals}")
    print(f"  controlled NIST sources checked: {len(required_source_ids)}")
    for error in errors:
        print(f"  ERROR: {error}")
    if errors:
        print("FAIL: Manual 04 integrity gate did not pass")
        return 1
    print("PASS: Manual 04 version-aware implementation gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
