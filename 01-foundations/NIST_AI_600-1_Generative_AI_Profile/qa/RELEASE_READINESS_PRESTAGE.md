# Manual 04 — Release Readiness Control

**Manual:** NIST AI 600-1 Generative AI Profile Implementation  
**Controlled content lineage:** `build/nist-ai-600-1-manual-04-2026`  
**Review-preparation branch:** `release/manual04-human-review-prep-2026-08-29`  
**Strict publication sequence predecessor:** Manual 03 — NIST AI RMF — **HUMAN REVIEW PENDING**  
**Release state:** PRE-STAGED FOR HUMAN REVIEW — FAIL-CLOSED

Manual 04 is not permitted to bypass Manual 03 in the strict controlled publication sequence. While Manual 03 closes its substantive human gates, Manual 04 may complete independent preflight, review preparation, defect remediation, and exact evidence reconciliation so it can move efficiently when it becomes front-of-line.

## Current evidence state

| Gate | State | Evidence / release condition |
|---|---|---|
| Controlled English chapter master | BUILT / MACHINE QA PASS | Four controlled 8-chapter source blocks are present. Final release requires exact-final QA after all remediation/review evidence. |
| Current NIST source-state verification | PASS / WATCH ACTIVE | `SOURCE_VERIFICATION_2026-08-25.md` records NIST AI 600-1 as the published GAI Profile companion to AI RMF 1.0 and preserves the revision watch. |
| Dedicated Manual 04 repository QA | PASS / FINAL RE-RUN REQUIRED | Dedicated Manual 04 QA has passed on the controlled lineage and continues to run in repository-wide checks. Exact-final release validation remains required. |
| GAI applicability/tailoring and risk-family evidence | BUILT / HUMAN REVIEW REQUIRED | Controlled baseline and implementation material preserve tailoring and the twelve GAI risk families. |
| Content provenance / pre-deployment testing / incident disclosure workpapers | BUILT / HUMAN REVIEW REQUIRED | Implementation content exists; substantive technical/editorial review and exact-final reconciliation remain required. |
| Technical/editorial/security/copyright QA | OPEN — HUMAN | Must close with reviewer/date/decision/evidence/findings/remediation and no unresolved blocker. |
| Accessible graphics and text equivalents | MACHINE PACKAGE VALIDATED / HUMAN RENDERED REVIEW REQUIRED | Publication QA reports three graphics per edition with DOCX alternative-text entries. Human inspection must still confirm legibility, captions/text equivalents, reading experience, and non-color-dependent meaning. |
| `es-419` localization | CONTROLLED DRAFT BUILT / AUTOMATED QA PASS / HUMAN SEMANTIC REVIEW REQUIRED | Four chapter-bearing source blocks plus `RUTAS_DE_IMPLEMENTACION_MANUAL_04.md` are present. Automated QA does not constitute semantic approval. |
| `pt-BR` localization | CONTROLLED DRAFT BUILT / AUTOMATED QA PASS / HUMAN SEMANTIC REVIEW REQUIRED | Four chapter-bearing source blocks plus `CAMINHOS_DE_IMPLEMENTACAO_MANUAL_04.md` are present. Automated QA does not constitute semantic approval. |
| Terminology / semantic review | OPEN — HUMAN | Competent human review required for localized meaning, terminology, assurance boundaries, graphics/captions, and reader comprehension. |
| DOCX/PDF generation | COMPLETE / DURABLE / MACHINE QA PASS | Durable EN, es-419, and pt-BR DOCX/PDF artifacts are committed under `publication/`; all six are recorded PASS in `publication/qa/MANUAL_04_PUBLICATION_REPORT.json`. |
| Page-level document QA | AUTOMATED PASS / HUMAN VISUAL-ACCESSIBILITY REVIEW REQUIRED | Page QA and renders were generated for all three PDFs; each edition is 15 pages. Human rendered review remains mandatory. |
| Release manifest / checksums / provenance | GENERATED / FINAL RECONCILIATION REQUIRED | `MANUAL_04_PUBLICATION_REPORT.json`, `MANUAL_04_PAGE_QA.csv`, and `MANUAL_04_SHA256SUMS.txt` durably record package evidence. Hashes must remain tied to the exact human-reviewed candidate and be recomputed if remediation changes artifacts. |
| Human review packet | PREPARED | `HUMAN_REVIEW_PACKET_2026-08-29.md` binds the substantive review gates to the durable artifact hashes and separates machine-complete work from human decisions. |
| Repository / workflow security release audit | MACHINE PASS ON CURRENT MAINLINE / EXACT-FINAL RE-RUN REQUIRED | Repository security/release controls are green on current mainline; final candidate must re-run after any review-driven remediation or release-state changes. |
| Changed-scope reconciliation | PRE-STAGED / FINAL HUMAN REVIEW REQUIRED | Durable artifacts and review packet are now identified; reviewer must confirm reviewed hashes and later changes before publication. |
| Final Human Release Approval | STANDING AUTHORITY / AUTOMATIC AFTER PRECEDING GATES | Standing approval is already recorded and requires no additional owner prompt. It becomes operative only after every substantive and exact-final machine gate is green. |

## Durable publication package — 2026-08-29 reconciliation

The repository now contains the complete six-file trilingual publication package under `publication/`, plus page QA, publication reports, and SHA-256 evidence under `publication/qa/`. This closes the former machine-level document-generation and checksum blockers; it does **not** close semantic, technical/editorial/security/copyright, rendered human accessibility/visual, or changed-scope review.

The controlled package report identifies source head `691c1aa5d01ef7395793be10195095551ace43a8` and records:

- English: 32 chapters, 3 graphics, 15 PDF pages;
- `es-419`: 32 chapters, 3 graphics, 15 PDF pages;
- `pt-BR`: 32 chapters, 3 graphics, 15 PDF pages;
- all six DOCX/PDF artifacts: automated publication status PASS.

## Human-review efficiency rule

Use `HUMAN_REVIEW_PACKET_2026-08-29.md` as the authoritative review checklist for the current durable package. Reviewers should not repeat machine work merely because the older readiness record once marked document generation or checksums open. They must still independently perform the substantive gates explicitly assigned to human judgment.

Any remediation that changes controlled content, localization meaning, figures, security meaning, or rendered artifacts invalidates the affected artifact hash and reopens the corresponding review gate.

## Localization automation lesson — 2026-08-26

Manual 04 exposed a deterministic false-failure class: a valid localized implementation-path Markdown file increased the raw `.md` count and caused an older localization check to report an extra source block. The corrected control classifies chapter-bearing files by chapter headings and validates support/implementation files separately. That content-role lesson remains a shared control for later manuals.

## Continuous-improvement lesson — 2026-08-29

Later Manual 07/08 preflight demonstrated that structurally green localized packages can still contain inherited English generator-owned boilerplate or captions. Before Manual 04 enters substantive review, its rendered/localized package should therefore also be tested against the reusable localized-publication regression pattern and visually spot-checked for the same defect family. Any finding must be repaired at the generator/source layer where practical, then the package hashes and review packet must be reconciled.

## Parallel-throughput rule

A wait in Manual 03 or any Manual 04 human gate must not idle the project. Independent capacity should continue downstream publication preflight, localization regression hardening, durable packaging, source verification, graphics, tooling, provenance, and future-manual architecture without bypassing dependency or human-review order.

## Fail-closed rule

Automated QA does not certify a GAI system or establish legal compliance, conformity, trustworthy-AI achievement, or an audit opinion. Material changes reopen affected review gates. Manual 04 may publish only when its substantive human evidence is complete, exact-final machine/security/provenance reconciliation is green, Manual 03 sequencing is satisfied, and the standing automatic-publication rule then applies.
