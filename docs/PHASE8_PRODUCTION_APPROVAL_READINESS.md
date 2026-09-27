# Phase 8 — Production approval and release readiness

Phase 8 prepares the repository for real production approval without manufacturing
human decisions.

## Improvement 49 — hosted CI toolchain attestation

The repository records the exact successful hosted-CI toolchain observed during
the Phase 7 closure run:

- Python 3.12.14
- GitHub-hosted Ubuntu 24.04 runner image 20260920.314.1
- poppler-utils 24.02.0-1ubuntu9.9
- pdftotext 24.02.0
- pdfinfo 24.02.0

Run:

`python scripts/toolchain_attestation.py --output toolchain-attestation.json`

The verifier fails on drift from that baseline. This is an attested CI baseline,
not an immutable production environment. The repository therefore retains
`REVIEW_REQUIRED` for production-toolchain status until an immutable build
environment or equivalent production verification is supplied.

No toolchain attestation authorizes publication.


## Improvement 50 — exact human approval evidence intake

Phase 8 uses two explicit registries:

- `config/human_approval_requirements.json` defines the required decision types
  for each candidate manual.
- `config/human_approval_evidence.json` contains only human-authored evidence
  records. It intentionally begins empty.

Every evidence record must identify the manual and decision type, carry a human
reviewer identifier and decision, bind to the exact current reviewer-readiness
packet hash, and bind to the exact SHA-256 of an evidence file.

The validator also reconciles evidence against the existing source-monitoring,
translation-lifecycle, accessibility-review, release-reviewer, and production
toolchain controls. An evidence record cannot bypass an incomplete subsystem.

Run:

`python scripts/human_approval_evidence.py --output human-approval-status.json`

The validator may report `CURRENT_APPROVED`, `INCOMPLETE`, `STALE`, or
`REJECTED` for a required decision. It never creates an approval and always
keeps `publication_authorized` false.

All six candidate manuals explicitly require authoritative-source,
localization/semantic, accessibility, and release-authorization decisions.
HIPAA additionally requires legal/semantic review; GDPR additionally requires
privacy/legal review.


## Improvement 51 — one-at-a-time controlled-release readiness queue

Phase 8 adds a repository-level release queue that consumes the exact human
evidence status from Improvement 50 and the global production prerequisites.

Run:

`python scripts/phase8_release_queue.py --output phase8-release-queue.json`

A candidate can become `ELIGIBLE_FOR_CONTROLLED_RELEASE_REVIEW` only when every
explicit human decision is current and approved and every global requirement is
complete. Even then, queue eligibility permits only a subsequent exact-candidate
controlled-release review.

The queue never changes `rollout_lane`, never bulk-promotes candidates, and
never authorizes publication. Promotion mode is explicitly
`one_candidate_at_a_time`.

At Phase 8 implementation time all six candidates remain blocked because the
human approval registries and immutable production environment are intentionally
not fabricated.
