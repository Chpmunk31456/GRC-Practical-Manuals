#!/usr/bin/env python3
"""Validate proposed Phase 10 reviewer authorizations and human evidence submissions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from controlled_publication_qa import sha256
from repository_publication_qa import ROOT, contained, read_json
import review_readiness_packets

SHA256 = re.compile(r"^[0-9a-f]{64}$")
DECISIONS = {"APPROVED", "REJECTED"}


def _safe_hashed_file(root: Path, path_value: str, digest: str) -> tuple[bool, str]:
    if not SHA256.fullmatch(digest):
        return False, "invalid_evidence_hash"
    try:
        path = contained(root, path_value)
    except ValueError:
        return False, "unsafe_evidence_path"
    if not path.is_file():
        return False, "evidence_file_missing"
    if sha256(path) != digest:
        return False, "evidence_hash_mismatch"
    return True, "valid"


def validate_reviewer_request(record: object, policy: dict, root: Path = ROOT) -> dict:
    fields = policy["reviewer_authorization"]["required_fields"]
    if not isinstance(record, dict):
        return {"status": "INVALID", "reason": "record_not_object"}
    if any(not isinstance(record.get(k), str) or not record.get(k) for k in fields):
        return {"status": "INVALID", "reason": "required_field_missing"}
    ok, reason = _safe_hashed_file(
        root,
        record["authorization_evidence_path"],
        record["authorization_evidence_sha256"],
    )
    return {
        "status": "VALID_PROPOSAL" if ok else "INVALID",
        "reason": reason,
        "reviewer_id": record.get("reviewer_id"),
        "authorization_applied": False,
    }


def validate_evidence_submission(record: object, policy: dict, packets: dict, root: Path = ROOT) -> dict:
    fields = policy["human_evidence_submission"]["required_fields"]
    if not isinstance(record, dict):
        return {"status": "INVALID", "reason": "record_not_object"}
    if any(not isinstance(record.get(k), str) or not record.get(k) for k in fields):
        return {"status": "INVALID", "reason": "required_field_missing"}
    if record["decision"] not in DECISIONS:
        return {"status": "INVALID", "reason": "invalid_decision"}

    packet_by_id = {p["manual_id"]: p for p in packets["packets"]}
    packet = packet_by_id.get(record["manual_id"])
    if packet is None:
        return {"status": "INVALID", "reason": "manual_not_current_candidate"}
    if record["packet_sha256"] != packet["packet_sha256"]:
        return {"status": "STALE", "reason": "packet_hash_mismatch"}

    ok, reason = _safe_hashed_file(root, record["evidence_path"], record["evidence_sha256"])
    return {
        "status": "VALID_PROPOSAL" if ok else "INVALID",
        "reason": reason,
        "manual_id": record.get("manual_id"),
        "decision_type": record.get("decision_type"),
        "evidence_applied": False,
    }


def run(root: Path = ROOT) -> dict:
    policy = read_json(root / "config/phase10_human_intake_policy.json")
    reviewer_queue = read_json(root / "config/reviewer_authorization_requests.json")
    evidence_queue = read_json(root / "config/human_evidence_submissions.json")
    release_policy = read_json(root / "config/release_policy.json")
    human_registry = read_json(root / "config/human_approval_evidence.json")
    packets = review_readiness_packets.run(root)

    reviewer_results = [
        validate_reviewer_request(row, policy, root)
        for row in reviewer_queue.get("requests", [])
    ]
    evidence_results = [
        validate_evidence_submission(row, policy, packets, root)
        for row in evidence_queue.get("submissions", [])
    ]

    minimum = max(
        int(policy["reviewer_authorization"]["minimum_independent_reviewers"]),
        int(release_policy.get("minimum_independent_reviewers", 2)),
    )
    current_reviewers = list(release_policy.get("reviewers", []))
    valid_reviewer_proposals = {
        row.get("reviewer_id")
        for row in reviewer_results
        if row.get("status") == "VALID_PROPOSAL" and row.get("reviewer_id")
    }

    return {
        "schema_version": 1,
        "kind": "phase10_human_intake_validation",
        "source_revision": packets["source_revision"],
        "reviewer_authorization": {
            "minimum_independent_reviewers": minimum,
            "current_authorized_reviewers": current_reviewers,
            "current_authorized_count": len(current_reviewers),
            "valid_pending_proposal_count": len(valid_reviewer_proposals),
            "status": "COMPLETE" if len(current_reviewers) >= minimum else "HUMAN_AUTHORIZATION_REQUIRED",
            "results": reviewer_results,
            "release_policy_mutations_applied": 0,
        },
        "human_evidence": {
            "current_registry_count": len(human_registry.get("evidence", [])),
            "submission_count": len(evidence_results),
            "valid_pending_submission_count": sum(
                row["status"] == "VALID_PROPOSAL" for row in evidence_results
            ),
            "results": evidence_results,
            "registry_mutations_applied": 0,
        },
        "publication_authorized": False,
        "boundary": "Valid proposals remain proposals. Automation never authorizes reviewers, applies human evidence, or authorizes publication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Phase 10 human intake: "
        f"reviewers={result['reviewer_authorization']['status']}, "
        f"pending_evidence={result['human_evidence']['valid_pending_submission_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
