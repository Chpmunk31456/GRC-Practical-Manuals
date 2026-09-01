# Manual 50 — Global AI Governance Crosswalk Architecture

**Canonical stage:** 2 — substantive common-control mapping architecture  
**Currentness baseline:** 1 September 2026

This file establishes independently authored common control objectives and qualified relationships across Manual 46, EU AI Act, ISO/IEC 42001, NIST AI RMF / AI 600-1, Singapore governance and OECD AI Principles. It does not reproduce protected standard text and does not assert automatic equivalence.

## GC-01 — Governance and accountability

**Common objective:** establish accountable ownership, decision rights, policies, escalation, exceptions and management oversight for AI.

- **EU AI Act:** supporting/direct relationship depending on the regulated actor and obligation; legal actor/scope remains source-specific.
- **ISO/IEC 42001:** direct management-system relationship at a high level; certification is separate.
- **NIST AI RMF:** direct relationship to GOVERN.
- **Singapore:** direct relationship to internal governance/accountability practices.
- **OECD:** direct relationship to accountability principle.

**Shared evidence:** governance charter, RACI, policy, committee decisions, exceptions, management reporting.

## GC-02 — AI inventory and system ownership

**Common objective:** maintain a current inventory of AI systems/use cases with owner, purpose, provider/model, lifecycle state and risk context.

- EU legal requirements vary by actor/system; inventory is a supporting enterprise mechanism, not itself proof of compliance.
- ISO relationship: supporting management-system information/control foundation.
- NIST: supporting GOVERN/MAP mechanism.
- Singapore: supporting/direct practical governance mechanism.
- OECD: supporting accountability/robustness practice.

## GC-03 — Role and value-chain responsibility

**Common objective:** determine who designs, provides, deploys, imports, distributes, operates, integrates or materially changes AI and allocate responsibilities accordingly.

**Qualification:** EU AI Act role definitions are legal and must not be replaced by generic enterprise labels. Other frameworks may describe responsibility without identical legal actor categories.

**Evidence:** role analysis, contracts, RACI, provider/deployer responsibilities, change records.

## GC-04 — Risk classification and tiering

**Common objective:** classify AI risk using the source regime's applicable method while maintaining an internal enterprise risk tier for governance depth.

**Qualification:** EU legal classification, internal risk tiering, NIST contextual risk assessment and Singapore governance assessment are not the same classification system.

## GC-05 — Risk and impact assessment

**Common objective:** identify intended purpose, context, affected parties, benefits, harms, misuse, dependencies and controls before deployment and after material change.

**Relationships:** EU specialist obligations may include system/actor-specific risk or impact requirements; NIST MAP is strongly related; ISO management-system risk treatment and Singapore risk assessment are supporting/direct at a governance level; OECD human-rights/democratic-values and robustness principles provide contextual/direct objectives.

## GC-06 — Data governance and privacy

**Common objective:** govern provenance, quality, access, minimisation, lineage, retention, sensitive data and data-related risks.

**Qualification:** privacy law bases/rights and EU AI Act data obligations remain source-specific. A common data-control library may support several requirements but does not merge them.

## GC-07 — Security, robustness and resilience

**Common objective:** protect AI systems against threats, failures, misuse and dependency compromise while maintaining reliable operation and recovery.

- EU: legal requirements apply where specified by system/role.
- NIST: strong relationship to trustworthiness, MEASURE/MANAGE and AI 600-1 security actions.
- Singapore: lifecycle technical controls and agentic controls support this objective.
- OECD: direct relationship to robustness, security and safety.
- ISO: management-system relationship without reproducing protected text.

## GC-08 — Transparency and communication

**Common objective:** provide accurate information about AI use, capabilities, limitations, material outputs and responsibilities to the appropriate audience.

**Qualification:** EU Article 50 and other legal transparency duties are source-specific and cannot be reduced to a generic notice. OECD transparency/explainability, Singapore stakeholder communication and NIST accountability/transparency concepts provide related but different objectives.

## GC-09 — Human oversight and accountable intervention

**Common objective:** ensure humans have competence, authority, information and practical means to intervene at meaningful decision/action points where required by risk or source obligations.

**Evidence:** oversight design, approval checkpoints, override/rejection logs, training, escalation, automation-bias monitoring.

## GC-10 — Testing, evaluation, verification and validation

**Common objective:** define claims/acceptance criteria and test performance, risk, robustness, security, privacy and control effectiveness with reproducible evidence proportional to risk.

**Qualification:** EU conformity-assessment or specific legal testing requirements are not interchangeable with NIST TEVV, AI Verify testing or internal validation.

## GC-11 — Documentation and recordkeeping

**Common objective:** maintain current technical/governance records sufficient to understand system design, versions, decisions, controls, evidence and material changes.

**Shared evidence:** system description, architecture, model/provider versions, risk records, evaluations, approvals, logs and change history.

## GC-12 — Deployment and approval gates

**Common objective:** require accountable disposition before production or material capability expansion: approve, conditionally approve, restrict, remediate, suspend or reject.

**Qualification:** enterprise approval is not a substitute for legally required conformity or registration processes.

## GC-13 — Third-party and supply-chain governance

**Common objective:** assess model/provider/tool/agent dependencies, contractual controls, data handling, security, change notification, incidents, continuity and exit.

**Shared evidence:** vendor assessment, data-flow/architecture, contract clauses, provider version/change log, exit plan.

## GC-14 — Monitoring and continuous assurance

**Common objective:** monitor performance, risk indicators, incidents, policy denials, user feedback, provider/model changes and open findings after deployment.

## GC-15 — Incident management

**Common objective:** detect, contain, investigate, preserve evidence, remediate and escalate AI incidents, including external reporting where applicable.

**Qualification:** legal notification thresholds/timelines remain regime-specific.

## GC-16 — Change management and revalidation

**Common objective:** identify material changes and trigger proportionate reassessment/retesting before or after controlled deployment as appropriate.

**Triggers:** model/provider, data/RAG, purpose, affected population, tools/APIs, autonomy, permissions, geography, safety/security controls.

## GC-17 — Audit and independent assurance

**Common objective:** provide independent challenge proportional to materiality and preserve findings/remediation evidence.

**Qualification:** internal audit, AI Verify testing, NIST-based independent TEVV, ISO certification and legal conformity assessment are different assurance mechanisms.

## GC-18 — AI literacy and competence

**Common objective:** ensure people performing AI governance, development, deployment, oversight, security, procurement and operations have competence appropriate to their responsibilities.

**Qualification:** EU legal AI-literacy requirements remain source-specific; broader training programs may support them but are not automatically equivalent.

## GC-19 — Continuous improvement

**Common objective:** use monitoring, incidents, audit, stakeholder feedback, testing and changes to improve controls and governance.

## GC-20 — Agent identity, autonomy, permissions and action provenance

**Common objective:** govern agentic AI through attributable identity, bounded autonomy, least privilege, tool/data restrictions, significant human checkpoints, provenance, monitoring and containment.

- Singapore Agentic AI governance: direct operating relationship.
- NIST/OWASP agent-security work: supporting technical relationship, preserving source status.
- EU/ISO relationships depend on applicability and management-system context.
- OECD accountability/robustness principles provide contextual/direct objectives.

## Evidence harmonisation rule

An evidence item may be reused across regimes only when it actually supports the target objective and scope. For each reused evidence item record:

**evidence → originating control → target source relationship → sufficiency/limitations → additional source-specific evidence**

## Gap-analysis method

For each common control:

1. identify implemented enterprise control;
2. map source relationships using the controlled relationship taxonomy;
3. identify missing source-specific scope, actor, threshold, process or evidence;
4. classify the gap: control / evidence / legal interpretation / process / assurance / competence;
5. assign owner and remediation;
6. retest and update mapping rationale.

## Stage-2 completion criterion

Stage 2 is complete when the major common-control domains have qualified source relationships, reusable evidence classes and explicit difference notes sufficient to begin detailed row-level crosswalk and scenario training.