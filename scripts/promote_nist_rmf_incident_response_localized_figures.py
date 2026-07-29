#!/usr/bin/env python3
"""Promote owner-approved Batch 4 Brazilian Portuguese localized figures."""

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


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
REVIEW_DIR = ROOT / "review/nist-rmf-incident-response-localized-figures"
MANIFEST = REVIEW_DIR / "manifest.json"
FAMILIES = ("NIST RMF / SP 800-53", "Incident Response / BCDR")
EXPECTED_PER_FAMILY = 10
EXPECTED_TOTAL = 20
EXPECTED_LANGUAGE = "Brazilian Portuguese"
EXPECTED_STATUS = "review_only_pending_owner_approval"
RECONSTRUCTION_DESCRIPTION = (
    "Programmatic localized reconstruction; not an exact visual reproduction."
)
APPROVAL_PATTERN = re.compile(r"^Issue #24 owner approval comment [1-9][0-9]*$")
ALLOWED_MARKDOWN = {
    "NIST RMF / SP 800-53": (
        "01-foundations/NIST_RMF_SP_800-53/Portugues_BR/"
        "NIST_RMF_and_SP_800-53_Release_5.2.0_Practical_Manual_Portugues_BR_v1.0.md"
    ),
    "Incident Response / BCDR": (
        "05-operational-resilience/Incident_Response_BCDR/Portugues_BR/"
        "Incident_Response_Business_Continuity_and_Disaster_Recovery_Manual_"
        "Portugues_BR_v1.0.md"
    ),
}
ALLOWED_DESTINATION_DIRS = {
    "NIST RMF / SP 800-53": (
        ROOT / "01-foundations/NIST_RMF_SP_800-53/Portugues_BR/media"
    ),
    "Incident Response / BCDR": (
        ROOT / "05-operational-resilience/Incident_Response_BCDR/Portugues_BR/media"
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def expected_review_path(record: dict) -> str:
    slug = (
        "nist-rmf"
        if record["manual_family"] == "NIST RMF / SP 800-53"
        else "incident-response-bcdr"
    )
    filename = Path(record["exact_image_path"]).name
    return (
        f"review/nist-rmf-incident-response-localized-figures/"
        f"pt-BR-{slug}-{filename}"
    )


def markdown_reference(alt_text: str, image_path: str) -> str:
    safe_alt = (alt_text or "Figura localizada").replace("[", "(").replace("]", ")")
    return f"![{safe_alt}]({image_path})"


def normalize_reference(text: str, image_path: str, alt_text: str) -> str:
    replacement = markdown_reference(alt_text, image_path)
    escaped = re.escape(image_path)
    html_pattern = re.compile(
        rf"<img\b(?=[^>]*\bsrc\s*=\s*['\"]{escaped}['\"])[^>]*?/?>",
        flags=re.IGNORECASE | re.DOTALL,
    )
    markdown_pattern = re.compile(
        rf"!\[[^\]]*\]\({escaped}\)(?:\{{[^}}]*\}})?"
    )
    html_matches = list(html_pattern.finditer(text))
    markdown_matches = list(markdown_pattern.finditer(text))
    if len(html_matches) + len(markdown_matches) != 1:
        raise SystemExit(
            f"Expected exactly one image reference for {image_path}, "
            f"found {len(html_matches) + len(markdown_matches)}"
        )
    if html_matches:
        return html_pattern.sub(replacement, text, count=1)
    return markdown_pattern.sub(replacement, text, count=1)


def verify_png(path: Path, expected_size: tuple[int, int]) -> None:
    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            if image.format != "PNG":
                raise SystemExit(f"Expected PNG review image: {path}")
            if image.size != expected_size:
                raise SystemExit(
                    f"Image dimensions mismatch for {path}: "
                    f"expected {expected_size}, got {image.size}"
                )
    except (OSError, ValueError) as exc:
        raise SystemExit(f"PNG integrity validation failed for {path}: {exc}") from exc


def authoritative_size(record: dict) -> tuple[int, int]:
    evidence = record["english_source_evidence"]
    container = ROOT / evidence["container"]
    if not container.is_file():
        raise SystemExit(f"Missing authoritative source DOCX: {container}")
    with ZipFile(container) as archive:
        try:
            source_bytes = archive.read(evidence["internal_path"])
        except KeyError as exc:
            raise SystemExit(
                f"Missing authoritative source image for {record['id']}: "
                f"{evidence['internal_path']}"
            ) from exc
    if sha256_bytes(source_bytes) != evidence["sha256"]:
        raise SystemExit(f"Authoritative SHA-256 mismatch for {record['id']}")
    if len(source_bytes) != evidence["size_bytes"]:
        raise SystemExit(f"Authoritative byte-count mismatch for {record['id']}")
    with Image.open(BytesIO(source_bytes)) as image:
        image.verify()
    with Image.open(BytesIO(source_bytes)) as image:
        return image.size


def load_and_validate() -> tuple[dict, list[dict], dict[str, dict]]:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(manifest, list) or len(manifest) != EXPECTED_TOTAL:
        raise SystemExit(
            f"Expected exactly {EXPECTED_TOTAL} manifest records, "
            f"found {len(manifest) if isinstance(manifest, list) else 'non-list'}"
        )

    inventory_records = [
        record
        for record in inventory["references"]
        if record.get("manual_family") in FAMILIES
        and record.get("primary_classification") == "requires_localization"
    ]
    if len(inventory_records) != EXPECTED_TOTAL:
        raise SystemExit(
            f"Expected exactly {EXPECTED_TOTAL} unresolved inventory records, "
            f"found {len(inventory_records)}"
        )

    manifest_ids = [item.get("inventory_id") for item in manifest]
    if len(set(manifest_ids)) != EXPECTED_TOTAL:
        raise SystemExit("Manifest inventory IDs are missing or not unique")
    records_by_id = {record["id"]: record for record in inventory_records}
    if set(manifest_ids) != set(records_by_id):
        raise SystemExit("Manifest and inventory record ID sets do not match")

    family_counts = Counter(item.get("manual_family") for item in manifest)
    inventory_family_counts = Counter(
        record.get("manual_family") for record in inventory_records
    )
    expected_counts = {family: EXPECTED_PER_FAMILY for family in FAMILIES}
    if dict(family_counts) != expected_counts:
        raise SystemExit(f"Unexpected manifest family counts: {dict(family_counts)}")
    if dict(inventory_family_counts) != expected_counts:
        raise SystemExit(
            f"Unexpected inventory family counts: {dict(inventory_family_counts)}"
        )

    review_paths: set[str] = set()
    destination_paths: set[str] = set()
    markdown_text: dict[Path, str] = {}

    for item in manifest:
        record = records_by_id[item["inventory_id"]]
        family = record["manual_family"]
        if item.get("manual_family") != family:
            raise SystemExit(f"Manifest family mismatch for {record['id']}")
        if record.get("language") != EXPECTED_LANGUAGE:
            raise SystemExit(
                f"Unexpected language for {record['id']}: {record.get('language')}"
            )
        if item.get("status") != EXPECTED_STATUS:
            raise SystemExit(f"Unexpected review status for {record['id']}")
        if item.get("description") != RECONSTRUCTION_DESCRIPTION:
            raise SystemExit(f"Review description mismatch for {record['id']}")
        if item.get("review_file") != expected_review_path(record):
            raise SystemExit(f"Unexpected review path for {record['id']}")
        if item["review_file"] in review_paths:
            raise SystemExit(f"Duplicate review path: {item['review_file']}")
        review_paths.add(item["review_file"])

        review_file = ROOT / item["review_file"]
        try:
            review_file.resolve().relative_to(REVIEW_DIR.resolve())
        except ValueError as exc:
            raise SystemExit(f"Review path escapes controlled directory: {review_file}") from exc
        if not review_file.is_file():
            raise SystemExit(f"Missing review PNG: {review_file}")
        digest = sha256_file(review_file)
        if digest != item.get("sha256"):
            raise SystemExit(f"Review SHA-256 mismatch for {record['id']}")

        source_size = authoritative_size(record)
        manifest_size = (item.get("width"), item.get("height"))
        if manifest_size != source_size:
            raise SystemExit(
                f"Review/source dimension mismatch for {record['id']}: "
                f"manifest {manifest_size}, authoritative {source_size}"
            )
        verify_png(review_file, source_size)

        markdown_path = record.get("markdown_file")
        if markdown_path != ALLOWED_MARKDOWN[family]:
            raise SystemExit(f"Unexpected Markdown destination for {record['id']}")
        markdown_file = ROOT / markdown_path
        if not markdown_file.is_file():
            raise SystemExit(f"Missing affected Markdown: {markdown_file}")
        current = markdown_text.setdefault(
            markdown_file, markdown_file.read_text(encoding="utf-8")
        )
        markdown_text[markdown_file] = normalize_reference(
            current, record["exact_image_path"], record.get("alt_text", "")
        )

        destination_path = record.get("localized_asset_path_checked")
        destination = ROOT / destination_path
        expected_dir = ALLOWED_DESTINATION_DIRS[family].resolve()
        if destination.resolve().parent != expected_dir:
            raise SystemExit(f"Unexpected localized destination for {record['id']}")
        if destination.name != Path(record["exact_image_path"]).name:
            raise SystemExit(f"Destination filename mismatch for {record['id']}")
        if destination_path in destination_paths:
            raise SystemExit(f"Duplicate localized destination: {destination_path}")
        destination_paths.add(destination_path)
        if destination.exists():
            raise SystemExit(f"Localized destination already exists: {destination}")

    if len(review_paths) != EXPECTED_TOTAL or len(destination_paths) != EXPECTED_TOTAL:
        raise SystemExit("Review or destination path count mismatch")
    if set(markdown_text) != {ROOT / path for path in ALLOWED_MARKDOWN.values()}:
        raise SystemExit("Expected exactly the two controlled Markdown files")

    return inventory, manifest, records_by_id


def update_summary(inventory: dict) -> None:
    summary = inventory["summary"]
    for family in FAMILIES:
        if summary["totals_by_manual"].get(family) != EXPECTED_PER_FAMILY:
            raise SystemExit(f"Unexpected unresolved summary count for {family}")
    if summary["totals_by_language"].get(EXPECTED_LANGUAGE, 0) < EXPECTED_TOTAL:
        raise SystemExit("Brazilian Portuguese unresolved summary is too small")
    if (
        summary["totals_by_primary_classification"].get("requires_localization", 0)
        < EXPECTED_TOTAL
    ):
        raise SystemExit("Requires-localization summary is too small")

    summary["total_unresolved_references"] -= EXPECTED_TOTAL
    summary["total_restored_localized_references"] += EXPECTED_TOTAL
    for family in FAMILIES:
        summary["totals_by_manual"][family] = 0
    summary["totals_by_language"][EXPECTED_LANGUAGE] -= EXPECTED_TOTAL
    summary["totals_by_primary_classification"][
        "requires_localization"
    ] -= EXPECTED_TOTAL
    summary["totals_by_primary_classification"]["restored_localized"] += EXPECTED_TOTAL


def promote(approval_evidence: str) -> None:
    if not APPROVAL_PATTERN.fullmatch(approval_evidence):
        raise SystemExit(
            "Promotion requires controlled approval evidence formatted as "
            "'Issue #24 owner approval comment <numeric-id>'"
        )

    inventory, manifest, records_by_id = load_and_validate()
    changed_markdown: dict[Path, str] = {}

    for item in manifest:
        record = records_by_id[item["inventory_id"]]
        review_file = ROOT / item["review_file"]
        destination = ROOT / record["localized_asset_path_checked"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(review_file, destination)
        if sha256_file(destination) != item["sha256"]:
            raise SystemExit(f"Promoted SHA-256 mismatch for {record['id']}")
        verify_png(destination, (item["width"], item["height"]))

        markdown_file = ROOT / record["markdown_file"]
        current = changed_markdown.setdefault(
            markdown_file, markdown_file.read_text(encoding="utf-8")
        )
        changed_markdown[markdown_file] = normalize_reference(
            current, record["exact_image_path"], record.get("alt_text", "")
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

    for path, text in changed_markdown.items():
        path.write_text(text, encoding="utf-8")
    update_summary(inventory)
    INVENTORY.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Promoted exactly {EXPECTED_TOTAL} approved Batch 4 localized figures "
        f"with evidence: {approval_evidence}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--approval-evidence",
        help="Controlled evidence string verified by the promotion workflow.",
    )
    parser.add_argument(
        "--validate-review-only",
        action="store_true",
        help="Validate the review manifest and assets without promoting files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.validate_review_only:
        load_and_validate()
        print("Batch 4 review manifest and all 20 review PNGs are promotion-ready.")
        return
    if not args.approval_evidence:
        raise SystemExit("Promotion requires --approval-evidence")
    promote(args.approval_evidence)


if __name__ == "__main__":
    main()
