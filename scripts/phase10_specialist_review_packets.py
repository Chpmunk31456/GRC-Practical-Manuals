#!/usr/bin/env python3
"""Generate exact specialist-review packets for Phase 10 human reviewers."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from repository_publication_qa import ROOT, read_json
import review_readiness_packets

SCOPES = {
  "localization_semantic": [
    "meaning_preservation",
    "terminology_consistency",
    "locale_appropriateness",
    "factual_equivalence",
    "no_unsupported_additions_or_omissions"
  ],
  "accessibility": [
    "reading_order",
    "screen_reader_behavior",
    "table_relationships",
    "alternative_text_meaning",
    "font_compatibility",
    "visual_layout"
  ],
  "legal_semantic": [
    "legal_rule_accuracy",
    "current_rule_vs_proposed_rule_distinction",
    "obligation_scope",
    "defined_terms",
    "implementation_guidance_not_legal_advice"
  ],
  "privacy_legal": [
    "regulatory_text_accuracy",
    "controller_processor_roles",
    "lawful_basis_and_rights",
    "cross_border_and_dpia_language",
    "implementation_guidance_not_legal_advice"
  ]
}


def run(root: Path = ROOT) -> dict:
    requirements = read_json(root / "config/human_approval_requirements.json")
    intake_policy = read_json(root / "config/phase10_human_intake_policy.json")
    readiness = review_readiness_packets.run(root)
    packet_by_id = {p["manual_id"]: p for p in readiness["packets"]}

    packets = []
    for manual_id, decision_types in requirements["required_by_candidate"].items():
        current = packet_by_id.get(manual_id)
        if current is None:
            continue
        for decision_type in decision_types:
            if decision_type not in SCOPES:
                continue
            artifacts = []
            for locale in sorted(current["artifacts"]):
                for kind in sorted(current["artifacts"][locale]):
                    row = current["artifacts"][locale][kind]
                    artifacts.append({
                        "locale": locale,
                        "kind": kind,
                        "path": row["path"],
                        "sha256": row["sha256"],
                    })
            packets.append({
                "manual_id": manual_id,
                "decision_type": decision_type,
                "packet_sha256": current["packet_sha256"],
                "source_revision": readiness["source_revision"],
                "artifacts": artifacts,
                "review_scope": SCOPES[decision_type],
                "submission_required_fields": intake_policy["human_evidence_submission"]["required_fields"],
                "allowed_decisions": intake_policy["human_evidence_submission"]["decisions"],
                "status": "HUMAN_REVIEW_REQUIRED",
                "automation_authored_decision": False,
                "publication_authorized": False,
            })

    packets.sort(key=lambda row: (row["manual_id"], row["decision_type"]))
    return {
        "schema_version": 1,
        "kind": "phase10_specialist_review_packets",
        "source_revision": readiness["source_revision"],
        "packet_count": len(packets),
        "packets": packets,
        "automation_authored_decisions": 0,
        "publication_authorized": False,
        "boundary": "These packets define review scope and exact evidence binding only. Specialist conclusions must be authored by qualified humans.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Phase 10 specialist packets: {result['packet_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
