#!/usr/bin/env python3
"""Read-only audit for Batch 4 localized figures: NIST RMF and Incident Response."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
REPORT = ROOT / "qa/images/NIST_RMF_INCIDENT_RESPONSE_LOCALIZED_FIGURE_AUDIT.md"
FAMILIES = ("NIST RMF / SP 800-53", "Incident Response / BCDR")
EXPECTED_PER_FAMILY = 10
EXPECTED_TOTAL = 20


def digest(data: bytes) -> str:
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

    counts = Counter(record["manual_family"] for record in records)
    for family in FAMILIES:
        if counts[family] != EXPECTED_PER_FAMILY:
            raise SystemExit(f"Expected {EXPECTED_PER_FAMILY} {family} records, found {counts[family]}")

    source_keys: set[tuple[str, str, str]] = set()
    destination_exists = 0
    rows: list[str] = []

    for record in sorted(records, key=lambda item: (item["manual_family"], item.get("figure_number", 0))):
        if record.get("language") != "Brazilian Portuguese":
            raise SystemExit(f"Unexpected language for {record['id']}: {record.get('language')}")
        if not record.get("requires_localization"):
            raise SystemExit(f"Localization flag missing for {record['id']}")
        if not record.get("recoverable") or record.get("no_trustworthy_source"):
            raise SystemExit(f"Unrecoverable or untrusted record: {record['id']}")

        evidence = record["english_source_evidence"]
        container = ROOT / evidence["container"]
        if not container.is_file():
            raise SystemExit(f"Missing source DOCX: {container}")

        with ZipFile(container) as archive:
            if evidence["internal_path"] not in archive.namelist():
                raise SystemExit(f"Missing internal source asset for {record['id']}")
            raw = archive.read(evidence["internal_path"])

        if digest(raw) != evidence["sha256"]:
            raise SystemExit(f"Source SHA-256 mismatch for {record['id']}")
        if len(raw) != evidence["size_bytes"]:
            raise SystemExit(f"Source byte-count mismatch for {record['id']}")

        with Image.open(BytesIO(raw)) as image:
            image.verify()
        with Image.open(BytesIO(raw)) as image:
            width, height = image.size
            image_format = image.format

        markdown = ROOT / record["markdown_file"]
        if not markdown.is_file():
            raise SystemExit(f"Missing Markdown file: {markdown}")
        text = markdown.read_text(encoding="utf-8")
        if record["exact_image_path"] not in text:
            raise SystemExit(f"Missing exact Markdown image path for {record['id']}")

        destination = ROOT / record["localized_asset_path_checked"]
        if destination.exists():
            destination_exists += 1
            raise SystemExit(f"Localized destination must remain absent during audit: {destination}")

        source_keys.add((evidence["container"], evidence["internal_path"], evidence["sha256"]))
        rows.append(
            "| {id} | {family} | {figure} | `{source}` | `{internal}` | {width}×{height} {fmt} | `{destination}` |".format(
                id=record["id"],
                family=record["manual_family"],
                figure=record.get("figure_number", ""),
                source=evidence["container"],
                internal=evidence["internal_path"],
                width=width,
                height=height,
                fmt=image_format,
                destination=record["localized_asset_path_checked"],
            )
        )

    if len(source_keys) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} unique authoritative source assets, found {len(source_keys)}")

    report = [
        "# NIST RMF and Incident Response Localized Figure Audit",
        "",
        "Read-only Batch 4 audit. No localized image, Markdown, DOCX, or PDF was modified.",
        "",
        f"- Total unresolved reference records: **{len(records)}**",
        f"- NIST RMF / SP 800-53 records: **{counts['NIST RMF / SP 800-53']}**",
        f"- Incident Response / BCDR records: **{counts['Incident Response / BCDR']}**",
        f"- Unique authoritative English source assets: **{len(source_keys)}**",
        f"- Existing localized destination files: **{destination_exists}**",
        "- Language scope: **Brazilian Portuguese only**",
        "- Classification: **requires localization**",
        "",
        "| Inventory ID | Family | Figure | Source DOCX | Internal source asset | Verified source image | Missing destination |",
        "|---|---|---:|---|---|---|---|",
        *rows,
        "",
        "All 20 records have trusted embedded English-source assets, exact Markdown references, verified SHA-256 values and byte counts, valid source images, and absent localized destinations.",
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Audited {len(records)} Batch 4 localized figure records.")


if __name__ == "__main__":
    main()
