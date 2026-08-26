# Manual 04 — Release Readiness Control

**Manual:** NIST AI 600-1 Generative AI Profile Implementation  
**Controlled branch:** `build/nist-ai-600-1-manual-04-2026`  
**Release sequence predecessor:** Manual 03 — NIST AI RMF — **MERGED**  
**Release state:** ACTIVE RELEASE/QC — FAIL-CLOSED

Manual 04 is now the front-of-line release candidate. Manual 03 no longer blocks progression, but every Manual 04 release gate below remains independently mandatory.

## Current evidence state

| Gate | State | Evidence / release condition |
|---|---|---|
| Controlled English chapter master | BUILT / QA REQUIRED | Four controlled 8-chapter source blocks are present; freeze only at the final exact release head. |
| Current NIST source-state verification | PASS / WATCH ACTIVE | `SOURCE_VERIFICATION_2026-08-25.md` records NIST AI 600-1 as the published GAI Profile companion to AI RMF 1.0 and preserves the revision watch. |
| Dedicated Manual 04 repository QA | PASS AT PRIOR HEAD / RE-RUN REQUIRED AFTER CHANGES | Workflow 12 passed before this control update; final release requires success at the exact final head. |
| GAI applicability/tailoring and risk-family evidence | BUILT / REVIEW REQUIRED | Controlled baseline and implementation material preserve tailoring and the twelve GAI risk families. |
| Content provenance / pre-deployment testing / incident disclosure workpapers | BUILT / REVIEW REQUIRED | Implementation content exists; release evidence must be reconciled to the exact final head. |
| Technical/editorial/security/copyright QA | OPEN | Must close with recorded findings/remediation and no unresolved blocker. |
| Accessible graphics and text equivalents | OPEN | Verify every instructional graphic, caption, alternative text/text equivalent, and non-color-dependent meaning. |
| `es-419` localization | OPEN | Controlled localized master and semantic approval required before publication in Spanish. |
| `pt-BR` localization | OPEN | Controlled localized master and semantic approval required before publication in Brazilian Portuguese. |
| Terminology / semantic review | OPEN | Human reviewer record required; automated parity/grammar QA is not semantic approval. |
| DOCX/PDF generation | OPEN | Generate only from the controlled approved source/localization state. |
| Page-level document/visual QA | OPEN | Verify headings, tables, lists, links, figures, captions, page breaks, clipping, metadata, language tags and reading order. |
| Release manifest / checksums / provenance | OPEN | Tie SHA-256 records and manifest to the exact reviewed release head and generated artifacts. |
| Repository / workflow security release audit | OPEN | Re-run and reconcile at exact final head. |
| Changed-scope reconciliation | OPEN | Confirm no material change escaped an affected human or deterministic review gate. |
| Final Human Release Approval | STANDING AUTHORITY / NOT YET OPERATIVE | Becomes operative only for the exact final candidate after every mandatory gate is green with no unresolved blocker. |

## Parallel-throughput rule

A wait in any Manual 04 gate must not idle the project. Independent capacity should move immediately to Manual 05 full-build work, Manual 06 source/legal architecture, Manual 07/08 controlled technical pre-stage, the shared AI Governance and Audit Toolkit, reusable graphics/localization/tooling, and research/intake for later manuals without bypassing dependency order.

## Fail-closed rule

Automated QA does not certify a GAI system or establish legal compliance, conformity, trustworthy-AI achievement, or an audit opinion. Material changes reopen affected review gates. Manual 04 may merge only after exact-head verification shows every mandatory release gate closed and no unresolved blocker remains.