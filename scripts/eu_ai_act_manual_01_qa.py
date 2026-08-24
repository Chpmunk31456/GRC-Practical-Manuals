#!/usr/bin/env python3
"""Fail-closed integrity gate for EU AI Act Manual 01.

Passing this check confirms repository structure, controlled-source references, and
implementation-path coverage. It does not establish legal compliance or assurance.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = REPO_ROOT / ".compliance" / "eu-ai-act-manual-01-baseline.json"
SOURCE_REGISTRY_PATH = REPO_ROOT / ".compliance" / "authoritative-sources.json"
CATALOG_PATH = REPO_ROOT / ".compliance" / "manual-catalog.json"
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "08-eu-ai-act-manual-01-qa.yml"
APPROVED_EU_DOMAINS = {
    "digital-strategy.ec.europa.eu",
    "eur-lex.europa.eu",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"required file is missing: {path.relative_to(REPO_ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}") from exc


def normalized_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        baseline = load_json(BASELINE_PATH)
        registry = load_json(SOURCE_REGISTRY_PATH)
        catalog = load_json(CATALOG_PATH)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    if baseline.get("schema_version") != "1.0":
        errors.append("baseline schema_version must be 1.0")
    if baseline.get("manual_id") != "eu-ai-act-manual-01":
        errors.append("unexpected manual_id")

    disclosure_relative = baseline.get("repository_disclosure_path")
    if not isinstance(disclosure_relative, str) or not disclosure_relative:
        errors.append("repository_disclosure_path must be a non-empty path")
    elif ".." in Path(disclosure_relative).parts:
        errors.append("repository_disclosure_path must remain inside the repository")
    else:
        disclosure_path = REPO_ROOT / disclosure_relative
        if not disclosure_path.is_file():
            errors.append("AI assistance disclosure is missing")
        else:
            disclosure_text = disclosure_path.read_text(encoding="utf-8")
            required_disclosure_phrases = (
                "Alberto “Al” Leiva",
                "ChatGPT and Codex, OpenAI",
                "human author",
                "does not imply",
                "does not provide legal advice",
            )
            for phrase in required_disclosure_phrases:
                if phrase not in disclosure_text:
                    errors.append(f"AI assistance disclosure is missing phrase: {phrase}")

    manual_relative = baseline.get("manual_path")
    if not isinstance(manual_relative, str) or not manual_relative:
        errors.append("manual_path must be a non-empty repository-relative path")
        manual_root = REPO_ROOT
    else:
        manual_root = REPO_ROOT / manual_relative
        if not manual_root.resolve().is_relative_to(REPO_ROOT) or ".." in Path(manual_relative).parts:
            errors.append("manual_path must remain inside the repository")
        if not manual_root.is_dir():
            errors.append(f"manual directory is missing: {manual_relative}")

    required_files = baseline.get("required_entry_files")
    if not isinstance(required_files, list) or not required_files:
        errors.append("required_entry_files must be a non-empty list")
        required_files = []
    for relative in required_files:
        if not isinstance(relative, str) or not relative or ".." in Path(relative).parts:
            errors.append(f"invalid required entry path: {relative!r}")
            continue
        candidate = manual_root / relative
        if not candidate.is_file():
            errors.append(f"required manual entry is missing: {candidate.relative_to(REPO_ROOT)}")
        elif candidate.stat().st_size < 200:
            errors.append(f"required manual entry is unexpectedly small: {candidate.relative_to(REPO_ROOT)}")

    implementation_path = manual_root / "MANUAL_01_IMPLEMENTATION_PATHS.md"
    implementation_text = (
        implementation_path.read_text(encoding="utf-8") if implementation_path.is_file() else ""
    )
    implementation_normalized = normalized_text(implementation_text)
    for topic in baseline.get("required_topics", []):
        if normalized_text(str(topic)) not in implementation_normalized:
            errors.append(f"implementation entry point is missing required topic: {topic}")

    required_size_phrases = {
        "micro and small organization",
        "midsize organization",
        "large or complex enterprise",
    }
    for phrase in required_size_phrases:
        if normalized_text(phrase) not in implementation_normalized:
            errors.append(f"implementation entry point is missing size path: {phrase}")

    try:
        required_visuals = int(baseline.get("required_visuals_per_entry"))
        if required_visuals < 1:
            raise ValueError
    except (TypeError, ValueError):
        errors.append("required_visuals_per_entry must be a positive integer")
        required_visuals = 0
    accessibility_labels = baseline.get("visual_accessibility_labels")
    if not isinstance(accessibility_labels, dict):
        errors.append("visual_accessibility_labels must be an object")
        accessibility_labels = {}
    if implementation_text.count("```mermaid") != required_visuals:
        errors.append("English entry has an unexpected number of Mermaid visuals")
    english_accessibility_label = accessibility_labels.get("en")
    if not isinstance(english_accessibility_label, str) or implementation_text.count(
        english_accessibility_label
    ) != required_visuals:
        errors.append("English visuals must each have a controlled accessible explanation")

    localized_entries = baseline.get("localized_entry_files")
    localized_phrases = baseline.get("localized_required_phrases")
    if not isinstance(localized_entries, dict) or set(localized_entries) != {"es-419", "pt-BR"}:
        errors.append("localized_entry_files must define exactly es-419 and pt-BR")
        localized_entries = {}
    if not isinstance(localized_phrases, dict):
        errors.append("localized_required_phrases must be an object")
        localized_phrases = {}
    for language, relative in localized_entries.items():
        if not isinstance(relative, str) or not relative or ".." in Path(relative).parts:
            errors.append(f"invalid localized entry path for {language}: {relative!r}")
            continue
        localized_path = manual_root / relative
        if not localized_path.is_file():
            errors.append(f"localized implementation entry is missing: {language}")
            continue
        if localized_path.stat().st_size < 5_000:
            errors.append(f"localized implementation entry is unexpectedly small: {language}")
        localized_text = localized_path.read_text(encoding="utf-8")
        localized_normalized = normalized_text(localized_text)
        phrases = localized_phrases.get(language)
        if not isinstance(phrases, list) or not phrases:
            errors.append(f"localized required phrases are missing: {language}")
            phrases = []
        for phrase in phrases:
            if normalized_text(str(phrase)) not in localized_normalized:
                errors.append(f"{language} entry is missing controlled phrase: {phrase}")
        numbered_sections = re.findall(r"(?m)^## [1-8]\. ", localized_text)
        if len(numbered_sections) != 8:
            errors.append(f"{language} entry must contain numbered sections 1 through 8")
        if localized_text.count("```mermaid") != required_visuals:
            errors.append(f"{language} entry has an unexpected number of Mermaid visuals")
        accessibility_label = accessibility_labels.get(language)
        if not isinstance(accessibility_label, str) or localized_text.count(
            accessibility_label
        ) != required_visuals:
            errors.append(f"{language} visuals must each have an accessible explanation")
        for source_id in baseline.get("binding_source_ids", []) + baseline.get(
            "implementation_source_ids", []
        ):
            if source_id not in localized_text:
                errors.append(f"{language} entry is missing controlled source id: {source_id}")

    readme_path = manual_root / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    if "Manual 01" not in readme_text:
        errors.append("manual README must identify this publication as Manual 01")
    if "MANUAL_01_IMPLEMENTATION_PATHS.md" not in readme_text:
        errors.append("manual README must link to the Manual 01 implementation paths")

    source_records = registry.get("sources", [])
    source_by_id = {
        item.get("id"): item for item in source_records if isinstance(item, dict) and item.get("id")
    }
    required_source_ids = baseline.get("binding_source_ids", []) + baseline.get(
        "implementation_source_ids", []
    )
    for source_id in required_source_ids:
        source = source_by_id.get(source_id)
        if source is None:
            errors.append(f"required EU source is absent from registry: {source_id}")
            continue
        parsed = urlparse(str(source.get("url", "")))
        if parsed.scheme != "https" or parsed.hostname not in APPROVED_EU_DOMAINS:
            errors.append(f"EU source is not on an approved official domain: {source_id}")
        try:
            last_verified = dt.date.fromisoformat(str(source.get("last_verified")))
            interval = int(source.get("review_interval_days"))
            if dt.date.today() > last_verified + dt.timedelta(days=interval):
                errors.append(f"EU source review is overdue: {source_id}")
        except (TypeError, ValueError):
            errors.append(f"EU source has invalid verification metadata: {source_id}")

    binding_ids = set(baseline.get("binding_source_ids", []))
    for source_id in binding_ids:
        source = source_by_id.get(source_id, {})
        if source.get("status") != "final":
            errors.append(f"binding source must have status 'final': {source_id}")

    catalog_entries = catalog.get("manuals", [])
    matching_entries = [
        item
        for item in catalog_entries
        if isinstance(item, dict) and item.get("id") == "eu-ai-act-grc"
    ]
    if len(matching_entries) != 1:
        errors.append("manual catalog must contain exactly one eu-ai-act-grc entry")
    else:
        entry = matching_entries[0]
        if entry.get("path") != manual_relative:
            errors.append("manual catalog path does not match controlled baseline")
        if entry.get("series_order") != 1:
            errors.append("EU AI Act must be series_order 1")

    if not WORKFLOW_PATH.is_file():
        errors.append("dedicated EU AI Act workflow is missing")
    else:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")
        required_workflow_controls = (
            "permissions:\n  contents: read",
            "pull_request:",
            "python3 scripts/eu_ai_act_manual_01_qa.py",
        )
        for control in required_workflow_controls:
            if control not in workflow_text:
                errors.append(f"dedicated workflow is missing control: {control!r}")
        if re.search(r"(?m)^\s*push:\s*$", workflow_text):
            errors.append("dedicated Manual 01 QA workflow must not push changes")

    print("EU AI Act Manual 01 QA")
    print(f"  required files checked: {len(required_files)}")
    print(f"  localized entries checked: {len(localized_entries)}")
    print(f"  controlled sources checked: {len(required_source_ids)}")
    print(f"  implementation topics checked: {len(baseline.get('required_topics', []))}")
    for warning in warnings:
        print(f"  WARNING: {warning}")
    for error in errors:
        print(f"  ERROR: {error}")

    if errors:
        print("FAIL: Manual 01 integrity gate did not pass")
        return 1

    print("PASS: Manual 01 integrity gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
