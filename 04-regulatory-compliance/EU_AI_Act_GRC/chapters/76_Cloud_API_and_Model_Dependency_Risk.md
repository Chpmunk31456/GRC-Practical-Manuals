# Chapter 76 — Cloud, API, and Model Dependency Risk

## 1. Purpose

AI systems commonly depend on external cloud platforms, application programming interfaces (APIs), hosted models, data services, orchestration tools, and other technical components. These dependencies can change, fail, become unavailable, or introduce new legal, operational, security, privacy, and human-impact risks.

This chapter establishes controls for identifying, assessing, monitoring, and managing those dependencies throughout the AI lifecycle.

> **Core principle:** An organization remains accountable for the AI-enabled service it delivers, even when important components are operated by third parties.

## 2. Requirement

Organizations should maintain sufficient visibility and control over material AI dependencies to:

- understand how the system operates;
- identify concentration and single-point-of-failure risks;
- detect material provider, API, model, data, or configuration changes;
- preserve human oversight and safe fallback arrangements;
- maintain evidence for governance, audit, incident response, and regulatory cooperation;
- suspend or restrict use when dependency risk exceeds approved tolerance.

Contracts may allocate operational duties, but they do not remove the organization’s responsibility to govern its own use of AI.

## 3. Plain-language explanation

An AI application may appear to be one system while actually depending on many external services. A customer-support assistant, for example, may rely on a cloud host, a foundation model, a retrieval database, a translation API, an identity provider, an analytics service, and several software libraries.

A failure or unannounced change in any one of these components can affect accuracy, security, accessibility, transparency, availability, or human decision-making. Dependency risk must therefore be managed as part of the complete system, not as a collection of unrelated vendor contracts.

## 4. Dependency inventory

The AI system owner must maintain a current dependency record covering at least:

| Dependency field | Required information |
|---|---|
| Component | Cloud service, API, model, dataset, library, plug-in, gateway, identity service, monitoring service, or subcontractor |
| Provider | Legal entity and service owner |
| Purpose | Function performed within the AI system |
| Criticality | Low, moderate, high, or critical |
| Data handled | Types, sensitivity, source, destination, and retention |
| Regions | Processing, storage, support, and failover locations |
| Version | Model, API, library, service, and configuration version |
| Change method | Notice period, release channel, deprecation policy, and emergency-change process |
| Availability | Service level, recovery targets, and support arrangements |
| Substitutes | Approved fallback, alternate provider, manual process, or no substitute |
| Owner | Accountable business and technical owners |
| Evidence | Contract, architecture record, test results, notices, logs, and approvals |

Unknown material dependencies are a deployment blocker.

## 5. Dependency risk categories

### 5.1 Concentration risk

Concentration exists when multiple critical AI services rely on the same provider, region, model family, identity service, data source, or technical control.

Examples include:

- all customer-facing AI services using one model API;
- production and backup environments operating in the same cloud region;
- several business processes depending on one shared vector database;
- multiple vendors relying on the same unreported subcontractor;
- a single identity provider controlling access to all AI administration tools.

### 5.2 Availability and outage risk

The organization must assess:

- provider service levels;
- realistic recovery time and recovery point objectives;
- regional and global outage scenarios;
- rate limiting, quota exhaustion, and capacity constraints;
- support availability during emergencies;
- degradation behavior when a service is slow or partially unavailable.

### 5.3 API change and deprecation risk

API changes may alter fields, limits, authentication, error handling, safety filters, response structure, logging, or pricing.

Controls should require:

- documented version pinning where feasible;
- advance notice of material changes;
- test-environment validation before production adoption;
- regression tests for safety, accuracy, accessibility, and human oversight;
- approved rollback or fallback procedures;
- monitoring for undocumented behavioral changes.

### 5.4 Model substitution and version-drift risk

A provider may update or replace a hosted model without changing the customer-facing service name. Even a nominally minor update can affect output quality, bias, refusal behavior, multilingual performance, latency, explainability, or safety.

The organization must define which model changes require:

- revalidation;
- legal or role reassessment;
- risk-assessment refresh;
- transparency-notice review;
- human-oversight review;
- renewed business approval.

### 5.5 Data-location and transfer risk

Dependency assessment must identify where data is stored, processed, logged, backed up, and accessed for support. The review should include:

- regional routing;
- cross-border transfers;
- support access;
- telemetry and prompt logging;
- model-improvement or training use;
- backup and deletion behavior;
- subprocessors and downstream services.

### 5.6 Security and privileged-access risk

Material dependencies must be assessed for:

- authentication and authorization;
- privileged administration;
- key and secret management;
- tenant separation;
- encryption;
- vulnerability management;
- software-supply-chain risk;
- incident detection and notification;
- log availability and integrity.

### 5.7 Financial and commercial risk

The owner should assess:

- unpredictable usage charges;
- price changes;
- minimum commitments;
- provider insolvency or acquisition;
- service withdrawal;
- intellectual-property restrictions;
- lock-in and migration cost.

## 6. Criticality assessment

A dependency is high or critical when its failure or change could materially affect:

- safety;
- fundamental rights;
- legal compliance;
- customer access to essential assistance;
- travel disruption response;
- financial loss;
- sensitive-data protection;
- availability of human escalation;
- regulatory reporting or evidence preservation.

Criticality must reflect the business service and affected people, not merely the provider’s technical classification.

## 7. GlobalWay Travel Services example

GlobalWay uses a third-party model API to support itinerary recommendations and traveler-disruption assistance.

### AI may do

- summarize available itinerary options;
- identify schedule conflicts;
- suggest alternatives based on approved travel-policy rules;
- translate routine traveler information;
- prepare a draft response for a travel consultant.

### Human decision

A travel consultant decides whether to:

- approve rebooking during significant disruption;
- recommend an option involving health, accessibility, immigration, or safety concerns;
- authorize an exception to client policy;
- communicate uncertain or high-impact advice.

### Dependency concern

The model provider deploys an unannounced update that changes multilingual behavior and begins omitting accessibility-related travel constraints from some recommendations.

### Required response

GlobalWay must:

1. detect the performance change through monitoring or user feedback;
2. restrict automated recommendations for affected languages and use cases;
3. route cases to trained human consultants;
4. preserve prompts, outputs, model/version evidence, and provider notices;
5. assess customer impact and notification obligations;
6. require provider investigation and corrective evidence;
7. revalidate the service before restoration.

### Accountable owner

The VP of Traveler Experience remains accountable for the service decision. The provider does not decide whether GlobalWay continues operating the affected feature.

## 8. Dependency-change control

Material dependency changes must follow a documented process:

```text
Provider or internal change detected
            ↓
Dependency record updated
            ↓
Materiality and role assessment
            ↓
Legal, risk, security, privacy, accessibility,
and human-oversight review as applicable
            ↓
Testing and evidence evaluation
            ↓
Approve, conditionally approve, defer, restrict, or reject
            ↓
Production monitoring and rollback readiness
```

## 9. Minimum change triggers

Reassessment is required when there is a material change to:

- model family or version;
- intended purpose;
- provider or subcontractor;
- hosting region;
- training or data-use terms;
- API behavior or schema;
- safety controls;
- performance limits;
- authentication or privileged access;
- logging or evidence access;
- service-level commitments;
- pricing that could alter operational behavior;
- fallback or continuity arrangements.

## 10. Continuity and fallback controls

Each high or critical dependency must have an approved continuity strategy. Options may include:

- human-only processing;
- reduced-function safe mode;
- alternate model or provider;
- cached approved content;
- delayed processing;
- manual travel-consultant escalation;
- controlled service suspension.

A fallback is not acceptable merely because it is technically available. It must be tested for security, privacy, accuracy, accessibility, transparency, human oversight, and operational capacity.

## 11. Model and provider substitution

An alternate model must not be treated as interchangeable without evidence. Substitution testing should address:

- output quality;
- bias and disparate impact;
- multilingual performance;
- safety and refusal behavior;
- explainability;
- accessibility;
- latency and reliability;
- logging and evidence;
- data use and retention;
- human-oversight effectiveness.

## 12. Stop and escalation conditions

The accountable owner must stop, restrict, or escalate the AI use when:

- a critical dependency is unknown or undocumented;
- the provider makes a material change without adequate evidence;
- model identity or version cannot be established;
- required logs or incident evidence are unavailable;
- the service exceeds approved error or harm thresholds;
- a fallback process cannot safely manage expected volume;
- provider terms permit unacceptable data use;
- data-location or subprocessor information is materially incomplete;
- concentration risk exceeds approved tolerance;
- the organization cannot preserve meaningful human oversight.

## 13. Control activities

| Control ID | Control activity | Frequency | Owner | Evidence |
|---|---|---|---|---|
| EUAI-DEP-01 | Maintain an AI dependency inventory | Continuous; quarterly certification | AI system owner | Inventory, architecture map, certifications |
| EUAI-DEP-02 | Assess dependency criticality and concentration | On intake and at least annually | Enterprise risk | Risk assessment, concentration analysis |
| EUAI-DEP-03 | Monitor provider, API, and model changes | Continuous | Technical owner | Release notices, monitoring logs, tickets |
| EUAI-DEP-04 | Test material dependency changes before production | Per change | Product and assurance owners | Test plan, results, approval |
| EUAI-DEP-05 | Maintain tested fallback and continuity arrangements | At least annually and after material change | Business continuity owner | Exercise results, corrective actions |
| EUAI-DEP-06 | Review data-location, security, and subprocessor changes | Per change and periodically | Privacy and security | Assessments, provider evidence |
| EUAI-DEP-07 | Escalate unapproved or unexplained dependency changes | Per event | AI governance lead | Incident record, decision log |

## 14. Evidence requirements

Evidence should include:

- system and dependency architecture;
- current versions and configurations;
- provider and subprocessor lists;
- service-level and support commitments;
- change and deprecation notices;
- test and regression results;
- performance and availability metrics;
- incident records;
- data-location and transfer records;
- fallback and continuity exercises;
- accountable-owner decisions;
- exception and risk-acceptance approvals.

Provider assurances alone are insufficient where independent testing or corroboration is reasonably available.

## 15. Audit tests

An auditor should:

1. select a sample of high and critical AI systems;
2. trace each system to its complete dependency inventory;
3. confirm versions, providers, regions, subprocessors, owners, and fallback arrangements;
4. examine recent provider or model changes;
5. verify that material changes received appropriate review and testing;
6. inspect outage, degradation, quota, or rate-limit events;
7. test whether human escalation and fallback procedures operated as designed;
8. confirm that unresolved dependency risks were escalated and approved by authorized owners;
9. assess whether evidence is complete, current, and independently supportable.

## 16. Metrics

Management should monitor:

- percentage of AI systems with complete dependency inventories;
- number of unknown or unsupported dependencies;
- concentration by provider, model family, region, and identity service;
- material changes detected before production;
- unplanned model or API behavior changes;
- dependency incidents and time to containment;
- fallback test success rate;
- percentage of critical dependencies without tested alternatives;
- overdue provider evidence and unresolved change reviews;
- incidents requiring human-only operation.

## 17. Management checklist

- [ ] All material dependencies are identified.
- [ ] Criticality and concentration are assessed.
- [ ] Model and API versions are known.
- [ ] Provider and subprocessor changes are monitored.
- [ ] Data locations and support access are documented.
- [ ] Material changes trigger appropriate reassessment.
- [ ] Fallback arrangements are safe and tested.
- [ ] Human oversight remains effective during degradation.
- [ ] Stop conditions and accountable decision rights are clear.
- [ ] Evidence is sufficient for audit and regulatory cooperation.

## 18. Graphic specification

### Figure 76-1 — AI Dependency and Resilience Map

Create an original formal process diagram showing:

1. Business AI service at the center;
2. surrounding dependencies: cloud, model API, identity, data, monitoring, and subcontractors;
3. risk paths for outage, change, data movement, security, and concentration;
4. control layers: inventory, monitoring, testing, fallback, human oversight, and escalation;
5. accountable human owner making the final continue, restrict, or stop decision.

**Alt text:** Diagram showing an AI business service connected to cloud, model, data, identity, monitoring, and subcontractor dependencies, with controls for change detection, testing, fallback, human oversight, and accountable escalation.

## 19. Key takeaway

Cloud, API, and model dependencies must be governed as part of the complete AI system. An organization should know what it depends on, detect material changes, test alternatives, preserve human accountability, and stop or restrict service when dependency risk cannot be controlled.
