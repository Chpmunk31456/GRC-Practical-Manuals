#!/usr/bin/env python3
"""Audit unresolved CIS Controls v8.1 localized figure references.

This script is intentionally read-only. It filters the authoritative legacy image
provenance inventory, checks current localized Markdown and media paths, and emits
a deterministic Markdown report. It does not generate, copy, or modify artwork.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "qa/images/LEGACY_IMAGE_PROVENANCE_INVENTORY.json"
REPORT = ROOT / "qa/images/CIS_CONTROLS_V8_1_LOCALIZED_FIGURE_AUDIT.md"
FAMILY = "CIS Controls v8.1"


def load_records() -> list[dict]:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    return [r for r in data["references"] if r.get("manual_family") == FAMILY]


def image_reference_count(markdown_path: Path, image_path: str) -> int:
    if not markdown_path.is_file():
        return 0
    text = markdown_path.read_text(encoding="utf-8")
    pattern = re.compile(r"(?:!\[[^\]]*\]\(|<img\b[^>]*?src=[\"'])" + re.escape(image_path))
    return len(pattern.findall(text))


def main() -> None:
    records = load_records()
    if len(records) != 11:
        raise SystemExit(f"Expected 11 CIS reference records, found {len(records)}")

    languages = Counter(r["language"] for r in records)
    source_assets = {(r["english_source_evidence"]["internal_path"], r["english_source_evidence"]["sha256"]) for r in records}
    if len(source_assets) != 10:
        raise SystemExit(f"Expected 10 unique English source assets, found {len(source_assets)}")

    rows: list[str] = []
    unresolved = 0
    duplicate_groups: dict[str, list[str]] = {}

    for r in records:
        md = ROOT / r["markdown_file"]
        media = md.parent / r["exact_image_path"]
        ref_count = image_reference_count(md, r["exact_image_path"])
        exists = media.is_file()
        if not exists:
            unresolved += 1
        src = r["english_source_evidence"]
        duplicate_groups.setdefault(src["sha256"], []).append(f'{r["language"]}: {r["exact_image_path"]}')
        rows.append(
            "| {id} | {lang} | {fig} | `{dest}` | {asset} | {refs} | `{src_path}` | `{sha}` |".format(
                id=r["id"],
                lang=r["language"],
                fig=r["figure_number"],
                dest=r["localized_asset_path_checked"],
                asset="present" if exists else "missing",
                refs=ref_count,
                src_path=src["internal_path"],
                sha=src["sha256"],
            )
        )

    cross_language = {sha: refs for sha, refs in duplicate_groups.items() if len(refs) > 1}
    if len(cross_language) != 1:
        raise SystemExit(f"Expected one cross-language duplicate source asset, found {len(cross_language)}")

    report = f"""# CIS Controls v8.1 Localized Figure Audit

**Scope:** Audit only. No image generation, substitution, Markdown repair, merge to `main`, or release publication is authorized by this report.

## Verified inventory

- Total unresolved reference records: **{len(records)}**
- Unique authoritative English source assets: **{len(source_assets)}**
- Latin American Spanish reference records: **{languages['Latin American Spanish']}**
- Brazilian Portuguese reference records: **{languages['Brazilian Portuguese']}**
- Localized assets currently missing: **{unresolved}**
- Cross-language duplicate source groups: **{len(cross_language)}**

The duplicate is English `word/media/image3.png`, which maps to Spanish `media/image3.png` and Brazilian Portuguese `media/image3.png`. Each language requires its own localized artwork; neither localized file may be copied into the other language directory.

## Record-level verification

| Record | Language | Figure | Localized destination | Asset | Current references | English source | Source SHA-256 |
|---|---|---:|---|---|---:|---|---|
{chr(10).join(rows)}

## Required next phase

1. Extract and visually inspect the ten authoritative English source assets.
2. Confirm source dimensions, layout, visible strings, and exact figure-to-path mapping.
3. Prepare one Spanish Figure 3 candidate and ten Brazilian Portuguese Figure 1–10 candidates.
4. Keep all candidates review-only until owner visual approval.
5. Promote approved PNGs only, then repair Markdown references and update provenance.
6. Rebuild and validate all 22 multilingual packages through a focused draft PR targeting `production/multilingual-grc-editions`.
"""
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")
    print(f"Wrote {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
