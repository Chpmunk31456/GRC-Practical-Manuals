# Phase 8 integration acceptance — 2026-09-27

## Scope

Phase 8 prepared the repository for real production approval and controlled
release without manufacturing human decisions.

This record accepts the implementation of Improvements 49 through 53. It does
not approve publication, translations, source baselines, legal conclusions,
accessibility, reviewer authorization, or production release.

## Accepted implementation baseline

The functional Phase 8 baseline before this acceptance record is:

`ff187daf31a9f6d82a48edf3f8f9a5229723529c`

That revision contains the merged implementations from PR #541 through PR #544.

## Completed improvements

| Improvement | Pull request | Result |
| --- | --- | --- |
| 49 — hosted CI toolchain attestation | #541 | Merged and green |
| 50 — exact human approval evidence intake | #542 | Merged and green |
| 51 — one-at-a-time controlled-release readiness queue | #543 | Merged and green |
| 52 — deterministic human/production handoff packet | #544 | Merged and green |
| 53 — Phase 8 integration acceptance and final CI | closure PR | This record and final exact-head CI |

## Improvement 49 acceptance

The repository records a concrete successful hosted-CI baseline for Python,
Ubuntu runner image, Poppler package, pdftotext, and pdfinfo. Drift is detected
automatically.

Hosted CI is not treated as an immutable production environment. Production
toolchain status remains governed independently and must reach `VERIFIED` with
the exact immutable environment evidence required by the controlled-release
verifier.

## Improvement 50 acceptance

Every candidate has an explicit human-decision requirements matrix. Human
approval evidence must bind a decision type, human reviewer identifier, exact
current reviewer-readiness packet hash, exact evidence-file SHA-256, and review
timestamp.

Automation validates the evidence but does not author it.

## Improvement 51 acceptance

The release queue operates one candidate at a time. It does not alter
`rollout_lane`, does not bulk-promote candidates, and never authorizes
publication. Eligibility only permits a later exact-candidate controlled-release
review.

## Improvement 52 acceptance

The human handoff packet makes the remaining source-baseline, chapter-mapping,
reviewer-authorization, immutable-toolchain, and per-candidate decision work
explicit.

The handoff records `automation_completed_human_actions: 0`.

## Preserved fail-closed boundaries

Phase 8 implementation completion is not production approval.

The following remain real external prerequisites until completed by authorized
humans or production owners:

- approved authoritative-source baselines and complete source-to-manual mappings;
- hash-bound localization/semantic approvals;
- independent accessibility approvals;
- legal/privacy review where required;
- an authorized independent release-reviewer allowlist;
- immutable production PDF/build environment digests and generator dependency
  lock evidence;
- exact-candidate controlled-release verification.

No Phase 8 automation may convert missing evidence into approval.

## Final CI acceptance

The Phase 8 closure branch is accepted only when all five required exact-head
checks pass:

- Controlled Publication Quality
- Document Writing Quality
- 06 - Workflow Security
- 21 - Release Pipeline Meta QA
- 07 - Release Package QA

The merge of the closure PR is the final technical acceptance event for Phase 8.

## Phase 8 conclusion

Phase 8 is technically complete when this closure PR merges after the five
required checks pass on its exact head. The repository is then prepared to
receive genuine human and immutable-production evidence and process candidates
one at a time through the existing controlled-release verifier.
