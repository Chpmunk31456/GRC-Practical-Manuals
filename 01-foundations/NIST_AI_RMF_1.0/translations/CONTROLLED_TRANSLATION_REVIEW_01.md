# Manual 03 — Controlled Localization and Semantic Review 01

**Manual:** NIST AI Risk Management Framework Implementation  
**Date:** 2026-08-25  
**Controlled source:** English 32-chapter master on `build/nist-ai-rmf-manual-03-2026`  
**Localized editions:** neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`)  
**Review type:** controlled AI-assisted semantic and terminology review with fail-closed defect remediation  
**Accountable human creator/release authority:** Alberto “Al” Leiva

## Review objective

Verify that the localized Manual 03 sources preserve the operational meaning, risk boundaries, NIST identifiers, assurance limitations, lifecycle logic, and decision/evidence requirements of the controlled English master without representing the localized material as an official NIST translation.

## Controlled terminology

The review preserves the following terms or concepts consistently across editions:

- NIST AI RMF 1.0 / NIST AI 100-1 as the current controlled baseline;
- NIST AI 600-1 as the companion profile when generative AI is in scope;
- the Core function names `GOVERN`, `MAP`, `MEASURE`, and `MANAGE` untranslated as controlled NIST identifiers;
- `TEVV` as testing/evaluation/verification/validation, with localized explanatory text;
- AI inventory, AI actors, affected parties, risk ownership, residual risk, evidence, monitoring, incident, corrective action, supplier/change risk, and human oversight;
- explicit version-awareness and impact analysis after a future final NIST revision; and
- the boundaries that AI RMF is voluntary guidance and that repository/manual use does not establish legal compliance, certification, trustworthy-AI achievement, ISO/IEC 42001 conformity, or an audit opinion.

English technical terms retained in localized prose (for example `prompt injection`, `rollback`, `fallback`, `benchmark`, `logging`, `red-team`, `downstream`, and similar terms) are used only where they are common technical terms or where preserving the English term reduces ambiguity. The surrounding sentence carries the localized operational meaning.

## Structural review

The controlled source is divided into four chapter parts covering chapters 1–32. The localized sources preserve the same ordered chapter inventory and the same Core progression:

1. preliminaries and GOVERN, chapters 1–8;
2. MAP, chapters 9–16;
3. MEASURE, chapters 17–24; and
4. MANAGE, chapters 25–32.

The implementation-path entries preserve Essential, Structured, and Enhanced implementation routes and the same fail-closed evidence/decision model.

## Finding L10N-03-001 — localized Parts 3 and 4 were materially condensed

**Severity:** release blocking  
**Languages:** `es-419`, `pt-BR`  
**Condition:** The earlier localized MEASURE and MANAGE files contained all numbered chapters but materially condensed multiple English subsections, control lists, evidence requirements, decision rules, and assurance details. Their control notices stated that they preserved the operational meaning of the English master, but the level of omission was too large to support that statement for a full publication edition.

**Risk:** A localized reader could receive weaker implementation guidance than an English reader, particularly around evaluation integrity, control design, release evidence, stop/rollback criteria, incident handling, supplier change, agentic controls, assurance, maturity, and framework revision.

**Decision:** FAIL CLOSED until semantic depth is restored.

**Remediation:**

- `es-419` MEASURE chapters 17–24 expanded to preserve the English subsection/control/evidence structure in commit `96e671dd26356a54bc06702fa353481581005fc5`.
- `pt-BR` MEASURE chapters 17–24 expanded to preserve the English subsection/control/evidence structure in commit `82ec2357d760bbcb0516cfa61c02f831d88793f1`.
- `es-419` MANAGE chapters 25–32 expanded to preserve the English subsection/control/evidence structure in commit `bfe40d72b82c644210464c8b2fc5c2cf6d7a6e36`.
- `pt-BR` MANAGE chapters 25–32 expanded to preserve the English subsection/control/evidence structure in commit `b488d9c4ec6d427bdfe6c6db5a65bf5f41e972b6`.

**Remediation status:** CLOSED for semantic-depth defect; final document/accessibility/visual QA remains separately required.

## Semantic boundary review

The localized content was checked for preservation of the following decision-critical meanings:

- governance remains transversal rather than a once-per-year committee exercise;
- MAP establishes the actual sociotechnical context and affected parties rather than a generic questionnaire;
- MEASURE creates decision-relevant evidence and does not treat a single score or benchmark as proof of trustworthiness;
- adversarial testing requires controlled environments and explicit authorization;
- uncertainty, failed/inconclusive/not-tested evidence, version mismatch, expiry, and material change can block a decision;
- MANAGE requires authorized residual-risk decisions rather than score-generated acceptance;
- deployment/release is tied to an exact configuration and current evidence;
- stop, rollback, fallback, incident, complaint, appeal, corrective-action, and retirement controls remain explicit;
- supplier and model changes can invalidate assumptions/evidence;
- NIST AI 600-1 is a companion profile rather than a universal checklist;
- agentic-system controls preserve least privilege, tool/action constraints, human confirmation for consequential actions, action traces, revocation, emergency stop, rollback, and downstream reconciliation;
- assurance distinguishes design effectiveness from operating effectiveness; and
- future NIST framework revision requires a controlled impact-review/relocalization/republication cycle rather than silent replacement.

## Accessibility and graphic language review

The source Markdown retains a text explanation adjacent to each Mermaid memory graphic. Graphic rendering, image alternative text, page placement, and final document accessibility are verified separately in the publication-processing gate and are not self-certified by this semantic review.

## Result

**CONTROLLED SEMANTIC / TERMINOLOGY REVIEW: PASS AFTER REMEDIATION**

No remaining release-blocking semantic omission was identified in the controlled localized source scope reviewed here. This review does not represent NIST authorization, native-language certification, legal advice, compliance certification, or an audit opinion. Final release remains fail-closed until publication candidates, page-level visual QA, provenance, repository/security audit, changed-scope review, and Final Human Release Approval are complete.
