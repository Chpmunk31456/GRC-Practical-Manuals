# Manual 10 — NIST RMF and SP 800-53 Controlled Implementation

**Status:** Controlled build / development, stacked behind Manual 09.

**Controlled source language:** English (`en`)

**Planned publication languages:** English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)

## Purpose

Manual 10 provides a practical, evidence-based implementation route for the NIST Risk Management Framework (RMF) and the SP 800-53 security and privacy control ecosystem. It supports organization-level and system-level risk management without reducing RMF to checklist-only compliance.

## Controlled baseline

The controlled baseline includes:

- NIST SP 800-37 Rev. 2 — RMF lifecycle;
- NIST SP 800-53 Rev. 5, Release 5.2.0 — security and privacy controls;
- NIST SP 800-53A Rev. 5, Release 5.2.0 — assessment procedures;
- NIST SP 800-53B, Release 5.2.0 — control baselines and tailoring context;
- NIST SP 800-18 Rev. 2 — system security, privacy, and C-SCRM planning;
- OSCAL and machine-readable planning/evidence concepts.

See [authoritative-source verification](./qa/SOURCE_VERIFICATION_2026-08-27.md).

## RMF operating cycle

Manual 10 preserves the seven RMF steps as a connected operating cycle:

1. PREPARE
2. CATEGORIZE
3. SELECT
4. IMPLEMENT
5. ASSESS
6. AUTHORIZE
7. MONITOR

## Implemented controlled content

- complete 32-chapter controlled English master;
- complete 32-chapter Spanish `es-419` controlled localization draft;
- complete 32-chapter Brazilian Portuguese `pt-BR` controlled localization draft;
- Essential / Structured / Enhanced implementation paths;
- three accessible source-level learning diagrams;
- organization-level and system-level risk management;
- system security/privacy/C-SCRM planning;
- control selection and tailoring;
- common, system-specific, and hybrid controls;
- implementation evidence and provenance;
- assessment planning, procedures, evidence quality, and findings;
- accountable authorization decisions and residual-risk boundaries;
- continuous monitoring, change impact, Plan of Action and Milestones (POA&M) governance, inherited-risk monitoring, and continuous authorization support;
- OSCAL and machine-readable evidence concepts;
- explicit fail-closed localization and document/accessibility publication gates.

## Assurance and authorization boundary

Manual 10 is **risk-based, tailorable, and evidence-based**.

The controlled boundaries are explicit:

- **No checklist-only compliance claim.** Completing a control checklist does not by itself demonstrate effective risk management, adequate implementation, or acceptable residual risk.
- **No automatic authorization.** Automation may assemble, test, or present evidence, but it cannot make the accountable authorization decision.
- The **human authorization decision** remains with the accountable authorizing official and must be supported by sufficient evidence and risk judgment.
- Repository QA can validate structure, mappings, evidence expectations, source state, and publication controls. It cannot authorize a system, determine acceptable residual risk, certify compliance, or substitute for the accountable authorizing official or competent assessor.

## Controlled progress

- [x] Machine-readable Manual 10 baseline.
- [x] Clean stack behind Manual 09.
- [x] Controlled architecture / purpose / assurance boundary.
- [x] Essential / Structured / Enhanced implementation paths.
- [x] Three accessible source-level evidence-flow diagrams.
- [x] Current NIST source-state verification record.
- [x] Catalog registration as controlled-build series order 10.
- [x] Dedicated fail-closed Manual 10 QA workflow and script.
- [x] Controlled source supplement for SP 800-53B and SP 800-18 Rev. 2.
- [x] Controlled 32-chapter English master.
- [x] `es-419` controlled localization draft.
- [x] `pt-BR` controlled localization draft.
- [x] Localization semantic-review gate pre-staged.
- [x] Document/accessibility publication gate pre-staged.
- [ ] Reconcile supplemental NIST source records into the shared authoritative-source registry when final upstream lineage is reconciled.
- [ ] Technical/editorial/control-mapping human review.
- [ ] Human semantic review of `es-419` and `pt-BR`.
- [ ] Rendered graphics/accessibility human review.
- [ ] DOCX/PDF publication-candidate generation and page QA.
- [ ] Repository/workflow security review and provenance/checksums/manifest.
- [ ] Exact-head compliance assessment and changed-scope reconciliation.
- [ ] Final Human Release Approval and publication after all mandatory gates are green.

## Release boundary

Manual 10 remains controlled development until technical/editorial review, localization and human semantic review, graphics/accessibility review, DOCX/PDF generation and page QA, repository/workflow security review, provenance/checksums/manifest, exact-head reconciliation, compliance assessment, and Final Human Release Approval are complete for the same exact candidate.
