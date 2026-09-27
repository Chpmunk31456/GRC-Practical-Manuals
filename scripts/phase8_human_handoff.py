#!/usr/bin/env python3
"""Generate a deterministic, non-authorizing Phase 8 human handoff packet."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from repository_publication_qa import ROOT, read_json
import human_approval_evidence


def run(root: Path = ROOT) -> dict:
    sources = read_json(root / ".compliance/authoritative-sources.json")["sources"]
    source_policy = read_json(root / "config/source_monitoring.json")
    release_policy = read_json(root / "config/release_policy.json")
    toolchain = read_json(root / "config/production_toolchain.json")
    human = human_approval_evidence.run(root)

    baselines = source_policy.get("baselines", {})
    mappings = source_policy.get("chapter_mappings", {})
    source_requests = []
    for source in sources:
        missing = []
        if source["id"] not in baselines:
            missing.append("approved_baseline")
        if source["id"] not in mappings:
            missing.append("chapter_mapping")
        if missing:
            source_requests.append({
                "source_id": source["id"],
                "title": source["title"],
                "registry_revision": source["version"],
                "url": source["url"],
                "missing": missing,
                "baseline_required_fields": [
                    "sha256", "publication_date", "revision", "approval_evidence"
                ],
                "status": "HUMAN_REVIEW_REQUIRED",
            })

    minimum = max(2, int(release_policy.get("minimum_independent_reviewers", 2)))
    reviewers = release_policy.get("reviewers", [])
    reviewer_status = {
        "minimum_independent_reviewers": minimum,
        "configured_reviewers": list(reviewers),
        "configured_count": len(reviewers),
        "status": "COMPLETE" if len(reviewers) >= minimum else "HUMAN_AUTHORIZATION_REQUIRED",
        "required_action": "Authorize at least the configured minimum of independent human GitHub reviewers on the default branch release policy.",
    }

    pdf = toolchain.get("pdf_toolchain", {})
    build = toolchain.get("build_environment", {})
    toolchain_missing = []
    if not pdf.get("container_digest"):
        toolchain_missing.append("pdf_toolchain.container_digest")
    if not build.get("container_digest"):
        toolchain_missing.append("build_environment.container_digest")
    if not build.get("generator_dependency_lock_sha256"):
        toolchain_missing.append("build_environment.generator_dependency_lock_sha256")
    if toolchain.get("status") != "VERIFIED":
        toolchain_missing.append("status=VERIFIED")

    candidate_requests = []
    for candidate in human["candidates"]:
        needed = [
            {
                "decision_type": row["decision_type"],
                "status": row["status"],
                "reason": row["reason"],
            }
            for row in candidate.get("decisions", [])
            if row["status"] != "CURRENT_APPROVED"
        ]
        candidate_requests.append({
            "manual_id": candidate["manual_id"],
            "packet_sha256": candidate.get("packet_sha256"),
            "required_human_actions": needed,
            "status": candidate["status"],
            "publication_authorized": False,
        })

    return {
        "schema_version": 1,
        "kind": "phase8_human_handoff",
        "source_revision": human["source_revision"],
        "authoritative_source_requests": source_requests,
        "authoritative_source_request_count": len(source_requests),
        "release_reviewer_authorization": reviewer_status,
        "production_toolchain": {
            "status": toolchain.get("status"),
            "missing": toolchain_missing,
            "hosted_ci_attestation": toolchain.get("hosted_ci_attestation"),
        },
        "candidate_requests": candidate_requests,
        "publication_authorized": False,
        "automation_completed_human_actions": 0,
        "boundary": "This packet is a worklist for human and production owners. It contains no approval and performs no policy mutation.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "Phase 8 human handoff: "
        f"{result['authoritative_source_request_count']} source requests, "
        f"{len(result['candidate_requests'])} candidate worklists"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
