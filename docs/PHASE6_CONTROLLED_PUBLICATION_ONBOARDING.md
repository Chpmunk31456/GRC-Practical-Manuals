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


## Improvement 43 — Manual 05 candidate enrollment

Manual 05 — AI Auditing and Assurance — is enrolled as the third Phase 6
candidate after Manuals 09 and 10. Its controlled English, Spanish (es-419), and
Brazilian Portuguese (pt-BR) sources cover all 32 chapters, and its durable
publication package includes DOCX/PDF artifacts, checksums, publication reports,
page QA, source verification, technical/editorial review, and a human-review
packet.

The substantive human gates remain open. The localization and accessibility
review records are fail-closed, and the retained human-review packet explicitly
states that it does not itself make Manual 05 publication-eligible. Older
series-level or standing approval language therefore does not substitute for the
Phase 5 controlled-release requirement for exact-candidate, hash-bound evidence
and authorized independent reviewers.

This onboarding changes validation coverage only. It does not activate Manual 05,
approve its translations, certify accessibility, or authorize publication.


## Improvement 44 — GDPR candidate enrollment

Manual 11 — GDPR Privacy and Data Protection Controlled Implementation — is
enrolled as a Phase 6 candidate. The repository contains 32 controlled chapters
for English, Spanish (es-419), and Brazilian Portuguese (pt-BR), together with
DOCX/PDF artifacts, checksums, a publication report, page QA, source verification,
and explicit localization and accessibility review gates.

The onboarding remains fail-closed. Competent privacy/legal review, localization
semantic approval, rendered-document accessibility review, changed-scope review,
and exact-final release approval remain mandatory.

The retained release-readiness pre-stage record also still describes some
localization and publication work as pending even though corresponding artifacts
exist in the repository. Phase 6 does not silently rewrite that historical
evidence. The inconsistency is preserved as a readiness-record reconciliation
blocker that must be resolved through reviewed governance evidence before any
active publication decision.

Automated validation can establish technical consistency only. It cannot provide
organization-specific legal advice, determine GDPR applicability or lawful basis,
approve transfers or breach decisions, or authorize publication.
