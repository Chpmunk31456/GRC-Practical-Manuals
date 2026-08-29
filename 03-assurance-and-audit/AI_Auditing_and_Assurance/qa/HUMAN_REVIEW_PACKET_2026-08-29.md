# Manual 05 — Human Review Packet

**Manual:** AI Auditing and Assurance  
**Purpose:** Pre-stage the substantive human review boundary before Manual 05 becomes front-of-line.  
**Controlled publication source head recorded by package:** `647eab3dda4bce3acadc9cd5a0874b354b360935`  
**Preparation branch:** `release/manual05-human-review-prep-2026-08-29`

## Control boundary

This packet does not itself make Manual 05 publication-eligible. It consolidates the already-completed machine/document/source evidence so reviewers can focus on the remaining human judgment gates. Standing Final Human Release Approval is already recorded for the manual series and must not be requested again after all preceding gates are green.

## Existing completed supporting evidence

- controlled English 32-chapter master;
- authoritative-source verification and source-state watch;
- ISO/NIST assurance baseline and ISACA AAIA professional-practice boundary;
- non-human technical/editorial source-readiness review: PASS;
- source-level graphics/accessibility and text-equivalent review: PASS;
- trilingual DOCX/PDF generation, page QA, metadata, image-alt-text checks, PDF content preflight and SHA-256 provenance: PASS;
- durable EN / es-419 / pt-BR DOCX/PDF publication package present on `main`.

Supporting records include:

- `qa/TECHNICAL_EDITORIAL_REVIEW_2026-08-26.md`
- `qa/SOURCE_GRAPHICS_ACCESSIBILITY_REVIEW_2026-08-26.md`
- `qa/SOURCE_VERIFICATION_2026-08-26.md`
- `qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md`
- `qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md`
- `publication/qa/MANUAL_05_PUBLICATION_REPORT.json`
- `publication/qa/MANUAL_05_PAGE_QA.csv`
- `publication/qa/MANUAL_05_SHA256SUMS.txt`

## Exact publication artifacts to review

### English controlled edition

- DOCX: `publication/Manual_05_AI_Auditing_and_Assurance_EN.docx`
  - SHA-256: `3b4d50de4fc9b1582eae9950011cba7097c829edd2d412d33e15d47383faa115`
- PDF: `publication/Manual_05_AI_Auditing_and_Assurance_EN.pdf`
  - SHA-256: `8d3be16debb6084835458245e5c4abdef516047d3367519a7a8758bff2c38240`
  - Pages: 14

### Spanish (`es-419`) controlled localization candidate

- DOCX: `publication/Manual_05_AI_Auditing_and_Assurance_ES-419.docx`
  - SHA-256: `07b286de9718782c9cb9313729eb6b02a6ba03549b74d2605f9579fb085faac4`
- PDF: `publication/Manual_05_AI_Auditing_and_Assurance_ES-419.pdf`
  - SHA-256: `d1cf88fe7e819469a2e8ebc21fb61b5feed568858b906a76e37d3fd4c4182b80`
  - Pages: 14

### Brazilian Portuguese (`pt-BR`) controlled localization candidate

- DOCX: `publication/Manual_05_AI_Auditing_and_Assurance_PT-BR.docx`
  - SHA-256: `abd8316ce439beca1629e5959b0afff1550eb1305061f0e6cfbf048ffc0b0edb`
- PDF: `publication/Manual_05_AI_Auditing_and_Assurance_PT-BR.pdf`
  - SHA-256: `de9f7def204527c27ff4f82af97081638f7e0ebaf7d796dd63d07a897576ab02`
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

Machine page QA is supporting evidence only.

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
3. run exact-final Manual 05 QA, publication-candidate QA, structure, trilingual parity, workflow security, release-package and release-pipeline meta QA;
4. reconcile catalog and release registry to the exact final candidate;
5. apply the standing Final Human Release Approval automatically;
6. publish immediately when every mandatory gate is green.

No additional repository-owner approval prompt is required at step 5.
