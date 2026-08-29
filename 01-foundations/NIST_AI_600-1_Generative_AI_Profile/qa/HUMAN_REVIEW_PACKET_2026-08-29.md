# Manual 04 — Human Review Packet

**Manual:** NIST AI 600-1 Generative AI Profile Implementation  
**Purpose:** Pre-stage the substantive human review boundary while Manual 03 remains the front-of-line publication target.  
**Corrected durable publication source head recorded by package:** `2b1e27f06c1f35ff2b95b8b528a30aae4682bd5d`  
**Current repair branch:** `repair/manual04-05-localization-preflight-2026-08-29`

## Control boundary

This packet does not make Manual 04 publication-eligible and does not replace competent human review. It consolidates machine-complete document/package evidence so reviewers can focus on substantive meaning, rendered usability, technical/editorial/security judgment, and changed scope.

Standing Final Human Release Approval is already recorded for the manual series. No additional owner approval prompt is required after all substantive gates and exact-final reconciliation are green.

## Preflight defects remediated before human review

Rendered/text preflight identified and corrected generator-owned defects before this packet was finalized:

- duplicate footer text caused by linked Word section footers;
- English footer status text remaining in the `es-419` and `pt-BR` PDFs.

The generator now creates the footer idempotently, localizes the footer status, and Workflow 22 fails closed on localized publication regressions including stale English boilerplate/captions, wrong-manual alt-text inheritance, and duplicate footer text.

The hashes below supersede all earlier Manual 04 review-packet hashes.

## Exact durable publication artifacts to review

### English controlled edition

- DOCX: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_EN.docx`
  - SHA-256: `9956abd742ee229b1adc4148ceab98e64aeee5ca89bf9d62455d62ac202bf116`
- PDF: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_EN.pdf`
  - SHA-256: `cf5f4469e18dfe13dfdd327fc07c0a6c971160bf0c3b51e93f742177af1ba209`
  - Pages: 15

### Spanish (`es-419`) controlled localization candidate

- DOCX: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_ES-419.docx`
  - SHA-256: `84d62af90ddc6766639e6a4aebdb81b1ce484b8a43adf3c1bd21666053ccfa95`
- PDF: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_ES-419.pdf`
  - SHA-256: `d67fc8a14e6ee182db998dcc50aef7507e51f64bbb8d39bed3f5a0402e4d0d03`
  - Pages: 15

### Brazilian Portuguese (`pt-BR`) controlled localization candidate

- DOCX: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_PT-BR.docx`
  - SHA-256: `5fe3e4b08555c01e4e677f85c11c7e3fac82bb4fc44b94382593c0179a4dc339`
- PDF: `publication/Manual_04_NIST_AI_600-1_Generative_AI_Profile_PT-BR.pdf`
  - SHA-256: `0ea9a96b924fbcae0d870542a940efd2ab8140dfa0668202450663c59d7a6f86`
  - Pages: 15

Supporting machine evidence:

- `publication/qa/MANUAL_04_PUBLICATION_REPORT.json`
- `publication/qa/MANUAL_04_PAGE_QA.csv`
- `publication/qa/MANUAL_04_SHA256SUMS.txt`
- `qa/SOURCE_VERIFICATION_2026-08-25.md`
- `qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md`
- `qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md`
- Workflow 22 localized-publication regression QA

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

Machine page QA and regression QA are supporting evidence only.

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
3. run exact-final Manual 04 QA, localization QA, localized-publication regression QA, document/publication QA, structure, trilingual parity, workflow security, release-package, and release-pipeline meta QA;
4. reconcile catalog and release registry to the exact final candidate;
5. apply the standing Final Human Release Approval automatically;
6. publish immediately when every mandatory gate is green and Manual 03 is already published.
