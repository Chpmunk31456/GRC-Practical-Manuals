#!/usr/bin/env python3
"""Validate provenance summary totals against individual inventory records."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
UNRESOLVED = "requires_localization"
RESTORED = "restored_localized"


def _counts_with_existing_keys(
    records: list[dict],
    field: str,
    existing: dict[str, int],
) -> dict[str, int]:
    counts = Counter(record.get(field) for record in records)
    counts.pop(None, None)
    keys = set(existing) | set(counts)
    return {key: counts.get(key, 0) for key in existing} | {
        key: counts[key] for key in sorted(keys - set(existing))
    }


def expected_summary(inventory: dict) -> dict:
    references = inventory["references"]
    summary = inventory["summary"]
    unresolved = [
        record
        for record in references
        if record.get("primary_classification") == UNRESOLVED
    ]
    primary_counts = Counter(
        record.get("primary_classification") for record in references
    )
    primary_counts.pop(None, None)
    return {
        "total_inventory_records": len(references),
        "total_unresolved_references": len(unresolved),
        "total_restored_localized_references": primary_counts.get(RESTORED, 0),
        "totals_by_manual": _counts_with_existing_keys(
            unresolved, "manual_family", summary["totals_by_manual"]
        ),
        "totals_by_language": _counts_with_existing_keys(
            unresolved, "language", summary["totals_by_language"]
        ),
        "totals_by_primary_classification": _counts_with_existing_keys(
            references,
            "primary_classification",
            summary["totals_by_primary_classification"],
        ),
    }


def reconcile_summary(inventory: dict) -> None:
    inventory["summary"].update(expected_summary(inventory))


def validate_summary(inventory: dict) -> None:
    expected = expected_summary(inventory)
    actual = inventory["summary"]
    mismatches = {
        key: {"stored": actual.get(key), "expected": value}
        for key, value in expected.items()
        if actual.get(key) != value
    }
    if mismatches:
        raise SystemExit(
            "Provenance inventory summary mismatch:\n"
            + json.dumps(mismatches, ensure_ascii=False, indent=2)
        )


def main() -> None:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    validate_summary(inventory)
    print(
        "Provenance inventory summary is consistent with "
        f"{len(inventory['references'])} individual records."
    )


if __name__ == "__main__":
    main()
