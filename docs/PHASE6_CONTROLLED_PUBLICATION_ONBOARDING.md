# Phase 6 controlled-publication onboarding

## Improvement 41 — Manual 09 candidate enrollment

Phase 6 begins repository-wide onboarding of existing published manuals into the
controlled-publication validation system created in Phases 4 and 5.

Manual 09 — NIST Cybersecurity Framework 2.0 Controlled Implementation — is the
first Phase 6 onboarding target because its repository tree already contains all
three controlled source locales, DOCX/PDF publication artifacts, a publication
report, SHA-256 checksum manifest, page-level QA, source-verification evidence,
and explicit localization and accessibility review gates.

The onboarding is deliberately fail-closed. Manual 09 is registered only in
`candidate_manifests`; it is not added to the active publication lane. Its
retained localization record states that human semantic review is required and
its accessibility/publication record remains PRE-STAGED / FAIL-CLOSED. Automated
validation may establish technical consistency but cannot convert those records
into approval.

The candidate manifest requires all 32 chapters in English, Spanish (es-419),
and Brazilian Portuguese (pt-BR), plus all six NIST CSF 2.0 Functions in the English
controlled source, exact publication-report and checksum agreement, DOCX/PDF
integrity, page-QA PASS evidence, stale-artifact checks, semantic round-trip
validation, and structural accessibility validation.

The path
`01-foundations/NIST_CSF_2_Controlled_Implementation` is removed from
`next_candidates` only because it is now explicitly represented by a candidate
manifest. This change does not approve the manual, translations, accessibility,
or a new release.

Future Phase 6 onboarding must follow the same rule: enroll technically complete
manuals as candidates first, preserve existing human-review boundaries, and move
a manual to the active lane only through separately reviewed governance evidence.


## Improvement 42 — Manual 10 candidate enrollment

Manual 10 — NIST RMF and SP 800-53 Controlled Implementation — is enrolled as
the second Phase 6 candidate. Its controlled English, Spanish (es-419), and
Brazilian Portuguese (pt-BR) sources cover all 32 chapters. Retained publication evidence includes
DOCX/PDF artifacts, report hashes, checksums, page QA, source verification,
localization review, accessibility review, and release-readiness pre-stage
records.

The retained governance evidence remains explicitly fail-closed. Localization
drafts are complete but human semantic review is open; accessibility remains
pre-staged; and final release approval remains mandatory. The candidate manifest
therefore cannot authorize publication or move Manual 10 into the active lane.

Manual 10 also preserves the repository's sequencing boundary: it follows
Manual 09 in the candidate list and must not bypass Manual 09 in controlled
publication progression.
