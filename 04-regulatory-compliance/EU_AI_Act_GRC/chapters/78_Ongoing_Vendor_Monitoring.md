# Chapter 78 — Ongoing Vendor Monitoring

## 1. Purpose

Initial due diligence does not establish permanent assurance. AI providers, models, services, datasets, subprocessors, contracts, technical dependencies, and regulatory expectations change throughout the relationship.

This chapter establishes a risk-based process for continuously monitoring AI vendors and taking timely human decisions when evidence, performance, risk, or accountability changes.

> Vendor approval is a point-in-time decision. Vendor assurance is a continuing control process.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 2. Scope

This chapter applies to external parties that provide or materially support:

- AI systems and hosted models;
- general-purpose AI models;
- cloud AI services and APIs;
- model-development and orchestration platforms;
- datasets, embeddings, retrieval services, and data-labeling services;
- plug-ins, agents, tools, and external connectors;
- model evaluation, red-team, monitoring, or assurance services;
- managed services involving AI-supported decisions;
- subprocessors and critical fourth parties;
- open-source components supported under a commercial agreement.

## 3. Governance principle

Monitoring must be proportionate to the vendor’s risk, role, criticality, data access, technical influence, and impact on people.

Monitoring must answer five questions:

1. Has the vendor, model, service, or dependency changed?
2. Is the service still operating within approved purpose and limits?
3. Has new evidence weakened or strengthened the original approval basis?
4. Are contractual and regulatory obligations still being met?
5. Does an accountable human need to restrict, suspend, remediate, replace, or exit?

## 4. Relationship to EU AI Act responsibilities

Contractual allocation does not replace statutory accountability. GlobalWay must continue to understand its role and duties throughout the vendor relationship.

Ongoing monitoring must support, where applicable:

- continued role classification across the AI value chain;
- compliance with approved intended purpose and instructions for use;
- human oversight and operational monitoring;
- logging and evidence retention;
- risk-management and post-market monitoring activities;
- incident detection, investigation, escalation, and reporting support;
- transparency and accessibility obligations;
- cybersecurity, accuracy, robustness, and data-governance controls;
- reassessment following material change or substantial modification;
- cooperation with providers, authorities, auditors, and affected business owners.

Legal and compliance teams must reassess whether a vendor or customer action changes GlobalWay’s role, obligations, or exposure.

## 5. Risk-tiered monitoring model

Each vendor must have a documented monitoring tier.

| Tier | Typical characteristics | Minimum monitoring approach |
|---|---|---|
| Tier 1 — Critical | High-risk use, safety or rights impact, sensitive data, critical operations, limited substitutes, systemic dependency | Continuous alerts, monthly control review, quarterly evidence review, annual reassessment, event-driven escalation |
| Tier 2 — High | Material customer or employee impact, significant data access, important operational dependency | Monthly alerts, quarterly review, annual reassessment, event-driven escalation |
| Tier 3 — Moderate | Limited decision impact, controlled data, available fallback | Quarterly alerts and review, annual evidence refresh |
| Tier 4 — Low | Low-impact experimentation, no sensitive production data, easy replacement | Annual review and event-driven monitoring |

The tier must be increased when actual use becomes more critical than originally approved.

## 6. Monitoring plan

Every material AI vendor must have an approved monitoring plan that identifies:

- accountable business owner;
- vendor-risk owner;
- technical owner;
- legal, privacy, security, accessibility, and compliance contacts;
- approved systems, models, versions, regions, and use cases;
- monitoring tier and frequency;
- required evidence and refresh dates;
- performance and risk thresholds;
- incident and change-notification channels;
- escalation and decision authority;
- fallback, suspension, replacement, and exit options;
- review records and retention period.

## 7. Monitoring domains

### 7.1 Corporate and ownership changes

Monitor for:

- merger, acquisition, insolvency, restructuring, or sale;
- change in controlling ownership;
- major leadership or governance changes;
- sanctions, enforcement actions, litigation, or regulatory restrictions;
- material financial deterioration;
- loss of key personnel or maintainers;
- geographic relocation of important operations.

These events may affect continuity, independence, contractual enforceability, data access, and regulatory exposure.

### 7.2 Product, model, and service changes

Monitor for:

- model-version changes;
- silent model substitution;
- API changes or deprecation;
- altered intended purpose or supported use cases;
- changed performance, limitations, or safety behavior;
- new tools, agents, plug-ins, or external actions;
- new data uses or retention practices;
- changed hosting region or infrastructure;
- changed logging or observability;
- new or removed human-oversight features;
- changed accessibility behavior;
- changed terms of service or acceptable-use rules.

No material vendor change may become an unreviewed production change.

### 7.3 Security and resilience

Monitor:

- vulnerabilities and security advisories;
- data breaches and unauthorized access;
- model theft, extraction, poisoning, backdoors, or manipulation;
- prompt injection and tool-abuse incidents;
- outages, latency, capacity, and regional failures;
- disaster-recovery and continuity performance;
- privileged-access changes;
- subprocessor and software-supply-chain incidents;
- remediation timeliness;
- penetration-test, certification, and assurance-report status.

### 7.4 Privacy and data governance

Monitor:

- changes in personal-data processing;
- special-category or sensitive-data exposure;
- retention, deletion, correction, and export capability;
- international transfers and data locations;
- model-training or service-improvement use of customer data;
- subprocessor additions or removals;
- data-quality and provenance concerns;
- memorization, leakage, and re-identification risk;
- unresolved data-subject or customer complaints.

### 7.5 Performance, bias, and human impact

Monitor:

- accuracy and error rates;
- hallucination, fabrication, or unsupported-output rates;
- false-positive and false-negative rates;
- model and data drift;
- performance by language, region, disability, demographic group, and use context;
- disparate impact and bias indicators;
- accessibility failures;
- human override, challenge, correction, and escalation rates;
- complaints, adverse outcomes, and near misses;
- user overreliance or automation bias;
- unexpected or out-of-scope behavior.

### 7.6 Legal, regulatory, and contractual status

Monitor:

- expired or changed certifications and attestations;
- changes in regulatory classification;
- noncompliance notices or authority inquiries;
- changes to licenses, intellectual-property terms, or model-use restrictions;
- failure to provide required documentation;
- missed incident-notification obligations;
- restrictions on audit, evidence access, portability, or termination;
- unresolved contractual breaches;
- changes affecting provider, deployer, importer, distributor, or downstream roles.

### 7.7 Fourth-party and concentration risk

Monitor:

- critical cloud, model, data, and infrastructure dependencies;
- new subprocessors and fourth parties;
- common dependencies shared across multiple critical services;
- geographic, technical, and financial concentration;
- unsupported or end-of-life components;
- substitution and portability constraints;
- fourth-party incidents that can affect GlobalWay.

## 8. Evidence-refresh schedule

Required evidence should be refreshed according to risk and expiration.

Examples include:

- current system and model documentation;
- instructions for use and known limitations;
- security and privacy assurance reports;
- certification status;
- penetration-test summaries;
- vulnerability and remediation reports;
- business-continuity and recovery-test results;
- subprocessor lists;
- data-flow and hosting-location records;
- accessibility conformance evidence;
- bias, performance, and robustness evaluations;
- insurance evidence;
- financial and operational viability evidence;
- contract and service-level compliance records;
- incident and complaint summaries.

Expired, incomplete, contradictory, or materially weakened evidence must trigger review.

## 9. Continuous and event-driven monitoring

Scheduled reviews are not sufficient for critical vendors. Event-driven monitoring must identify material changes as they occur.

Trigger events include:

- confirmed or suspected security incident;
- serious operational outage;
- material model or API change;
- new safety, bias, privacy, accessibility, or rights concern;
- regulatory investigation or enforcement;
- change in ownership or financial viability;
- certification lapse;
- missed service or remediation target;
- new critical subprocessor;
- material contract or policy change;
- customer or employee harm;
- evidence that the service is used outside approved purpose;
- indication of substantial modification or changed legal role.

## 10. Monitoring dashboard

The vendor-monitoring dashboard should show, at minimum:

- vendor and service;
- risk tier;
- accountable owner;
- approved use cases;
- current model and version;
- evidence status and expiration;
- open incidents and findings;
- overdue remediation;
- performance and bias thresholds;
- service availability and resilience status;
- subprocessor changes;
- material contract changes;
- next review date;
- current decision: approved, conditional, restricted, suspended, or exiting.

Dashboard status must be traceable to supporting evidence.

## 11. Thresholds and decision rules

Each monitoring plan must define measurable thresholds.

Examples:

- maximum error or hallucination rate;
- minimum availability and recovery performance;
- maximum unresolved critical vulnerabilities;
- maximum incident-notification delay;
- maximum overdue remediation period;
- acceptable bias or disparity thresholds;
- minimum multilingual and accessibility performance;
- maximum rate of human overrides or complaints;
- maximum period for expired evidence;
- maximum unapproved model-version drift.

Threshold breaches must not be treated as informational only. They must route to an accountable human decision.

## 12. Human review and decision rights

### AI may do

- collect vendor alerts and status information;
- compare evidence dates and versions;
- identify threshold breaches;
- correlate incidents, complaints, outages, and performance changes;
- prioritize vendors for review;
- draft monitoring summaries.

### Human decision

An authorized human decides whether to:

- continue approval;
- impose corrective conditions;
- increase monitoring;
- restrict data, users, features, or use cases;
- require independent testing;
- suspend production use;
- invoke audit rights;
- escalate to legal, executive, or regulatory review;
- replace the vendor;
- begin exit or termination.

### Stop and escalation

Automated monitoring must not independently restore a suspended vendor or waive a material finding. Restoration requires documented human approval and evidence that the risk is controlled.

### Accountable owner

The business owner remains accountable for continued use. Vendor risk, legal, privacy, security, accessibility, compliance, procurement, and technical owners retain their assigned responsibilities.

### Challenge, correction, and override

Reviewers must be able to challenge vendor claims, correct inaccurate monitoring data, require additional evidence, and override automated prioritization.

## 13. Corrective-action management

Each material finding must include:

- unique identifier;
- source and date;
- affected service and use case;
- severity and rationale;
- legal, technical, operational, rights, and customer impact;
- required action;
- accountable owner;
- target date;
- interim controls;
- validation method;
- closure evidence;
- approval or risk-acceptance decision.

Repeated findings or missed commitments must increase vendor risk and may justify suspension or exit.

## 14. Stop and escalation conditions

Use must stop, be restricted, or receive urgent review when:

- the vendor makes an unapproved material model or service change;
- required evidence is withheld, expired, or materially unreliable;
- a critical vulnerability or compromise remains uncontrolled;
- the service causes or may cause serious harm;
- outputs materially exceed approved error, bias, or accessibility thresholds;
- the vendor fails to notify GlobalWay of a material incident;
- data is processed outside approved purposes, locations, or retention terms;
- human oversight, logging, correction, or override becomes ineffective;
- the vendor or a critical subprocessor becomes unable to maintain service;
- continued use may constitute a prohibited practice or uncontrolled high-risk use;
- responsible owners cannot explain or defend continued use.

## 15. GlobalWay Travel Services example

GlobalWay uses a third-party AI service to prioritize travelers affected by flight cancellations and recommend rebooking options.

### Approved purpose

The service may rank disruption cases and recommend options. It may not finalize refunds, deny assistance, change safety instructions, or send traveler communications without approved human review.

### Monitoring signals

GlobalWay monitors:

- model and API version;
- ranking accuracy;
- missed high-priority travelers;
- performance across languages and accessibility needs;
- false assumptions about visa, medical, or mobility requirements;
- service outages and latency;
- traveler complaints;
- human override rates;
- subprocessor and data-location changes;
- incident and vulnerability notices.

### Trigger event

The vendor silently changes the underlying model. GlobalWay detects a sharp increase in missed Spanish-language disruption cases and accessibility-related errors.

### Human response

The Director of Travel Operations restricts the service to recommendation-only mode, activates manual prioritization, and blocks automated traveler messages. Vendor risk and legal teams invoke change-notification and evidence-access rights. The technical team compares versions and validates corrected performance before any restoration.

### Accountable decision

The service remains restricted until accountable owners confirm that language, accessibility, safety, privacy, and operational thresholds are met.

## 16. Control activities

| Control ID | Control activity | Evidence |
|---|---|---|
| EUAI-VMON-01 | Assign vendor risk tiers and approved monitoring plans | Tier assessment and monitoring plan |
| EUAI-VMON-02 | Maintain current vendor, service, model, dependency, and owner records | Vendor inventory and service register |
| EUAI-VMON-03 | Monitor material changes, incidents, performance, and evidence expiration | Alerts, dashboards, and review records |
| EUAI-VMON-04 | Define thresholds and route breaches to accountable humans | Threshold register and escalation records |
| EUAI-VMON-05 | Refresh legal, security, privacy, accessibility, resilience, and performance evidence | Current assurance package |
| EUAI-VMON-06 | Track corrective actions through validated closure | Findings and remediation records |
| EUAI-VMON-07 | Reassess role, intended purpose, and substantial-modification risk after change | Legal and classification reassessment |
| EUAI-VMON-08 | Maintain tested restriction, suspension, replacement, and exit capability | Exercise and decision evidence |

## 17. Evidence requirements

Evidence should include:

- vendor monitoring plan;
- risk-tier decision;
- vendor and service inventory;
- model and version records;
- current documentation and assurance evidence;
- monitoring dashboards and alerts;
- performance, bias, accessibility, and robustness results;
- security and privacy notices;
- subprocessor and dependency records;
- incident and complaint records;
- threshold-breach decisions;
- corrective-action records;
- audit-right invocation records;
- restriction, suspension, restoration, replacement, or exit decisions;
- meeting minutes and accountable approvals.

## 18. Audit test

Select a sample of active AI vendors, prioritizing critical and high-risk relationships.

For each sample:

1. Confirm the vendor has a current risk tier and monitoring plan.
2. Verify approved systems, models, versions, regions, and use cases.
3. Inspect evidence-refresh status and identify expired or contradictory evidence.
4. Trace monitoring alerts to documented review and action.
5. Test whether model, API, contract, subprocessor, and data-use changes were detected.
6. Compare actual performance, bias, accessibility, security, and availability results to thresholds.
7. Confirm incidents and complaints were escalated and preserved.
8. Verify corrective actions were validated before closure.
9. Confirm role and substantial-modification assessments were refreshed after material change.
10. Verify restriction, suspension, rollback, replacement, and exit arrangements are usable.
11. Confirm restoration decisions were made by authorized humans and supported by evidence.

## 19. Metrics

Suggested metrics:

- percentage of material AI vendors with current monitoring plans;
- percentage assigned a current risk tier;
- percentage with current evidence packages;
- number of expired critical assurance documents;
- number of unapproved model or API changes;
- number of material incidents reported late;
- percentage of threshold breaches reviewed within target time;
- percentage of overdue corrective actions;
- average time to restrict a high-risk vendor after a critical alert;
- percentage of critical vendors with tested alternatives or exit plans;
- number of vendors under conditional approval, restriction, suspension, or exit;
- repeat-finding rate by vendor.

## 20. Management checklist

- [ ] Is every material AI vendor assigned a monitoring tier?
- [ ] Is an accountable business owner identified?
- [ ] Are approved systems, models, versions, regions, and use cases recorded?
- [ ] Are evidence-refresh dates tracked?
- [ ] Are material product, model, API, contract, and subprocessor changes monitored?
- [ ] Are performance, bias, accessibility, privacy, security, and resilience thresholds defined?
- [ ] Do threshold breaches reach an accountable human?
- [ ] Are incidents, complaints, and near misses preserved and reviewed?
- [ ] Are corrective actions validated before closure?
- [ ] Are role and substantial-modification assessments refreshed after change?
- [ ] Can GlobalWay restrict, suspend, replace, or exit the service?
- [ ] Is restoration prohibited without documented human approval?

## 21. Graphic specification

### Figure 78-1 — Continuous AI Vendor Assurance Cycle

Create an original formal circular process diagram with seven stages:

1. Inventory and tier
2. Collect evidence
3. Monitor change and performance
4. Detect threshold breach
5. Human review and decision
6. Remediate, restrict, suspend, or exit
7. Validate and return to monitoring

Place **“Accountable human oversight”** at the center. Show incident alerts, complaints, model changes, and evidence expiration entering the cycle from the outside.

**Purpose:** Demonstrate that vendor approval is continuously revalidated and that material decisions remain human-owned.

**Alt text:** Circular AI vendor-assurance process showing inventory, evidence collection, continuous monitoring, threshold detection, human decision, remediation or exit, and validation before monitoring resumes.

## 22. Key takeaway

Ongoing vendor monitoring is not a periodic paperwork exercise. It is the control process that determines whether the original approval remains justified as the vendor, model, service, evidence, dependencies, and real-world impact change.
