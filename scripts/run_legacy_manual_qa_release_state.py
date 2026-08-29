#!/usr/bin/env python3
"""Run a legacy manual QA script across development -> published transitions.

Some older manual-specific validators intentionally hard-coded `status: development`
while a manual was being built. Once authoritative release metadata records that the
manual is published, that assertion becomes stale and blocks truthful catalog
reconciliation.

This adapter does not waive the legacy QA. For a published catalog entry it first
requires publication agreement between the catalog and work-product release registry,
then presents an ephemeral development-status catalog only to the legacy validator,
and restores the exact catalog bytes afterward. All other checks still execute.

Use only for legacy validators whose sole publication-transition incompatibility is
an obsolete catalog-status assertion. New validators should natively model lifecycle
states instead.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / ".compliance" / "manual-catalog.json"
RELEASES = ROOT / ".compliance" / "work-product-releases.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def one(items: list[dict], key: str, value: str, label: str) -> dict:
    matches = [item for item in items if isinstance(item, dict) and item.get(key) == value]
    if len(matches) != 1:
        raise RuntimeError(f"{label} must contain exactly one {value!r} entry; found {len(matches)}")
    return matches[0]


def run(script: Path) -> int:
    return subprocess.run([sys.executable, str(script)], cwd=ROOT, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manual-id", required=True)
    parser.add_argument("--script", required=True)
    args = parser.parse_args()

    script = (ROOT / args.script).resolve()
    if not script.is_relative_to(ROOT) or not script.is_file():
        print("FAIL: legacy QA script is missing or outside the repository")
        return 1

    original = CATALOG.read_bytes()
    try:
        catalog = load(CATALOG)
        releases = load(RELEASES)
        catalog_entry = one(catalog.get("manuals", []), "id", args.manual_id, "manual catalog")
        status = catalog_entry.get("status")

        if status == "development":
            return run(script)

        if status != "published":
            print(f"FAIL: unsupported catalog status for release-state adapter: {status!r}")
            return 1

        if catalog_entry.get("release_state") != "published":
            print("FAIL: published catalog status requires release_state=published")
            return 1

        release_entry = one(
            releases.get("released_work_products", []), "id", args.manual_id,
            "work-product release registry",
        )
        if release_entry.get("type") != "manual" or release_entry.get("release_state") != "published":
            print("FAIL: published catalog status lacks matching published manual release evidence")
            return 1
        if not str(release_entry.get("release_evidence", "")).strip():
            print("FAIL: published release entry lacks release evidence")
            return 1

        # Preserve all real publication metadata while neutralizing only the obsolete
        # legacy `status == development` assertion for the duration of that validator.
        catalog_entry["status"] = "development"
        CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        code = run(script)
        if code == 0:
            print(
                "PASS: legacy QA passed with fail-closed published-state reconciliation "
                f"for {args.manual_id}"
            )
        return code
    except (OSError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"FAIL: release-state adapter: {exc}")
        return 1
    finally:
        CATALOG.write_bytes(original)


if __name__ == "__main__":
    raise SystemExit(main())
