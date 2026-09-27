#!/usr/bin/env python3
"""Validate human approval evidence against exact current candidate packets."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from controlled_publication_qa import sha256
from repository_publication_qa import ROOT, contained, read_json
import review_readiness_packets as readiness

SHA256 = re.compile(r"^[0-9a-f]{64}$")
DECISIONS = {"APPROVED", "REJECTED"}


def load_config(root: Path = ROOT) -> tuple[dict, dict, dict]:
    requirements = read_json(root / "config/human_approval_requirements.json")
    registry = read_json(root / "config/human_approval_evidence.json")
    release = read_json(root / "config/release_policy.json")
    if requirements.get("schema_version") != 1:
        raise ValueError("invalid human approval requirements schema")
    if registry.get("schema_version") != 1 or not isinstance(registry.get("evidence"), list):
        raise ValueError("invalid human approval evidence schema")
    return requirements, registry, release


def validate_record(record: object, root: Path = ROOT) -> tuple[bool, str]:
    if not isinstance(record, dict):
        return False, "record_not_object"
    required = (
        "manual_id", "decision_type", "decision", "reviewer_id",
        "packet_sha256", "evidence_path", "evidence_sha256", "reviewed_at",
    )
    if any(not isinstance(record.get(k), str) or not record.get(k) for k in required):
        return False, "required_field_missing"
    if record["decision"] not in DECISIONS:
        return False, "invalid_decision"
    if not SHA256.fullmatch(record["packet_sha256"]) or not SHA256.fullmatch(record["evidence_sha256"]):
        return False, "invalid_hash"
    try:
        path = contained(root, record["evidence_path"])
    except ValueError:
        return False, "unsafe_evidence_path"
    if not path.is_file():
        return False, "evidence_file_missing"
    if sha256(path) != record["evidence_sha256"]:
        return False, "evidence_hash_mismatch"
    return True, "valid"


def current_records(packet: dict, decision_type: str, records: list[dict], release_policy: dict, root: Path = ROOT) -> dict:
    matching = [
        row for row in records
        if isinstance(row, dict)
        and row.get("manual_id") == packet["manual_id"]
        and row.get("decision_type") == decision_type
    ]
    if not matching:
        return {"status": "INCOMPLETE", "reason": "human_evidence_missing", "valid_records": []}

    valid = []
    stale = False
    rejected = False
    for row in matching:
        ok, reason = validate_record(row, root)
        if not ok:
            if reason == "evidence_hash_mismatch":
                stale = True
            continue
        if row["packet_sha256"] != packet["packet_sha256"]:
            stale = True
            continue
        if row["decision"] == "REJECTED":
            rejected = True
        valid.append(row)

    if rejected:
        return {"status": "REJECTED", "reason": "current_human_rejection", "valid_records": valid}
    if not valid:
        return {
            "status": "STALE" if stale else "INCOMPLETE",
            "reason": "current_exact_evidence_missing",
            "valid_records": [],
        }

    if decision_type == "release_authorization":
        allowlist = set(release_policy.get("reviewers", []))
        minimum = max(2, int(release_policy.get("minimum_independent_reviewers", 2)))
        approved_reviewers = {
            row["reviewer_id"] for row in valid
            if row["decision"] == "APPROVED" and row["reviewer_id"] in allowlist
        }
        if len(approved_reviewers) < minimum:
            return {
                "status": "INCOMPLETE",
                "reason": "authorized_independent_reviewers_insufficient",
                "valid_records": valid,
            }

    approved = [row for row in valid if row["decision"] == "APPROVED"]
    if not approved:
        return {"status": "INCOMPLETE", "reason": "current_approval_missing", "valid_records": valid}
    return {"status": "CURRENT_APPROVED", "reason": "exact_human_evidence_match", "valid_records": valid}


def subsystem_status(decision_type: str, root: Path = ROOT) -> tuple[bool, str | None]:
    if decision_type == "authoritative_source":
        data = read_json(root / "config/source_monitoring.json")
        return bool(data.get("baselines")), "approved_source_baseline_missing"
    if decision_type == "localization_semantic":
        data = read_json(root / "config/translation_lifecycle.json")
        return bool(data.get("dependencies")) and bool(data.get("reviews")), "hash_bound_translation_review_missing"
    if decision_type == "accessibility":
        data = read_json(root / "config/accessibility_reviews.json")
        return bool(data.get("reviews")), "independent_accessibility_review_missing"
    return True, None


def run(root: Path = ROOT, registry_override: dict | None = None) -> dict:
    requirements, registry, release = load_config(root)
    if registry_override is not None:
        registry = registry_override
    packets = readiness.run(root)
    packet_by_id = {p["manual_id"]: p for p in packets["packets"]}
    candidates = []

    for manual_id, required_types in requirements["required_by_candidate"].items():
        packet = packet_by_id.get(manual_id)
        if packet is None:
            candidates.append({
                "manual_id": manual_id,
                "status": "INCOMPLETE",
                "reason": "candidate_packet_missing",
                "publication_authorized": False,
            })
            continue

        decisions = []
        for decision_type in required_types:
            status = current_records(packet, decision_type, registry["evidence"], release, root)
            subsystem_ok, subsystem_reason = subsystem_status(decision_type, root)
            if not subsystem_ok and status["status"] == "CURRENT_APPROVED":
                status = {
                    **status,
                    "status": "INCOMPLETE",
                    "reason": subsystem_reason,
                }
            decisions.append({
                "decision_type": decision_type,
                "status": status["status"],
                "reason": status["reason"],
                "current_valid_record_count": len(status["valid_records"]),
            })

        manual_status = "READY_FOR_CONTROLLED_RELEASE_REVIEW" if all(
            d["status"] == "CURRENT_APPROVED" for d in decisions
        ) else "HUMAN_REVIEW_INCOMPLETE"
        if any(d["status"] == "REJECTED" for d in decisions):
            manual_status = "HUMAN_REVIEW_REJECTED"

        candidates.append({
            "manual_id": manual_id,
            "packet_sha256": packet["packet_sha256"],
            "status": manual_status,
            "decisions": decisions,
            "publication_authorized": False,
        })

    toolchain = read_json(root / "config/production_toolchain.json")
    global_requirements = [{
        "requirement": "immutable_production_toolchain",
        "status": "COMPLETE" if toolchain.get("status") == "VERIFIED" else "INCOMPLETE",
        "reason": None if toolchain.get("status") == "VERIFIED" else "production_toolchain_not_immutable_verified",
    }]

    overall = "READY_FOR_CONTROLLED_RELEASE_REVIEW" if (
        candidates
        and all(c["status"] == "READY_FOR_CONTROLLED_RELEASE_REVIEW" for c in candidates)
        and all(g["status"] == "COMPLETE" for g in global_requirements)
    ) else "HUMAN_OR_PRODUCTION_EVIDENCE_INCOMPLETE"

    return {
        "schema_version": 1,
        "kind": "phase8_human_approval_evidence_status",
        "source_revision": packets["source_revision"],
        "status": overall,
        "candidates": candidates,
        "global_requirements": global_requirements,
        "publication_authorized": False,
        "boundary": "Automation validates exact human evidence and authorization prerequisites only. It never authors, approves, or substitutes for a human decision.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Phase 8 human evidence: " + result["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
