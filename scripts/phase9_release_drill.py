#!/usr/bin/env python3
"""Run the Phase 9 non-authorizing controlled-release drill."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from repository_publication_qa import ROOT, read_json
import phase8_release_queue
import production_environment_certification
import pdf_toolchain_certification
import review_readiness_packets


def artifact_fingerprint(packet: dict) -> str:
    rows = []
    for locale in sorted(packet["artifacts"]):
        for kind in sorted(packet["artifacts"][locale]):
            row = packet["artifacts"][locale][kind]
            rows.append((locale, kind, row["path"], row["sha256"]))
    raw = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def load_recovery(path: Path | None) -> dict:
    if path is None:
        return {"status": "NOT_SUPPLIED"}
    return json.loads(path.read_text(encoding="utf-8"))


def run(root: Path = ROOT, recovery_report: dict | None = None) -> dict:
    policy = read_json(root / "config/phase9_operations_policy.json")
    env = production_environment_certification.run(root)
    pdf = pdf_toolchain_certification.validate(root)
    queue = phase8_release_queue.run(root)
    packets = review_readiness_packets.run(root)

    packet_rows = []
    for packet in packets["packets"]:
        packet_rows.append({
            "manual_id": packet["manual_id"],
            "packet_sha256": packet["packet_sha256"],
            "artifact_fingerprint_sha256": artifact_fingerprint(packet),
            "artifact_count": sum(len(v) for v in packet["artifacts"].values()),
            "publication_authorized": False,
        })

    recovery = recovery_report or {"status": "NOT_SUPPLIED"}
    technical_controls = {
        "production_toolchain_verified": env["status"] == "VERIFIED"
        and pdf["immutable_pdf_toolchain_verified"],
        "isolated_recovery_pass": recovery.get("status") == "PASS",
        "exact_candidate_artifact_fingerprints": bool(packet_rows)
        and all(row["artifact_count"] == 6 for row in packet_rows),
        "one_candidate_at_a_time_queue": (
            queue["promotion_mode"] == "one_candidate_at_a_time"
            and queue["bulk_promotion_allowed"] is False
        ),
        "publication_authorized_false_until_controlled_release_verifier": (
            queue["publication_authorized"] is False
        ),
    }

    technical_ready = all(technical_controls.values())
    human_blocked = any(row["status"] == "BLOCKED" for row in queue["queue"])
    status = (
        "TECHNICAL_READY_HUMAN_APPROVALS_REQUIRED"
        if technical_ready and human_blocked
        else "TECHNICAL_PREREQUISITE_INCOMPLETE"
    )

    return {
        "schema_version": 1,
        "kind": "phase9_controlled_release_drill",
        "source_revision": packets["source_revision"],
        "status": status,
        "technical_controls": technical_controls,
        "candidate_artifact_fingerprints": packet_rows,
        "candidate_queue": [
            {
                "manual_id": row["manual_id"],
                "status": row["status"],
                "blockers": row["blockers"],
                "publication_authorized": False,
            }
            for row in queue["queue"]
        ],
        "maintenance": policy["maintenance"],
        "rollout_changes_applied": 0,
        "publication_performed": False,
        "publication_authorized": False,
        "boundary": "This drill proves technical readiness only. Human approvals and exact-candidate controlled-release verification remain mandatory before any publication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recovery", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    recovery = load_recovery(args.recovery)
    result = run(recovery_report=recovery)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Phase 9 release drill: " + result["status"])
    return 0 if result["status"] == "TECHNICAL_READY_HUMAN_APPROVALS_REQUIRED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
