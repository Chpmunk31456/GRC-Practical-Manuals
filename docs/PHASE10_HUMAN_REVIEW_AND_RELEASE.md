# Phase 10 — Human review completion and first controlled candidate release

Phase 10 begins only after the production environment is technically certified.

Its purpose is to organize and consume genuine human evidence, one candidate at a
time, until a candidate becomes eligible for the existing exact-candidate
controlled-release verifier.

## Improvement 58 — deterministic human-review campaign

Run:

`python scripts/phase10_review_campaign.py --output phase10-review-campaign.json`

The campaign orders candidates using a deterministic rule:

1. fewest unresolved human decisions;
2. then `manual_id`.

Each unresolved decision lists the exact evidence fields required by the existing
Phase 8 evidence registry. The campaign does not create those records.

The campaign never chooses or invents reviewer identities, never changes rollout
lanes, never marks a human decision approved, and never authorizes publication.

The first campaign candidate is only the next item to review. It is not a release
recommendation or publication approval.
