# Phase 6 integration acceptance — 2026-09-27

## Scope

Phase 6 completed the repository-wide onboarding queue identified by the Phase 4
controlled-publication rollout. The work enrolled technically complete manuals
into the generic Phase 4/5 validation system without converting technical PASS
results into human approval or active publication status.

This record documents integration acceptance of Improvements 41 through 45. It
does not approve publication, translations, legal interpretations, accessibility,
or release authorization.

## Completed improvements

| Improvement | Pull request | Result |
| --- | --- | --- |
| 41 — Manual 09 NIST CSF 2.0 candidate onboarding | #531 | Merged and green |
| 42 — Manual 10 NIST RMF / SP 800-53 candidate onboarding | #532 | Merged and green |
| 43 — Manual 05 AI Auditing and Assurance candidate onboarding | #533 | Merged and green |
| 44 — Manual 11 GDPR candidate onboarding | #534 | Merged and green |
| 45 — Manual 06 HIPAA candidate onboarding | #535 | Merged and green |

## Final rollout state

The active lane remains deliberately narrow:

- `config/controlled_publications/manual03.json` is active.
- Manuals 04, 09, 10, 05, 11, and 06 are candidate manifests.
- `next_candidates` is empty because every target identified by the Phase 4
  rollout index is now represented by a controlled manifest.

An empty onboarding queue means technical enrollment is complete. It does not
mean candidate manuals are approved, publishable, or active.

## Technical acceptance evidence

Every Phase 6 candidate is validated by the same generic repository publication
engine. The enrolled manifests require:

- complete 32-chapter inventories for English, Spanish `es-419`, and Brazilian
  Portuguese `pt-BR`;
- publication-report hash agreement;
- SHA-256 checksum agreement;
- DOCX/PDF structural integrity;
- page-QA PASS evidence;
- stale-artifact checks;
- source → DOCX → PDF preservation validation;
- rendered/layout validation;
- structural accessibility validation;
- retained fail-closed review records.

Repository rollout regressions were generalized so expected gate counts derive
from the registered manifest inventory instead of assuming a fixed number of
manuals.

Phase 6 also hardened framework-identifier round-trip parsing after Manual 05
exposed a PDF text-extraction edge case. Complete identifiers such as
`NIST SP 800-53A` remain protected even when `pdftotext` inserts whitespace at
a line wrap after the hyphen, while genuinely truncated fragments such as
`NIST SP 800-` are not accepted as complete identifiers.

## Preserved fail-closed boundaries

Candidate status does not grant publication approval.

- Manual 09 remains blocked on human localization and accessibility review.
- Manual 10 remains blocked on human localization, accessibility, and release
  review and retains its sequencing boundary.
- Manual 05 retains open substantive localization/accessibility gates. Older
  standing series-level approval language is non-substitutive for exact-candidate,
  hash-bound Phase 5 release verification.
- GDPR remains blocked on competent privacy/legal review, localization semantic
  approval, accessibility review, changed-scope review, exact-final release
  approval, and reconciliation of its retained readiness record.
- HIPAA remains blocked on competent legal/semantic and rendered-accessibility
  review. Proposed Security Rule material remains readiness-only unless a final
  HHS rule changes the controlled legal baseline.
- Phase 5 controlled-release requirements for exact revision, artifact hashes,
  production toolchain verification, authorized independent reviewers, and
  mandatory CI checks remain in force.

## Phase 6 acceptance conclusion

Phase 6 repository-wide controlled-publication onboarding is complete for the
identified rollout queue. Improvements 41–45 are integrated into `main`, and
all targeted manuals are represented by active or candidate manifests under the
same fail-closed validation system.

This acceptance is for implementation and technical onboarding only. It does not
alter any retained human-review decision or authorize publication.
