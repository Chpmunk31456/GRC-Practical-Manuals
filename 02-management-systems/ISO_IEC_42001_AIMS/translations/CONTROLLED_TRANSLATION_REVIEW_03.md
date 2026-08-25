# Manual 02 — Controlled Translation and Semantic Review 03

**Repository:** `Chpmunk31456/GRC-Practical-Manuals`

**Branch:** `build/iso-iec-42001-manual-02-2026`

**Pull request:** `#89` (draft)

**Starting HEAD:** `f5b751911f5f0283774b07100101ab4b9d95285b`

**Review date:** 2026-08-24

**Controlled source:** English Markdown master

**Localized drafts:** neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`)

**Boundary:** AI-assisted source-to-source translation review only. The human semantic-review gate remains open. This report is not human approval, an ISO-authorized translation, a conformity assessment, certification evidence, or an audit opinion.

## Method and current-source dependency

- Revalidated the complete existing 32-chapter localized source sets after Source Verification Report 01.
- Retained the chapter-by-chapter semantic review and high-confidence corrections documented in Controlled Translation Review 02.
- Compared chapter sequence, heading hierarchy, table and bullet structure, image placement, controlled terminology, risk/impact distinctions, audit/evidence logic, and external URLs.
- Checked the source-verification changes separately in `es-419` and `pt-BR`.
- Did not alter English or guess at unresolved clause, Annex, certification, normative-strength, legal, assurance, or licensed-text questions.

Current automated parity result for each language: 32 chapters in order, 91 second-level headings, 228 bullet items, 10 image placements, and 37 unique HTTPS destinations. The localized URL sets exactly match English.

## A. Spanish (`es-419`)

### Structural result

PASS. Chapters 1–32 occur exactly once and in English order. Heading hierarchy, tables, procedures, bullets, figures, references, and reusable templates retain source structure. No omitted, duplicated, or displaced chapter was found.

### Semantic result

PASS for AI-assisted parity, subject to human approval. The localized source preserves context, interested parties, leadership, policy, responsibility, risk treatment, objectives, resources, competence, communication, operational control, performance evaluation, internal audit, management review, nonconformity, corrective action, and continual improvement.

`evaluación de riesgos de IA` and `evaluación de impacto de sistemas de IA` remain distinct processes and records. Requirement/control/owner/frequency/evidence/test/finding/remediation/retest relationships remain intact.

### Terminology, omissions, and corrections

- `Declaración de Aplicabilidad` remains consistent; 26 occurrences were found across the chapter source set.
- No new omission or high-confidence semantic defect was found after the source corrections.
- No localized prose correction was applied in Review 03. Earlier corrections remain documented in Review 02.
- Human choice remains necessary for technical loanwords including `prompt`, `logs`, `logging`, `pipeline`, `framework`, `endpoint`, `sandbox`, `red teaming`, and `RAG`.

### Source/citation parity

PASS. Spanish reflects the August 24, 2026 current-information wording; distinct ISO/IEC 42003 and 42007 development status; `ISO/IEC 27001:2022`; canonical Giskard OSS, Microsoft PyRIT, and Presidio links; the three added ISO references; and ISO/IEC 17021-1 systematic-review status.

### Graphics text

PASS for source parity, subject to human terminology/accessibility review. Ten Spanish figure placements retain localized captions, alternative text, and accessible explanations. Graphic files were not changed. Human judgment remains required for Figures 4, 7, and 10 and final rendered accessibility.

## B. Brazilian Portuguese (`pt-BR`)

### Structural result

PASS. Chapters 1–32 occur exactly once and in English order. Heading hierarchy, tables, procedures, bullets, figures, references, and reusable templates retain source structure. No omitted, duplicated, or displaced chapter was found.

### Semantic result

PASS for AI-assisted parity, subject to human approval. The localized source preserves context, interested parties, leadership, policy, responsibility, risk treatment, objectives, resources, competence, communication, operational control, performance evaluation, internal audit, management review, nonconformity, corrective action, and continual improvement.

`avaliação de riscos de IA` and `avaliação de impacto de sistemas de IA` remain distinct processes and records. Requirement/control/owner/frequency/evidence/test/finding/remediation/retest relationships remain intact.

### Terminology, omissions, and corrections

- `Declaração de Aplicabilidade` remains consistent; 26 occurrences were found across the chapter source set.
- No new omission or high-confidence semantic defect was found after the source corrections.
- No localized prose correction was applied in Review 03. Earlier corrections remain documented in Review 02.
- Human choice remains necessary for technical loanwords including `prompt`, `logs`, `logging`, `pipeline`, `framework`, `endpoint`, `sandbox`, `drift`, `rollback`, `red teaming`, and `RAG`.
- Human confirmation remains necessary for `asseguração`, `constatação`, `subprocessador`, and certification `auditoria de supervisão`.

### Source/citation parity

PASS. Portuguese reflects the August 24, 2026 current-information wording; distinct ISO/IEC 42003 and 42007 development status; `ISO/IEC 27001:2022`; canonical Giskard OSS, Microsoft PyRIT, and Presidio links; the three added ISO references; and ISO/IEC 17021-1 systematic-review status.

### Graphics text

PASS for source parity, subject to human terminology/accessibility review. Ten Portuguese figure placements retain localized captions, alternative text, and accessible explanations. Graphic files were not changed. Human judgment remains required for Figures 4, 5, 7, and 10 and final rendered accessibility.

## C. Cross-language parity

- No material chapter-order, heading, procedure, table, bullet, image-placement, or URL difference was found.
- English remains the controlled source; neither localization claims ISO authorization.
- Both languages preserve the distinction between AI risk assessment and AI system impact assessment.
- Both preserve Annex A/Statement of Applicability boundaries without resolving the source report's open normative questions.
- Both preserve audit independence, evidence testing, findings, corrective action, retesting, and certification limitations.
- Both contain the same 37 external destinations as English and preserve the new source-status distinctions.
- No graphics file change was justified in this gate.

## D. Human-review queue

1. Complete competent human semantic review of all 32 chapters for both locales and record reviewer identity, competence, date, decisions, and issue closure in `HUMAN_SEMANTIC_REVIEW_CHECKLIST.md`.
2. Approve consistent technical-loanword policies for each locale.
3. Confirm Spanish and Portuguese safety terminology remains distinct from cybersecurity throughout prose, tables, and figures.
4. Confirm Figure 4 acceptance/escalation wording cannot imply unqualified acceptance of harm.
5. Confirm Figure 7 governed retention/deletion wording and Figure 10 competence/retest terminology.
6. Confirm the identified Brazilian Portuguese GRC terms for the intended audience.
7. Preserve for authorized-source review: exact Clause 4–10 and Annex A–D scope, Chapters 23/26/27 Annex applicability wording, the 38-control count, Stage 1/Stage 2 wording, the eight normative-language cues, and licensed-text similarity.

TRANSLATION REVIEW STATUS: READY FOR HUMAN SEMANTIC APPROVAL
