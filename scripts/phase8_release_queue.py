#!/usr/bin/env python3
"""Build a fail-closed one-at-a-time controlled-release readiness queue."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from repository_publication_qa import ROOT, read_json
import human_approval_evidence


def run(root: Path = ROOT) -> dict:
    policy = read_json(root / "config/phase8_release_queue_policy.json")
    status = human_approval_evidence.run(root)
    queue = []

    for candidate in status["candidates"]:
        blockers = []
        for decision in candidate.get("decisions", []):
            if decision["status"] != "CURRENT_APPROVED":
                blockers.append({
                    "kind": "human_decision",
                    "decision_type": decision["decision_type"],
                    "status": decision["status"],
                    "reason": decision["reason"],
                })

        for global_requirement in status["global_requirements"]:
            if global_requirement["status"] != "COMPLETE":
                blockers.append({
                    "kind": "global_requirement",
                    "requirement": global_requirement["requirement"],
                    "status": global_requirement["status"],
                    "reason": global_requirement["reason"],
                })

        eligible = (
            candidate["status"] == policy["required_candidate_state"]
            and not blockers
        )

        queue.append({
            "manual_id": candidate["manual_id"],
            "packet_sha256": candidate.get("packet_sha256"),
            "status": "ELIGIBLE_FOR_CONTROLLED_RELEASE_REVIEW" if eligible else "BLOCKED",
            "eligible_for_controlled_release_review": eligible,
            "blockers": blockers,
            "rollout_change_permitted": False,
            "publication_authorized": False,
        })

    eligible_ids = [row["manual_id"] for row in queue if row["eligible_for_controlled_release_review"]]

    return {
        "schema_version": 1,
        "kind": "phase8_controlled_release_queue",
        "source_revision": status["source_revision"],
        "promotion_mode": policy["promotion_mode"],
        "bulk_promotion_allowed": policy["bulk_promotion_allowed"],
        "eligible_candidate_count": len(eligible_ids),
        "eligible_candidate_ids": eligible_ids,
        "queue": queue,
        "rollout_changes_applied": 0,
        "publication_authorized": False,
        "boundary": "Queue eligibility permits only a subsequent exact-candidate controlled-release review. This tool never promotes a rollout lane, bulk-approves candidates, or authorizes publication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Controlled release queue: "
        f"{result['eligible_candidate_count']} eligible / {len(result['queue'])} candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
