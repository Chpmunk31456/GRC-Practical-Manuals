# Chapter 71 — AI Vendor Due Diligence and Contractual Assurance

## 71.1 Purpose

This chapter provides a practical governance, risk, compliance, control, evidence, and audit model for selecting, contracting with, onboarding, monitoring, changing, and exiting third-party AI providers.

The objective is not merely to collect questionnaires. The objective is to determine whether the organisation understands the AI service, its role under the EU AI Act, the risks introduced across the value chain, the evidence available to support compliance, and the contractual rights needed to control the relationship.

> **Core principle:** A vendor may supply the technology, but the organisation retains responsibility for the decisions it makes, the way it deploys the system, and the risks it accepts.

---

## 71.2 Regulatory context

The EU AI Act allocates responsibilities across providers, deployers, importers, distributors, authorised representatives, product manufacturers, and other third parties. Article 25 addresses responsibilities along the AI value chain and identifies circumstances in which a deployer, distributor, importer, or other third party may become a provider of a high-risk AI system—for example, by placing its own name on the system or making a substantial modification.

Vendor contracts may allocate work, evidence delivery, support, notification, and cooperation duties, but they cannot erase statutory responsibility.

### Plain-language explanation

A contract can say who must do what. It cannot make a legal obligation disappear.

### GlobalWay Travel Services example

GlobalWay licenses an AI system that scores applicants for travel-service roles. The vendor markets the model under its own name, but GlobalWay changes the scoring logic, adds new behavioural features, and uses the outputs to decide who advances to interview.

GlobalWay must assess whether those changes alter its role, create a substantial modification, or cause it to assume provider obligations. Procurement cannot treat the system as an ordinary software subscription.

---

## 71.3 Scope

This chapter applies to:

- AI software and hosted AI services;
- general-purpose AI models and model-enabled applications;
- embedded AI features in travel, HR, fraud, customer-service, pricing, analytics, and security platforms;
- AI APIs, agents, copilots, recommendation engines, classifiers, and decision-support tools;
- subcontractors, subprocessors, model providers, data providers, hosting providers, and specialist AI consultants;
- open-source or freely available components integrated into organisational systems;
- material updates, model changes, retraining, fine-tuning, feature expansion, and changes in intended purpose.

---

## 71.4 Vendor-risk classification

GlobalWay shall classify each AI vendor engagement before procurement approval.

| Tier | Description | Minimum treatment |
|---|---|---|
| Tier 1 | High-risk, prohibited-practice-sensitive, employment, biometrics, critical safety, or fundamental-rights impact | Enhanced due diligence, legal review, technical testing, executive approval, contract controls, continuous monitoring |
| Tier 2 | Material customer, traveller, fraud, pricing, recommendation, or operational impact | Standard enhanced review, evidence validation, contract controls, periodic monitoring |
| Tier 3 | Low-impact productivity or internal support with no material decision authority | Proportionate review, approved-use restrictions, basic security/privacy and transparency controls |
| Tier 4 | Experimental or sandbox use with synthetic/non-sensitive data and no production impact | Time-limited approval, restricted environment, no operational reliance |

Classification shall consider:

- intended and reasonably foreseeable use;
- affected persons;
- autonomy and decision influence;
- sensitive or personal data;
- model opacity;
- jurisdiction and regulatory exposure;
- ability to challenge, override, or correct outputs;
- dependency and concentration risk;
- vendor and subcontractor maturity;
- exit feasibility.

---

## 71.5 Pre-contract due diligence

### 71.5.1 Corporate and governance review

Confirm:

- legal entity, ownership, operating locations, and financial stability;
- AI governance structure and accountable executives;
- regulatory history, material complaints, litigation, and enforcement;
- policies covering AI risk, privacy, security, accessibility, human oversight, incident management, and responsible use;
- subcontractor and fourth-party governance;
- insurance relevant to cyber, technology, professional, and AI-related claims.

### 71.5.2 System and model transparency

Require sufficient information to understand:

- intended purpose and prohibited uses;
- model or system type;
- provider and downstream actor roles;
- training, validation, and testing approach;
- known limitations and failure modes;
- accuracy, robustness, cybersecurity, and bias testing;
- data sources and provenance at an appropriate level;
- model update and change process;
- logging and traceability capabilities;
- explainability and user-instruction materials;
- human-oversight design;
- content marking and transparency functions where applicable.

Trade secrets may justify controlled disclosure mechanisms, but not a complete absence of compliance evidence.

### 71.5.3 Legal and regulatory review

Assess:

- EU AI Act role and risk classification;
- GDPR controller, processor, joint-controller, or independent-controller status;
- international transfers;
- sector-specific employment, consumer, travel, accessibility, safety, and anti-discrimination duties;
- intellectual-property and training-data risks;
- use of customer or organisational data for vendor model improvement;
- record-retention and regulatory-cooperation obligations.

### 71.5.4 Security and resilience review

Review:

- secure development and vulnerability management;
- identity and access management;
- encryption and key management;
- tenant isolation;
- logging and monitoring;
- adversarial testing and abuse prevention;
- prompt-injection and data-exfiltration controls;
- incident response and notification;
- business continuity and disaster recovery;
- model, API, hosting, and geographic concentration risk;
- service-level commitments and recovery objectives.

### 71.5.5 Accessibility and human-impact review

Require evidence that the service supports:

- accessible interfaces and notices;
- keyboard navigation and assistive technology;
- captions, transcripts, and text alternatives;
- accessible human escalation;
- understandable explanations;
- accommodation and correction channels;
- testing with diverse users where the use case may affect rights or access to services.

---

## 71.6 AI vendor questionnaire

The procurement record should include answers and supporting evidence for at least the following areas:

1. Product identity and intended purpose.
2. EU AI Act actor role.
3. Risk classification and prohibited-practice screening.
4. Model and system architecture.
5. Data sources, provenance, quality, and lawful use.
6. Testing for accuracy, bias, robustness, cybersecurity, and accessibility.
7. Human oversight and override.
8. Logging, traceability, and evidence export.
9. Transparency notices and AI-generated-content marking.
10. Incident and serious-incident notification.
11. Model updates, retraining, and substantial modifications.
12. Subprocessors, model providers, hosting providers, and other fourth parties.
13. Data retention, deletion, and model-training use.
14. Audit rights and regulatory cooperation.
15. Exit, portability, deletion, and continuity.

Answers without evidence shall be treated as assertions, not verified controls.

---

## 71.7 Contractual control requirements

Contracts shall be proportionate to the risk tier and should address the following.

### 71.7.1 Role and responsibility allocation

The contract shall identify:

- each party's intended EU AI Act role;
- who performs conformity, documentation, monitoring, and notification activities;
- responsibility for instructions for use;
- responsibility for data, configuration, prompts, fine-tuning, and substantial modifications;
- change-control triggers that require reassessment.

### 71.7.2 Evidence and documentation

Require access to evidence needed for compliance, including as applicable:

- technical documentation;
- instructions for use;
- declarations, registrations, certificates, and conformity evidence;
- testing reports;
- logs and event records;
- model and version information;
- known limitations;
- audit reports and remediation status;
- post-market monitoring information.

### 71.7.3 Change notification

The vendor shall provide advance notice of material changes, including:

- model replacement;
- substantial modification;
- new training or fine-tuning methods;
- material data-source changes;
- changed subprocessors or hosting locations;
- reduced functionality or control coverage;
- changed intended purpose, restrictions, or known limitations;
- regulatory classification changes.

GlobalWay shall have the right to suspend use pending reassessment.

### 71.7.4 Incident notification

Specify notification periods and escalation paths for:

- security incidents;
- personal-data breaches;
- harmful or discriminatory outputs;
- material accuracy failures;
- transparency failures;
- loss of logs or traceability;
- regulatory inquiries;
- suspected serious incidents;
- falsified or invalid conformity documentation.

### 71.7.5 Audit and cooperation rights

GlobalWay should obtain rights to:

- receive independent assurance reports;
- request control evidence;
- perform or commission proportionate audits;
- test agreed controls;
- review subcontractor arrangements;
- require remediation plans;
- cooperate with competent authorities;
- preserve relevant records and evidence.

### 71.7.6 Data use and model improvement

The contract shall state clearly whether the vendor may use:

- prompts;
- traveller data;
- employee data;
- customer communications;
- uploaded documents;
- outputs and feedback;
- operational logs;

for training, fine-tuning, benchmarking, product improvement, or other secondary purposes.

Default silence is not acceptable for material or sensitive data.

### 71.7.7 Human oversight and service continuity

Require:

- human override and escalation capability;
- documented fallback procedures;
- support during material failures;
- export of records needed to reconstruct decisions;
- continuity arrangements for service interruption or vendor exit.

### 71.7.8 Termination and exit

Include rights addressing:

- immediate suspension for prohibited or materially unsafe use;
- termination for regulatory nonconformity;
- data return and deletion;
- model and configuration portability where feasible;
- evidence retention;
- transition support;
- certification of deletion;
- continued cooperation for incidents discovered after termination.

---

## 71.8 Ongoing monitoring

Vendor approval is not permanent.

GlobalWay shall monitor:

- changes in model or system versions;
- incidents and complaints;
- performance and error rates;
- bias and accessibility findings;
- regulatory developments;
- security posture;
- subcontractor changes;
- audit findings and remediation;
- dependency and concentration risk;
- business continuity performance;
- changes in organisational use.

High-risk and material vendors shall be reviewed at least annually and after significant changes or incidents.

---

## 71.9 Stop and escalation conditions

Use shall be stopped or restricted when:

- prohibited-practice screening fails;
- the vendor cannot establish its identity or regulatory role;
- required conformity or technical documentation is missing or unreliable;
- evidence appears falsified;
- the system materially departs from its instructions for use;
- an unauthorised substantial modification occurs;
- serious bias, safety, privacy, security, or accessibility failures remain unmitigated;
- essential logs or human-oversight functions are unavailable;
- the vendor refuses required cooperation;
- regulatory classification becomes uncertain and the risk cannot be controlled.

The accountable owner—not the vendor—decides whether organisational use may continue.

---

## 71.10 GlobalWay case study

### Scenario

GlobalWay plans to procure an AI itinerary-optimisation service that combines traveller profiles, corporate travel policy, real-time disruption data, and supplier pricing.

### AI may do

- identify compliant itinerary options;
- rank alternatives;
- flag disruption risks;
- draft traveller communications.

### Human decision

A travel counsellor or authorised traveller selects or approves the itinerary where material cost, accessibility, safety, or policy exceptions exist.

### Required controls

- vendor role and value-chain assessment;
- privacy and international-transfer review;
- accessibility and accommodation testing;
- pricing and recommendation-bias testing;
- human override;
- change notification;
- incident reporting;
- evidence export;
- exit and continuity plan.

### Evidence

- completed due-diligence questionnaire;
- risk classification;
- contract-control matrix;
- testing reports;
- approved data-flow diagram;
- human-oversight plan;
- model/version register;
- monitoring dashboard;
- annual review record.

### Audit test

Select a sample of vendor-assisted bookings and verify that:

- the approved model version was used;
- applicable travel-policy and accessibility requirements were respected;
- material exceptions received human approval;
- the recommendation rationale and override were logged;
- traveller data was handled according to contract;
- relevant incidents and complaints were investigated.

---

## 71.11 Control library

| Control ID | Control objective | Control activity | Owner | Frequency | Evidence |
|---|---|---|---|---|---|
| AI-TPRM-01 | Identify regulatory roles | Document provider, deployer, importer, distributor, and other relevant roles | Legal / AI Governance | Before approval and on change | Role assessment |
| AI-TPRM-02 | Classify vendor risk | Apply AI vendor tiering and prohibited-practice screening | Procurement / AI Risk | Before procurement | Risk classification |
| AI-TPRM-03 | Verify vendor claims | Require evidence for material questionnaire responses | Procurement / Control Owners | Before approval | Evidence register |
| AI-TPRM-04 | Secure contractual rights | Execute approved AI contract clauses | Legal / Procurement | Before production use | Signed contract and clause matrix |
| AI-TPRM-05 | Control material changes | Review vendor and model changes before continued use | System Owner / Change Advisory | On change | Change assessment |
| AI-TPRM-06 | Monitor performance and incidents | Review vendor metrics, complaints, incidents, and audit findings | System Owner / TPRM | Quarterly or risk-based | Monitoring records |
| AI-TPRM-07 | Preserve exit capability | Maintain tested suspension, fallback, portability, and deletion procedures | Business Owner / IT | Annually | Exit test and continuity plan |

---

## 71.12 Metrics

Recommended measures include:

- percentage of AI vendors with completed role assessments;
- percentage with verified evidence rather than unsupported assertions;
- percentage of Tier 1 and Tier 2 contracts containing required AI clauses;
- overdue vendor findings;
- unreviewed model or subprocessor changes;
- incidents reported within contractual timelines;
- systems without tested fallback or exit procedures;
- concentration of critical services by model, provider, cloud, or region;
- percentage of vendor systems with current accessibility and bias testing.

Metrics should reveal uncontrolled dependency, not merely count completed questionnaires.

---

## 71.13 Audit programme

Auditors should:

1. Reconcile the AI inventory to the vendor and contract registers.
2. Sample vendors across risk tiers.
3. Verify role assessments and risk classification.
4. Inspect evidence supporting questionnaire responses.
5. Confirm required contract clauses are executed.
6. Test change-notification and reassessment records.
7. Review incidents, complaints, and remediation.
8. Verify human oversight and fallback capability.
9. Confirm data-use restrictions and deletion evidence.
10. Test exit and continuity readiness.

A completed questionnaire without evidence, contract rights, monitoring, and enforceable remediation should not be rated effective.

---

## 71.14 Figure specification

### Figure 71-1 — AI Third-Party Risk and Contract Assurance Lifecycle

**Type:** Formal process diagram.

**Flow:**

1. Identify AI service and vendor chain
2. Classify role, use case, and risk
3. Perform legal, technical, privacy, security, accessibility, and human-impact due diligence
4. Validate evidence
5. Negotiate contract controls
6. Approve, restrict, reject, or sandbox
7. Monitor performance, incidents, changes, and subcontractors
8. Reassess on material change
9. Suspend, remediate, renew, or exit

**Control gates:**

- prohibited-practice screen;
- high-risk classification;
- provider-role or substantial-modification trigger;
- evidence sufficiency;
- contract-rights sufficiency;
- exit feasibility.

**Caption:** Vendor assurance is a lifecycle. Procurement approval is only the beginning.

**Alt text:** A nine-stage circular workflow showing identification, classification, due diligence, evidence validation, contracting, approval, monitoring, reassessment, and exit, with legal and control gates placed before deployment and after material changes.

---

## 71.15 Key takeaways

- AI procurement is a regulatory and operational-risk decision, not only a commercial purchase.
- Actor roles and responsibilities must be assessed explicitly.
- Contracts allocate duties but do not remove legal accountability.
- Vendor statements require evidence.
- Material changes can alter risk classification and legal roles.
- Human oversight, incident rights, audit access, data-use restrictions, and exit capability are essential.
- Continuous monitoring is required because vendors, models, subprocessors, and uses change.

---

## 71.16 Authoritative sources

- Regulation (EU) 2024/1689, including Articles 16, 23–26, 43, 47, 72, 73, and 79, as applicable.
- European Commission and EU AI Office implementation materials.
- Applicable GDPR, cybersecurity, accessibility, employment, consumer-protection, and sector-specific requirements.

**Source-status rule:** Confirm current legal text, enacted amendments, applicable dates, and official guidance before operational use. Clearly distinguish binding law from guidance, codes, standards, contractual practice, and recommended controls.
