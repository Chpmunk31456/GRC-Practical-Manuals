# Manual 03 — Human Review Packet

**Manual:** NIST AI Risk Management Framework Implementation  
**Purpose:** Close the remaining substantive human gates without repeating completed machine QA.  
**Controlled content source head:** `0c5e219dcca52266f6ea60d24fd16690df0de575`  
**Corrected publication-generation revision recorded in durable QA report:** `415cb1bb4afcda24109137eca1d6890462458cd8`  
**Release branch:** `release/manual03-publication-repair-2026-08-28`

## Review boundary

This packet is for competent human review only. Automated QA and AI-assisted inspection already support structural, document-processing, provenance, and rendered-preflight evidence, but do not substitute for the semantic, terminology, accessibility/visual, or changed-scope decisions below.

Standing Final Human Release Approval is already recorded. Do **not** request a second final owner approval after the substantive reviews and exact-final reconciliation are green.

## Preflight defects already remediated before human review

Rendered/document preflight identified and corrected generator-owned localization defects before this packet was finalized:

- Spanish and Portuguese figure captions had remained in English;
- localized title/status/control-line/assurance-boundary/section-heading/footer boilerplate had inherited English generator text;
- all 15 Spanish figure captions and all 15 Portuguese figure captions now render in their target language;
- regenerated Spanish and Portuguese contact sheets were visually rechecked as supporting evidence;
- PDF text preflight confirms zero stale English `Implementation memory graphic` / `Chapter memory graphic` captions in the two localized PDFs.

These corrections changed generated publication artifacts and therefore the hashes below supersede all earlier Manual 03 review-packet hashes.

## Exact publication artifacts to review

### English controlled edition

- DOCX: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_EN.docx`
  - SHA-256: `a56e5a342d41d17df8201aa8bad2adb952881956de339c40036069ba5f8e8ebc`
- PDF: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_EN.pdf`
  - SHA-256: `14d7a1774c3a2b8cded02e318035e52064867f0324c41faeaaefdf3ba66ce784`
  - Pages: 47

### Spanish (`es-419`) controlled localization candidate

- DOCX: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_ES-419.docx`
  - SHA-256: `f07b5cafa67c5bf7400cb8a7c7cfdea4bbd67a6ba566acdf07436766fdc7704f`
- PDF: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_ES-419.pdf`
  - SHA-256: `d739d0974e70e9125198bb99953b4302a70aeab221e2fc803f7e7b9f58e0e707`
  - Pages: 48

### Brazilian Portuguese (`pt-BR`) controlled localization candidate

- DOCX: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_PT-BR.docx`
  - SHA-256: `cc7ffb0efdd89665bd9fd5a66c87115ad5ab73dd676640cba7ac0afb81a0ec44`
- PDF: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_PT-BR.pdf`
  - SHA-256: `b8b4789552a6a4e7c4861eee8c71168f1e355127a8834703260a9c504bd719c3`
  - Pages: 48

Supporting evidence:

- `01-foundations/NIST_AI_RMF_1.0/publication/qa/MANUAL_03_PUBLICATION_REPORT.json`
- `01-foundations/NIST_AI_RMF_1.0/publication/qa/MANUAL_03_PAGE_QA.csv`
- `01-foundations/NIST_AI_RMF_1.0/publication/qa/MANUAL_03_SHA256SUMS.txt`

## Gate A — `es-419` semantic and terminology review

Reviewer must compare the Spanish edition against the controlled English edition and confirm that:

- NIST identifiers, GOVERN/MAP/MEASURE/MANAGE, roles, decision rights, applicability boundaries, residual-risk language, stop/rollback language, evidence expectations, and assurance disclaimers preserve meaning;
- no localized wording implies NIST certification, mandatory law, universal applicability, trustworthy-AI achievement, or an audit opinion;
- instructional graphics, captions, accessible explanations, and terminology are semantically consistent with the English source;
- any finding is recorded and remediated before approval.

**Reviewer:** ____________________  
**Qualification/competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate B — `pt-BR` semantic and terminology review

Reviewer must compare the Portuguese edition against the controlled English edition using the same criteria as Gate A. Particular attention should be paid to retained industry terms or English-derived terminology (for example `red team`, `rollback`, `logging`, or other technical terms) to confirm that the chosen terminology is appropriate for the intended Brazilian Portuguese professional audience.

**Reviewer:** ____________________  
**Qualification/competence basis:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate C — rendered accessibility and visual review

Human reviewer must inspect all three final PDFs and, where relevant, DOCX behavior. Review at minimum:

- headings and hierarchy;
- tables and lists;
- figures and captions;
- instructional-graphic legibility and accessible explanations;
- clipping, overlaps, orphaned content, page breaks, whitespace anomalies, and blank/near-blank pages;
- links where present;
- language presentation and localized labels;
- document metadata/language presentation where visible to the reviewer;
- practical reading sequence and usable reading order.

Machine page QA and AI-assisted inspection are supporting evidence only.

**Reviewer:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Evidence reviewed:** EN 47 pages / ES 48 pages / PT 48 pages / DOCX as needed  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Gate D — changed-scope review

Reviewer must confirm that the reviewed artifact hashes above correspond to the intended content candidate and that later release-branch changes are limited to package placement, publication-generator localization repair, workflow/release-pipeline repair, or review-evidence reconciliation unless explicitly re-reviewed.

Any content, translation, figure-content, or substantive document change after Gates A–C requires the affected gate to reopen and the new artifact hashes to be reviewed.

**Reviewer:** ____________________  
**Date:** ____________________  
**Decision:** APPROVED / APPROVED WITH REMEDIATION / REJECTED  
**Scope/evidence compared:** ____________________  
**Findings:** ____________________  
**Remediation / closure evidence:** ____________________

## Publication transition

After Gates A–D are approved and their evidence is committed:

1. regenerate artifacts only if remediation changed content;
2. recompute and reconcile hashes/provenance if artifacts changed;
3. run exact-final structure, trilingual parity, Manual 03, publication-repair, release-package, workflow-security, and release-pipeline meta QA;
4. if every required substantive and machine gate is green, apply the standing Final Human Release Approval automatically;
5. merge/publish Manual 03 immediately and update `.compliance/manual-catalog.json` and `.compliance/work-product-releases.json` to `published` in the same controlled release sequence.

No additional owner approval prompt is required at step 4.
