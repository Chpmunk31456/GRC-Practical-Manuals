# Manual 02 — Controlled Editorial QA Review 01

**Repository:** `Chpmunk31456/GRC-Practical-Manuals`

**Pull request:** `#89` (draft)

**Branch:** `build/iso-iec-42001-manual-02-2026`

**Starting HEAD:** `14102d291d48523828448df6e7a1028a60e721f5`

**Review date:** 2026-08-24

**Controlled English source:** `English/ISO_IEC_42001_2023_Practical_AIMS_Manual_English_v1.0.md`

**Objective:** Help managers and junior analysts understand and implement an AIMS without changing technical, regulatory, audit, risk, or certification meaning.

**Audience and style assumption:** International professional audience; US English with the Oxford comma. Standard identifiers, code, URLs, direct quotations, and localized-language prose are excluded from English copy-edit judgments.

**Boundary:** This is an advisory copy-edit. It suggests minimal changes and does not rewrite the controlled master. It does not close the human semantic-review gate or replace licensed-source review. It does not approve translations and does not determine conformity, certification, legal compliance, accessibility, or audit success.

## Summary

**Grammar 3 · Logic 2 · Flow 5 — ready with advisory corrections.**

The English master is organized, practical, and appropriately bounded for its intended readers. No broad rewrite is recommended. Ten targeted items would improve clarity and consistency; two logic items should be resolved before publication because their present wording can conflict with the manual's own assurance boundary or obscure responsibility.

## Top fixes

1. **Critical — opening scope, “audit, certify, and improve”:** “Certify” can imply that the manual or organization performs the independent certification decision, which conflicts with the later third-party boundary. Suggested fix: “audit, prepare for certification, and improve.”
2. **High — Section 5.3, “the same team creates, validates, accepts, and audits high-impact risk”:** a team may create a system or implementation, but it does not “create” risk in the same grammatical series. Name the object of each action.
3. **High — Section 27.1, “Affected people: that AI is used where appropriate, role in the decision”:** the list loses grammatical parallelism and leaves “role” without a clear possessor. Suggested fix: “Affected people: whether and where AI is used, its role in the decision…”
4. **Medium — terminology consistency, “life cycle” / “life-cycle” / “lifecycle”:** select one noun form and one attributive form and apply them consistently, except in official titles.
5. **Medium — resource wording, “system/compute”:** the slash construction is opaque for managers and junior analysts. Suggested fix: “system and computing resources” or another approved precise term.

## Full advisory table

| # | Location (quote) | Category | Issue | Suggested fix | Why |
|---:|---|---|---|---|---|
| 1 | Opening callout, “operate, audit, certify, and improve” | Logic | The verb can imply that the manual or implementing organization performs certification | “operate, audit, prepare for certification, and improve” | Certification is an independent third-party decision elsewhere in the manual |
| 2 | Preface, “explains concepts in original language” | Grammar | The idiom is incomplete and can mean the source language rather than original wording | “explains concepts in its own words” | The revision states the intended copyright boundary directly |
| 3 | Section 5.3, “the same team creates, validates, accepts, and audits high-impact risk” | Logic | The four verbs do not take the same object coherently | “the same team creates the system, validates it, accepts its risk, and audits it” | Naming each object makes the conflict-of-interest scenario testable |
| 4 | Sections 23 and Annex A summary, “system/compute” | Flow | Slash shorthand is unclear and “compute” is jargon for the stated audience | Use an approved term such as “system and computing resources” | Managers and junior analysts should not have to infer the relationship |
| 5 | Section 24 lead, “supplies complementary current guidance” | Flow | “Supplies” is stiff and “current” interrupts the core point | “provides complementary guidance” | The edition and current-source note already establish currency |
| 6 | Section 27.1, “Affected people: that AI is used where appropriate, role in the decision” | Grammar | The list is not parallel, and “role” lacks a clear possessor | “Affected people: whether and where AI is used, its role in the decision…” | The revised list clearly identifies the information affected people receive |
| 7 | Sections 2, 13, 23–28, “life cycle” / “life-cycle” / “lifecycle” | Flow | Three forms are used for the same concept | Choose one noun form and one attributive form; preserve official titles | Consistency reduces avoidable terminology friction |
| 8 | Section 29.1 and similar tables, “organization/role/system/data/supplier boundaries” | Flow | Dense slash chains hide the relationship among fields | Use commas or “and,” or give each boundary its own short label | The content is a teaching aid, not a database field name |
| 9 | Section 31.10, “scope, documented system, readiness and planning” | Grammar | “Documented system” benefits from an article; the list omits the manual's usual serial comma | “scope, the documented system, readiness, and planning” | The revision reads naturally and matches the prevailing style |
| 10 | Section 31.13, “Verify correction, root-cause action, application to similar conditions…” | Flow | “Application” has no stated object and may be read several ways | Specify what is applied to similar conditions, using the authorized corrective-action meaning | The evidence instruction should be unambiguous without expanding the requirement |

## Objective and tone check

The manual serves its educational objective and maintains a professional, practical tone for managers and junior analysts. The strongest features are its evidence questions, assurance boundaries, scaled implementation paths, and repeated connection among requirements, owners, evidence, testing, findings, and corrective action. The ten advisory items are local; they do not justify restructuring or wholesale rewriting.

## Localized mechanical checks

The grammar-review skill does not treat foreign-language prose as English copy-edit material. Spanish and Brazilian Portuguese therefore received mechanical and parity checks only; competent human editorial and terminology approval remains mandatory.

| Check | English | `es-419` | `pt-BR` |
|---|---:|---:|---:|
| Chapter sequence | 32/32 | 32/32 | 32/32 |
| Unique HTTPS destinations | 37 | 37 | 37 |
| Repeated adjacent nonblank lines | 0 | 0 | 0 |
| Malformed Markdown table lines | 0 | 0 | 0 |
| Trailing-whitespace findings after cleanup | 0 | 0 | 0 |

Two trailing spaces—one in each localized Chapter 2 lead sentence—were removed as non-semantic repository hygiene. No localized wording was rewritten in this gate.

## Deferred and protected items

- The Chapter 23, 26, and 27 Annex A applicability wording, control count, normative strength, and Stage 1/Stage 2 detail remain licensed-source/human review items recorded in Source Verification Report 01.
- Spanish and Portuguese semantic, terminology, naturalness, and graphics-language decisions remain in `translations/HUMAN_SEMANTIC_REVIEW_CHECKLIST.md`.
- The ten English advisory suggestions require accountable editorial acceptance before application; this report does not silently alter controlled meaning.
- DOCX/PDF generation, page rendering, visual QA, and final accessibility approval are separate downstream gates.

## Next controlled action

The accountable editor should accept, reject, or refine the ten suggestions. Any accepted wording changes must be applied to English first, assessed for localized impact, propagated to `es-419` and `pt-BR` where applicable, and followed by Manual 02 integrity, translation-parity, DOCX, and visual/accessibility QA.

EDITORIAL QA STATUS: PASS WITH ADVISORY ITEMS
