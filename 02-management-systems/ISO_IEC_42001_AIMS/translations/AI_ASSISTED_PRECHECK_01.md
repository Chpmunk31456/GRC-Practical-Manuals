# Manual 02 — AI-assisted localization precheck 01

**Scope:** draft Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) 32-chapter source sets

**Review type:** AI-assisted precheck only; automated and AI-assisted issue detection

**Human semantic-review gate:** the human gate remains OPEN

This precheck supports, but does not replace, the controlled human semantic and terminology review. It does not identify an individual as a human reviewer, approve either language, or change the baseline status `draft-human-review-required`.

## Corrections applied

| ID | Language | Location | Finding | Resolution | Classification |
|---|---|---|---|---|---|
| AP-001 | `es-419` | Chapter 23 | English imperative `Reconcile` remained in Spanish prose. | Replaced with the natural instruction `Concilie` and adjusted articles for readability. | Major source-language residue |
| AP-002 | `es-419` | Chapter 29 | English imperative `Reconcile` remained in Spanish prose. | Replaced with `Concilie` and adjusted the coordinated list. | Major source-language residue |
| AP-003 | `pt-BR` | Chapters 3–4 | `compliance` appeared where professional Portuguese `conformidade` preserves the meaning. | Replaced with `conformidade` and `obrigações vinculantes de conformidade`. | Minor terminology |
| AP-004 | `pt-BR` | Chapters 3 and 28 | `due diligence` appeared without a Portuguese equivalent. | Replaced with `diligência prévia`. | Minor terminology |
| AP-005 | `pt-BR` | Chapters 12, 22, and 27 | `feedback` appeared in governance and complaint-handling prose. | Replaced with `retorno`. | Minor terminology |

## Human decisions still required

The following technical terms remain because their best treatment depends on professional locale preference and context. A competent human reviewer should approve one consistent approach or document context-specific exceptions:

| Language | Terms requiring decision | Review question |
|---|---|---|
| `es-419` | `prompt`, `logs`, `pipeline` | Retain common technical usage, introduce a Spanish equivalent at first use, or localize every occurrence? |
| `pt-BR` | `prompt`, `logs`, `pipeline`, `drift`, `rollback` | Retain common Brazilian AI/technology usage, define each term at first use, or use `instrução`, `registros`, `fluxo`, `desvio` and `reversão` where meaning remains precise? |

## Automated observations

- Chapter headings 1–32 remain present exactly once and in order in each language.
- The controlled ISO identifiers and editions remain unchanged.
- Risk assessment and AI system impact assessment remain separately named.
- The Declaración/Declaração de Aplicabilidad, internal audit, management review, nonconformity, correction, corrective action, supplier, evidence, and certification-boundary concepts remain present.
- Ten localized alternative-text descriptions and ten accessible explanations remain present per language.
- Ten language-specific SVG/PNG graphics now replace the English-visible-label dependency in each localized source set; human review of their terminology, meaning, readability, and accessibility remains required.

## Boundary

Only an identified competent human reviewer may complete the sign-off rows in `HUMAN_SEMANTIC_REVIEW_CHECKLIST.md`. This precheck must not be treated as human approval or cited as an ISO-authorized translation, certification evidence, legal advice, or an audit opinion.
