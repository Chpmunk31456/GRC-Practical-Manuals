#!/usr/bin/env python3
"""Promote owner-approved ISO/IEC 27001 and PCI DSS localized review figures."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
MANIFEST = ROOT / "review/iso27001-pci-dss-localized-figures/manifest.json"
FAMILIES = ("ISO/IEC 27001/27002", "PCI DSS v4.0.1")
EXPECTED_TOTAL = 18
APPROVAL = "Issue #22 owner approval comment 5112334399"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def markdown_reference(alt_text: str, image_path: str) -> str:
    alt = (alt_text or "Figura localizada").replace("[", "(").replace("]", ")")
    return f"![{alt}]({image_path})"


def normalize_reference(text: str, image_path: str, alt_text: str) -> str:
    replacement = markdown_reference(alt_text, image_path)
    escaped = re.escape(image_path)

    html_pattern = re.compile(
        rf"<img\b(?=[^>]*\bsrc\s*=\s*['\"]{escaped}['\"])[^>]*?/?>",
        flags=re.IGNORECASE | re.DOTALL,
    )
    md_pattern = re.compile(rf"!\[[^\]]*\]\({escaped}\)")

    html_matches = list(html_pattern.finditer(text))
    md_matches = list(md_pattern.finditer(text))
    total = len(html_matches) + len(md_matches)
    if total != 1:
        raise SystemExit(f"Expected exactly one image reference for {image_path}, found {total}")

    if html_matches:
        return html_pattern.sub(replacement, text, count=1)
    return md_pattern.sub(replacement, text, count=1)


def main() -> None:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if len(manifest) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} manifest records, found {len(manifest)}")

    by_id = {item["inventory_id"]: item for item in manifest}
    records = [
        record
        for record in inventory["references"]
        if record.get("manual_family") in FAMILIES
        and record.get("primary_classification") == "requires_localization"
    ]
    if len(records) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} inventory records, found {len(records)}")
    if set(by_id) != {record["id"] for record in records}:
        raise SystemExit("Manifest and inventory record sets do not match")

    changed_markdown: dict[Path, str] = {}
    for record in records:
        item = by_id[record["id"]]
        source = ROOT / item["review_file"]
        destination = ROOT / record["localized_asset_path_checked"]
        if not source.is_file():
            raise SystemExit(f"Missing approved review file: {source}")
        if sha256(source) != item["sha256"]:
            raise SystemExit(f"Review SHA-256 mismatch: {source}")
        with Image.open(source) as image:
            image.verify()
        with Image.open(source) as image:
            if image.format != "PNG" or image.size != (item["width"], item["height"]):
                raise SystemExit(f"Review image validation failed: {source}")

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if sha256(destination) != item["sha256"]:
            raise SystemExit(f"Promoted SHA-256 mismatch: {destination}")

        markdown_path = ROOT / record["markdown_file"]
        current = changed_markdown.get(markdown_path)
        if current is None:
            current = markdown_path.read_text(encoding="utf-8")
        current = normalize_reference(current, record["exact_image_path"], record.get("alt_text", ""))
        changed_markdown[markdown_path] = current

        record.update(
            {
                "localized_asset_exists": True,
                "brazilian_portuguese_localized_asset_exists": True,
                "primary_classification": "restored_localized",
                "validation_status": "technical_validation_passed_owner_visual_review_approved",
                "restored_destination": record["localized_asset_path_checked"],
                "localized_image_sha256": item["sha256"],
                "localized_image_format": "PNG",
                "localized_image_dimensions": {"width": item["width"], "height": item["height"]},
                "owner_approval_evidence": APPROVAL,
                "restoration_description": "Programmatic localized reconstruction; not an exact visual reproduction.",
            }
        )

    for path, text in changed_markdown.items():
        path.write_text(text, encoding="utf-8")

    inventory["summary"]["total_unresolved_references"] -= EXPECTED_TOTAL
    inventory["summary"]["total_restored_localized_references"] += EXPECTED_TOTAL
    inventory["summary"]["totals_by_manual"]["ISO/IEC 27001/27002"] = 0
    inventory["summary"]["totals_by_manual"]["PCI DSS v4.0.1"] = 0
    inventory["summary"]["totals_by_language"]["Brazilian Portuguese"] -= EXPECTED_TOTAL
    inventory["summary"]["totals_by_primary_classification"]["requires_localization"] -= EXPECTED_TOTAL
    inventory["summary"]["totals_by_primary_classification"]["restored_localized"] += EXPECTED_TOTAL

    INVENTORY.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Promoted and recorded {EXPECTED_TOTAL} approved localized figures.")


if __name__ == "__main__":
    main()
