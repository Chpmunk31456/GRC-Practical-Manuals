# Appendix H — AI Risk Assessment

> **Legal status:** Corrected English master. Inherent and residual risk ratings are enterprise risk-management concepts. They are not statutory EU AI Act classifications and must not replace Article 5, Article 6, GPAI, transparency, actor-role, conformity, incident, or notification analysis.

## Purpose

Use this assessment to identify, analyse, evaluate, treat, monitor, communicate, and reassess risks arising from an AI system throughout its lifecycle.

The assessment should connect risk scenarios to affected persons, legal obligations, system versions, controls, evidence, acceptance criteria, monitoring thresholds, and accountable decisions. Planned or untested controls must not be treated as effective.

## 1. Assessment context

| Field | Response |
|---|---|
| System/model | |
| Version/configuration | |
| Inventory ID | |
| Legal entity and actor role | |
| Intended purpose | |
| Actual or proposed use | |
| Users and affected persons | |
| Jurisdictions | |
| Statutory classification | |
| Lifecycle stage | |
| Provider/vendor and dependencies | |
| Current legal source and application dates | |
| Business owner | |
| Technical owner | |
| Risk assessor | |
| Assessment date and version | |

## 2. Risk context

Describe:

- business objective and expected benefit;
- decision or process supported;
- affected persons, vulnerable groups, assets, and services;
- system boundaries, interfaces, tools, agents, and dependencies;
- model, data, infrastructure, cloud, and supplier components;
- legal classification and organizational role;
- decision criticality and degree of automation;
- human oversight and appeal mechanisms;
- assumptions, limitations, uncertainty, and evidence gaps;
- foreseeable misuse, repurposing, and abuse;
- fallback, continuity, suspension, rollback, and exit arrangements.

## 3. Risk categories

Assess each applicable category.

| Category | Risk scenario | Existing controls | Likelihood | Impact | Inherent risk | Residual risk | Evidence/uncertainty |
|---|---|---|---|---|---|---|---|
| Legal and regulatory | | | | | | | |
| Fundamental rights | | | | | | | |
| Safety and health | | | | | | | |
| Accuracy and reliability | | | | | | | |
| Bias and discrimination | | | | | | | |
| Transparency and explainability | | | | | | | |
| Human oversight and automation bias | | | | | | | |
| Privacy and data protection | | | | | | | |
| Cybersecurity, misuse, and abuse | | | | | | | |
| Robustness, resilience, and continuity | | | | | | | |
| Vendor, supply chain, and concentration | | | | | | | |
| Data quality, provenance, and lineage | | | | | | | |
| Change, drift, and substantial modification | | | | | | | |
| Operational and financial | | | | | | | |
| Reputational | | | | | | | |
| Environmental and resource | | | | | | | |
| Societal and cumulative impact | | | | | | | |

## 4. Scenario analysis

For each material risk, document:

- initiating event;
- threat, error, misuse, or failure mechanism;
- exposed person, group, asset, process, or service;
- potential consequence and legal implication;
- affected population and scale;
- duration, detectability, reversibility, and cumulative effect;
- control dependencies and single points of failure;
- credible worst case;
- current evidence and uncertainty;
- immediate containment and escalation requirement;
- monitoring signal that would indicate risk materialization.

| Scenario ID | Initiating event | Failure mechanism | Affected scope | Consequence | Existing controls | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 5. Risk-rating method

Use the organization’s approved methodology. Define at minimum:

- likelihood scale and time horizon;
- impact scale across rights, safety, legal, operational, financial, and reputational dimensions;
- aggregation method;
- treatment and escalation thresholds;
- criteria and authority for residual-risk acceptance;
- treatment deadlines by severity;
- confidence or evidence-quality rating;
- treatment of low-frequency, high-impact events;
- treatment of uncertainty and missing evidence.

Do not use a numerical score as a substitute for professional judgment, legal analysis, or verified evidence. Do not average away severe rights, safety, or legal blockers.

## 6. Inherent risk

Assess exposure before controls.

| Scenario | Cause | Affected persons/assets | Likelihood | Impact | Inherent rating | Confidence | Evidence/uncertainty |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 7. Controls and effectiveness

| Control | Owner | Status | Evidence | Design result | Operating result | Limitation | Dependency |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Do not reduce risk for controls that are planned, incomplete, unapproved, untested, inconsistently operated, unsupported by evidence, or dependent on unavailable supplier information.

## 8. Residual risk and legal blockers

| Risk | Residual rating | Legal blocker? | Treatment | Owner | Due date | Validation requirement |
|---|---|---|---|---|---|---|
| | | | | | | |

A risk-acceptance decision cannot:

- authorize a prohibited practice;
- waive a statutory obligation;
- replace a required conformity assessment, registration, declaration, marking, consultation, notification, or authority decision;
- permit operation outside an approved intended purpose or legal role;
- prevent required incident reporting, corrective action, restriction, recall, or withdrawal;
- override applicable privacy, employment, safety, consumer, accessibility, equality, or sector law.

## 9. Risk treatment

Select one or more:

- avoid or prohibit the use;
- reduce through technical controls;
- reduce through process, staffing, or human oversight;
- reduce through data, interface, or scope changes;
- transfer or allocate through contract or insurance, without transferring legal accountability that remains with the organization;
- limit purpose, population, geography, data, capability, or degree of automation;
- pilot with enhanced monitoring and exit criteria;
- accept residual risk through authorized approval;
- suspend, restrict, roll back, withdraw, or decommission pending remediation.

| Treatment action | Owner | Due date | Priority | Status | Validation method | Closure evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

## 10. Key risk indicators and thresholds

| Indicator | Threshold | Data source | Frequency | Owner | Escalation action |
|---|---|---|---|---|---|
| | | | | | |

Consider:

- error and abstention rates;
- subgroup and language disparities;
- override, disagreement, appeal, and complaint rates;
- incidents, near misses, and notification triggers;
- security alerts and misuse attempts;
- model, data, prompt, tool, or supplier changes;
- unavailable logs, evidence, or documentation;
- drift, unexpected behaviour, and failed regression tests;
- overdue findings and repeated exceptions;
- service continuity and fallback failures.

## 11. Residual-risk decision

- [ ] Acceptable within approved tolerance
- [ ] Acceptable with conditions and enhanced monitoring
- [ ] Executive risk acceptance required
- [ ] Board escalation required
- [ ] Remediation required before approval
- [ ] Restricted pilot only
- [ ] Deployment blocked or suspended
- [ ] Prohibited, withdrawn, or decommissioned
- [ ] Qualified legal review required

### Decision rationale

Document:

- expected benefits and supporting evidence;
- less risky alternatives considered;
- control design and operating effectiveness;
- legal blockers and mandatory obligations;
- uncertainty and evidence limitations;
- affected persons and vulnerable groups;
- residual-risk conditions, duration, and monitoring;
- acceptance authority and rationale;
- criteria requiring suspension, rollback, or reassessment.

## 12. Monitoring and reassessment

Define:

- indicators, thresholds, and source systems;
- affected-person, subgroup, language, and accessibility outcomes;
- human-oversight, override, appeal, and complaint monitoring;
- incident, near-miss, and notification triggers;
- model, vendor, data, prompt, tool, and jurisdiction changes;
- review frequency and reporting recipients;
- suspension, rollback, restriction, withdrawal, and exit criteria;
- evidence-retention and version-linking requirements.

## 13. Reassessment triggers

Reassess after:

- model, data, prompt, tool, agent, architecture, or interface change;
- intended-purpose, actual-use, population, sector, or degree-of-automation change;
- deployment in a new jurisdiction or legal entity;
- material incident, complaint, appeal, adverse outcome, or near miss;
- performance, bias, subgroup, language, accessibility, or security drift;
- vendor, contract, subprocessor, licence, or critical-dependency change;
- security vulnerability, threat intelligence, or misuse pattern;
- legal, regulatory, authority, standard, or code development;
- audit, validation, conformity, or control-testing finding;
- substantial modification, repurposing, or role change.

## GlobalWay Travel Services example

GlobalWay assesses a traveler-disruption assistant that recommends itinerary changes and can initiate rebooking tools. Material scenarios include inaccurate safety advice, unauthorized refunds, privacy leakage, prompt injection, vendor outages, language disparities, and automation bias. GlobalWay requires human confirmation for external actions, restricts sensitive data, adds multilingual regression testing, monitors override and complaint rates, and defines immediate suspension thresholds. Residual risk is approved only for a restricted pilot pending supplier evidence and independent validation.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| Technical owner | | | |
| Risk owner | | | |
| Legal/Compliance | | | |
| Privacy/Security/Data, as applicable | | | |
| Executive or board, where required | | | |

**Evidence references:**  
**Accepted assumptions and uncertainty:**  
**Conditions, restrictions, and expiry:**  
**Open actions and due dates:**  
**Next review trigger/date:**  
**Assessment version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, high-risk, GPAI, transparency, human-oversight, accuracy, robustness, cybersecurity, monitoring, incident, corrective-action, and authority provisions.
- Regulation (EU) 2026/1744 where applicable.
- Regulation (EU) 2016/679 and applicable employment, equality, accessibility, cybersecurity, product-safety, consumer-protection, intellectual-property, environmental, and sector law.
- Enterprise risk ratings in this template are governance tools and do not alter statutory classifications or legal duties.