# Manual 04 — Human Review Packet

**Manual:** NIST AI 600-1 Generative AI Profile Implementation  
**Purpose:** Pre-stage the substantive human review boundary while Manual 03 remains the front-of-line publication target.  
**Controlled publication source head recorded by package:** `691c1aa5d01ef7395793be10195095551ace43a8`  
**Preparation branch:** `release/manual04-human-review-prep-2026-08-29`

## Control boundary

This packet does not make Manual 04 publication-eligible and does not replace competent human review. It consolidates machine-complete document/package evidence so reviewers can focus on substantive meaning, rendered usability, technical/editorial/security judgment, and changed scope.

Standing Final Human Release Approval is already recorded for the manual series. No additional owner approval prompt is required after all substantive gates and exact-final reconciliation are green.

## Durable publication artifacts already present on `main`

### English controlled edition

- DOCX: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_EN.docx`
  - SHA-256: `83dfd0c6cbfc405d119d875da4d8bb71773b4d3beb3d4baf8bac79bc44b03f3d`
- PDF: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_EN.pdf`
  - SHA-256: `a42fe4029aa65b1d5fc3f72e2690790fb359ec5615e0e882a43bea4286ea9177`
  - Pages: 15

### Spanish (`es-419`) controlled localization candidate

- DOCX: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_ES-419.docx`
  - SHA-256: `028a543729cb42188481fda3414ea25bcf0ef10d5306ef56bdce58d7e27e2193`
- PDF: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_ES-419.pdf`
  - SHA-256: `9b4d56fafebc1432a1e43f3971df209c7b3b3137622b64d85b3b8ab15289aa64`
  - Pages: 15

### Brazilian Portuguese (`pt-BR`) controlled localization candidate

- DOCX: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_PT-BR.docx`
  - SHA-256: `f23ccb0abd823a6aec364c3b252aede501e3a84aeef296ebb8be51fc36158340`
- PDF: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_PT-BR.pdf`
  - SHA-256: `5247e98a9a33c00b43bc6feb6a7ebc6893f5e2505337de72cafd4a6ff63b5d73`
  - Pages: 15

Supporting machine evidence:

- `publication/qa/MANUAL_04_PUBLICATION_REPORT.json`
- `publication/qa/MANUAL_04_PAGE_QA.csv`
- `publication/qa/MANUAL_04_SHA256SUMS.txt`
- `qa/SOURCE_VERIFICATION_2026-08-25.md`
- `qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md`
- `qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md`

## Gate A — `es-419` semantic / terminology review

Reviewer must compare the Spanish edition against the controlled English edition and confirm preservation of:

- NIST AI 600-1 / AI RMF identifiers and voluntary-guidance boundary;
- applicability/tailoring logic and the twelve GAI risk families;
- GOVERN, MAP, MEASURE, and MANAGE relationships where used;
- provenance, pre-deployment testing, incident disclosure, supplier/model dependency, human oversight, stop/restrict/rollback, and residual-risk meaning;
- assurance disclaimers and the distinction between guidance, evidence, legal obligations, and audit conclusions;
- instructional graphics, captions, accessible explanations, and terminology.

**Reviewer:** ____________________  
**Qualification/competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate B — `pt-BR` semantic / terminology review

Apply the same criteria as Gate A to the Brazilian Portuguese edition, including deliberate review of retained English technical terms where professional usage may justify them.

**Reviewer:** ____________________  
**Qualification/competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate C — technical / editorial / security / copyright review

Review the final candidate for technical accuracy, NIST attribution and source boundaries, security-control meaning, misleading equivalence claims, editorial defects, copyright/provenance concerns, and unresolved material findings.

**Reviewer:** ____________________  
**Competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate D — rendered accessibility / visual review

Human reviewer must inspect all three final PDFs and DOCX behavior where relevant, including:

- headings and hierarchy;
- tables, lists, links, figures, captions, and text equivalents;
- instructional-graphic legibility and non-color-dependent meaning;
- clipping, overlaps, page breaks, orphaned material, whitespace anomalies, and blank/near-blank pages;
- language presentation and localized labels;
- document metadata/language presentation where visible;
- practical reading sequence and usable reading order.

Machine page QA is supporting evidence only.

**Reviewer:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** EN 15 pages / ES 15 pages / PT 15 pages / DOCX as needed  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate E — changed-scope review

Confirm that the reviewed artifact hashes above represent the intended controlled candidate. Any later content, localization, figure-content, security-meaning, or substantive document change reopens the affected review gate and requires new hashes to be reviewed.

**Reviewer:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Scope/evidence compared:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Publication transition

When Manual 04 becomes the front-of-line release candidate and Gates A–E are approved:

1. regenerate only if remediation changed controlled content/artifacts;
2. reconcile hashes/provenance after any regeneration;
3. run exact-final Manual 04 QA, localization QA, document/publication QA, structure, trilingual parity, workflow security, release-package, and release-pipeline meta QA;
4. reconcile catalog and release registry to the exact final candidate;
5. apply the standing Final Human Release Approval automatically;
6. publish immediately when every mandatory gate is green.
