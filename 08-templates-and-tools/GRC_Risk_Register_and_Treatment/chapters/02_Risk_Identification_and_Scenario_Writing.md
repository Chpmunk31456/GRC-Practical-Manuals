# 2. Risk Identification and Scenario Writing

## Identify risks from objectives

Start with the objective, not with a generic threat list. Review strategic goals, critical services, legal and contractual obligations, key assets, important data, major third parties, projects, changes, and known dependencies.

Useful identification inputs include:

- Business and mission objectives
- Business impact analyses
- Architecture and data-flow diagrams
- Asset and service inventories
- Threat intelligence and incident history
- Audit findings and control-test results
- Vulnerability and configuration data
- Vendor and concentration-risk assessments
- Regulatory and contractual requirements
- Change portfolios and transformation plans
- Complaints, near misses, exceptions, and loss events

## Scenario structure

A defensible risk scenario contains four elements:

1. **Context or cause** — the condition that creates exposure.
2. **Event** — what may happen.
3. **Affected objective or asset** — what matters to the organization.
4. **Consequence** — the credible harm or missed opportunity.

Example:

> Because privileged accounts are not reviewed consistently, an unauthorized or excessive privilege may remain active, enabling inappropriate access to sensitive customer information and causing regulatory, financial, and reputational harm.

## Avoid weak statements

Weak entries include single words such as “ransomware,” “vendor risk,” or “noncompliance.” They do not explain the business consequence or support a repeatable assessment.

Rewrite vague statements by asking:

- What condition makes the event possible?
- What event could occur?
- Which objective, service, asset, or obligation is affected?
- What is the credible consequence?
- What evidence supports the scenario?

## Risk taxonomy

A taxonomy helps aggregate entries without replacing scenario-level analysis. Categories may include:

- Strategic
- Operational
- Cybersecurity
- Privacy
- Legal and regulatory
- Financial
- Technology
- Third-party and supply-chain
- Resilience and continuity
- Safety
- Workforce
- Reputation
- Project and change

Use primary and secondary categories when one scenario spans several domains.

## Evidence and assumptions

Every material scenario should cite evidence such as reports, tickets, assessments, contracts, test results, incident records, metrics, or expert analysis. Record assumptions separately so decision-makers can distinguish known facts from estimates.

Examples of assumptions:

- A service will remain dependent on one provider for the next twelve months.
- A control operates as designed between quarterly tests.
- A threat frequency estimate is based on sector data rather than internal history.

## Entry identifiers and relationships

Assign stable identifiers such as `RR-2026-001`. Do not recycle identifiers. Link related records, including:

- Controls
- Findings
- Incidents
- Exceptions
- Projects
- Vendors
- Assets
- Policies
- Treatment actions
- Accepted-risk decisions

## Identification workshop method

1. Define the objective and scope.
2. Present current evidence and known constraints.
3. Identify causes, events, and consequences.
4. Consolidate duplicates without losing distinct causes or impacts.
5. Assign provisional owners.
6. Document assumptions and evidence gaps.
7. Send entries for validation before scoring.

A workshop should not force consensus by averaging incompatible views. Material disagreement should be recorded and escalated for decision.
