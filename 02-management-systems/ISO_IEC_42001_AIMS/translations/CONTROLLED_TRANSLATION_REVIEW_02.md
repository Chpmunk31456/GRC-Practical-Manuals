# Manual 02 — Controlled Translation and Semantic Review 02

**Repository:** `Chpmunk31456/GRC-Practical-Manuals`

**Branch:** `build/iso-iec-42001-manual-02-2026`

**Pull request:** `#89`

**Starting HEAD:** `983a08638a533c790805726c5c761cecf24122b6`

**Controlled source language:** English

**Localized drafts reviewed:** neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`)

**Review boundary:** This is an AI-assisted source-to-source review and correction pass. It does not complete the controlled human semantic-review gate, establish conformity, provide certification evidence, or express an audit opinion.

## Method and evidence

- Reviewed the English Markdown master and each localized chapter in source order, Chapters 1–32.
- Reviewed the localized implementation-path entry for each language.
- Compared chapter order, heading hierarchy, tables, table rows, bullets, images, links, official URLs, standard identifiers, captions, alternative text, and accessible explanations.
- Reviewed the twenty localized figures through their editable SVG text and rendered PNG contact sheets.
- Used direct source-context review; no machine-translation library, translation API, local translation model, or browser translation generated the prose.
- Applied only high-confidence corrections. Locale-preference and domain-terminology decisions remain in the human-review queue.

Automated comparison found no chapter-level differences in the count of second-level headings, tables, table rows, bullets, image placements, or external links. Each localized source contains Chapters 1–32 exactly once and in order. The 34 external URLs in each full source set match the English master.

## Corrections applied in this pass

| ID | Language | Location | Issue | Resolution |
|---|---|---|---|---|
| CTR-001 | `es-419` | Chapter 1 | `secure` and `safe` were collapsed while `reliable` was introduced. | Restored separate threat-protection and human-safety concepts and removed the unsupported reliability substitution. |
| CTR-002 | `es-419` | Chapter 6 | Imperative agreement error: `intégralas`. | Corrected to `intégrelas`. |
| CTR-003 | `es-419` | Chapter 15 | `safety concern` was ambiguous with cybersecurity. | Clarified as `preocupación de seguridad funcional`. |
| CTR-004 | `es-419` | Chapter 29 | Certification surveillance was shortened to generic `vigilancia`. | Clarified as `auditorías de vigilancia`. |
| CTR-005 | `es-419` | Chapter 30 and related templates/playbook | `reprueba` could be read as failure rather than retesting. | Replaced with neutral `nueva prueba`. |
| CTR-006 | `es-419` | Implementation entry | The localized language was incorrectly labeled as the controlled language. | Restored English as the controlled source and labeled `es-419` as the localization language. |
| CTR-007 | `es-419` | Implementation entry | Risk and impact screening wording could be read as one collapsed assessment. | Clarified that the risk and impact evaluations are documented and distinct. |
| CTR-008 | `es-419` | Implementation entry | Repository QA was described as checking unqualified linguistic parity. | Limited the statement to automated structural parity. |
| CTR-009 | `pt-BR` | Chapter 1 | `secure` and `safe` were collapsed while `reliable` was introduced. | Restored separate threat-protection and human-safety concepts and removed the unsupported reliability substitution. |
| CTR-010 | `pt-BR` | Chapter 15 | `safety concern` was ambiguous with cybersecurity. | Clarified as `preocupação de segurança funcional`. |
| CTR-011 | `pt-BR` | Chapter 20, Annex A.8 row | The qualifier tying “other information” to interested parties was omitted. | Restored `outras informações para partes interessadas`. |
| CTR-012 | `pt-BR` | Chapter 29 | Certification surveillance was shortened to generic `supervisão`. | Clarified as `auditorias de supervisão`. |
| CTR-013 | `pt-BR` | Implementation entry | The localized language was incorrectly labeled as the controlled language. | Restored English as the controlled source and labeled `pt-BR` as the localization language. |
| CTR-014 | `pt-BR` | Implementation entry | English recommendations using `should` were strengthened to `deve`. | Restored recommendation strength with `deveria` in both affected passages. |
| CTR-015 | `pt-BR` | Implementation entry | Risk and impact screening wording could be read as one collapsed assessment. | Clarified that the risk and impact screenings are documented and distinct. |
| CTR-016 | `pt-BR` | Implementation entry | Repository QA was described as checking unqualified linguistic parity. | Limited the statement to automated structural parity. |

## A. Spanish (`es-419`)

### PASS items

- Chapters 1–32 occur exactly once and in the English source order.
- Heading levels, tables, numbered content, bullets, figure placements, and official links preserve structural parity.
- `Declaración de Aplicabilidad` is consistent in chapters, tables, headings, the glossary, and the implementation entry.
- Risk assessment and AI system impact assessment remain separate in Chapters 7, 9, 15, 24, 31, and 32.
- Requirement, control, owner, evidence, test, finding, remediation, retention, and review relationships remain operationally intact.
- Internal-audit independence, management accountability, correction, corrective action, and continual improvement remain distinct.
- All ten chapter figures reference only `assets/es-419/media/`; each has a localized caption, alternative text, and accessible explanation.
- Official source URLs and standard identifiers were preserved.

### Chapter-by-chapter result

| Chapter | Result | Review note |
|---:|---|---|
| 1 | Corrected | Restored the security/safety distinction in the certification boundary. |
| 2 | PASS | PDCA stages, evidence outputs, and integration logic preserved. |
| 3 | PASS | Organizational roles, audit independence, and roadmap preserved. |
| 4 | PASS | Context, interested parties, binding obligations, scope, and process logic preserved. |
| 5 | PASS | Leadership, policy, accountability, authority, and conflict controls preserved. |
| 6 | Corrected | Fixed imperative grammar; risk/opportunity action strength preserved. |
| 7 | PASS | Risk criteria, scenarios, inherent/current/target/residual distinctions, and evidence preserved. |
| 8 | PASS | Treatment, Annex A comparison, residual approval, and applicability-record fields preserved. |
| 9 | PASS | Impact assessment remains distinct from risk assessment; affected-party and redress logic preserved. |
| 10 | PASS | Objectives, metrics, evidence, and controlled-change requirements preserved. |
| 11 | PASS | Resource categories, independence, constraints, and residual-risk effects preserved. |
| 12 | PASS with human term choice | Competence, awareness, and communication logic preserved; technical loanword policy remains open. |
| 13 | PASS with human term choice | Document-control lifecycle and retention preserved; `prompt` and `logs` remain for human terminology choice. |
| 14 | PASS | Lifecycle gates, evidence decisions, control operation, and external provision preserved. |
| 15 | Corrected | Clarified the safety trigger; risk, treatment, and impact operations remain distinct. |
| 16 | PASS | Measurement design, data quality, severe-failure views, and action triggers preserved. |
| 17 | PASS | Audit criteria, independence, sampling, evidence, testing, findings, and follow-up preserved. |
| 18 | PASS | Management-review inputs, outputs, decisions, resources, and closure evidence preserved. |
| 19 | PASS | Correction, cause analysis, corrective action, effectiveness, and recurrence review preserved. |
| 20 | PASS with human term choice | Annex groups and 38-control boundary preserved; `logs` remains a terminology decision. |
| 21 | PASS | Policy evidence and test relationships preserved. |
| 22 | PASS | Accountability, escalation, protected reporting, and non-retaliation preserved. |
| 23 | PASS with human term choice | Resource traceability preserved; `frameworks` and `prompts` remain terminology decisions. |
| 24 | PASS | Individual/group and societal impact outcomes and quality checks preserved. |
| 25 | PASS with human term choice | Lifecycle evidence preserved; `prompts`, `endpoints`, and `logs` remain terminology decisions. |
| 26 | PASS | Data acquisition, quality, provenance, preparation, segregation, and testing preserved. |
| 27 | PASS | Audience-specific information, reporting, incidents, privacy, and redress preserved. |
| 28 | PASS with human term choice | Responsibility allocation and supplier/customer duties preserved; `logging` and `subprocesadores` need locale confirmation. |
| 29 | Corrected | Clarified certification surveillance; Stage 1/Stage 2 and assurance boundaries preserved. |
| 30 | Corrected with human term choice | Corrected ambiguous retest wording; tool names, URLs, safe-use limits, and evidence schema preserved. |
| 31 | PASS | Manager and analyst authority boundaries, laboratory safeguards, and interview answers preserved. |
| 32 | PASS | Templates, glossary distinctions, index, URLs, and blank fields preserve source function. |

### Semantic, terminology, omission, and structural findings

- The material semantic issues detected were corrected under CTR-001, CTR-003, CTR-006, and CTR-007.
- The high-confidence terminology/readability issues detected were corrected under CTR-002, CTR-004, CTR-005, and CTR-008.
- No unresolved omission or duplicated section was found.
- No unresolved structural mismatch was found.
- Remaining terminology choices are listed in the human-review queue and do not authorize closing that gate.

### Graphic and accessibility result

- Ten SVG/PNG figure pairs were present, nonblank, distinct, readable in contact-sheet review, and referenced only by the Spanish source.
- Visible labels were Spanish; no unintended English-visible label was found.
- Captions, alternative text, and accessible explanations preserved the intended process or decision relationship.
- Human review is still required for professional word choice in Figures 4, 7, and 10 and for final rendering accessibility.

### Recommended corrections

The high-confidence corrections listed as CTR-001 through CTR-008 were applied. A competent human reviewer should resolve the remaining loanword and figure-language choices before signing the Spanish row in the controlled checklist.

## B. Brazilian Portuguese (`pt-BR`)

### PASS items

- Chapters 1–32 occur exactly once and in the English source order.
- Heading levels, tables, numbered content, bullets, figure placements, and official links preserve structural parity.
- `Declaração de Aplicabilidade` is consistent in chapters, tables, headings, the glossary, and the implementation entry.
- Risk assessment and AI system impact assessment remain separate in Chapters 7, 9, 15, 24, 31, and 32.
- Requirement, control, owner, evidence, test, finding, remediation, retention, and review relationships remain operationally intact.
- Internal-audit independence, management accountability, correction, corrective action, and continual improvement remain distinct.
- All ten chapter figures reference only `assets/pt-BR/media/`; each has a localized caption, alternative text, and accessible explanation.
- Official source URLs and standard identifiers were preserved.

### Chapter-by-chapter result

| Chapter | Result | Review note |
|---:|---|---|
| 1 | Corrected | Restored the security/safety distinction in the certification boundary. |
| 2 | PASS | PDCA stages, evidence outputs, and integration logic preserved. |
| 3 | PASS | Organizational roles, audit independence, and roadmap preserved. |
| 4 | PASS | Context, interested parties, binding obligations, scope, and process logic preserved. |
| 5 | PASS | Leadership, policy, accountability, authority, and conflict controls preserved. |
| 6 | PASS | Risk/opportunity planning inputs, ownership, evidence, and effectiveness preserved. |
| 7 | PASS with human term choice | Risk method preserved; `drift` remains a terminology decision. |
| 8 | PASS | Treatment, Annex A comparison, residual approval, and applicability-record fields preserved. |
| 9 | PASS with human term choice | Impact assessment remains distinct; `drift` remains a terminology decision. |
| 10 | PASS with human term choice | Controlled-change logic preserved; `rollback` remains a terminology decision. |
| 11 | PASS with human term choice | Resources preserved; `logging` and `sandbox` remain terminology decisions. |
| 12 | PASS | Competence, awareness, communication, correction, and escalation preserved. |
| 13 | PASS with human term choice | Document-control and retention preserved; `prompt`, `logs`, and `rollback` remain terminology decisions. |
| 14 | PASS with human term choice | Lifecycle evidence preserved; `drift` and `rollback` remain terminology decisions. |
| 15 | Corrected with human term choice | Clarified the safety trigger; `prompt` and `drift` remain terminology decisions. |
| 16 | PASS | Measurement design, severe-failure views, and management action preserved. |
| 17 | PASS | Audit criteria, independence, evidence, testing, findings, and follow-up preserved. |
| 18 | PASS | Management-review inputs, outputs, decisions, resources, and closure evidence preserved. |
| 19 | PASS | Correction, cause analysis, corrective action, effectiveness, and recurrence review preserved. |
| 20 | Corrected with human term choice | Restored the interested-party qualifier in A.8; `logs` remains a terminology decision. |
| 21 | PASS | Policy evidence and test relationships preserved. |
| 22 | PASS | Accountability, escalation, protected reporting, and non-retaliation preserved. |
| 23 | PASS with human term choice | Resource traceability preserved; `frameworks`, `prompts`, and the preferred subprocessor term need confirmation. |
| 24 | PASS | Individual/group and societal impact outcomes and quality checks preserved. |
| 25 | PASS with human term choice | Lifecycle evidence preserved; `prompts`, `drift`, `rollback`, `endpoints`, and `logs` remain terminology decisions. |
| 26 | PASS | Data acquisition, quality, provenance, preparation, segregation, and testing preserved. |
| 27 | PASS | Audience-specific information, reporting, incidents, privacy, and redress preserved. |
| 28 | PASS with human term choice | Responsibility allocation preserved; `logging`, `subprocessadores`, and `asseguração` need professional-locale confirmation. |
| 29 | Corrected | Clarified certification surveillance; Stage 1/Stage 2 and assurance boundaries preserved. |
| 30 | PASS with human term choice | Tool names, URLs, safe-use limits, and evidence schema preserved; technical loanword policy remains open. |
| 31 | PASS with human term choice | Authority boundaries and laboratory safeguards preserved; `rollback` remains a terminology decision. |
| 32 | PASS | Templates, glossary distinctions, index, URLs, and blank fields preserve source function. |

### Semantic, terminology, omission, and structural findings

- The material semantic issues detected were corrected under CTR-009 through CTR-015.
- The QA-claim boundary was corrected under CTR-016.
- No unresolved omission or duplicated section was found.
- No unresolved structural mismatch was found.
- Remaining terminology choices are listed in the human-review queue and do not authorize closing that gate.

### Graphic and accessibility result

- Ten SVG/PNG figure pairs were present, nonblank, distinct, readable in contact-sheet review, and referenced only by the Portuguese source.
- Visible labels were Portuguese; no unintended English-visible label was found.
- Captions, alternative text, and accessible explanations preserved the intended process or decision relationship.
- Human review is still required for professional word choice in Figures 4, 5, 7, and 10 and for final rendering accessibility.

### Recommended corrections

The high-confidence corrections listed as CTR-009 through CTR-016 were applied. A competent human reviewer should resolve the remaining technical-loanword, assurance, supplier, and figure-language choices before signing the Portuguese row in the controlled checklist.

## C. Cross-language parity

- The three source sets retain identical chapter order and chapter-level counts for headings, tables, table rows, bullets, images, and external links.
- The same 34 official/project URLs are present in English, Spanish, and Portuguese; no official source URL or source identifier was replaced.
- English remains the controlled source after correcting both localized implementation-entry labels.
- Safety and cybersecurity are now explicitly distinct in the corrected certification and operational-trigger passages.
- Risk assessment and AI system impact assessment remain separate processes, records, decisions, and templates; the implementation-entry screening language was clarified in both localized editions.
- Portuguese recommendation language was reduced from an unsupported obligation back to the English recommendation strength.
- The Portuguese Annex A.8 summary now includes the previously omitted interested-party qualifier.
- Certification surveillance is now explicit in both localized certification paths.
- Spanish retest language no longer risks being interpreted as a failed test.
- No localized source claims that repository QA establishes conformity, certification, legal compliance, or audit assurance.

## D. Human-review queue

1. `es-419`: decide and document a consistent policy for `prompt`, `logs`, `logging`, `pipeline`, `framework`, `endpoint`, `sandbox`, `red teaming`, `RAG`, and related technical loanwords.
2. `pt-BR`: decide and document a consistent policy for `prompt`, `logs`, `logging`, `pipeline`, `framework`, `endpoint`, `sandbox`, `drift`, `rollback`, `red teaming`, and `RAG`.
3. `pt-BR`: confirm the preferred professional terms for `asseguração`, `constatação`, `subprocessador`, and certification `auditoria de supervisão` across intended Brazilian GRC audiences.
4. Both languages: confirm that safety terminology remains distinguishable from cybersecurity in every context, including figures and tables.
5. Both languages: confirm that “accept/escalate” in Figure 4 cannot be read as permitting unqualified acceptance of harm rather than an accountable impact decision.
6. Both languages: confirm that the final retain/delete wording in Figure 7 communicates governed retention and deletion rather than simultaneous actions.
7. Both languages: confirm Figure 10 terminology for competence evidence, corrective-action retesting, and portfolio work.
8. Both languages: perform a competent human semantic review of all 32 chapters and record reviewer identity, date, competence, decisions, and issue closure in `HUMAN_SEMANTIC_REVIEW_CHECKLIST.md`.
9. Both languages: after human review, consolidate one Markdown master per locale, then generate accessible DOCX and PDF artifacts and conduct page-by-page visual QA.

## E. Release gate

TRANSLATION REVIEW STATUS: READY FOR HUMAN SEMANTIC APPROVAL
