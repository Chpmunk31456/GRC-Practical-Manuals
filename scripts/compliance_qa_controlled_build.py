#!/usr/bin/env python3
"""Controlled-build-aware fail-closed repository QA compatibility layer.

Preserves the existing compliance_qa checks while adding explicit publication
validation for manuals whose catalog layout is ``controlled-build``. Published
controlled-build manuals must have identifiable English, es-419, and pt-BR
Markdown, DOCX, and PDF artifacts; this layer is not an exemption from the
publication controls.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import compliance_qa as base


ES_MARKERS = ("es-419", "spanish_es-419", "spanish/", "espanol", "español")
PT_MARKERS = ("pt-br", "portuguese_pt-br", "portuguese/", "portugues")


def _language_files(directory: Path, language: str) -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {ext: [] for ext in base.PUBLISHED_FORMATS}
    for path in directory.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in base.PUBLISHED_FORMATS:
            continue
        rel = path.relative_to(directory).as_posix().lower()
        filename = path.name.lower()
        es = any(marker in rel or marker in filename for marker in ES_MARKERS)
        pt = any(marker in rel or marker in filename for marker in PT_MARKERS)
        if language == "en" and not es and not pt:
            found[path.suffix.lower()].append(path)
        elif language == "es-419" and es:
            found[path.suffix.lower()].append(path)
        elif language == "pt-BR" and pt:
            found[path.suffix.lower()].append(path)
    return found


def _require_controlled_language_artifacts(
    result: base.CheckResult, directory: Path, language: str
) -> None:
    artifacts = _language_files(directory, language)
    for extension in base.PUBLISHED_FORMATS:
        if not artifacts[extension]:
            result.errors.append(
                f"controlled-build {language} package lacks {extension}: "
                f"{directory.relative_to(base.REPO_ROOT)}"
            )


def check_structure() -> base.CheckResult:
    result = base.CheckResult("manual structure")
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
        if not (base.REPO_ROOT / relative).is_file():
            result.errors.append(f"missing required root file: {relative}")
    for relative in required_sections:
        section = base.REPO_ROOT / relative
        if not section.is_dir():
            result.errors.append(f"missing required section: {relative}")
        elif not (section / "README.md").is_file():
            result.errors.append(f"missing section README: {relative}/README.md")

    try:
        catalog = base.load_json(base.CATALOG_PATH)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result

    checked = 0
    for manual in catalog.get("manuals", []):
        if manual.get("status") not in {"published", "development"}:
            continue
        relative = manual.get("path", "")
        directory = base.REPO_ROOT / relative
        checked += 1
        if not directory.is_dir():
            result.errors.append(f"cataloged {manual['status']} path is missing: {relative}")
            continue
        if not (directory / "README.md").is_file():
            result.errors.append(f"missing manual README: {relative}/README.md")
        if manual.get("status") != "published":
            continue

        artifacts = base.files_with_extensions(directory, base.PUBLISHED_FORMATS)
        for extension, matches in artifacts.items():
            if not matches:
                result.errors.append(f"published manual lacks {extension} artifact: {relative}")

        if manual.get("layout") == "controlled-build":
            if not _language_files(directory, "en")[".md"]:
                result.errors.append(
                    f"published controlled-build manual lacks an identifiable English source: {relative}"
                )
        elif not any(path.name.startswith("English_Source_") for path in artifacts[".md"]):
            english_dir = directory / "English"
            if not english_dir.is_dir() or not list(english_dir.glob("*.md")):
                result.errors.append(f"published manual lacks an identifiable English source: {relative}")

    result.details = {"active_manual_paths_checked": checked}
    return result


def check_translations() -> base.CheckResult:
    result = base.CheckResult("trilingual publication parity")
    try:
        catalog = base.load_json(base.CATALOG_PATH)
    except ValueError as exc:
        result.errors.append(str(exc))
        return result

    checked = 0
    for manual in catalog.get("manuals", []):
        if manual.get("status") != "published":
            continue
        directory = base.REPO_ROOT / manual["path"]
        layout = manual.get("layout")
        checked += 1
        if layout == "standard":
            base.require_language_artifacts(result, directory, "English/root")
            base.require_language_artifacts(result, directory / "Espanol", "es-419")
            base.require_language_artifacts(result, directory / "Portugues_BR", "pt-BR")
        elif layout == "language-directories":
            base.require_language_artifacts(result, directory / "English", "English")
            base.require_language_artifacts(result, directory / "Espanol", "es-419")
            base.require_language_artifacts(result, directory / "Portugues_BR", "pt-BR")
        elif layout == "controlled-build":
            _require_controlled_language_artifacts(result, directory, "en")
            _require_controlled_language_artifacts(result, directory, "es-419")
            _require_controlled_language_artifacts(result, directory, "pt-BR")
        else:
            result.errors.append(
                f"published manual uses a non-publication layout: {manual['id']} ({layout})"
            )

    result.details = {"published_manuals_checked": checked}
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("catalog", "structure", "translations", "crosswalks", "workflow-security"):
        subparsers.add_parser(name)
    sources = subparsers.add_parser("sources")
    sources.add_argument("--network", action="store_true")
    release = subparsers.add_parser("release")
    release.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    commands = {
        "catalog": [base.check_catalog],
        "structure": [check_structure],
        "translations": [check_translations],
        "crosswalks": [base.check_crosswalks],
        "workflow-security": [base.check_workflow_security],
    }
    if args.command == "sources":
        return base.run_results([base.check_sources(network=args.network)])
    if args.command == "release":
        checks = [
            base.check_catalog(),
            check_structure(),
            base.check_sources(network=False),
            check_translations(),
            base.check_crosswalks(),
            base.check_workflow_security(),
            base.check_zenodo(),
        ]
        return base.run_results(checks, output=args.output)
    return base.run_results([function() for function in commands[args.command]])


if __name__ == "__main__":
    sys.exit(main())
