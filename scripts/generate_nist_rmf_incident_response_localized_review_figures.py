#!/usr/bin/env python3
"""Generate Batch 4 review-only Brazilian Portuguese reconstructions."""

from __future__ import annotations

import json
from pathlib import Path

import generate_iso27001_pci_localized_review_figures as engine

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "review/nist-rmf-incident-response-localized-figures"
FAMILIES = ("NIST RMF / SP 800-53", "Incident Response / BCDR")
EXPECTED_TOTAL = 20


def main() -> None:
    data = json.loads(engine.INVENTORY.read_text(encoding="utf-8"))
    records = [
        record
        for record in data["references"]
        if record.get("manual_family") in FAMILIES
        and record.get("primary_classification") == "requires_localization"
    ]
    if len(records) != EXPECTED_TOTAL:
        raise SystemExit(f"Expected {EXPECTED_TOTAL} records, found {len(records)}")

    manifest = []
    for record in records:
        family_slug = (
            "nist-rmf"
            if record["manual_family"] == "NIST RMF / SP 800-53"
            else "incident-response-bcdr"
        )
        suffix = record["exact_image_path"].split("image", 1)[-1]
        destination = OUTPUT / f"pt-BR-{family_slug}-image{suffix}"
        manifest.append(engine.draw_candidate(record, destination))

    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Generated {len(manifest)} review-only localized figures in {OUTPUT}")


if __name__ == "__main__":
    main()
