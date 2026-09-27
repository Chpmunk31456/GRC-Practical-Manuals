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


## Improvement 59 — authoritative-source baseline review packets

Run:

`python scripts/phase10_source_review_packets.py --output phase10-source-review-packets.json`

Each registered authoritative source receives a deterministic review packet with
its current registry metadata, any existing approved baseline, current
source-to-manual mappings, and explicit blockers.

A source remains `REVIEW_REQUIRED` when either an approved baseline is missing
or no source-to-manual mapping exists.

The packet lists the required human-approved baseline fields:

- exact SHA-256;
- publication date;
- revision;
- approval evidence.

Automation applies zero baseline updates and cannot convert an observation into
approval.


## Improvement 60 — reviewer authorization and human-evidence intake

Phase 10 now has explicit proposal queues for:

- reviewer authorization requests;
- human decision evidence submissions.

Run:

`python scripts/phase10_human_intake.py --output phase10-human-intake.json`

Reviewer authorization proposals must contain a reviewer identifier, human
authorizer, authorization timestamp, evidence path, and exact evidence SHA-256.

Human evidence submissions must contain the exact current candidate packet hash
and exact evidence-file SHA-256 in addition to the existing decision fields.

Valid proposals remain proposals. Automation does not add reviewer identities to
`config/release_policy.json`, does not copy records into
`config/human_approval_evidence.json`, and does not mutate translation,
accessibility, source, legal/privacy, or publication approval state.

Stale packet hashes and changed evidence hashes fail closed.
