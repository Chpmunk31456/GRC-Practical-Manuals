# Appendix M — Post-Market Monitoring Plan

> **Legal status:** Corrected English master. For providers of high-risk AI systems, this plan supports Article 72. For deployers and other actors, monitoring may be required by other AI Act provisions, other law, contract, or organizational policy and must be identified separately.

## Purpose

Use this plan to define how an AI system will be monitored after market placement or deployment for performance, safety, fundamental-rights impacts, cybersecurity, complaints, incidents, misuse, supplier changes, control failures, and continued compliance.

The plan must be active, systematic, proportionate, version-linked, integrated with risk and quality management, and capable of triggering timely investigation, restriction, suspension, notification, corrective action, withdrawal, or recall.

## 1. Applicability record

| Field | Response |
|---|---|
| Legal entity and actor role | |
| System/model and inventory ID | |
| Production version/configuration | |
| Intended purpose | |
| High-risk classification/legal basis | |
| Article 72 applies? | |
| Other monitoring duties | |
| Jurisdictions | |
| Provider/vendor and dependencies | |
| Current legal source/application date | |
| Monitoring owner | |
| Plan version/date | |

## 2. Monitoring objectives

Define objectives for:

- accuracy, reliability, and performance;
- subgroup, language, accessibility, and fairness outcomes;
- safety, health, and fundamental-rights risk;
- human-oversight effectiveness, overrides, and escalation;
- cybersecurity, misuse, abuse, prompt injection, and tool/agent actions;
- transparency, instructions, disclosure, complaints, and appeals;
- drift, data, model, supplier, and infrastructure changes;
- resilience, fallback, continuity, and recovery;
- legal, conformity, registration, and regulatory commitments;
- corrective-action effectiveness and repeat failures.

## 3. Indicators and thresholds

| Indicator | Baseline | Warning threshold | Critical threshold | Data source | Frequency | Owner | Required action |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Indicators should be risk-based and include where relevant:

- accuracy, error, abstention, and reliability;
- false-positive and false-negative rates;
- subgroup and intersectional disparities;
- language and accessibility defects;
- override, disagreement, appeal, and complaint rates;
- incidents, near misses, and adverse outcomes;
- security alerts, misuse attempts, and anomalous tool actions;
- drift and out-of-distribution conditions;
- supplier/model/version changes;
- missing logs, evidence, or documentation;
- fallback, outage, and recovery failures;
- overdue findings and repeated corrective actions.

## 4. Data collection and evidence

Document collection and governance for:

- production logs and telemetry;
- sampled inputs and outputs;
- prompts, retrieval sources, tool calls, and agent actions;
- human-review, override, stop, and escalation records;
- complaints, appeals, corrections, and remedies;
- incidents, near misses, and notifications;
- security alerts and threat intelligence;
- supplier notices, releases, outages, and documentation changes;
- drift, performance, bias, language, accessibility, and robustness tests;
- internal audit, conformity, notified-body, and authority findings;
- change, rollback, suspension, withdrawal, recall, and restoration records.

Apply privacy, minimisation, confidentiality, access, integrity, retention, legal-hold, and cross-border controls.

## 5. Review cadence

| Review | Frequency | Participants | Inputs | Output |
|---|---|---|---|---|
| Operational monitoring | | | | |
| Technical validation | | | | |
| Risk and compliance review | | | | |
| Fundamental-rights/privacy review | | | | |
| Security review | | | | |
| Supplier review | | | | |
| Executive/board reporting | | | | |
| Independent assurance | | | | |

## 6. Trigger and response matrix

| Trigger | Required action | Actor/owner | Deadline/legal source | Escalation | Evidence |
|---|---|---|---|---|---|
| Serious incident or credible harm allegation | | | | | |
| Significant performance degradation | | | | | |
| Subgroup, language, or accessibility disparity | | | | | |
| Material complaint or appeal trend | | | | | |
| Security compromise or misuse | | | | | |
| Supplier model, service, data, or contract change | | | | | |
| Intended-purpose, population, or jurisdiction change | | | | | |
| Missing logs or evidence | | | | | |
| Legal or regulatory development | | | | | |
| Material audit, conformity, or control finding | | | | | |
| Potential substantial modification | | | | | |

Possible actions include investigation, evidence preservation, enhanced oversight, configuration change, scope restriction, user communication, retraining, supplier escalation, suspension, rollback, withdrawal, recall, conformity reassessment, documentation update, and notification where legally required.

## 7. Incident and corrective-action integration

For material signals:

1. preserve relevant evidence and identify affected versions;
2. contain immediate risk;
3. assess serious-incident and parallel notification duties;
4. identify affected persons, jurisdictions, suppliers, and systems;
5. perform root-cause and affected-scope analysis;
6. define corrective and preventive actions;
7. update risk, technical, QMS, instructions, notices, and monitoring records;
8. validate remediation before restoration or closure;
9. share lessons across similar systems.

## 8. Supplier and dependency monitoring

Monitor:

- model releases, deprecations, changed capabilities, and known limitations;
- data-source, subprocessor, hosting, and location changes;
- service levels, outages, security events, and incident notices;
- licensing, open-source, copyright, and contractual changes;
- audit, documentation, logging, and evidence-access limitations;
- concentration, continuity, portability, and exit risk.

## 9. Reporting and escalation

| Condition | Recipient | Deadline | Required content/evidence | Decision authority |
|---|---|---|---|---|
| | | | | |

Reports must distinguish facts, assumptions, uncertainty, legal duties, current controls, residual risk, and required decisions.

## 10. Evidence retention

Retain monitoring data, analyses, decisions, approvals, complaints, incident records, notifications, authority correspondence, supplier notices, test results, and corrective-action evidence under the applicable statutory, contractual, operational, privacy, and legal-hold schedule.

## 11. Decision

- [ ] Article 72 provider plan approved
- [ ] Other-actor monitoring plan approved
- [ ] Approved with conditions
- [ ] Restricted pilot monitoring only
- [ ] Remediation required
- [ ] Deployment blocked or suspended

**Decision rationale:**  
**Conditions and thresholds:**  
**Retention basis:**  
**Open actions:**  

## 12. Review triggers

Review after:

- model, system, data, prompt, tool, agent, supplier, or infrastructure change;
- new purpose, population, jurisdiction, or affected-person context;
- incident, complaint, appeal, drift, or failed control;
- monitoring threshold breach;
- substantial modification or conformity change;
- legal, authority, standard, or code development;
- suspension, rollback, withdrawal, recall, or restoration.

## GlobalWay Travel Services example

GlobalWay monitors a traveler-disruption assistant for incorrect rebooking, safety-sensitive advice, subgroup and language disparities, unauthorized tool actions, override rates, complaints, supplier changes, and outages. A supplier update increases incorrect recommendations in severe-weather cases. Critical thresholds trigger feature restriction, evidence preservation, human-only rebooking, supplier escalation, regression testing, and legal review before restoration.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Provider/technical owner | | | |
| Monitoring owner | | | |
| Quality/Compliance | | | |
| Legal | | | |
| Risk/Privacy/Security, as applicable | | | |

**Evidence references:**  
**Retention basis:**  
**Next review trigger/date:**  
**Plan version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 72 and applicable provider, deployer, risk-management, quality-management, logging, monitoring, incident, corrective-action, authority, and high-risk provisions.
- Regulation (EU) 2026/1744 where applicable.
- Applicable privacy, cybersecurity, product-safety, employment, consumer-protection, and sector law.
- Current consolidated official texts control over this plan.