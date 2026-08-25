#!/usr/bin/env python3
"""Fail-closed integrity gate for ISO/IEC 42001 Manual 02.

Passing this check confirms the controlled English master, trilingual
proportional implementation entries, draft 32-chapter localized source sets,
official-source registry, accessible graphics, and workflow boundary. It does
not establish conformity, certification, legal compliance, or an audit opinion.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = REPO_ROOT / ".compliance" / "iso-42001-manual-02-baseline.json"
SOURCE_REGISTRY_PATH = REPO_ROOT / ".compliance" / "authoritative-sources.json"
CATALOG_PATH = REPO_ROOT / ".compliance" / "manual-catalog.json"
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "09-iso-42001-manual-02-qa.yml"
APPROVED_SOURCE_DOMAINS = {"www.iso.org"}
WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DRAWING_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"required file is missing: {path.relative_to(REPO_ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}") from exc


def normalized_text(value: str) -> str:
    return re.sub(r"[^a-z0-9áéíóúüñãõâêôàç]+", " ", value.casefold()).strip()


def repository_path(relative: object, field: str, errors: list[str]) -> Path | None:
    if not isinstance(relative, str) or not relative:
        errors.append(f"{field} must be a non-empty repository-relative path")
        return None
    candidate = REPO_ROOT / relative
    if ".." in Path(relative).parts or not candidate.resolve().is_relative_to(REPO_ROOT):
        errors.append(f"{field} must remain inside the repository")
        return None
    return candidate


def validate_implementation_structure(
    text: str,
    language: str,
    baseline: dict,
    required_visuals: int,
    errors: list[str],
) -> None:
    structure = baseline.get("implementation_structure")
    if not isinstance(structure, dict):
        errors.append("implementation_structure must be an object")
        return

    actual = {
        "numbered_sections": len(re.findall(r"(?m)^## [1-8]\. ", text)),
        "subsections": len(re.findall(r"(?m)^### ", text)),
        "table_rows": len(re.findall(r"(?m)^\|.*\|$", text)),
        "bullet_items": len(re.findall(r"(?m)^- ", text)),
    }
    for field, count in actual.items():
        try:
            expected = int(structure.get(field))
        except (TypeError, ValueError):
            errors.append(f"implementation_structure.{field} must be an integer")
            continue
        if count != expected:
            errors.append(f"{language} entry has {count} {field}; expected {expected}")

    mermaid_blocks = re.findall(r"(?ms)^```mermaid\s*\n(.*?)^```\s*$", text)
    if len(mermaid_blocks) != required_visuals:
        errors.append(f"{language} entry must contain {required_visuals} closed Mermaid blocks")
    for index, block in enumerate(mermaid_blocks, start=1):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines or lines[0] != "flowchart TD":
            errors.append(f"{language} Mermaid visual {index} must be a top-down flowchart")
        if "-->" not in block:
            errors.append(f"{language} Mermaid visual {index} lacks a relationship arrow")
        if block.count('"') % 2:
            errors.append(f"{language} Mermaid visual {index} has unbalanced quoted labels")
        if "click " in block or "%%{" in block:
            errors.append(f"{language} Mermaid visual {index} contains disallowed directives")

    visual_labels = baseline.get("required_visual_labels")
    if not isinstance(visual_labels, dict):
        errors.append("required_visual_labels must be an object")
        return
    language_labels = visual_labels.get(language)
    if not isinstance(language_labels, list) or len(language_labels) != required_visuals:
        errors.append(f"required visual labels must define {required_visuals} items for {language}")
        return
    for label in language_labels:
        if str(label) not in text:
            errors.append(f"{language} entry is missing localized visual label: {label}")


def validate_localized_full_sources(
    manual_root: Path,
    baseline: dict,
    accessibility_labels: dict,
    errors: list[str],
) -> int:
    source_sets = baseline.get("localized_full_source_parts")
    if not isinstance(source_sets, dict) or set(source_sets) != {"es-419", "pt-BR"}:
        errors.append("localized_full_source_parts must define exactly es-419 and pt-BR")
        return 0

    try:
        required_chapters = int(baseline.get("required_localized_chapters"))
        required_graphics = int(baseline.get("required_localized_source_graphics"))
    except (TypeError, ValueError):
        errors.append("localized source chapter/graphic requirements must be integers")
        return 0

    full_phrases = baseline.get("localized_full_required_phrases")
    if not isinstance(full_phrases, dict):
        errors.append("localized_full_required_phrases must be an object")
        full_phrases = {}

    asset_roots = baseline.get("localized_graphic_asset_roots")
    if not isinstance(asset_roots, dict) or set(asset_roots) != {"es-419", "pt-BR"}:
        errors.append("localized_graphic_asset_roots must define exactly es-419 and pt-BR")
        asset_roots = {}

    checked = 0
    for language, relatives in source_sets.items():
        if not isinstance(relatives, list) or len(relatives) != 4:
            errors.append(f"{language} full source must define exactly four reviewable parts")
            continue

        texts: list[str] = []
        for relative in relatives:
            if not isinstance(relative, str) or not relative or ".." in Path(relative).parts:
                errors.append(f"invalid localized full-source path for {language}: {relative!r}")
                continue
            path = manual_root / relative
            if not path.is_file():
                errors.append(f"localized full-source part is missing for {language}: {relative}")
                continue
            text = path.read_text(encoding="utf-8")
            if len(text) < 4_000:
                errors.append(f"localized full-source part is unexpectedly small for {language}: {relative}")
            texts.append(text)

        if len(texts) != 4:
            continue

        combined = "\n\n".join(texts)
        chapters = [
            int(value)
            for value in re.findall(r"(?m)^# ([1-9]|[12][0-9]|3[0-2])\. ", combined)
        ]
        expected = list(range(1, required_chapters + 1))
        if chapters != expected:
            errors.append(
                f"{language} localized full source must contain chapters 1-{required_chapters} "
                "exactly once and in order"
            )

        phrases = full_phrases.get(language)
        if not isinstance(phrases, list) or not phrases:
            errors.append(f"localized full-source required phrases are missing: {language}")
            phrases = []
        normalized = normalized_text(combined)
        for phrase in phrases:
            if normalized_text(str(phrase)) not in normalized:
                errors.append(f"{language} full source is missing controlled phrase: {phrase}")

        graphics = re.findall(
            r'<img\s+src="([^"]+)"[^>]*\salt="([^"]+)"\s*/?>', combined
        )
        if len(graphics) != required_graphics:
            errors.append(
                f"{language} localized full source has {len(graphics)} graphics; "
                f"expected {required_graphics}"
            )
        expected_sources = {
            f"../../../assets/{language}/media/image{number}.png"
            for number in range(1, required_graphics + 1)
        }
        actual_sources = {source for source, _ in graphics}
        if actual_sources != expected_sources:
            errors.append(
                f"{language} localized source must reference exactly its own "
                f"image1-image{required_graphics} PNG graphics"
            )
        if any("assets/English/" in source for source, _ in graphics):
            errors.append(f"{language} localized source must not fall back to English graphics")
        for source, alt_text in graphics:
            if not alt_text.strip():
                errors.append(f"{language} localized graphic has empty alternative text: {source}")
                continue
            first_part = manual_root / relatives[0]
            asset_path = (first_part.parent / source).resolve()
            if not asset_path.is_relative_to(manual_root.resolve()) or not asset_path.is_file():
                errors.append(f"{language} localized graphic path is missing/outside Manual 02: {source}")

        asset_root_relative = asset_roots.get(language)
        asset_root = manual_root / str(asset_root_relative)
        if not isinstance(asset_root_relative, str) or ".." in Path(asset_root_relative).parts:
            errors.append(f"invalid localized graphic asset root for {language}")
        elif not asset_root.is_dir():
            errors.append(f"localized graphic asset root is missing for {language}")
        else:
            expected_names = {
                f"image{number}.{extension}"
                for number in range(1, required_graphics + 1)
                for extension in ("png", "svg")
            }
            actual_names = {path.name for path in asset_root.iterdir() if path.is_file()}
            if actual_names != expected_names:
                errors.append(
                    f"{language} must contain exactly image1-image{required_graphics} "
                    "as editable SVG and PNG derivatives"
                )
            for number in range(1, required_graphics + 1):
                png_path = asset_root / f"image{number}.png"
                svg_path = asset_root / f"image{number}.svg"
                if png_path.is_file():
                    try:
                        png_data = png_path.read_bytes()[:24]
                        if png_data[:8] != b"\x89PNG\r\n\x1a\n":
                            raise ValueError("invalid PNG signature")
                        width, height = struct.unpack(">II", png_data[16:24])
                        if (width, height) != (1657, 871):
                            errors.append(
                                f"{language} image{number}.png is {width}x{height}; expected 1657x871"
                            )
                    except (OSError, ValueError, struct.error) as exc:
                        errors.append(f"{language} image{number}.png is invalid: {exc}")
                if svg_path.is_file():
                    svg_text = svg_path.read_text(encoding="utf-8")
                    for marker in ('role="img"', "<title", "<desc", f"Figura {number}"):
                        if marker not in svg_text:
                            errors.append(
                                f"{language} image{number}.svg lacks accessible marker: {marker}"
                            )

        label = accessibility_labels.get(language)
        if not isinstance(label, str) or combined.count(label) != required_graphics:
            errors.append(
                f"{language} localized source graphics must each have one accessible explanation"
            )

        if "ISO/IEC 42001" not in combined or "ISO/IEC 42005" not in combined or "ISO/IEC 42006" not in combined:
            errors.append(f"{language} localized full source is missing core ISO references")
        checked += 1

    return checked


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
    if baseline.get("manual_id") != "iso-42001-manual-02":
        errors.append("unexpected manual_id")
    if baseline.get("development_phase") != "trilingual-full-source-review":
        errors.append("development phase must remain trilingual-full-source-review")
    if baseline.get("localized_full_source_status") != "draft-human-review-required":
        errors.append("localized full-source status must remain draft-human-review-required")
    if baseline.get("planned_publication_languages") != ["en", "es-419", "pt-BR"]:
        errors.append("planned publication languages must be en, es-419, and pt-BR")

    visual_standard = repository_path(
        baseline.get("visual_learning_standard_path"), "visual_learning_standard_path", errors
    )
    if visual_standard and not visual_standard.is_file():
        errors.append("project visual-learning standard is missing")

    manual_root = repository_path(baseline.get("manual_path"), "manual_path", errors)
    if manual_root is None:
        manual_root = REPO_ROOT
    elif not manual_root.is_dir():
        errors.append("Manual 02 directory is missing")

    readme_path = manual_root / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""
    required_readme_phrases = (
        "Manual 02",
        "Controlled trilingual implementation entry",
        "MANUAL_02_IMPLEMENTATION_PATHS.md",
        "MANUAL_02_RUTAS_DE_IMPLEMENTACION.md",
        "MANUAL_02_CAMINHOS_DE_IMPLEMENTACAO.md",
        "does not reproduce the copyrighted text",
        "does not determine conformity, certification, legal compliance, or audit success",
    )
    for phrase in required_readme_phrases:
        if phrase not in readme_text:
            errors.append(f"manual README is missing controlled phrase: {phrase}")

    entry_relative = baseline.get("implementation_entry")
    entry_path = manual_root / str(entry_relative)
    entry_text = entry_path.read_text(encoding="utf-8") if entry_path.is_file() else ""
    if len(entry_text) < 8_000:
        errors.append("Manual 02 implementation entry is missing or unexpectedly small")
    entry_normalized = normalized_text(entry_text)
    for path_name in baseline.get("implementation_paths", []):
        if normalized_text(str(path_name)) not in entry_normalized:
            errors.append(f"implementation entry is missing proportional path: {path_name}")
    for topic in baseline.get("required_topics", []):
        if normalized_text(str(topic)) not in entry_normalized:
            errors.append(f"implementation entry is missing required topic: {topic}")

    try:
        required_visuals = int(baseline.get("required_visuals_in_implementation_entry"))
        if required_visuals < 1:
            raise ValueError
    except (TypeError, ValueError):
        errors.append("required_visuals_in_implementation_entry must be a positive integer")
        required_visuals = 0
    if entry_text.count("```mermaid") != required_visuals:
        errors.append("implementation entry has an unexpected number of Mermaid visuals")
    accessibility_label = baseline.get("visual_accessibility_label")
    if not isinstance(accessibility_label, str) or entry_text.count(accessibility_label) != required_visuals:
        errors.append("every implementation-entry visual must have an accessible explanation")
    validate_implementation_structure(entry_text, "en", baseline, required_visuals, errors)

    localized_entries = baseline.get("localized_entry_files")
    localized_phrases = baseline.get("localized_required_phrases")
    accessibility_labels = baseline.get("visual_accessibility_labels")
    if not isinstance(localized_entries, dict) or set(localized_entries) != {"es-419", "pt-BR"}:
        errors.append("localized_entry_files must define exactly es-419 and pt-BR")
        localized_entries = {}
    if not isinstance(localized_phrases, dict):
        errors.append("localized_required_phrases must be an object")
        localized_phrases = {}
    if not isinstance(accessibility_labels, dict):
        errors.append("visual_accessibility_labels must be an object")
        accessibility_labels = {}
    if accessibility_labels.get("en") != accessibility_label:
        errors.append("English visual accessibility label must match the controlled label")

    for language, relative in localized_entries.items():
        if not isinstance(relative, str) or not relative or ".." in Path(relative).parts:
            errors.append(f"invalid localized entry path for {language}: {relative!r}")
            continue
        localized_path = manual_root / relative
        if not localized_path.is_file():
            errors.append(f"localized implementation entry is missing: {language}")
            continue
        localized_text = localized_path.read_text(encoding="utf-8")
        if len(localized_text) < 10_000:
            errors.append(f"localized implementation entry is unexpectedly small: {language}")
        localized_normalized = normalized_text(localized_text)
        phrases = localized_phrases.get(language)
        if not isinstance(phrases, list) or not phrases:
            errors.append(f"localized required phrases are missing: {language}")
            phrases = []
        for phrase in phrases:
            if normalized_text(str(phrase)) not in localized_normalized:
                errors.append(f"{language} entry is missing controlled phrase: {phrase}")
        if localized_text.count("```mermaid") != required_visuals:
            errors.append(f"{language} entry has an unexpected number of Mermaid visuals")
        localized_label = accessibility_labels.get(language)
        if not isinstance(localized_label, str) or localized_text.count(localized_label) != required_visuals:
            errors.append(f"{language} visuals must each have an accessible explanation")
        for source_id in baseline.get("required_source_ids", []):
            if source_id not in localized_text:
                errors.append(f"{language} entry is missing controlled source id: {source_id}")
        validate_implementation_structure(localized_text, language, baseline, required_visuals, errors)

    localized_full_sets_checked = validate_localized_full_sources(
        manual_root, baseline, accessibility_labels, errors
    )

    translations_readme = manual_root / "translations" / "README.md"
    translations_text = (
        translations_readme.read_text(encoding="utf-8") if translations_readme.is_file() else ""
    )
    for phrase in (
        "trilingual full-source review",
        "32-chapter Spanish and Brazilian Portuguese source drafts are present",
        "draft localized sources subject to human review",
        "consolidated single-file masters and derived DOCX/PDF release artifacts remain in development",
    ):
        if phrase not in translations_text:
            errors.append(f"translations README is missing controlled phrase: {phrase}")

    precheck_relative = baseline.get("ai_assisted_precheck")
    precheck_path = manual_root / str(precheck_relative)
    precheck_text = precheck_path.read_text(encoding="utf-8") if precheck_path.is_file() else ""
    for phrase in (
        "AI-assisted precheck only",
        "human gate remains OPEN",
        "must not be treated as human approval",
    ):
        if phrase not in precheck_text:
            errors.append(f"AI-assisted precheck is missing boundary phrase: {phrase}")

    if baseline.get("editorial_qa_status") != "advisory-pass-human-review-open":
        errors.append("editorial QA must remain advisory with human review open")
    editorial_relative = baseline.get("editorial_qa_report")
    editorial_path = manual_root / str(editorial_relative)
    editorial_text = editorial_path.read_text(encoding="utf-8") if editorial_path.is_file() else ""
    for phrase in (
        "Grammar 3 · Logic 2 · Flow 5",
        "does not close the human semantic-review gate",
        "does not determine conformity",
        "EDITORIAL QA STATUS: PASS WITH ADVISORY ITEMS",
    ):
        if phrase not in editorial_text:
            errors.append(f"editorial QA report is missing boundary/result phrase: {phrase}")

    if baseline.get("visual_qa_status") != "conditional-pass-human-accessibility-review-open":
        errors.append("visual QA must retain the human accessibility-review boundary")
    visual_qa_relative = baseline.get("visual_qa_report")
    visual_qa_path = manual_root / str(visual_qa_relative)
    visual_qa_text = visual_qa_path.read_text(encoding="utf-8") if visual_qa_path.is_file() else ""
    for phrase in (
        "30/30 controlled PNG graphics",
        "20/20 localized editable SVG sources",
        "does not close the human semantic-review gate",
        "VISUAL QA STATUS: CONDITIONAL PASS — HUMAN ACCESSIBILITY AND TERMINOLOGY REVIEW OPEN",
    ):
        if phrase not in visual_qa_text:
            errors.append(f"visual QA report is missing boundary/result phrase: {phrase}")

    generator_relative = baseline.get("localized_graphic_generator")
    generator_path = repository_path(
        generator_relative, "localized_graphic_generator", errors
    )
    if generator_path and not generator_path.is_file():
        errors.append("localized graphic generator is missing")

    markdown_relative = baseline.get("english_markdown_master")
    markdown_path = manual_root / str(markdown_relative)
    markdown_text = markdown_path.read_text(encoding="utf-8") if markdown_path.is_file() else ""
    if len(markdown_text) < 90_000:
        errors.append("English Markdown master is missing or unexpectedly small")
    if len(re.findall(r"(?m)^# (?:[1-9]|[12][0-9]|3[0-2])\. ", markdown_text)) != 32:
        errors.append("English Markdown master must contain chapters 1 through 32")

    try:
        required_graphics = int(baseline.get("required_placed_source_graphics"))
        if required_graphics < 1:
            raise ValueError
    except (TypeError, ValueError):
        errors.append("required_placed_source_graphics must be a positive integer")
        required_graphics = 0
    graphics = re.findall(r'<img\s+src="([^"]+)"[^>]*\salt="([^"]+)"\s*/?>', markdown_text)
    if len(graphics) != required_graphics:
        errors.append("English Markdown master has an unexpected number of accessible graphics")
    for source, alt_text in graphics:
        if not alt_text.strip():
            errors.append(f"source graphic has empty alternative text: {source}")
        if source.startswith(("/", "http://", "https://")) or ".." not in Path(source).parts:
            errors.append(f"source graphic must use the controlled relative asset path: {source}")
            continue
        asset_path = (markdown_path.parent / source).resolve()
        if not asset_path.is_relative_to(manual_root.resolve()) or not asset_path.is_file():
            errors.append(f"source graphic is missing or outside Manual 02: {source}")

    docx_relative = baseline.get("english_docx_source")
    docx_path = manual_root / str(docx_relative)
    if not docx_path.is_file() or docx_path.stat().st_size < 500_000:
        errors.append("preserved English DOCX source is missing or unexpectedly small")
    else:
        try:
            with zipfile.ZipFile(docx_path) as archive:
                document_xml = ET.fromstring(archive.read("word/document.xml"))
            tables = document_xml.findall(f".//{{{WORD_NS}}}tbl")
            required_docx_tables = int(baseline.get("required_docx_data_tables"))
            if len(tables) != required_docx_tables:
                errors.append(f"English DOCX must contain {required_docx_tables} controlled data tables")
            layout_tables = 0
            for table_index, table in enumerate(tables, start=1):
                rows = table.findall(f"{{{WORD_NS}}}tr")
                cells = rows[0].findall(f"{{{WORD_NS}}}tc") if rows else []
                if len(rows) == 1 and len(cells) == 1:
                    layout_tables += 1
                header = rows[0].find(f"{{{WORD_NS}}}trPr/{{{WORD_NS}}}tblHeader") if rows else None
                if header is None:
                    errors.append(f"English DOCX data table {table_index} lacks header-row metadata")
            if layout_tables != int(baseline.get("required_docx_layout_tables")):
                errors.append("English DOCX contains an unexpected number of layout tables")
            image_descriptions = document_xml.findall(f".//{{{DRAWING_NS}}}docPr")
            if len(image_descriptions) != required_graphics:
                errors.append("English DOCX has an unexpected number of placed image descriptions")
            for image in image_descriptions:
                if not str(image.get("descr", "")).strip():
                    errors.append("English DOCX contains an image without alternative text")
        except (KeyError, TypeError, ValueError, zipfile.BadZipFile, ET.ParseError) as exc:
            errors.append(f"English DOCX accessibility structure could not be validated: {exc}")

    required_source_ids = baseline.get("required_source_ids")
    if not isinstance(required_source_ids, list) or not required_source_ids:
        errors.append("required_source_ids must be a non-empty list")
        required_source_ids = []
    source_by_id = {
        item.get("id"): item
        for item in registry.get("sources", [])
        if isinstance(item, dict) and item.get("id")
    }
    for source_id in required_source_ids:
        source = source_by_id.get(source_id)
        if source is None:
            errors.append(f"required ISO source is absent from registry: {source_id}")
            continue
        if source.get("status") != "final":
            errors.append(f"required ISO source must have final status: {source_id}")
        parsed = urlparse(str(source.get("url", "")))
        if parsed.scheme != "https" or parsed.hostname not in APPROVED_SOURCE_DOMAINS:
            errors.append(f"required source is not on the approved official ISO domain: {source_id}")
        if source_id not in entry_text or source_id not in readme_text:
            errors.append(f"controlled source id must appear in README and implementation entry: {source_id}")
        try:
            verified = dt.date.fromisoformat(str(source.get("last_verified")))
            interval = int(source.get("review_interval_days"))
            if dt.date.today() > verified + dt.timedelta(days=interval):
                errors.append(f"required source review is overdue: {source_id}")
        except (TypeError, ValueError):
            errors.append(f"required source has invalid verification metadata: {source_id}")

    catalog_matches = [
        item
        for item in catalog.get("manuals", [])
        if isinstance(item, dict) and item.get("id") == "iso-42001-aims"
    ]
    if len(catalog_matches) != 1:
        errors.append("manual catalog must contain exactly one iso-42001-aims entry")
    else:
        catalog_entry = catalog_matches[0]
        if catalog_entry.get("path") != baseline.get("manual_path"):
            errors.append("Manual 02 catalog path does not match baseline")
        if catalog_entry.get("status") != "development":
            errors.append("Manual 02 catalog status must remain development")
        if catalog_entry.get("layout") != "controlled-build" or catalog_entry.get("series_order") != 2:
            errors.append("Manual 02 catalog must use controlled-build layout and series_order 2")

    if not WORKFLOW_PATH.is_file():
        errors.append("dedicated Manual 02 QA workflow is missing")
    else:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")
        for control in (
            "permissions:\n  contents: read",
            "pull_request:",
            "python3 scripts/iso_42001_manual_02_qa.py",
        ):
            if control not in workflow_text:
                errors.append(f"Manual 02 workflow is missing control: {control!r}")
        if re.search(r"(?m)^\s*push:\s*$", workflow_text):
            errors.append("Manual 02 QA workflow must not push changes")

    print("ISO/IEC 42001 Manual 02 QA")
    print(f"  proportional paths checked: {len(baseline.get('implementation_paths', []))}")
    print(f"  implementation visuals checked: {required_visuals}")
    print(f"  localized implementation entries checked: {len(localized_entries)}")
    print(f"  localized 32-chapter source sets checked: {localized_full_sets_checked}")
    print(f"  placed source graphics checked: {required_graphics}")
    print(f"  controlled sources checked: {len(required_source_ids)}")
    print(f"  required topics checked: {len(baseline.get('required_topics', []))}")
    print("  editorial QA advisory checked: 1")
    print("  visual QA review checked: 1")
    for error in errors:
        print(f"  ERROR: {error}")
    if errors:
        print("FAIL: Manual 02 integrity gate did not pass")
        return 1
    print("PASS: Manual 02 integrity gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
