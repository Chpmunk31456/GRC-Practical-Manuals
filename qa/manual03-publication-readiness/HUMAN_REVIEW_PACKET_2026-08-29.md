# Manual 03 — Human Review Packet

**Manual:** NIST AI Risk Management Framework Implementation  
**Purpose:** Close the remaining substantive human gates without repeating completed machine QA.  
**Controlled content source head:** `0c5e219dcca52266f6ea60d24fd16690df0de575`  
**Release branch:** `release/manual03-publication-repair-2026-08-28`

## Review boundary

This packet is for competent human review only. Automated QA and AI-assisted inspection already support structural, document-processing, provenance, and rendered-preflight evidence, but do not substitute for the semantic, terminology, accessibility/visual, or changed-scope decisions below.

Standing Final Human Release Approval is already recorded. Do **not** request a second final owner approval after the substantive reviews and exact-final reconciliation are green.

## Exact publication artifacts to review

### English controlled edition

- DOCX: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_EN.docx`
  - SHA-256: `3a9c588d8a06cf1fbc56df9dccbf318891450d7b83a722ccdbaa878041ce5370`
- PDF: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_EN.pdf`
  - SHA-256: `d6d17e92108b9374270faf34d970594b81059e928ee605c194ecf76071c10603`
  - Pages: 47

### Spanish (`es-419`) controlled localization candidate

- DOCX: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_ES-419.docx`
  - SHA-256: `84d92ca2136b057f9033f9ae5abcce46c739101c437f320fb64b335b68b86bd1`
- PDF: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_ES-419.pdf`
  - SHA-256: `d95ac0140fe72073f0ad49e97bf57aa7dbe6123c8705d8e9d7daa83a1456b37e`
  - Pages: 48

### Brazilian Portuguese (`pt-BR`) controlled localization candidate

- DOCX: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_PT-BR.docx`
  - SHA-256: `caad011fc8f2e60b4b09a0097b5161b8c41ed367eb470f7b169c8c16ed64779d`
- PDF: `01-foundations/NIST_AI_RMF_1.0/publication/Manual_03_NIST_AI_RMF_Implementation_PT-BR.pdf`
  - SHA-256: `f6f87a258d7ce1e46783c55e412485eea210ffe87db84378fb1c4d14794bc486`
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

Reviewer must compare the Portuguese edition against the controlled English edition using the same criteria as Gate A.

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

Reviewer must confirm that the reviewed artifact hashes above correspond to the intended content candidate and that later release-branch changes are limited to package placement, workflow/release-pipeline repair, or review-evidence reconciliation unless explicitly re-reviewed.

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
