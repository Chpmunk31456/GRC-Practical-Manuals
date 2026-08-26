# Manual 06 — HIPAA Implementation and Audit

**Status:** Controlled implementation intake, stacked behind Manual 05.

**Controlled source language:** English (`en`)

**Planned publication languages:** English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)

**Author and accountable human creator:** Alberto “Al” Leiva

## Purpose

Manual 06 will provide a practical implementation and audit method for HIPAA Privacy, Security, Breach Notification, and Business Associate obligations. It is designed to help organizations build operational controls, collect evidence, prepare for internal/external review, and manage remediation without representing repository QA as legal advice or a compliance determination.

## Controlled legal baseline

Current-law sources are maintained separately from proposed changes. The controlled source IDs are:

- `hhs-hipaa-security-rule` — current HIPAA Security Rule;
- `hhs-hipaa-privacy-rule` — current HIPAA Privacy Rule;
- `hhs-hipaa-breach-notification` — current Breach Notification Rule;
- `hhs-hipaa-business-associates` — current HHS Business Associate guidance;
- `hhs-hipaa-security-rule-nprm` — **proposed rule only**, not current law.

The manual must never present NPRM language as an existing obligation. Proposed-rule material may be used for readiness planning only and must be visibly labeled as proposed until a final rule is issued and the controlled source baseline is updated through impact analysis.

## Implementation model

Manual 06 will use the project-wide **Essential / Structured / Enhanced** paths. Each path will cover:

- entity and role classification;
- protected health information (PHI) and electronic protected health information (ePHI) inventory and data flows;
- privacy governance and minimum-necessary controls;
- Security Rule risk analysis and risk management;
- administrative, physical, and technical safeguards;
- identity/access, logging, transmission, endpoint, backup, and recovery controls;
- workforce authorization and training;
- business-associate due diligence and BAAs;
- incident response and breach assessment;
- documentation and retention;
- evidence collection, testing, findings, and corrective action;
- change monitoring for HHS rulemaking and official guidance.

See [Manual 06 implementation paths](./MANUAL_06_IMPLEMENTATION_PATHS.md).

## Audit and evidence boundary

A control is not considered demonstrated merely because a policy exists. The controlled master requires traceable implementation evidence such as inventories, risk analyses, access records, workforce records, technical configurations, audit logs, incident records, BAAs, breach assessments, remediation evidence, and management approvals where applicable.

## Release gates

- [x] Controlled branch and machine-readable legal baseline staged.
- [x] Current-law versus NPRM separation encoded.
- [x] Proportional implementation paths staged.
- [x] Current HHS/OCR source-state verification completed on 2026-08-26; current law remains in effect and NPRM content remains readiness-only.
- [x] Controlled English chapter master complete across four source blocks covering Chapters 01–32.
- [x] Dedicated Manual 06 QA passed at controlled head `13c5c54729baa37417b66fa53d79bf5b27ed914f`; the new chapter-master head requires a fresh exact-head run before promotion.
- [ ] Complete legal-boundary/editorial/technical review.
- [ ] Complete `es-419` and `pt-BR` localization and human semantic review.
- [ ] Complete learning graphics and accessibility review.
- [ ] Generate and QA DOCX/PDF publication artifacts.
- [ ] Complete security/repository release audit.
- [ ] Complete release manifest, checksums, and provenance.
- [ ] Record final human release approval.

## Important notice

This manual is educational implementation guidance. It does not determine whether a specific organization is a covered entity or business associate, does not provide legal advice, and does not establish HIPAA compliance or whether an incident constitutes a reportable breach.
