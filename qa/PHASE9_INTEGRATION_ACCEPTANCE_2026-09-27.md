# Phase 9 integration acceptance — 2026-09-27

## Scope

Phase 9 converts Phase 8 production-readiness controls into independently
reproduced production-toolchain evidence and a non-authorizing controlled-release
drill.

This record accepts Improvements 54 through 57. It does not approve any manual,
source baseline, translation, accessibility review, legal/privacy conclusion,
reviewer authorization, or publication.

## Accepted implementation baseline

The functional Phase 9 baseline before this acceptance record is:

`4b8e9f4423d6ac2668f29caf2df92e78e0442d9d`

That revision contains the merged implementations from PR #546, PR #548, and
PR #549.

## Completed improvements

| Improvement | Pull request | Result |
| --- | --- | --- |
| 54 — immutable production runtime certification | #546 | Merged and green |
| 55 — immutable PDF toolchain certification | #548 | Merged and green |
| 56 — controlled-release drill and operational handoff | #549 | Merged and green |
| 57 — Phase 9 integration acceptance and final CI | closure PR | This record and final exact-head CI |

## Improvement 54 acceptance

The production runtime is pinned to an exact Python base image manifest and exact
dependency lock. Two isolated BuildKit jobs reproduced the same OCI manifest.
The runtime certification remains non-authorizing.

## Improvement 55 acceptance

The PDF inspection toolchain is isolated from the runtime image. Two isolated
BuildKit jobs independently reproduced the same pinned Poppler OCI manifest.

The first PDF reproducibility attempt produced different manifests and was
rejected. A normalization defect and recovery-backup coverage defect were fixed,
then the certification was rerun until the exact manifests matched and the full
publication/recovery suite passed.

The production toolchain status is now `VERIFIED`.

## Improvement 56 acceptance

The release drill consumes the verified production toolchain, exact
reviewer-readiness packets, one-candidate-at-a-time release queue, and isolated
recovery result.

Each candidate receives an exact aggregate SHA-256 fingerprint over its six
controlled publication artifacts.

A passing drill reports
`TECHNICAL_READY_HUMAN_APPROVALS_REQUIRED`.

No rollout changes or publication actions are performed.

## Preserved fail-closed boundaries

Phase 9 technical completion is not publication approval.

The following remain mandatory external prerequisites where applicable:

- approved authoritative-source baselines and source-to-manual mappings;
- hash-bound localization and semantic approval;
- independent accessibility approval;
- legal/privacy review for regulated-content candidates;
- at least two authorized independent release reviewers;
- exact-candidate controlled-release verification after all current evidence is
  bound to the exact candidate revision and artifact hashes.

Bulk release remains prohibited.

## Final CI acceptance

The Phase 9 closure branch is accepted only when the complete exact-head gate
set passes:

- Controlled Publication Quality
- Document Writing Quality
- 06 - Workflow Security
- 21 - Release Pipeline Meta QA
- 07 - Release Package QA
- Phase 9 Production Certification
- Phase 9 PDF Toolchain Certification

The merge of the closure PR is the final technical acceptance event for Phase 9.

## Phase 9 conclusion

Phase 9 is technically complete when this closure PR merges after the complete
gate set passes on its exact head. The repository then has independently
reproducible production runtime/PDF environments, recovery-tested release
operations, exact candidate artifact fingerprints, and a controlled-release
drill while retaining every human approval boundary.
