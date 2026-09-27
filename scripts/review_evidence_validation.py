#!/usr/bin/env python3
"""Validate exact, hash-bound human review evidence without inferring approval from prose."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path, PurePosixPath
import re

from repository_publication_qa import ROOT, read_json, contained
from controlled_publication_qa import sha256
import review_readiness_packets as readiness

INDEX = "config/review_evidence/index.json"
POLICY = "config/review_readiness_policy.json"


def flatten_artifacts(packet: dict) -> dict[str, str]:
    return {
        row["path"]: row["sha256"]
        for locale in packet["artifacts"].values()
        for row in locale.values()
    }


def flatten_review_records(packet: dict) -> dict[str, str]:
    return {row["path"]: row["sha256"] for row in packet["review_records"]}


def record_path(root: Path, relative: str) -> Path:
    path = contained(root, relative)
    base = (root / "config/review_evidence").resolve()
    if path.parent != base or path.name == "index.json" or path.suffix != ".json":
        raise ValueError("review evidence record must be a JSON file in config/review_evidence")
    return path


def evidence_hashes(record: dict, root: Path) -> list[str]:
    errors = []
    files = record.get("evidence_files")
    if not isinstance(files, dict) or not files:
        return ["evidence_files_missing"]
    for relative, digest in files.items():
        if not isinstance(relative, str) or not re.fullmatch(r"[0-9a-f]{64}", digest or ""):
            errors.append("invalid_evidence_file_entry")
            continue
        try:
            path = contained(root, relative)
        except ValueError:
            errors.append("evidence_file_path_invalid")
            continue
        if not path.is_file() or sha256(path) != digest:
            errors.append("evidence_file_hash_mismatch")
    return sorted(set(errors))


def validate_record(record: dict, packet: dict, required_scopes: list[str], policy: dict, root: Path) -> tuple[str, list[str]]:
    errors = []
    stale = []
    required = {
        "schema_version","manual_id","source_revision","packet_sha256","reviewer","prepared_by",
        "decision","scopes","artifacts","review_records","evidence_files","reviewed_at",
    }
    if set(record) != required or record.get("schema_version") != 1:
        errors.append("record_shape_invalid")
    if record.get("manual_id") != packet["manual_id"]:
        errors.append("manual_id_mismatch")
    if record.get("source_revision") != packet["source_revision"]:
        stale.append("source_revision_stale")
    if record.get("packet_sha256") != packet["packet_sha256"]:
        stale.append("packet_hash_stale")
    reviewer = record.get("reviewer")
    prepared = record.get("prepared_by")
    if not isinstance(reviewer, str) or not reviewer.strip() or reviewer == prepared:
        errors.append("independent_reviewer_required")
    if record.get("decision") not in policy["allowed_decisions"]:
        errors.append("decision_invalid")
    scopes = record.get("scopes")
    if not isinstance(scopes, list) or not scopes or len(scopes) != len(set(scopes)):
        errors.append("scopes_invalid")
    elif any(scope not in required_scopes for scope in scopes):
        errors.append("scope_not_required")
    if record.get("artifacts") != flatten_artifacts(packet):
        stale.append("artifact_hashes_stale")
    if record.get("review_records") != flatten_review_records(packet):
        stale.append("review_record_hashes_stale")
    reviewed_at = record.get("reviewed_at")
    try:
        parsed = datetime.fromisoformat(reviewed_at)
        if parsed.tzinfo is None:
            errors.append("review_timestamp_timezone_required")
    except (TypeError, ValueError):
        errors.append("review_timestamp_invalid")
    errors.extend(evidence_hashes(record, root))
    if errors:
        return "INVALID", sorted(set(errors + stale))
    if stale:
        return "STALE", sorted(set(stale))
    return "CURRENT", []


def run(root: Path = ROOT, index_path: str = INDEX, policy_path: str = POLICY) -> dict:
    packet_report = readiness.run(root)
    packets = {packet["manual_id"]: packet for packet in packet_report["packets"]}
    policy = read_json(contained(root, policy_path))
    required_map = policy.get("required_scopes", {})
    if set(required_map) != set(packets):
        raise ValueError("review policy must cover every candidate exactly")
    index = read_json(contained(root, index_path))
    records = index.get("records")
    if index.get("schema_version") != 1 or not isinstance(records, list) or len(records) != len(set(records)):
        raise ValueError("invalid review evidence index")
    results = []
    coverage = {manual_id: {scope: set() for scope in scopes} for manual_id, scopes in required_map.items()}
    invalid_count = 0
    stale_count = 0
    seen_paths = set()
    for relative in records:
        path = record_path(root, relative)
        if path in seen_paths:
            raise ValueError("duplicate review evidence path")
        seen_paths.add(path)
        record = read_json(path)
        manual_id = record.get("manual_id")
        if manual_id not in packets:
            status, errors = "INVALID", ["unknown_or_non_candidate_manual"]
        else:
            status, errors = validate_record(record, packets[manual_id], required_map[manual_id], policy, root)
            if status == "CURRENT" and record["decision"] in policy["current_decisions"]:
                for scope in record["scopes"]:
                    coverage[manual_id][scope].add(record["reviewer"])
        invalid_count += status == "INVALID"
        stale_count += status == "STALE"
        results.append({
            "path": relative,
            "manual_id": manual_id,
            "status": status,
            "errors": errors,
        })
    manuals = []
    minimum = policy.get("minimum_reviewers_per_scope", 1)
    if type(minimum) is not int or minimum < 1:
        raise ValueError("invalid reviewer threshold")
    for manual_id, scopes in required_map.items():
        missing = [scope for scope in scopes if len(coverage[manual_id][scope]) < minimum]
        manuals.append({
            "manual_id": manual_id,
            "status": "CURRENT" if not missing else "REVIEW_REQUIRED",
            "missing_scopes": missing,
            "publication_authorized": False,
        })
    if invalid_count:
        status = "INVALID"
    elif stale_count:
        status = "STALE"
    elif all(row["status"] == "CURRENT" for row in manuals):
        status = "CURRENT"
    else:
        status = "REVIEW_REQUIRED"
    return {
        "schema_version": 1,
        "kind": "exact_review_evidence",
        "source_revision": packet_report["source_revision"],
        "status": status,
        "records": results,
        "manuals": manuals,
        "invalid_records": invalid_count,
        "stale_records": stale_count,
        "publication_authorized": False,
        "boundary": "Exact human review evidence supports readiness only. It cannot replace controlled-release verification or authorize publication.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = run()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {
            "schema_version": 1,
            "kind": "exact_review_evidence",
            "status": "INVALID",
            "error_type": type(exc).__name__,
            "publication_authorized": False,
        }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Exact review evidence: " + result["status"])
    return 1 if result["status"] in {"INVALID", "STALE"} else 0


if __name__ == "__main__":
    raise SystemExit(main())
