# Chapter 101 — Third-Party Risk

## Purpose

This chapter defines a practical method for identifying, assessing, controlling, and monitoring risks introduced by external AI providers, model vendors, cloud platforms, data suppliers, integrators, consultants, open-source components, and subcontractors.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should manage third-party AI risk throughout the full relationship lifecycle: intake, due diligence, contracting, implementation, operation, change, incident response, renewal, and exit. Outsourcing a model, platform, or service does not outsource accountability.

## Plain-language explanation

An organization may rely on a vendor for the model, hosting, data, monitoring, or technical documentation, yet still remain responsible for how the AI system is selected, configured, used, monitored, and stopped. Third-party risk management ensures that critical obligations are not hidden behind a supplier relationship.

## Risk domains

Assess at minimum:

- legal and regulatory applicability;
- provider and deployer role allocation;
- model purpose, limitations, and prohibited uses;
- data provenance, quality, licensing, and privacy;
- cybersecurity, resilience, and incident response;
- transparency, explainability, and human oversight;
- bias, discrimination, accessibility, and fundamental-rights impacts;
- model and service change management;
- subcontractor and fourth-party dependencies;
- auditability, evidence access, and documentation quality;
- continuity, portability, and exit capability;
- concentration and lock-in risk.

## Lifecycle controls

### Intake and classification

Before engagement, document:

- business purpose and accountable owner;
- proposed AI role and use case;
- affected people and jurisdictions;
- data categories;
- criticality and risk tier;
- expected supplier dependencies;
- required review functions.

### Due diligence

Review proportionately:

- corporate and financial viability;
- technical architecture;
- model and system cards;
- data-governance practices;
- testing and evaluation methods;
- security certifications and independent assurance;
- incident history;
- privacy and cross-border processing;
- accessibility and fairness controls;
- subcontractor governance;
- continuity and recovery capability;
- regulatory and litigation exposure.

### Contracting

Contracts should address:

- permitted use and restrictions;
- documentation and information rights;
- security and privacy requirements;
- incident notification;
- model or service change notification;
- testing, audit, and assurance rights;
- performance and service levels;
- data ownership, retention, deletion, and return;
- subcontractor approval or disclosure;
- cooperation with regulators and affected-person requests;
- suspension and termination rights;
- transition assistance and portability.

### Ongoing monitoring

Monitor:

- service and model changes;
- control attestations and certifications;
- incidents and vulnerabilities;
- performance and quality deterioration;
- regulatory developments;
- financial viability;
- concentration risk;
- unresolved findings;
- dependency changes;
- contract and insurance expiry.

## Fourth-party risk

Identify material subcontractors, cloud services, data providers, model providers, and tooling dependencies used by the primary supplier. Determine whether the organization has sufficient visibility, notification rights, and continuity options when a critical fourth party changes or fails.

## GlobalWay Travel Services example

GlobalWay proposes using a third-party generative-AI platform for traveler support. Due diligence identifies that the vendor relies on a separate cloud host and an external retrieval service. GlobalWay documents both as critical fourth parties, requires notification of material model changes, restricts use of traveler data for provider training, obtains audit evidence, and establishes a tested fallback to human consultants.

When the retrieval supplier later changes its indexing behavior, GlobalWay triggers reassessment before accepting the update in production.

## Control activities

- Maintain a complete AI supplier and dependency inventory.
- Apply risk-tiered due diligence before approval.
- Define mandatory AI contract clauses.
- Track fourth parties and concentration risk.
- Monitor changes, incidents, assurance, and financial viability.
- Reassess after material supplier or model change.
- Maintain tested exit and continuity arrangements.
- Preserve supplier evidence and accountable approvals.

## Evidence

- supplier inventory;
- intake and classification records;
- due-diligence reports;
- security, privacy, and legal assessments;
- model and system documentation;
- contracts and amendments;
- audit reports and certifications;
- incident and change notifications;
- monitoring reviews;
- fourth-party maps;
- continuity and exit plans;
- renewal and termination decisions.

## Audit tests

1. Select critical AI suppliers and confirm risk classification and due diligence were completed before approval.
2. Verify contracts include required documentation, notification, audit, security, privacy, change, and exit provisions.
3. Trace material fourth-party dependencies to monitoring and continuity controls.
4. Review whether supplier incidents and model changes triggered reassessment.
5. Confirm overdue findings are tracked and escalated.
6. Test whether data return, deletion, portability, and service transition are feasible.
7. Review concentration risk and fallback arrangements.

## Metrics

- critical AI suppliers by risk tier;
- suppliers with overdue due diligence;
- contracts missing mandatory clauses;
- undisclosed or unassessed fourth parties;
- supplier incidents and material changes;
- overdue remediation;
- concentration exposures;
- suppliers without tested exit plans;
- percentage of critical suppliers with current assurance evidence.

## Management checklist

- Do we know every critical external dependency supporting the AI service?
- Are supplier and internal responsibilities clearly allocated?
- Can we obtain the evidence needed for compliance and audit?
- Will we be notified before material model or service changes?
- Can we suspend, replace, or exit the service safely?
- Are fourth-party and concentration risks understood?

## Figure specification — AI Third-Party Risk Lifecycle

Create a lifecycle showing intake, classification, due diligence, approval, contracting, implementation, monitoring, change reassessment, incident response, renewal, and exit. Show fourth-party visibility and concentration risk as cross-cutting controls.

**Alt text:** AI third-party risk lifecycle from intake and due diligence through contracting, monitoring, change reassessment, incident response, renewal, and exit, with fourth-party and concentration-risk oversight throughout.
