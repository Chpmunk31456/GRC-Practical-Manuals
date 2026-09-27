#!/usr/bin/env python3
"""Build the Phase 10 human-review campaign from exact current candidate evidence status."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from repository_publication_qa import ROOT, read_json
import human_approval_evidence
import phase8_release_queue


def run(root: Path = ROOT) -> dict:
    policy = read_json(root / "config/phase10_review_campaign_policy.json")
    human = human_approval_evidence.run(root)
    release = phase8_release_queue.run(root)

    release_by_id = {row["manual_id"]: row for row in release["queue"]}
    candidates = []

    for row in human["candidates"]:
        unresolved = [
            {
                "decision_type": decision["decision_type"],
                "status": decision["status"],
                "reason": decision["reason"],
                "required_evidence_fields": policy["required_evidence_fields"],
                "human_action_required": True,
            }
            for decision in row.get("decisions", [])
            if decision["status"] != "CURRENT_APPROVED"
        ]
        qrow = release_by_id[row["manual_id"]]
        candidates.append({
            "manual_id": row["manual_id"],
            "packet_sha256": row.get("packet_sha256"),
            "unresolved_decision_count": len(unresolved),
            "unresolved_decisions": unresolved,
            "release_queue_status": qrow["status"],
            "eligible_for_controlled_release_review": qrow["eligible_for_controlled_release_review"],
            "publication_authorized": False,
        })

    candidates.sort(key=lambda x: (x["unresolved_decision_count"], x["manual_id"]))
    for i, row in enumerate(candidates, start=1):
        row["campaign_priority"] = i

    first = candidates[0] if candidates else None
    return {
        "schema_version": 1,
        "kind": "phase10_human_review_campaign",
        "source_revision": human["source_revision"],
        "campaign_mode": policy["campaign_mode"],
        "priority_rule": policy["priority_rule"],
        "candidate_count": len(candidates),
        "next_candidate": first["manual_id"] if first else None,
        "campaign": candidates,
        "automation_authored_evidence_count": 0,
        "rollout_changes_applied": 0,
        "publication_authorized": False,
        "boundary": "This campaign orders and describes human review work. It does not create approvals, choose reviewer identities, change rollout lanes, or authorize publication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Phase 10 human review campaign: "
        f"{result['candidate_count']} candidates; next={result['next_candidate']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
