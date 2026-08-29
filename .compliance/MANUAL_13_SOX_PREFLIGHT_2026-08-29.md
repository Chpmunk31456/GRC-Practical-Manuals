# Manual 13 — SOX ITGC / ICFR Authoritative-Source Preflight

**Status:** PRE-STAGE / NOT RELEASE AUTHORIZATION  
**Preflight date:** 2026-08-29  
**Series order:** 13  
**Planned title:** SOX — ITGC, ICFR and Technology Controls

## Purpose

Establish a current, primary-source baseline before controlled drafting. This file does not substitute for legal, technical/editorial, audit, accessibility, localization-semantic, or changed-scope human review.

## Primary authoritative source baseline

1. **Sarbanes-Oxley Act of 2002, Sections 302 and 404** — statutory foundation for executive certifications and management responsibility/assessment of internal control over financial reporting (ICFR). Statutory text should be sourced from an official U.S. government publication at drafting/release time.
2. **SEC final rule — Management's Report on Internal Control Over Financial Reporting and Certification of Disclosure in Exchange Act Periodic Reports** — implements SOX Section 404 management reporting and related certification requirements. Official SEC source: https://www.sec.gov/rules-regulations/2003/03/managements-report-internal-control-over-financial-reporting-certification-disclosure-exchange-act
3. **SEC management guidance / staff materials on ICFR** — use only to explain risk-based management evaluation and evidence concepts; distinguish Commission rules from staff guidance and historical implementation materials.
4. **PCAOB AS 2201 — An Audit of Internal Control Over Financial Reporting That Is Integrated with An Audit of Financial Statements** — primary audit-standard source for ICFR audit planning, top-down risk assessment, control selection/testing, deficiency evaluation, and reporting. Current official source: https://pcaobus.org/oversight/standards/auditing-standards/details/AS2201
5. **PCAOB standards effective-date watch** — the PCAOB page states amendments to AS 2201 are approved and become effective **2026-12-15**. Because this preflight is dated 2026-08-29, the manual must distinguish the currently effective standard from amendments that are approved but not yet effective. Exact release-candidate verification is mandatory.

## Controlled legal / audit boundaries

- Do not equate SOX compliance with a generic cybersecurity-control program. Manual 13 must remain anchored to ICFR and financial-reporting risk.
- IT general controls (ITGCs) should be presented as technology controls relevant to ICFR where they support financially significant systems, automated controls, reports, interfaces, access, program changes, computer operations, data integrity, and evidence relied upon for financial reporting.
- Do not represent COSO or any other control framework as a statute or SEC rule. A recognized control framework may support management's ICFR evaluation, but framework content must be cited/interpreted without reproducing copyrighted material beyond permitted limits.
- Management assessment responsibilities and external-auditor responsibilities must remain distinct.
- Material weakness, significant deficiency, deficiency, reasonable assurance, relevant assertion, significant account/disclosure, and control objective terminology must be sourced and used consistently with SEC/PCAOB definitions as applicable.
- Applicability, filer status, auditor-attestation scope, exemptions, and transition provisions require exact-current legal verification and human legal/editorial review before publication.

## Manual architecture preflight

The controlled build should cover at minimum:

1. SOX statutory and SEC rule context
2. Scope and applicability boundaries
3. ICFR governance and accountability
4. Financial-statement risk and assertion linkage
5. Entity-level controls
6. ITGC domains and financially relevant technology scope
7. Automated application controls and configurable controls
8. Reports, interfaces, spreadsheets, end-user computing and data lineage
9. Identity/access controls relevant to ICFR
10. Change management and SDLC controls relevant to ICFR
11. Computer operations, job scheduling, backups and incident effects on ICFR
12. Third-party/service-organization dependencies
13. Control design vs. operating effectiveness
14. Evidence design, retention and reproducibility
15. Testing strategy, sampling and reliance boundaries
16. Deficiency evaluation and escalation
17. Remediation and retesting
18. Management certification support
19. External-auditor interaction and evidence handoff
20. Continuous monitoring and change-triggered reassessment
21. Cloud/SaaS and modern architecture considerations
22. AI/automation used in financially relevant processes
23. Common failure modes
24. Essential / Structured / Enhanced implementation paths
25. Scenario exercises and practitioner assessment questions

## Pre-release source-state controls

Before Manual 13 becomes a release candidate:

- reverify all SEC and PCAOB sources against live official pages;
- verify the effective AS 2201 version for the planned publication date;
- verify Section 302/404 statutory text from an official government source;
- verify current exemptions, filer-status and attestation boundaries;
- record source verification date and immutable evidence where repository policy requires it;
- complete genuine-human legal/audit/editorial review;
- complete es-419 and pt-BR human semantic review after localization;
- complete rendered accessibility/visual review;
- bind all review decisions to exact candidate artifact hashes.

## Current preflight conclusion

Manual 13 can proceed into controlled source mapping and architecture without waiting for Manual 12 publication. Publication remains sequential. The most important time-sensitive dependency already identified is the approved AS 2201 amendment effective 2026-12-15; release logic must not accidentally treat that future-effective text as current before that date.
