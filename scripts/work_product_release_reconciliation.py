#!/usr/bin/env python3
"""Fail closed when work-product release evidence and catalog state diverge.

This is a generic repository control for manuals, toolkits, guides, release
packages, and comparable controlled deliverables. It does not replace human
semantic, accessibility, editorial, legal, or final-release review.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / ".compliance" / "manual-catalog.json"
REGISTRY = ROOT / ".compliance" / "work-product-releases.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has_artifact(root: Path, suffix: str) -> bool:
    return any(p.is_file() for p in root.rglob(f"*{suffix}"))


def main() -> int:
    errors: list[str] = []
    catalog = load(CATALOG)
    registry = load(REGISTRY)

    manuals = {
        item.get("id"): item
        for item in catalog.get("manuals", [])
        if isinstance(item, dict) and item.get("id")
    }

    seen: set[str] = set()
    for item in registry.get("released_work_products", []):
        if not isinstance(item, dict):
            errors.append("release registry entry must be an object")
            continue
        work_id = item.get("id")
        work_type = item.get("type")
        state = item.get("release_state")
        evidence = str(item.get("release_evidence", "")).strip()
        if not work_id or work_id in seen:
            errors.append(f"invalid or duplicate work-product id: {work_id!r}")
            continue
        seen.add(work_id)
        if not evidence:
            errors.append(f"{work_id}: release evidence is required")

        if work_type != "manual":
            continue
        manual = manuals.get(work_id)
        if manual is None:
            errors.append(f"{work_id}: release registry manual is missing from manual catalog")
            continue

        catalog_release = manual.get("release_state")
        if catalog_release != state:
            errors.append(
                f"{work_id}: catalog release_state={catalog_release!r} does not match registry={state!r}"
            )

        manual_root = ROOT / str(manual.get("path", ""))
        if state == "published":
            if not manual_root.is_dir():
                errors.append(f"{work_id}: published manual path is missing")
                continue
            for suffix in (".docx", ".pdf"):
                if not has_artifact(manual_root, suffix):
                    errors.append(f"{work_id}: published manual lacks a {suffix} artifact")
        elif state.startswith("published"):
            errors.append(f"{work_id}: ambiguous published-like state is not allowed: {state}")

    if errors:
        print("Work-product release reconciliation: FAIL")
        for error in errors:
            print(f"  ERROR: {error}")
        return 1

    print(f"Work-product release reconciliation: PASS ({len(seen)} registered work product(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
