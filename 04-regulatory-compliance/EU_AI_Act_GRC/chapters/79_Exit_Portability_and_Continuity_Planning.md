# Chapter 79 — Exit, Portability, and Continuity Planning

## 1. Purpose

AI services may become unavailable, unaffordable, unsupported, unsafe, non-compliant, or strategically unsuitable. Organizations must be able to reduce, suspend, replace, or terminate an AI dependency without losing control of data, records, configurations, evidence, business operations, or accountability.

This chapter establishes governance requirements for planned exit, emergency exit, portability, fallback operations, transition, and controlled restoration.

> A vendor exit plan is not complete until the organization can operate safely without the vendor.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 2. Scope

This chapter applies to:

- hosted AI systems and models;
- cloud AI platforms;
- model and inference APIs;
- AI-enabled software-as-a-service;
- external data, retrieval, vector, and orchestration services;
- model marketplaces and managed model endpoints;
- third-party agents, plug-ins, connectors, and tools;
- open-source components maintained by external communities;
- subcontractors and critical fourth parties;
- internally hosted solutions dependent on external licenses, updates, or support.

## 3. Governance principle

Exit planning must begin before contract signature or production approval. The organization must know:

- what must be recovered;
- what must be deleted;
- what must remain available;
- what must be replaced;
- what evidence must be preserved;
- who may authorize restriction, suspension, migration, restoration, or termination;
- how affected people and business teams will be protected during transition.

Exit rights in a contract are useful only when supported by tested technical and operational capability.

## 4. Exit triggers

Exit or transition planning may be activated by:

- service failure or repeated outages;
- material performance deterioration;
- safety, rights, privacy, security, or accessibility failures;
- prohibited or unapproved use;
- unresolved audit findings;
- failure to provide required documentation or evidence;
- material model, API, subprocessor, data-location, or ownership changes;
- regulatory action or legal incompatibility;
- vendor insolvency, acquisition, restructuring, or market withdrawal;
- loss of critical personnel or support;
- license expiration or material price increase;
- end-of-life or deprecation;
- unacceptable concentration risk;
- contract breach;
- inability to meet recovery, portability, deletion, or incident obligations;
- strategic replacement or internalization.

## 5. Exit types

### 5.1 Planned exit

A scheduled transition at contract end, service retirement, strategic replacement, or approved migration.

### 5.2 Corrective exit

A transition required because the provider cannot remediate material deficiencies within the approved timeframe.

### 5.3 Emergency exit

Immediate restriction or suspension because continued use creates unacceptable legal, safety, rights, privacy, cybersecurity, or operational risk.

### 5.4 Partial exit

Removal of a model, feature, region, subprocessor, data flow, user group, or decision function while other approved services continue.

### 5.5 Temporary fallback

A controlled shift to manual processing, approved templates, rules-based logic, another provider, or a reduced service while the primary dependency is unavailable or under review.

## 6. Exit-readiness assessment

Before production approval, the owner must assess:

| Area | Required question |
|---|---|
| Data | Can all required data, metadata, logs, embeddings, prompts, outputs, and records be exported? |
| Format | Are exports complete, documented, machine-readable, and usable without proprietary tools? |
| Models | Can approved models, weights, adapters, or configurations be transferred where contractually and technically permitted? |
| Configuration | Can prompts, policies, workflows, guardrails, routing, and integration settings be reproduced? |
| Evidence | Can compliance, testing, monitoring, incident, approval, and audit evidence be retained? |
| Identity | Can accounts, roles, keys, certificates, and integrations be revoked safely? |
| Continuity | Is there a tested manual or technical fallback? |
| Replacement | Is a substitute provider, platform, model, or process available? |
| Deletion | Can the vendor prove deletion from active systems, logs, backups, and subprocessors where applicable? |
| People | Are employees, travelers, customers, and other affected people protected during transition? |
| Cost | Are migration, extraction, parallel-run, and termination costs known? |
| Timing | Can exit occur within the required recovery and risk timeframe? |

## 7. Portability requirements

Portability must cover more than raw business data. Depending on the service, the organization may need:

- input and output records;
- prompts and prompt versions;
- system instructions and policies;
- model and endpoint identifiers;
- fine-tuning records and adapters;
- retrieval indexes and source mappings;
- embeddings or the ability to recreate them;
- evaluation datasets and results;
- human-review and override records;
- monitoring thresholds and alert history;
- safety filters and guardrail configurations;
- workflow and orchestration logic;
- access-control mappings;
- incident and corrective-action records;
- audit trails and regulatory evidence;
- documentation of known limitations;
- dependency and subprocessor records.

The owner must distinguish between information that can be exported, information that can be recreated, and information that will be lost.

## 8. Portability quality controls

An export is not adequate merely because a file can be downloaded. Portability testing must assess:

- completeness;
- accuracy;
- format documentation;
- field definitions;
- timestamps and sequence integrity;
- relationship preservation;
- character encoding;
- multilingual content;
- accessibility information;
- security and encryption;
- usability in the target environment;
- reconciliation to source totals;
- repeatability;
- time required to complete extraction.

Critical exports must be tested before an exit is needed.

## 9. Continuity strategies

### 9.1 Manual fallback

Personnel use approved procedures, templates, scripts, and decision criteria without relying on the AI service.

### 9.2 Reduced-service mode

The organization disables higher-risk functionality and retains only approved low-risk capabilities.

### 9.3 Alternate provider

Traffic or workloads move to a previously assessed provider, model, or platform.

### 9.4 Internal capability

The organization operates an approved internal model, rules engine, knowledge base, or human workflow.

### 9.5 Static safe mode

The service provides verified information, approved notices, or escalation routes without generating new recommendations or decisions.

### 9.6 Queue and recover

Non-urgent work is held securely until the approved service is restored, with deadlines and traveler impact monitored.

## 10. Human decision rights

The exit plan must identify who may:

- declare an AI service degraded;
- restrict a feature or user group;
- suspend processing;
- activate manual fallback;
- switch providers or models;
- approve emergency changes;
- communicate with affected users;
- notify clients, authorities, or other stakeholders;
- accept temporary residual risk;
- approve restoration;
- terminate the service permanently.

Technical automation may detect conditions and recommend actions, but accountable humans must retain authority over material business, safety, rights, and compliance decisions.

## 11. Transition controls

A controlled transition should include:

1. approved exit decision and scope;
2. legal, privacy, security, accessibility, and operational review;
3. evidence preservation and legal-hold assessment;
4. data and configuration export;
5. export reconciliation and integrity testing;
6. target-environment validation;
7. parallel operation where appropriate;
8. human acceptance testing;
9. stakeholder communication;
10. cutover approval;
11. credential, key, connector, and access revocation;
12. vendor and subprocessor deletion confirmation;
13. post-transition monitoring;
14. closure approval and lessons learned.

## 12. Emergency continuity process

When continued use creates unacceptable risk:

1. detect and validate the condition;
2. preserve evidence;
3. restrict or suspend the affected function;
4. activate the approved fallback;
5. notify accountable owners;
6. protect affected people and urgent operations;
7. determine legal, contractual, regulatory, and client-notification duties;
8. evaluate replacement, repair, or permanent termination;
9. test any proposed restoration;
10. obtain human approval before resuming service.

Restoration must not occur solely because the vendor states that the issue is resolved.

## 13. Data retention and deletion

The exit plan must define:

- records that must be retained;
- retention periods and legal bases;
- records subject to deletion;
- secure transfer methods;
- backup treatment;
- log and telemetry treatment;
- subprocessor deletion;
- model-training or service-improvement use;
- evidence required to confirm deletion;
- exceptions caused by legal hold or mandatory retention.

Deletion certificates should identify the scope, systems, subprocessors, date, method, exceptions, and accountable signatory.

## 14. Knowledge transfer

Required knowledge transfer may include:

- architecture and data-flow documentation;
- integration specifications;
- API schemas;
- configuration and deployment records;
- known defects and workarounds;
- model limitations;
- operating procedures;
- monitoring and incident history;
- pending corrective actions;
- security and privacy controls;
- accessibility requirements;
- user-support procedures;
- contact and escalation information.

Knowledge transfer must be completed early enough to support safe transition, not after the departing provider has withdrawn support.

## 15. Exit testing

Critical AI services must undergo periodic exit or continuity exercises proportionate to risk.

Tests should verify:

- export completion;
- data reconciliation;
- configuration recovery;
- replacement compatibility;
- manual fallback capacity;
- service-level impacts;
- user and accessibility impacts;
- credential revocation;
- evidence preservation;
- restoration approval;
- communication procedures;
- recovery and transition timing.

Test results must produce corrective actions with owners and deadlines.

## 16. GlobalWay Travel Services example

GlobalWay uses a third-party AI service to prioritize travelers affected by flight cancellations and recommend rebooking options.

### AI may do

- identify affected itineraries;
- group travelers by operational urgency;
- suggest available alternatives;
- draft traveler communications;
- flag cases needing specialist review.

### Human decision

A travel-operations specialist decides which rebooking action is appropriate and whether the traveler communication may be sent.

### Exit scenario

The provider announces that the current model endpoint will be retired in 30 days. The replacement endpoint produces materially different rankings and weaker results for Spanish-language requests.

### Required response

GlobalWay:

- freezes unapproved migration;
- exports prompts, configurations, logs, evaluation results, and relevant records;
- tests the replacement and an alternate provider;
- activates approved manual prioritization for high-impact cases;
- validates Spanish-language performance and accessibility;
- informs affected client teams;
- obtains human approval before cutover.

### Stop and escalation

The automated workflow remains suspended when rankings cannot be explained sufficiently for operational review, language performance falls below approved thresholds, accessibility fails, traveler information cannot be protected, or fallback capacity is insufficient.

### Accountable owner

The VP of Traveler Operations owns the continuity decision. Technology, security, privacy, legal, accessibility, procurement, and vendor-risk teams retain their assigned responsibilities.

### Challenge, correction, and override

Travel specialists may disregard the AI ranking, use approved operational criteria, contact travelers directly, and route vulnerable or complex travelers for priority human handling.

## 17. Control activities

| Control ID | Control activity | Evidence |
|---|---|---|
| EUAI-EXIT-01 | Assess exit and portability before production approval | Exit-readiness assessment |
| EUAI-EXIT-02 | Define contractual export, assistance, deletion, and transition rights | Contract and responsibility schedule |
| EUAI-EXIT-03 | Maintain tested manual or technical fallback | Continuity plan and exercise results |
| EUAI-EXIT-04 | Preserve data, configurations, evidence, and audit records | Export and reconciliation records |
| EUAI-EXIT-05 | Control migration, cutover, and restoration through human approval | Change and approval records |
| EUAI-EXIT-06 | Revoke access and confirm vendor and subprocessor deletion | Revocation logs and deletion evidence |
| EUAI-EXIT-07 | Test critical exit plans periodically | Test reports and corrective actions |
| EUAI-EXIT-08 | Maintain replacement, portability, and concentration-risk options | Architecture and sourcing records |

## 18. Evidence requirements

Evidence should include:

- exit-readiness assessment;
- approved exit and continuity plan;
- data and configuration inventory;
- contractual portability and assistance terms;
- export specifications and test results;
- fallback procedures;
- replacement-provider assessment;
- human decision and approval records;
- transition schedule;
- stakeholder communications;
- access and credential revocation logs;
- deletion confirmations;
- exercise results;
- corrective-action records;
- closure report and lessons learned.

## 19. Audit test

Select a sample of critical third-party AI services.

For each sample:

1. Confirm an approved exit-readiness assessment exists.
2. Verify the plan identifies data, configurations, evidence, dependencies, owners, and decision rights.
3. Inspect contractual export, assistance, deletion, and transition provisions.
4. Review the most recent portability or continuity test.
5. Reconcile exported records to source records.
6. Confirm fallback operations are usable and adequately staffed.
7. Test whether accountable humans can restrict, suspend, migrate, and restore the service.
8. Verify access revocation and deletion processes.
9. Confirm unresolved test findings have owners and deadlines.
10. Determine whether the exit plan remains aligned with the current architecture, model, vendor, and risk classification.

## 20. Metrics

Suggested metrics:

- percentage of critical AI vendors with approved exit plans;
- percentage with tested portability in the last review cycle;
- percentage with tested manual or alternate-provider fallback;
- average time to export critical data and configurations;
- percentage of exports successfully reconciled;
- number of overdue exit-test findings;
- number of services without a viable replacement or fallback;
- average time to revoke vendor access;
- percentage of terminated services with complete deletion evidence;
- number of emergency suspensions and restorations;
- actual versus target recovery and transition times.

## 21. Management checklist

- [ ] Is exit readiness assessed before approval?
- [ ] Are data, configurations, evidence, and dependencies inventoried?
- [ ] Are exports usable outside the provider environment?
- [ ] Are manual or technical fallbacks tested?
- [ ] Are human decision rights explicit?
- [ ] Are migration and restoration separately approved?
- [ ] Can access be revoked promptly?
- [ ] Can deletion be verified across subprocessors and backups where applicable?
- [ ] Are replacement and concentration-risk options maintained?
- [ ] Are exit tests current and deficiencies tracked?

## 22. Graphic specification

### Figure 79-1 — AI Exit, Portability, and Continuity Lifecycle

Create an original formal process diagram showing:

**Prepare → Inventory → Export → Validate → Transition or Fallback → Revoke and Delete → Monitor → Close**

Include decision gates for:

- planned versus emergency exit;
- export completeness;
- fallback readiness;
- human cutover approval;
- deletion confirmation;
- human restoration approval.

Use restrained corporate colors, accessible contrast, clear directional flow, concise labels, and meaningful alt text. The figure must explain the control process and must not be decorative.

Suggested alt text:

“Lifecycle diagram showing preparation, inventory, export, validation, transition or fallback, access revocation and deletion, monitoring, and closure, with human approval gates for cutover and restoration.”

## 23. Key takeaway

An organization does not control an AI dependency unless it can leave it safely. Effective exit planning preserves data, evidence, operational capability, human authority, and protection for affected people throughout suspension, migration, replacement, and restoration.