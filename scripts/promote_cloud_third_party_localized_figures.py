#!/usr/bin/env python3
"""Promote owner-approved Batch 5 Brazilian Portuguese localized figures."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from PIL import Image

from validate_provenance_inventory_summary import reconcile_summary, validate_summary


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
REVIEW_DIR = ROOT / "review/cloud-third-party-localized-figures"
MANIFEST = REVIEW_DIR / "manifest.json"
FAMILIES = (
    "Cloud Security and Compliance",
    "Third-Party Risk and Supply Chain Security",
)
EXPECTED_IDS = {f"LEGACY-IMG-{number:03d}" for number in range(63, 83)}
EXPECTED_PER_FAMILY = 10
EXPECTED_TOTAL = 20
EXPECTED_LANGUAGE = "Brazilian Portuguese"
EXPECTED_STATUS = "review_only_pending_owner_approval"
RECONSTRUCTION_DESCRIPTION = (
    "Programmatic localized reconstruction; not an exact visual reproduction."
)
APPROVAL_PATTERN = re.compile(r"^Issue #28 owner approval comment [1-9][0-9]*$")
ALLOWED_MARKDOWN = {
    "Cloud Security and Compliance": (
        "06-cloud-and-technology-risk/Cloud_Security_and_Compliance/Portugues_BR/"
        "Cloud_Security_and_Cloud_Compliance_Practical_Manager_and_Junior_Analyst_"
        "Manual_Portugues_BR_v1.0.md"
    ),
    "Third-Party Risk and Supply Chain Security": (
        "07-third-party-risk/Third_Party_Risk_and_Supply_Chain/Portugues_BR/"
        "Third_Party_Risk_Management_and_Cyber_Supply_Chain_Security_Manual_"
        "Portugues_BR_v1.0.md"
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def verify_png(path: Path, expected_size: tuple[int, int]) -> None:
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        if image.format != "PNG" or image.size != expected_size:
            raise SystemExit(
                f"PNG validation failed for {path}: "
                f"{image.format} {image.size}, expected PNG {expected_size}"
            )


def authoritative_size(record: dict) -> tuple[int, int]:
    evidence = record["english_source_evidence"]
    container = ROOT / evidence["container"]
    with ZipFile(container) as archive:
        source = archive.read(evidence["internal_path"])
    if sha256_bytes(source) != evidence["sha256"] or len(source) != evidence["size_bytes"]:
        raise SystemExit(f"Authoritative source evidence mismatch for {record['id']}")
    with Image.open(BytesIO(source)) as image:
        image.verify()
    with Image.open(BytesIO(source)) as image:
        return image.size


def expected_review_path(record: dict) -> str:
    slug = (
        "cloud-security"
        if record["manual_family"] == "Cloud Security and Compliance"
        else "third-party-risk"
    )
    return (
        "review/cloud-third-party-localized-figures/"
        f"pt-BR-{slug}-image{record['figure_number']}.png"
    )


def normalize_reference(text: str, image_path: str, alt_text: str) -> str:
    replacement = f"![{alt_text.replace('[', '(').replace(']', ')')}]({image_path})"
    escaped = re.escape(image_path)
    html = re.compile(
        rf"<img\b(?=[^>]*\bsrc\s*=\s*['\"]{escaped}['\"])[^>]*?/?>",
        re.IGNORECASE | re.DOTALL,
    )
    markdown = re.compile(rf"!\[[^\]]*\]\({escaped}\)(?:\{{[^}}]*\}})?")
    matches = len(html.findall(text)) + len(markdown.findall(text))
    if matches != 1:
        raise SystemExit(
            f"Expected exactly one image reference for {image_path}, found {matches}"
        )
    return html.sub(replacement, text, count=1) if html.search(text) else markdown.sub(
        replacement, text, count=1
    )


def load_and_validate() -> tuple[dict, list[dict], dict[str, dict]]:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    validate_summary(inventory)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = [
        record
        for record in inventory["references"]
        if record.get("id") in EXPECTED_IDS
    ]
    if len(manifest) != EXPECTED_TOTAL or len(records) != EXPECTED_TOTAL:
        raise SystemExit("Batch 5 requires exactly 20 manifest and inventory records")
    if {item.get("inventory_id") for item in manifest} != EXPECTED_IDS:
        raise SystemExit("Manifest IDs are not exactly LEGACY-IMG-063 through 082")
    if {record["id"] for record in records} != EXPECTED_IDS:
        raise SystemExit("Inventory IDs are not exactly LEGACY-IMG-063 through 082")
    expected_counts = Counter({family: EXPECTED_PER_FAMILY for family in FAMILIES})
    if Counter(item["manual_family"] for item in manifest) != expected_counts:
        raise SystemExit("Manifest family counts are not exactly 10 and 10")
    if Counter(record["manual_family"] for record in records) != expected_counts:
        raise SystemExit("Inventory family counts are not exactly 10 and 10")

    records_by_id = {record["id"]: record for record in records}
    review_paths: set[str] = set()
    destinations: set[str] = set()
    markdown_updates: dict[Path, str] = {}
    for item in manifest:
        record = records_by_id[item["inventory_id"]]
        family = record["manual_family"]
        if (
            item.get("manual_family") != family
            or record.get("language") != EXPECTED_LANGUAGE
            or item.get("language") != EXPECTED_LANGUAGE
            or item.get("status") != EXPECTED_STATUS
            or item.get("description") != RECONSTRUCTION_DESCRIPTION
            or record.get("primary_classification") != "requires_localization"
        ):
            raise SystemExit(f"Review/provenance classification mismatch for {record['id']}")
        if item.get("review_file") != expected_review_path(record):
            raise SystemExit(f"Unexpected review path for {record['id']}")
        if item["review_file"] in review_paths:
            raise SystemExit(f"Duplicate review path: {item['review_file']}")
        review_paths.add(item["review_file"])
        review = ROOT / item["review_file"]
        if not review.is_file() or sha256_file(review) != item["sha256"]:
            raise SystemExit(f"Missing or mismatched review PNG for {record['id']}")
        source_size = authoritative_size(record)
        if (item["width"], item["height"]) != source_size:
            raise SystemExit(f"Authoritative dimension mismatch for {record['id']}")
        verify_png(review, source_size)

        if record["markdown_file"] != ALLOWED_MARKDOWN[family]:
            raise SystemExit(f"Unexpected Markdown path for {record['id']}")
        markdown = ROOT / record["markdown_file"]
        current = markdown_updates.setdefault(
            markdown, markdown.read_text(encoding="utf-8")
        )
        markdown_updates[markdown] = normalize_reference(
            current, record["exact_image_path"], item["alt_text"]
        )

        destination_path = record["localized_asset_path_checked"]
        destination = ROOT / destination_path
        if destination.name != Path(record["exact_image_path"]).name:
            raise SystemExit(f"Destination filename mismatch for {record['id']}")
        if destination.parent != (ROOT / record["markdown_file"]).parent / "media":
            raise SystemExit(f"Destination directory mismatch for {record['id']}")
        if destination_path in destinations or destination.exists():
            raise SystemExit(f"Duplicate or existing destination for {record['id']}")
        destinations.add(destination_path)

    if len(review_paths) != EXPECTED_TOTAL or len(destinations) != EXPECTED_TOTAL:
        raise SystemExit("Review/destination uniqueness validation failed")
    if set(markdown_updates) != {ROOT / path for path in ALLOWED_MARKDOWN.values()}:
        raise SystemExit("Expected exactly two affected Markdown files")
    return inventory, manifest, records_by_id


def promote(approval_evidence: str) -> None:
    if not APPROVAL_PATTERN.fullmatch(approval_evidence):
        raise SystemExit(
            "Promotion requires 'Issue #28 owner approval comment <numeric-id>'"
        )
    inventory, manifest, records_by_id = load_and_validate()
    markdown_updates: dict[Path, str] = {}
    for item in manifest:
        record = records_by_id[item["inventory_id"]]
        review = ROOT / item["review_file"]
        destination = ROOT / record["localized_asset_path_checked"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(review, destination)
        if sha256_file(destination) != item["sha256"]:
            raise SystemExit(f"Promoted SHA-256 mismatch for {record['id']}")
        verify_png(destination, (item["width"], item["height"]))

        markdown = ROOT / record["markdown_file"]
        current = markdown_updates.setdefault(
            markdown, markdown.read_text(encoding="utf-8")
        )
        markdown_updates[markdown] = normalize_reference(
            current, record["exact_image_path"], item["alt_text"]
        )
        record.update(
            {
                "localized_asset_exists": True,
                "brazilian_portuguese_localized_asset_exists": True,
                "primary_classification": "restored_localized",
                "restoration_status": "restored",
                "localization_status": "localized_brazilian_portuguese",
                "validation_status": (
                    "technical_validation_passed_owner_visual_review_approved"
                ),
                "restored_destination": record["localized_asset_path_checked"],
                "localized_image_sha256": item["sha256"],
                "localized_image_format": "PNG",
                "localized_image_dimensions": {
                    "width": item["width"],
                    "height": item["height"],
                },
                "owner_approval_evidence": approval_evidence,
                "restoration_description": RECONSTRUCTION_DESCRIPTION,
            }
        )
    for path, text in markdown_updates.items():
        path.write_text(text, encoding="utf-8", newline="\n")
    reconcile_summary(inventory)
    validate_summary(inventory)
    INVENTORY.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Promoted exactly 20 approved Batch 5 figures: {approval_evidence}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--approval-evidence")
    parser.add_argument("--validate-review-only", action="store_true")
    args = parser.parse_args()
    if args.validate_review_only:
        load_and_validate()
        print("All 20 Batch 5 review figures are promotion-ready.")
        return
    if not args.approval_evidence:
        raise SystemExit("Promotion requires --approval-evidence")
    promote(args.approval_evidence)


if __name__ == "__main__":
    main()
