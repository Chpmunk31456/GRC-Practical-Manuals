# Manual 05 — Human Review Packet

**Manual:** AI Auditing and Assurance  
**Purpose:** Pre-stage the substantive human review boundary before Manual 05 becomes front-of-line.  
**Corrected durable publication source head recorded by package:** `d42b12447646993c54caade2b399efd4fb37f8d9`  
**Current repair branch:** `repair/manual04-05-localization-preflight-2026-08-29`

## Control boundary

This packet does not itself make Manual 05 publication-eligible. It consolidates the already-completed machine/document/source evidence so reviewers can focus on the remaining human judgment gates. Standing Final Human Release Approval is already recorded for the manual series and must not be requested again after all preceding gates are green.

## Preflight defects remediated before human review

Rendered/text preflight identified and corrected generator-owned localization defects before this packet was finalized:

- Spanish and Brazilian Portuguese figure captions remained in English;
- the localized control lines retained an English generator-owned suffix;
- localized document subject/comments metadata remained English.

The generator now localizes those fields, and Workflow 23 fails closed on stale English localized boilerplate/captions, inherited wrong-manual alt text, and duplicate footer text.

The hashes below supersede all earlier Manual 05 review-packet hashes.

## Existing completed supporting evidence

- controlled English 32-chapter master;
- authoritative-source verification and source-state watch;
- ISO/NIST assurance baseline and ISACA AAIA professional-practice boundary;
- non-human technical/editorial source-readiness review: PASS;
- source-level graphics/accessibility and text-equivalent review: PASS;
- trilingual DOCX/PDF generation, page QA, metadata, image-alt-text checks, PDF content preflight, localized-publication regression QA and SHA-256 provenance: PASS;
- corrected durable EN / es-419 / pt-BR DOCX/PDF publication package present on the repair branch for merge to `main`.

Supporting records include:

- `qa/TECHNICAL_EDITORIAL_REVIEW_2026-08-26.md`
- `qa/SOURCE_GRAPHICS_ACCESSIBILITY_REVIEW_2026-08-26.md`
- `qa/SOURCE_VERIFICATION_2026-08-26.md`
- `qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md`
- `qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md`
- `publication/qa/MANUAL_05_PUBLICATION_REPORT.json`
- `publication/qa/MANUAL_05_PAGE_QA.csv`
- `publication/qa/MANUAL_05_SHA256SUMS.txt`

## Exact durable publication artifacts to review

### English controlled edition

- DOCX: `publication/Manual_05_AI_Auditing_and_Assurance_EN.docx`
  - SHA-256: `6e7d6663ddd759b498d12bd49606bda2f4694afe02b866484563f010dd54744e`
- PDF: `publication/Manual_05_AI_Auditing_and_Assurance_EN.pdf`
  - SHA-256: `85cc051d4888c0672e17877fab9972bcce26f06cb658159eb21565f6608a12e1`
  - Pages: 14

### Spanish (`es-419`) controlled localization candidate

- DOCX: `publication/Manual_05_AI_Auditing_and_Assurance_ES-419.docx`
  - SHA-256: `911aeea6872c1b24e35fcb83273c5e3aeaf20e37c9828fe977d65b3b448b65db`
- PDF: `publication/Manual_05_AI_Auditing_and_Assurance_ES-419.pdf`
  - SHA-256: `b6ef241df607a97409cbe670e7b15d23ccdbf8d11e9f9cec99b300d09c7d26b7`
  - Pages: 14

### Brazilian Portuguese (`pt-BR`) controlled localization candidate

- DOCX: `publication/Manual_05_AI_Auditing_and_Assurance_PT-BR.docx`
  - SHA-256: `e2f490631a20bf9905ec6f27df1a806a309f80f7e77691c5219c53f5e8e38703`
- PDF: `publication/Manual_05_AI_Auditing_and_Assurance_PT-BR.pdf`
  - SHA-256: `bbc85e98c48857f4b1507fcf539c47093455b3c3bab0d294940900ac7bc1450f`
  - Pages: 14

## Gate A — `es-419` semantic / terminology review

Reviewer must compare the Spanish edition against the controlled English edition and confirm preservation of:

- audit mandate, objective, criteria, scope, independence and competence boundaries;
- evidence sufficiency/appropriateness, sampling, testing, findings, severity, root cause, management response, residual risk, remediation validation and follow-up meaning;
- distinctions among readiness, advisory, internal audit, external audit, certification/conformity assessment and technical testing;
- the rule that documentary evidence does not itself prove operating effectiveness;
- the rule that supplier assertions/questionnaires do not constitute independent assurance;
- AAIA classification as a professional-practice/job-practice reference, not law, regulation, ISO requirement, organizational certification or audit opinion;
- instructional graphics, captions, accessible explanations and assurance disclaimers.

**Reviewer:** ____________________  
**Qualification/competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate B — `pt-BR` semantic / terminology review

Apply the same criteria as Gate A to the Brazilian Portuguese edition, including deliberate review of retained audit/security/AI technical terms where Brazilian professional usage may justify an English term.

**Reviewer:** ____________________  
**Qualification/competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate C — rendered accessibility / visual review

Human reviewer must inspect all three final PDFs and DOCX behavior where relevant. Review at minimum:

- headings and hierarchy;
- lists, figures, captions, workpaper examples and findings presentation;
- instructional-graphic legibility, alternative text/text equivalents and non-color-dependent meaning;
- clipping, overlaps, page breaks, orphaned material, whitespace anomalies and blank/near-blank pages;
- metadata/language presentation, reading order, links and bookmarks where applicable;
- preservation of audit/assurance disclaimers so the publication does not imply certification, conformity or a formal audit opinion.

Machine page QA and regression QA are supporting evidence only.

**Reviewer:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** EN 14 pages / ES 14 pages / PT 14 pages / DOCX as needed  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate D — changed-scope review

Confirm that the reviewed artifact hashes above represent the intended controlled candidate and that later changes are limited to review evidence, release metadata or other non-substantive reconciliation unless explicitly re-reviewed.

Any material source, localization, figure-content, assurance-boundary or rendered-document change reopens the affected review gate and requires updated hashes.

**Reviewer:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Scope/evidence compared:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Publication transition

When Manual 05 becomes front-of-line and Gates A–D are approved:

1. regenerate only if remediation changed controlled content/artifacts;
2. reconcile hashes/provenance after any regeneration;
3. run exact-final Manual 05 QA, publication-candidate QA, localized-publication regression QA, structure, trilingual parity, workflow security, release-package and release-pipeline meta QA;
4. reconcile catalog and release registry to the exact final candidate;
5. apply the standing Final Human Release Approval automatically;
6. publish immediately when every mandatory gate is green and Manuals 03–04 are already published.

No additional repository-owner approval prompt is required at step 5.
