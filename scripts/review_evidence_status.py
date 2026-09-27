#!/usr/bin/env python3
"""Report incomplete or stale human-review evidence without inferring approval."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from controlled_publication_qa import sha256
from repository_publication_qa import ROOT, contained, read_json
import review_readiness_packets as readiness

SHA256 = re.compile(r"^[0-9a-f]{64}$")


def load_bindings(root: Path = ROOT) -> dict:
    data = read_json(root / "config/review_evidence_bindings.json")
    if data.get("schema_version") != 1 or not isinstance(data.get("bindings"), dict):
        raise ValueError("invalid review evidence binding configuration")
    return data["bindings"]


def assess_binding(packet: dict, review_path: str, binding: object, root: Path = ROOT) -> dict:
    row = {"review_record": review_path}
    if not isinstance(binding, dict):
        return {**row, "status": "INCOMPLETE", "reason": "binding_missing"}

    if binding.get("packet_sha256") != packet["packet_sha256"]:
        return {**row, "status": "STALE", "reason": "packet_hash_mismatch"}

    evidence_path = binding.get("evidence_path")
    evidence_hash = binding.get("evidence_sha256")
    if not isinstance(evidence_path, str) or not evidence_path:
        return {**row, "status": "INCOMPLETE", "reason": "evidence_path_missing"}
    if not isinstance(evidence_hash, str) or not SHA256.fullmatch(evidence_hash):
        return {**row, "status": "INCOMPLETE", "reason": "evidence_hash_missing"}

    try:
        path = contained(root, evidence_path)
    except ValueError:
        return {**row, "status": "INCOMPLETE", "reason": "unsafe_evidence_path"}
    if not path.is_file():
        return {**row, "status": "INCOMPLETE", "reason": "evidence_file_missing"}
    if sha256(path) != evidence_hash:
        return {**row, "status": "STALE", "reason": "evidence_hash_mismatch"}

    return {
        **row,
        "status": "CURRENT",
        "reason": "exact_packet_and_evidence_hash_match",
        "evidence_path": path.relative_to(root.resolve()).as_posix(),
        "evidence_sha256": evidence_hash,
    }


def run(root: Path = ROOT, bindings: dict | None = None) -> dict:
    packet_result = readiness.run(root)
    binding_map = load_bindings(root) if bindings is None else bindings
    manuals = []

    for packet in packet_result["packets"]:
        manual_bindings = binding_map.get(packet["manual_id"], {})
        if not isinstance(manual_bindings, dict):
            manual_bindings = {}
        evidence = [
            assess_binding(packet, record["path"], manual_bindings.get(record["path"]), root)
            for record in packet["review_records"]
        ]
        statuses = {row["status"] for row in evidence}
        if "STALE" in statuses:
            evidence_status = "STALE"
        elif "INCOMPLETE" in statuses:
            evidence_status = "INCOMPLETE"
        else:
            evidence_status = "CURRENT"

        manuals.append({
            "manual_id": packet["manual_id"],
            "packet_sha256": packet["packet_sha256"],
            "evidence_status": evidence_status,
            "review_evidence": evidence,
            "repository_blockers": list(packet["repository_blockers"]),
            "readiness_status": "REVIEW_REQUIRED",
            "publication_authorized": False,
        })

    overall = "STALE" if any(m["evidence_status"] == "STALE" for m in manuals) else (
        "INCOMPLETE" if any(m["evidence_status"] == "INCOMPLETE" for m in manuals) else "CURRENT"
    )
    return {
        "schema_version": 1,
        "kind": "review_evidence_status",
        "source_revision": packet_result["source_revision"],
        "status": overall,
        "candidate_count": len(manuals),
        "manuals": manuals,
        "publication_authorized": False,
        "boundary": "Evidence freshness is metadata only. CURRENT does not mean approved; controlled-release human review and exact-candidate verification remain authoritative.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Review evidence status: {result['status']} ({result['candidate_count']} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
