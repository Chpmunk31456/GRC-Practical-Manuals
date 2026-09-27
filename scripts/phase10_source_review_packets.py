#!/usr/bin/env python3
"""Generate deterministic authoritative-source baseline review packets."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from repository_publication_qa import ROOT, read_json


def run(root: Path = ROOT) -> dict:
    registry = read_json(root / ".compliance/authoritative-sources.json")
    policy = read_json(root / "config/source_monitoring.json")
    baselines = policy.get("baselines", {})
    mappings = policy.get("chapter_mappings", {})

    packets = []
    for source in registry["sources"]:
        source_id = source["id"]
        baseline = baselines.get(source_id)
        source_mappings = mappings.get(source_id, [])
        blockers = []
        if baseline is None:
            blockers.append("approved_baseline_missing")
        if not source_mappings:
            blockers.append("source_to_manual_mapping_missing")

        packets.append({
            "source_id": source_id,
            "title": source["title"],
            "family": source["family"],
            "registry_revision": source["version"],
            "registry_status": source["status"],
            "url": source["url"],
            "last_verified": source["last_verified"],
            "review_interval_days": source["review_interval_days"],
            "current_baseline": baseline,
            "affected_manuals": source_mappings,
            "required_baseline_fields": [
                "sha256",
                "publication_date",
                "revision",
                "approval_evidence",
            ],
            "status": "REVIEW_REQUIRED" if blockers else "CURRENT",
            "blockers": blockers,
            "human_approval_required": bool(blockers),
            "automation_may_update_baseline": False,
        })

    packets.sort(key=lambda row: (row["status"] != "REVIEW_REQUIRED", row["source_id"]))
    return {
        "schema_version": 1,
        "kind": "phase10_authoritative_source_review_packets",
        "source_count": len(packets),
        "review_required_count": sum(p["status"] == "REVIEW_REQUIRED" for p in packets),
        "packets": packets,
        "baseline_updates_applied": 0,
        "publication_authorized": False,
        "boundary": "Packets organize human source review only. Automation does not approve or update authoritative-source baselines.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Phase 10 source baseline packets: "
        f"{result['review_required_count']} review-required / {result['source_count']} sources"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
