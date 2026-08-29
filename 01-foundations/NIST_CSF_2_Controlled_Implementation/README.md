# Manual 09 — NIST Cybersecurity Framework 2.0 Controlled Implementation

Manual 09 is the controlled-series successor to the repository's earlier published NIST CSF 2.0 practical manual. The prior publication remains an immutable historical release; this directory introduces the current fail-closed production model, exact-head source verification, three implementation paths, controlled English, localization gates, evidence requirements, accessibility controls, and release provenance.

## Authoritative baseline

The controlling framework is **NIST CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0**, final February 26, 2024. Manual 09 also tracks current NIST CSF 2.0 implementation resources, including **NIST SP 1308** (final March 2026) and **NIST SP 1347** (final August 2026).

See [Manual 09 authoritative-source verification](./qa/SOURCE_VERIFICATION_2026-08-26.md).

## Operating model

The manual implements the six CSF 2.0 Functions as a connected risk-management system:

1. **GOVERN** — organizational context, risk strategy, roles, policy, oversight, and supply-chain governance;
2. **IDENTIFY** — assets, risk assessment, and improvement priorities;
3. **PROTECT** — identity/access, awareness, data security, platform security, and infrastructure resilience;
4. **DETECT** — continuous monitoring and adverse-event analysis;
5. **RESPOND** — incident management, analysis, communication, and mitigation;
6. **RECOVER** — recovery execution and communication.

The framework is outcome-based and does not prescribe one universal control implementation. Manual 09 therefore distinguishes desired outcomes, organization-specific implementation decisions, evidence, residual risk, and human approval.

## Proportional implementation

Manual 09 uses three controlled paths:

- **Essential** — minimum viable governance and evidence discipline for smaller or lower-complexity environments;
- **Structured** — repeatable enterprise implementation with Profiles, Tiers, metrics, formal ownership, and cross-functional risk integration;
- **Enhanced** — mature, highly integrated implementation with quantitative decision support, continuous assurance, advanced supplier/ecosystem governance, and machine-consumable informative-reference workflows where appropriate.

See [Manual 09 implementation paths](./MANUAL_09_IMPLEMENTATION_PATHS.md).

## Explicit control boundaries

- **No certification claim:** use of this manual or a QA pass must not be represented as NIST certification or certified CSF conformance.
- **No universal control sufficiency claim:** no single mapped control set is presumed sufficient for every organization or every CSF outcome.
- Implementation remains risk-based and organization-specific.
- Material risk acceptance and final release decisions require accountable human approval.

## Controlled build status

- [x] Controlled branch and baseline established.
- [x] Current CSF 2.0 authoritative-source state verified for intake.
- [x] Proportional implementation architecture defined.
- [x] Complete 32-chapter controlled English master.
- [ ] Complete dedicated exact-head Manual 09 QA.
- [ ] Complete technical/editorial/security review.
- [ ] Complete `es-419` and `pt-BR` localization and human semantic review.
- [ ] Complete graphics and accessibility review.
- [ ] Generate and inspect DOCX/PDF publication candidates.
- [ ] Complete manifest, checksums, provenance, repository/workflow security review, and changed-scope reconciliation.
- [ ] Apply Final Human Release Approval to the exact final candidate after all prior mandatory gates are green.

## Assurance boundary

Automated QA may verify chapter inventory, source-state metadata, required terminology, evidence fields, implementation-path structure, and publication-package properties. It does **not** determine that an organization has achieved CSF outcomes, that cybersecurity risk is acceptable, or that a particular control set is universally sufficient.
