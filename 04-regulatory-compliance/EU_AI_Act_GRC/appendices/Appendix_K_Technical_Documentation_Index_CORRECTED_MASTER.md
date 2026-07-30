# Appendix K — Technical-Documentation Index

> **Legal status:** Corrected English master. For providers of high-risk AI systems, use this index to support Article 11 and Annex IV documentation. For other actors or systems, use it as governance evidence and do not represent it as statutory Annex IV documentation unless the legal trigger applies.

## Purpose

Use this index to organize, control, reconcile, and evidence the technical documentation needed to explain an AI system’s design, development, data, operation, testing, risk controls, oversight, monitoring, changes, and conformity status.

The index must be linked to the exact production version and updated before release, after material change, and whenever legal or conformity requirements change.

## 1. Applicability and document control

| Field | Response |
|---|---|
| System/model | |
| Inventory ID | |
| Legal entity and actor role | |
| High-risk legal basis | |
| Intended purpose | |
| Production version/configuration | |
| Provider/vendor | |
| Annex IV applies? | |
| Applicable conformity route | |
| Current legal source and application date | |
| Documentation owner | |
| Repository/system of record | |
| Index version and review date | |

## 2. Annex IV crosswalk where applicable

| Annex IV area | Required content | Document/evidence reference | Owner | Version | Status | Gap/action |
|---|---|---|---|---|---|---|
| General description | System name, provider, version, intended purpose, users, operating context, interfaces, hardware/software dependencies | | | | | |
| System elements and development process | Design decisions, methods, tools, environments, architecture, components, computation resources, dependencies | | | | | |
| Design specifications and assumptions | Design choices, assumptions, trade-offs, limitations, foreseeable misuse, prohibited uses | | | | | |
| Data and data governance | Sources, provenance, collection, preparation, annotation, quality, representativeness, bias, lineage, retention | | | | | |
| Training, tuning, and development | Methods, parameters, runs, resources, versioning, reproducibility | | | | | |
| Validation and testing | Metrics, scenarios, acceptance criteria, subgroup, language, accessibility, robustness, misuse, and security testing | | | | | |
| Accuracy, robustness, cybersecurity, and resilience | Performance, uncertainty, stress, attack, recovery, continuity, and fallback evidence | | | | | |
| Human oversight | Roles, competence, information, authority, override, stop, fallback, escalation, and test evidence | | | | | |
| Transparency and instructions | Instructions for use, limitations, notices, disclosure, accessibility, language, user information | | | | | |
| Logging and recordkeeping | Events captured, retention, access, integrity, version linkage, and export | | | | | |
| Risk-management system | Hazards, scenarios, controls, residual risks, decisions, and updates | | | | | |
| Quality-management system | Policies, procedures, ownership, release, supplier, incident, corrective action, and change control | | | | | |
| Predetermined changes and version history | Approved change plan, release history, modifications, reassessment, rollback | | | | | |
| Standards and conformity | Harmonised standards, common specifications, conformity route, notified-body records, declarations, registration, marking | | | | | |
| Post-market monitoring | Monitoring plan, metrics, thresholds, complaints, incidents, trends, corrective action | | | | | |
| Supplier and component evidence | Contracts, model/system cards, attestations, licences, dependencies, change notices, audit evidence | | | | | |
| Incident and remediation | Incident chronology, notification, containment, root cause, corrective action, validation, lessons learned | | | | | |

## 3. Supporting governance documentation

Where relevant, index:

- applicability, role, prohibited-practice, and high-risk assessments;
- FRIA, DPIA, data-governance, security, vendor, and risk assessments;
- control and evidence registers;
- release, residual-risk, exception, and executive approvals;
- deployer handoff, instructions, training, and competence evidence;
- authority, notified-body, auditor, customer, and supplier correspondence.

## 4. Production-version reconciliation

| Production component | Production version/checksum | Documentation version | Evidence location | Match? | Resolution/owner |
|---|---|---|---|---|---|
| Model | | | | | |
| System code | | | | | |
| Prompts/system instructions | | | | | |
| Tools/agents/integrations | | | | | |
| Datasets/retrieval sources | | | | | |
| Configuration/thresholds | | | | | |
| User interface/notices | | | | | |
| Monitoring/logging configuration | | | | | |

No release may rely on documentation that describes a materially different system, model, dataset, configuration, or oversight process.

## 5. Evidence-quality checks

For each indexed item, confirm:

- authentic and attributable to an accountable owner;
- complete for the applicable legal purpose;
- current, approved, and linked to the deployed version;
- internally consistent with other documentation;
- supported by source evidence and reproducible where required;
- protected from unauthorized alteration;
- accessible only to authorized persons while available to auditors, notified bodies, and authorities as legally required;
- retrievable within required timeframes;
- retained under the applicable legal, contractual, operational, and legal-hold schedule;
- available in the required language and format.

## 6. Gaps and release decision

| Gap | Legal/operational impact | Interim control | Owner | Due date | Validation | Release blocker? |
|---|---|---|---|---|---|---|
| | | | | | | |

- [ ] Complete for applicable legal purpose
- [ ] Complete with approved conditions
- [ ] Governance index only; Annex IV not applicable
- [ ] Incomplete — release or conformity review blocked
- [ ] Qualified legal or conformity review required

**Decision rationale:**  
**Open conditions:**  
**Conformity implications:**  

## 7. Change and review triggers

Update after:

- model, system, code, prompt, tool, data, threshold, or infrastructure change;
- intended-purpose, actor-role, population, jurisdiction, or product change;
- supplier, component, licence, or dependency change;
- validation, monitoring, incident, complaint, or audit finding;
- predetermined change-plan use or substantial modification;
- conformity, registration, declaration, marking, authority, or legal development;
- suspension, rollback, withdrawal, recall, or retirement.

## GlobalWay Travel Services example

GlobalWay reconciles the technical documentation for an employee-allocation system against production. The review finds that the deployed supplier model and multilingual interface differ from the documented versions. Release remains blocked until the model version, data tests, oversight instructions, transparency notices, monitoring thresholds, and conformity evidence are updated and independently reconciled.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Provider/technical owner | | | |
| Quality/Compliance | | | |
| Legal/conformity owner | | | |
| Security/Data/Privacy, as applicable | | | |

**Evidence references:**  
**Residual gaps and restrictions:**  
**Next review trigger/date:**  
**Index version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 11, Annex IV, and applicable risk-management, data, logging, transparency, oversight, accuracy, robustness, cybersecurity, quality-management, conformity, monitoring, incident, and authority-access provisions.
- Regulation (EU) 2026/1744 where applicable.
- Applicable Annex I product legislation and conformity requirements.
- Current consolidated official texts control over this index.