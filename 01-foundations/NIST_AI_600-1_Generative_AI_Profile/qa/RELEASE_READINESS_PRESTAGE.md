# Manual 04 — Release Readiness Control

**Manual:** NIST AI 600-1 Generative AI Profile Implementation  
**Controlled branch:** `build/nist-ai-600-1-manual-04-2026`  
**Release sequence predecessor:** Manual 03 — NIST AI RMF — **MERGED**  
**Release state:** ACTIVE RELEASE/QC — FAIL-CLOSED

Manual 04 is the front-of-line release candidate. Manual 03 no longer blocks progression, but every Manual 04 release gate below remains independently mandatory.

## Current evidence state

| Gate | State | Evidence / release condition |
|---|---|---|
| Controlled English chapter master | BUILT / EXACT-HEAD QA PASS | Four controlled 8-chapter source blocks are present. Workflow 12 passed at exact head `6095a8f187be5bdac1b04592ac3b349d79795188`; freeze only at the final release head. |
| Current NIST source-state verification | PASS / WATCH ACTIVE | `SOURCE_VERIFICATION_2026-08-25.md` records NIST AI 600-1 as the published GAI Profile companion to AI RMF 1.0 and preserves the revision watch. |
| Dedicated Manual 04 repository QA | PASS / FINAL RE-RUN REQUIRED AFTER MATERIAL CHANGES | Workflow 12 passed at exact head `6095a8f187be5bdac1b04592ac3b349d79795188`. Final release still requires success at the exact final artifact head. |
| GAI applicability/tailoring and risk-family evidence | BUILT / REVIEW REQUIRED | Controlled baseline and implementation material preserve tailoring and the twelve GAI risk families. |
| Content provenance / pre-deployment testing / incident disclosure workpapers | BUILT / REVIEW REQUIRED | Implementation content exists; release evidence must be reconciled to the exact final head. |
| Technical/editorial/security/copyright QA | OPEN | Must close with recorded findings/remediation and no unresolved blocker. |
| Accessible graphics and text equivalents | OPEN | Verify every instructional graphic, caption, alternative text/text equivalent, and non-color-dependent meaning. |
| `es-419` localization | CONTROLLED DRAFT BUILT / AUTOMATED QA PASS / HUMAN SEMANTIC REVIEW REQUIRED | Four chapter-bearing source blocks plus `RUTAS_DE_IMPLEMENTACION_MANUAL_04.md` are present. Workflow 18 passed at exact head `6095a8f187be5bdac1b04592ac3b349d79795188`. Automated QA does not constitute semantic approval. |
| `pt-BR` localization | CONTROLLED DRAFT BUILT / AUTOMATED QA PASS / HUMAN SEMANTIC REVIEW REQUIRED | Four chapter-bearing source blocks plus `CAMINHOS_DE_IMPLEMENTACAO_MANUAL_04.md` are present. Workflow 18 passed at exact head `6095a8f187be5bdac1b04592ac3b349d79795188`. Automated QA does not constitute semantic approval. |
| Terminology / semantic review | OPEN — HUMAN | Human reviewer record required for localized meaning, terminology, assurance boundaries, and reader comprehension; automated parity/grammar QA is not semantic approval. |
| DOCX/PDF generation | OPEN | Generate controlled EN / es-419 / pt-BR publication candidates from the approved source state, then run content-presence/parity preflight. |
| Page-level document/visual QA | OPEN | Verify headings, tables, lists, links, figures, captions, page breaks, clipping, metadata, language tags and reading order. |
| Release manifest / checksums / provenance | OPEN | Tie SHA-256 records and manifest to the exact reviewed release head and generated artifacts. |
| Repository / workflow security release audit | PASS AT CURRENT SOURCE HEAD / FINAL RE-RUN REQUIRED | Workflow Security and Release Package QA passed at exact head `6095a8f187be5bdac1b04592ac3b349d79795188`; re-run after publication artifacts and any material corrections. |
| Changed-scope reconciliation | CURRENT SOURCE LINEAGE RECONCILED / FINAL RE-RUN REQUIRED | Branch is reconciled to hardened `main`; publication-generation and review changes must be reconciled again at the exact final head. |
| Final Human Release Approval | STANDING AUTHORITY / NOT YET OPERATIVE | Becomes operative only for the exact final candidate after every mandatory gate is green with no unresolved blocker. |

## Mainline hardening reconciliation — 2026-08-26

Manual 04 was reconciled onto hardened `main` commit `0d962a69f1caa8bae6e63afaa5f95a72e530a88b` through merge commit `e69d6d3a0aa23f720eded9a7307525f7f7fb4430`. The resulting branch comparison was **20 commits ahead / 0 commits behind** `main`, with only the intended Manual 04 controlled delta remaining.

The reconciled lineage inherits the repository-wide blank/contentless PDF preflight, work-product release-state reconciliation, and current Manual 03 publication-repair controls from `main`. This is lineage and changed-scope evidence only; it does **not** close Manual 04 publication-artifact, semantic-review, accessibility/visual-review, provenance, or final-release gates.

## Localization automation lesson — 2026-08-26

Manual 04 exposed a deterministic false-failure class: a valid localized implementation-path Markdown file increased the raw `.md` count from four to five and caused an older localization check to report an extra source block. The corrected control classifies chapter-bearing files by chapter headings and validates support/implementation files separately. The same content-role lesson is being propagated into the shared Manuals 05–08 preflight so future manuals do not repeat raw file-count assumptions.

## Parallel-throughput rule

A wait in any Manual 04 gate must not idle the project. Independent capacity should move immediately to Manual 05 full-build work, Manual 06 source/legal architecture, Manual 07/08 controlled technical pre-stage, the shared AI Governance and Audit Toolkit, reusable graphics/localization/tooling, and research/intake for later manuals without bypassing dependency order.

## Fail-closed rule

Automated QA does not certify a GAI system or establish legal compliance, conformity, trustworthy-AI achievement, or an audit opinion. Material changes reopen affected review gates. Manual 04 may merge only after exact-head verification shows every mandatory release gate closed and no unresolved blocker remains.
