# Chapter 72 — AI Contract Clauses and Allocation of Responsibilities

## 72.1 Purpose

AI contracts must convert legal, technical, operational, and governance duties into clear, testable responsibilities. They should identify who must do what, when evidence must be supplied, what happens when risk changes, and who has authority to stop or suspend use.

A contract may allocate work, information, and remedies between parties. It cannot remove statutory accountability or make an unlawful AI use lawful.

This chapter applies to contracts with AI providers, model providers, cloud and API vendors, data suppliers, system integrators, resellers, subcontractors, and other parties in the AI value chain.

## 72.2 Legal and governance foundation

The EU AI Act assigns duties according to the party's actual role and conduct. A distributor, importer, deployer, or other third party may become the provider of a high-risk AI system when it places its own name or trademark on the system, makes a substantial modification, or changes the intended purpose in a way that creates a high-risk system.

Contracts therefore must not rely on labels alone. The parties should document their actual activities and reassess roles when branding, intended purpose, technical architecture, model configuration, or system capabilities change.

For high-risk AI systems, the agreement should support:

- provider compliance and conformity-assessment duties;
- deployer access to clear instructions, limitations, and oversight measures;
- monitoring, incident escalation, suspension, and corrective action;
- access to technical documentation and evidence;
- importer, distributor, and authorised-representative cooperation;
- protection of intellectual property, confidential information, and trade secrets without blocking regulatory or audit obligations.

## 72.3 Contracting principle

**Responsibility follows control, conduct, and legal role—not merely the contract heading.**

GlobalWay must not accept wording stating that a supplier is “solely responsible for AI Act compliance” where GlobalWay controls deployment, input data, human oversight, monitoring, worker use, customer communication, or downstream modification.

## 72.4 Pre-contract role-allocation schedule

Every material AI agreement should include a role schedule covering at least:

| Topic | Provider responsibility | GlobalWay responsibility | Shared responsibility |
|---|---|---|---|
| Intended purpose | Define and document approved use | Use only within approved scope | Review changes |
| AI Act role | State provider and value-chain role | State deployer or other role | Reassess after change |
| Technical documentation | Prepare and maintain applicable records | Retain required downstream evidence | Provide to authorities when required |
| Instructions for use | Supply complete, clear, accessible instructions | Implement instructions and controls | Resolve ambiguities |
| Human oversight | Design effective oversight features | Appoint trained, authorised personnel | Test override and escalation |
| Monitoring | Maintain provider monitoring programme | Monitor operational use and outcomes | Exchange risk and incident data |
| Incidents | Investigate product-side causes | Detect and escalate use-side incidents | Coordinate reporting and corrective action |
| Data governance | Document model and training-data controls | Govern input and operational data | Address shared data risks |
| Transparency | Supply marking and disclosure capabilities | Configure and display required notices | Test continued operation |
| Accessibility | Support accessible design | Implement accessible user journeys | Remediate defects |
| Security | Protect product and model | Secure deployment and integrations | Coordinate vulnerabilities |
| Change control | Notify model and service changes | Assess configuration and use changes | Reclassify substantial modifications |

## 72.5 Mandatory clause families

### 72.5.1 Scope and intended purpose

The contract should define:

- approved use cases;
- prohibited uses;
- affected populations;
- deployment locations;
- system boundaries and integrations;
- permitted data categories;
- approved model and version;
- material assumptions and limitations;
- whether human review is mandatory before action.

Use outside the approved purpose should require documented reassessment and approval.

### 72.5.2 Role and responsibility clause

The parties should record their expected AI Act roles and acknowledge that the allocation must be reviewed when facts change. The clause should require prompt notice when a party:

- places its name or trademark on the system;
- materially modifies the system;
- changes the intended purpose;
- integrates the system into a new high-risk use;
- adds or replaces a model, major component, or data source;
- begins acting as importer, distributor, provider, or authorised representative.

### 72.5.3 Documentation and evidence clause

The supplier should provide evidence appropriate to the system and role, which may include:

- system description and intended purpose;
- architecture and component inventory;
- model and system cards;
- instructions for use;
- performance and limitation data;
- risk-management records;
- data-governance information;
- evaluation and testing results;
- human-oversight design;
- logging capabilities;
- cybersecurity controls;
- conformity, registration, and declaration records where applicable;
- post-market monitoring information;
- incident and corrective-action history;
- accessibility test results;
- subcontractor and dependency disclosures.

The contract should define delivery timing, update frequency, format, retention, confidentiality controls, and consequences for incomplete evidence.

### 72.5.4 Audit and verification rights

Audit rights should be risk-based and usable in practice. They may include:

- documentary review;
- independent assurance reports;
- control attestations;
- technical demonstrations;
- access to test environments;
- interviews with responsible personnel;
- targeted sampling;
- vulnerability and incident evidence;
- regulator-directed cooperation;
- additional review after material change or serious incident.

Trade-secret protections should be proportionate and should not prevent GlobalWay from obtaining evidence necessary for compliance, risk management, or regulatory cooperation.

### 72.5.5 Incident and risk-notification clause

The supplier should notify GlobalWay without undue delay of:

- serious incidents;
- material safety or fundamental-rights risks;
- significant performance degradation;
- security vulnerabilities or exploitation;
- data leakage or unauthorised model access;
- prohibited or unexpected model behaviour;
- regulator inquiries affecting the service;
- loss, suspension, or restriction of conformity status;
- defects in transparency, marking, logging, or oversight features.

The clause should define severity levels, initial notification deadlines, required facts, update cadence, evidence preservation, root-cause analysis, corrective action, and closure approval.

### 72.5.6 Change-management clause

The supplier should give advance notice of changes that may affect risk, classification, compliance, or performance, including:

- model replacement or version change;
- retraining or fine-tuning;
- safety-filter changes;
- new features or autonomous functions;
- revised intended purpose;
- material changes to training or input data;
- new subprocessors or cloud locations;
- changes to logging, monitoring, transparency, or human oversight;
- major architectural or security changes;
- retirement of a model, API, or service.

GlobalWay should retain the right to test, reject, delay, restrict, or suspend a change pending reassessment.

### 72.5.7 Data-use and confidentiality clause

The contract should address:

- ownership and permitted use of input, output, feedback, and telemetry;
- whether GlobalWay data may be used for training or model improvement;
- retention and deletion;
- cross-border transfers;
- special-category and sensitive data;
- data minimisation;
- confidentiality and trade secrets;
- access controls;
- segregation of customer data;
- evidence of deletion and return;
- use of synthetic or derived data.

Supplier rights to reuse GlobalWay data should be explicit, limited, and separately approved.

### 72.5.8 Human-oversight clause

The supplier should provide capabilities and information necessary for effective human oversight, including:

- meaningful status and confidence information where appropriate;
- limitations and foreseeable misuse;
- override, stop, and escalation functions;
- logs supporting review;
- training materials;
- known automation-bias risks;
- safe fallback modes;
- support for challenge and correction.

GlobalWay remains responsible for appointing competent, trained, authorised, and supported personnel where it acts as deployer.

### 72.5.9 Transparency and accessibility clause

The supplier should support required disclosures, content marking, notices, and user information. The contract should require:

- configurable notices;
- persistent or appropriately timed disclosure;
- accessible text and interface components;
- compatibility with assistive technology;
- language and localisation support;
- retention of notice and marking evidence;
- regression testing after updates.

### 72.5.10 Security and resilience clause

Required terms may include:

- secure development and vulnerability management;
- threat modelling;
- prompt-injection and model-manipulation controls;
- data-poisoning controls;
- model and credential protection;
- logging and forensic support;
- incident response;
- backup, recovery, and continuity;
- service-level commitments;
- emergency suspension and safe shutdown;
- notification of critical dependencies.

### 72.5.11 Subcontractor and dependency clause

The supplier should disclose material subprocessors, model providers, datasets, plugins, APIs, and cloud dependencies. GlobalWay should receive notice of material additions or changes and retain risk-based objection, testing, restriction, or termination rights.

Flow-down terms should require subcontractors to support the supplier’s contractual and regulatory obligations.

### 72.5.12 Regulatory cooperation clause

The parties should cooperate with competent authorities and preserve evidence required for inquiries, market-surveillance actions, investigations, corrective measures, and incident reporting.

The clause should define:

- responsible contacts;
- response timelines;
- approval and communication protocol;
- access to documents and knowledgeable personnel;
- preservation and legal hold;
- confidentiality and privilege handling;
- cost allocation where appropriate.

### 72.5.13 Suspension, termination, and exit clause

GlobalWay should be able to suspend or terminate use where:

- the system may be prohibited or non-compliant;
- serious risk cannot be controlled;
- evidence is withheld or unreliable;
- required documentation or conformity status is lost;
- a serious incident remains unresolved;
- security or privacy risk is unacceptable;
- an unapproved material change occurs;
- human oversight or transparency controls fail.

Exit provisions should address data return and deletion, transition support, model and configuration portability, continuity, replacement, records retention, and preservation of audit evidence.

## 72.6 GlobalWay example

GlobalWay contracts with an AI supplier for automated itinerary recommendations. The supplier provides the base model, API, safety controls, performance documentation, and model-change notices. GlobalWay configures the service, supplies traveller preferences, determines where recommendations appear, and requires travel-consultant review for high-risk disruptions.

The contract states that:

- the approved purpose is recommendation support, not autonomous booking during safety-critical disruptions;
- the supplier must provide model limitations, test evidence, incident notices, and 60 days' advance notice of material model changes where practicable;
- GlobalWay may suspend a model version that fails safety, accessibility, transparency, or security testing;
- both parties must investigate serious incidents and preserve relevant logs;
- GlobalWay must maintain trained human oversight and monitor operational use;
- any new autonomous-booking function requires role, risk, and substantial-modification reassessment before use.

## 72.7 Contract approval workflow

1. Identify system, use case, parties, and dependencies.
2. Determine expected legal and AI Act roles.
3. Assign risk tier.
4. Complete vendor due diligence.
5. Build the responsibility schedule.
6. Select required clause families.
7. Resolve evidence, audit, incident, change, and exit rights.
8. Obtain legal, privacy, security, accessibility, procurement, and business approval.
9. Record residual risks and exceptions.
10. Execute the agreement.
11. Monitor obligations, changes, incidents, and evidence.
12. Reassess on renewal or material change.

## 72.8 Control library

| Control ID | Control objective | Control activity | Owner | Evidence | Frequency |
|---|---|---|---|---|---|
| EUAI-CON-01 | Allocate AI responsibilities | Maintain a role and responsibility schedule | Legal / AI Governance | Approved schedule | Contract and change |
| EUAI-CON-02 | Obtain required evidence | Define evidence deliverables and update duties | Procurement / Risk | Contract, evidence index | Contract and annual |
| EUAI-CON-03 | Preserve auditability | Include usable audit and verification rights | Legal / Internal Audit | Executed clauses | Contract |
| EUAI-CON-04 | Manage incidents | Define notification, investigation, and cooperation | Security / Legal | Incident clauses, tests | Contract and exercise |
| EUAI-CON-05 | Control material changes | Require notice, reassessment, and approval | Product / AI Governance | Change notices, decisions | Each change |
| EUAI-CON-06 | Protect data | Restrict data use, retention, and reuse | Privacy / Legal | Data schedule | Contract and annual |
| EUAI-CON-07 | Support oversight and transparency | Contract for required features and evidence | Product / Accessibility | Requirements, test results | Release and change |
| EUAI-CON-08 | Enable safe exit | Maintain suspension, termination, portability, and continuity rights | Procurement / Operations | Exit plan, test | Annual |

## 72.9 Evidence register

Minimum evidence should include:

- executed contract and schedules;
- role-assessment worksheet;
- due-diligence report;
- approved deviations and residual-risk acceptance;
- documentation and evidence index;
- audit and assurance records;
- incident-notification tests;
- model-change notices and approvals;
- subcontractor inventory;
- data-use and deletion records;
- renewal and exit assessments.

## 72.10 Audit tests

Auditors should:

1. Select a risk-based sample of AI contracts.
2. Verify that actual party activities match the documented role allocation.
3. Confirm that required clause families are present or that approved exceptions exist.
4. Test whether evidence deliverables were received, current, and usable.
5. Inspect model-change records and confirm reassessment occurred.
6. Review incidents and determine whether contractual notification and cooperation operated effectively.
7. Confirm audit rights are practical and not nullified by restrictive confidentiality terms.
8. Verify that data-use, training, retention, deletion, and subcontractor terms match actual practice.
9. Test suspension, exit, continuity, and evidence-preservation arrangements.
10. Report gaps where contracts allocate responsibility but operational controls do not implement it.

## 72.11 Metrics

- percentage of material AI contracts with an approved role schedule;
- percentage with complete evidence and audit clauses;
- overdue supplier evidence items;
- material changes received without required advance notice;
- incidents reported within contractual deadlines;
- unresolved high-risk contract exceptions;
- suppliers lacking tested exit plans;
- contracts with unapproved data-reuse rights.

## 72.12 Stop and escalation conditions

Do not execute, renew, or continue the arrangement where:

- roles and intended purpose are materially unclear;
- the supplier refuses necessary documentation or evidence;
- audit or regulatory-cooperation rights are unusable;
- incident or change-notification duties are absent for a material-risk system;
- GlobalWay data may be reused for training without explicit approval;
- required human-oversight, transparency, accessibility, or security capabilities are missing;
- the exit plan is not feasible for a critical service;
- contractual wording conflicts with the parties' actual legal roles.

Escalate to Legal, AI Governance, Security, Privacy, Accessibility, Procurement, and the accountable business executive.

## 72.13 Figure specification

### Figure 72-1 — AI Contract Responsibility and Escalation Map

A professional process diagram showing:

**AI supplier and upstream dependencies** → **contractual responsibility schedule** → **GlobalWay deployment controls** → **monitoring and evidence exchange** → **incident/change escalation** → **regulatory cooperation and corrective action**.

Each stage identifies the accountable party, shared obligations, required evidence, and stop authority.

**Alt text:** Diagram showing how AI responsibilities, evidence, monitoring, incident escalation, and regulatory cooperation flow between a supplier, GlobalWay, upstream dependencies, and authorities.

## 72.14 Key message

A strong AI contract does not merely transfer risk. It makes responsibilities operational, evidence available, changes visible, incidents actionable, and safe exit possible.