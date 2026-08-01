#!/usr/bin/env python3
"""Read-only audit for ISO/IEC 27001/27002 and PCI DSS v4.0.1 localized figures."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
REPORT = ROOT / "qa/images/ISO27001_PCI_LOCALIZED_FIGURE_AUDIT.md"
FAMILIES = ("ISO/IEC 27001/27002", "PCI DSS v4.0.1")
EXPECTED_PER_FAMILY = 9
EXPECTED_TOTAL = 18


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    records = [
        record
        for record in data["references"]
        if record.get("manual_family") in FAMILIES
        and record.get("primary_classification") == "requires_localization"
    ]

    if len(records) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} unresolved records, found {len(records)}")

    counts = {family: 0 for family in FAMILIES}
    rows: list[str] = []
    source_assets: set[tuple[str, str, str]] = set()

    for record in records:
        family = record["manual_family"]
        counts[family] += 1

        if record.get("language") != "Brazilian Portuguese":
            raise SystemExit(f"Unexpected language for {record['id']}: {record.get('language')}")
        if not record.get("recoverable") or not record.get("requires_localization"):
            raise SystemExit(f"Invalid classification flags for {record['id']}")
        if record.get("no_trustworthy_source") or record.get("obsolete"):
            raise SystemExit(f"Unexpected source/obsolete flag for {record['id']}")

        markdown = ROOT / record["markdown_file"]
        if not markdown.is_file():
            raise SystemExit(f"Missing Markdown file for {record['id']}: {markdown}")
        markdown_text = markdown.read_text(encoding="utf-8")
        image_path = record["exact_image_path"]
        if image_path not in markdown_text:
            raise SystemExit(f"Markdown reference not found for {record['id']}: {image_path}")

        localized = ROOT / record["localized_asset_path_checked"]
        if localized.exists():
            raise SystemExit(f"Localized destination unexpectedly exists for {record['id']}: {localized}")

        evidence = record["english_source_evidence"]
        container = ROOT / evidence["container"]
        internal_path = evidence["internal_path"]
        if not container.is_file():
            raise SystemExit(f"Missing authoritative DOCX for {record['id']}: {container}")
        with ZipFile(container) as archive:
            try:
                source_bytes = archive.read(internal_path)
            except KeyError as exc:
                raise SystemExit(f"Missing authoritative source asset for {record['id']}: {internal_path}") from exc

        digest = sha256(source_bytes)
        if digest != evidence["sha256"]:
            raise SystemExit(
                f"Source SHA-256 mismatch for {record['id']}: expected {evidence['sha256']}, got {digest}"
            )
        if len(source_bytes) != evidence["size_bytes"]:
            raise SystemExit(
                f"Source size mismatch for {record['id']}: expected {evidence['size_bytes']}, got {len(source_bytes)}"
            )

        source_assets.add((evidence["container"], internal_path, digest))
        rows.append(
            "| {id} | {family} | {figure} | `{source}` | `{destination}` |".format(
                id=record["id"],
                family=family,
                figure=record.get("figure_number", ""),
                source=internal_path,
                destination=record["localized_asset_path_checked"],
            )
        )

    for family, count in counts.items():
        if count != EXPECTED_PER_FAMILY:
            raise SystemExit(f"Expected {EXPECTED_PER_FAMILY} records for {family}, found {count}")

    report = "\n".join(
        [
            "# ISO/IEC 27001/27002 and PCI DSS Localized Figure Audit",
            "",
            "## Result",
            "",
            "**PASS — exact restoration scope confirmed.**",
            "",
            f"- Total unresolved reference records: **{len(records)}**",
            f"- ISO/IEC 27001/27002 records: **{counts['ISO/IEC 27001/27002']}**",
            f"- PCI DSS v4.0.1 records: **{counts['PCI DSS v4.0.1']}**",
            f"- Unique authoritative English source assets: **{len(source_assets)}**",
            "- Target language: **Brazilian Portuguese**",
            "- Existing localized destination files: **0**",
            "- All authoritative DOCX assets matched recorded SHA-256 and byte size.",
            "- All current Markdown files contain their recorded image paths.",
            "",
            "All source graphics contain visible English text according to the provenance inventory and therefore require localized reconstruction before promotion.",
            "",
            "## Records",
            "",
            "| Inventory ID | Family | Figure | Authoritative DOCX asset | Planned localized destination |",
            "|---|---|---:|---|---|",
            *rows,
            "",
            "## Safety status",
            "",
            "This audit is read-only. No image, manual, generated package, release, `main`, or PR #3 content is modified.",
            "",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
