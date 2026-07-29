#!/usr/bin/env python3
"""Read-only audit for Batch 5 Cloud and Third-Party Risk localized figures."""

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
REPORT = ROOT / "qa/images/CLOUD_THIRD_PARTY_LOCALIZED_FIGURE_AUDIT.md"
FAMILIES = (
    "Cloud Security and Compliance",
    "Third-Party Risk and Supply Chain Security",
)
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
    review_keys: set[tuple[str, str]] = set()
    destination_paths: set[str] = set()
    rows: list[str] = []

    for record in sorted(records, key=lambda item: (item["manual_family"], item["figure_number"])):
        if record.get("language") != "Brazilian Portuguese":
            raise SystemExit(f"Unexpected language for {record['id']}: {record.get('language')}")
        if not record.get("requires_localization"):
            raise SystemExit(f"Localization flag missing for {record['id']}")
        if not record.get("recoverable") or record.get("no_trustworthy_source"):
            raise SystemExit(f"Unrecoverable or untrusted record: {record['id']}")
        if record.get("duplicate_reference") or record.get("duplicate_reference_locations"):
            raise SystemExit(f"Duplicate Markdown reference recorded for {record['id']}")

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
        reference_count = markdown.read_text(encoding="utf-8").count(record["exact_image_path"])
        if reference_count != 1:
            raise SystemExit(
                f"Expected one exact Markdown path for {record['id']}, found {reference_count}"
            )

        destination = ROOT / record["localized_asset_path_checked"]
        if destination.exists():
            raise SystemExit(f"Localized destination must remain absent during audit: {destination}")
        if record["localized_asset_path_checked"] in destination_paths:
            raise SystemExit(f"Duplicate localized destination: {record['localized_asset_path_checked']}")
        destination_paths.add(record["localized_asset_path_checked"])

        source_key = (evidence["container"], evidence["internal_path"], evidence["sha256"])
        if source_key in source_keys:
            raise SystemExit(f"Duplicate authoritative source asset for {record['id']}")
        source_keys.add(source_key)
        review_key = (record["manual_family"], record["exact_image_path"])
        if review_key in review_keys:
            raise SystemExit(f"Duplicate family/image path for {record['id']}")
        review_keys.add(review_key)

        rows.append(
            "| {id} | {family} | {figure} | `{source}` | `{internal}` | `{sha}` | "
            "{width}×{height} {fmt} | `{markdown}` → `{image}` | `{destination}` |".format(
                id=record["id"],
                family=record["manual_family"],
                figure=record["figure_number"],
                source=evidence["container"],
                internal=evidence["internal_path"],
                sha=evidence["sha256"],
                width=width,
                height=height,
                fmt=image_format,
                markdown=record["markdown_file"],
                image=record["exact_image_path"],
                destination=record["localized_asset_path_checked"],
            )
        )

    report = [
        "# Cloud and Third-Party Risk Localized Figure Audit",
        "",
        "Read-only Batch 5 audit. No localized image, Markdown, DOCX, or PDF was modified.",
        "",
        f"- Total unresolved reference records: **{len(records)}**",
        f"- Cloud Security and Compliance records: **{counts['Cloud Security and Compliance']}**",
        f"- Third-Party Risk and Supply Chain Security records: **{counts['Third-Party Risk and Supply Chain Security']}**",
        f"- Unique authoritative English source assets: **{len(source_keys)}**",
        f"- Unique localized destinations: **{len(destination_paths)}**",
        "- Existing localized destination files: **0**",
        "- Duplicate references or destinations: **0**",
        "- Language scope: **Brazilian Portuguese only**",
        "- Classification: **requires localization**",
        "",
        "| Inventory ID | Family | Figure | Source DOCX | Internal source | SHA-256 | Verified source | Markdown reference | Missing destination |",
        "|---|---|---:|---|---|---|---|---|---|",
        *rows,
        "",
        "All 20 records have trusted embedded English-source assets, exact single Markdown references, verified SHA-256 values and byte counts, valid source images, unique destinations, and absent localized files.",
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8", newline="\n")
    print(f"Audited {len(records)} Batch 5 localized figure records.")


if __name__ == "__main__":
    main()
