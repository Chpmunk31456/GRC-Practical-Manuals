# 71. AI Vendor Due Diligence

## 71.1 Purpose

Organizations frequently acquire AI capability through cloud services, embedded software, application programming interfaces, general-purpose AI models, managed services, and specialist vendors. Outsourcing the technology does not outsource accountability.

Before GlobalWay Travel Services approves an external AI product or service, it must understand:

- what the system does;
- how it is built, hosted, changed, and monitored;
- which legal role each party performs;
- which people, rights, and business processes may be affected;
- what evidence the supplier can provide;
- whether the risks can be controlled throughout the relationship.

This chapter establishes a risk-based vendor due-diligence process. Chapter 72 addresses contractual clauses after the applicable responsibilities and risks are understood.

## 71.2 Core principle

> Buy evidence, not promises.

A polished demonstration, marketing claim, certification badge, or generic security statement is not sufficient evidence that an AI system is lawful, safe, secure, accessible, accurate, or suitable for the intended purpose.

Approval must be based on documented facts, testing, accountable decisions, and enforceable follow-up actions.

## 71.3 Regulatory context

The EU AI Act assigns obligations according to the role performed in the AI value chain. A customer may normally act as a deployer, but a distributor, importer, deployer, or other third party may become the provider of a high-risk AI system when it:

- places its own name or trademark on the system;
- makes a substantial modification while the system remains high-risk; or
- changes the intended purpose so that a system becomes high-risk.

Contractual arrangements may allocate operational responsibilities, but they do not eliminate statutory accountability.

Vendor review must therefore determine:

- the system, model, service, and deployment architecture;
- the intended purpose and reasonably foreseeable misuse;
- whether GlobalWay acts as deployer, provider, importer, distributor, product manufacturer, or another regulated actor;
- whether the supplier relies on subcontractors, cloud providers, model providers, data brokers, or open-source components;
- whether fine-tuning, retrieval augmentation, integration, branding, or workflow redesign could alter the legal role or risk classification;
- which evidence must remain available for authorities, auditors, affected persons, and internal oversight.

## 71.4 Scope

The process applies before acquisition, renewal, material expansion, or substantial change involving:

- standalone AI systems;
- AI embedded in software-as-a-service products;
- general-purpose AI models;
- generative-AI assistants and copilots;
- recommendation, ranking, pricing, fraud, safety, recruitment, or performance systems;
- biometric or emotion-related functionality;
- cloud AI services and model APIs;
- open-source models or components supported by a commercial supplier;
- professional services that configure, fine-tune, evaluate, or operate AI.

## 71.5 Due-diligence tiers

| Tier | Typical risk | GlobalWay example | Minimum review |
|---|---|---|---|
| Tier 1 — Limited | Low-impact internal assistance with no sensitive data or consequential decision | Internal drafting assistant using approved public material | Business, privacy, security, and acceptable-use review |
| Tier 2 — Moderate | Customer-facing or operational system with limited decision impact | Itinerary recommendation engine | Full functional, privacy, security, accessibility, transparency, and vendor review |
| Tier 3 — Elevated | Sensitive data, safety, fraud, pricing, employment, or material customer impact | Fraud-detection or travel-risk alert platform | Enhanced legal, technical, human-rights, bias, resilience, and executive review |
| Tier 4 — High-risk or prohibited-practice concern | Potential Annex III high-risk use, biometric use, employment decision, or Article 5 concern | Recruitment-screening system or emotion-recognition tool | Formal legal classification, prohibited-practice screening, high-risk readiness, independent testing, and senior approval |

Tiering must reflect the intended use, not merely the supplier’s product category.

## 71.6 Due-diligence workflow

### Step 1 — Define the proposed use

Document:

- business purpose;
- users and affected persons;
- decisions or recommendations produced;
- data inputs and outputs;
- jurisdictions;
- integrations;
- human oversight;
- expected benefits;
- potential harms;
- alternatives, including a non-AI option.

A vendor must not be assessed only against its generic capabilities. The same product may present very different risks when used for itinerary drafting, fraud scoring, recruitment, or employee monitoring.

### Step 2 — Determine the legal and operational roles

Identify each party’s role across the lifecycle:

- model provider;
- AI-system provider;
- deployer;
- importer;
- distributor;
- authorised representative;
- product manufacturer;
- data controller or processor;
- subprocessor;
- hosting provider;
- systems integrator.

Record the basis for each conclusion and reassess it when branding, intended purpose, model configuration, or integration changes.

### Step 3 — Classify the AI use

Complete:

- AI Act applicability assessment;
- prohibited-practice screening;
- high-risk classification;
- transparency-obligation assessment;
- GPAI dependency assessment;
- privacy and automated-decision assessment;
- fundamental-rights and accessibility screening;
- sector-specific legal review.

### Step 4 — Request evidence

Evidence must be proportionate to risk and may include:

- system and model documentation;
- intended-purpose and limitation statements;
- architecture and data-flow diagrams;
- training, testing, and evaluation summaries;
- accuracy, robustness, bias, and accessibility results;
- cybersecurity programme evidence;
- privacy and data-governance documentation;
- human-oversight instructions;
- logging and monitoring capabilities;
- incident history;
- change-management procedures;
- subcontractor and dependency inventory;
- conformity, registration, or declaration evidence where applicable;
- business-continuity and exit documentation.

### Step 5 — Validate, do not merely collect

The review team must assess whether evidence is:

- current;
- relevant to the proposed configuration and intended use;
- complete enough to support the stated claim;
- independently verifiable where appropriate;
- consistent across technical, legal, security, privacy, and product materials;
- subject to reliable change control.

A generic report for a different model version, region, deployment mode, or use case must not be accepted without documented justification.

### Step 6 — Test the system

Testing should cover, as applicable:

- functional accuracy;
- hallucination and unsupported-claim risk;
- harmful or discriminatory outputs;
- privacy leakage;
- prompt injection and misuse;
- security controls;
- human override and escalation;
- accessibility;
- language and cultural performance;
- failure modes and degraded operation;
- logging and auditability;
- vendor-imposed limits that affect compliance.

### Step 7 — Decide and record conditions

The decision must be one of:

- approve;
- approve with conditions;
- pilot in a restricted environment;
- defer pending evidence or remediation;
- reject;
- escalate for legal, executive, or ethics review.

Conditions must have owners, deadlines, evidence requirements, and consequences for non-completion.

## 71.7 AI vendor questionnaire

### Corporate and service information

1. What legal entity provides the service?
2. Which countries host, support, or access the service?
3. Which subcontractors and model providers are involved?
4. Which exact product, model, and version will GlobalWay use?
5. What is the intended purpose and what uses are prohibited or unsupported?

### AI Act and role information

6. Which AI Act role does the vendor believe it performs, and why?
7. Has the system been classified under the AI Act?
8. Could the system become high-risk in any supported use case?
9. What changes could constitute a substantial modification?
10. What downstream documentation is supplied to integrators and deployers?

### Data and privacy

11. What data is collected, generated, retained, or inferred?
12. Is customer data used for training, tuning, evaluation, or service improvement?
13. Can such use be disabled contractually and technically?
14. What deletion, correction, export, and retention controls exist?
15. How are special-category, biometric, children’s, employee, or traveler data handled?

### Accuracy, bias, and human impact

16. How are accuracy and reliability measured for the proposed use?
17. What limitations, confidence measures, and known failure modes are documented?
18. Which demographic, language, accessibility, and regional tests have been performed?
19. How are harmful patterns, bias, and disparate impact monitored and corrected?
20. What human-review, override, challenge, and appeal capabilities are supported?

### Security and resilience

21. What secure-development, threat-modeling, vulnerability-management, and incident-response practices apply?
22. How does the vendor address prompt injection, data poisoning, model extraction, insecure plugins, and dependency risk?
23. What logs are available to GlobalWay?
24. What availability, recovery, backup, and continuity controls exist?
25. How and when will GlobalWay be notified of incidents and vulnerabilities?

### Change management and assurance

26. How are model, dataset, policy, interface, and dependency changes communicated?
27. Can GlobalWay delay or reject material changes?
28. What assurance reports, certifications, test results, or regulatory evidence are available?
29. What audit and information rights are supported?
30. What export, transition, and deletion assistance is available at termination?

## 71.8 Evidence-quality rules

| Claim | Weak evidence | Stronger evidence |
|---|---|---|
| “The model is unbiased” | Marketing statement | Defined metrics, datasets, subgroup results, limitations, remediation records, and independent review |
| “Customer data is not used for training” | Sales email | Contract term, technical setting, data-flow evidence, and audit right |
| “The system is secure” | Certification logo | Scope-matched report, penetration results, vulnerability process, architecture evidence, and incident terms |
| “Human oversight is available” | General product description | Tested workflow, trained reviewer, override logs, escalation times, and stop authority |
| “The service is accessible” | Conformance claim | Current accessibility report, assistive-technology tests, defect register, remediation evidence, and user testing |

## 71.9 GlobalWay example — itinerary optimisation platform

### Requirement

GlobalWay must assess a vendor’s itinerary-optimisation platform before allowing it to recommend flight, hotel, and ground-transport combinations to corporate travelers.

### Plain-language explanation

The product may appear to offer convenient suggestions, but its ranking logic could disadvantage travelers with disabilities, ignore client policy, expose personal data, or prioritize supplier incentives over traveler needs.

### Control activity

The procurement owner, AI governance team, privacy officer, security team, accessibility lead, and traveler-experience owner complete a Tier 2 review. They test:

- accessible travel preferences;
- explainability of recommendations;
- prohibited and unsupported routing;
- personal-data use;
- supplier-bias risk;
- human-agent escalation;
- model and ranking changes;
- record retention.

### Evidence

- approved use-case intake;
- role and classification assessment;
- completed questionnaire;
- data-flow diagram;
- test scripts and results;
- accessibility findings;
- security and privacy review;
- supplier-dependency list;
- conditional approval record;
- remediation tracker.

### Audit test

Select the vendor file and confirm that the review addressed the actual configuration and use. Inspect evidence supporting key claims, trace unresolved risks to approval conditions, and confirm that no production use occurred before required approvals.

## 71.10 Stop and escalation conditions

GlobalWay must pause or reject procurement when:

- the intended use may be prohibited;
- high-risk classification cannot be resolved;
- the vendor refuses to identify material subcontractors or model dependencies;
- evidence is materially inconsistent, obsolete, or unrelated to the proposed use;
- customer data use cannot be controlled;
- critical security, privacy, bias, accessibility, or human-oversight defects remain unresolved;
- required logs, documentation, incident notification, or change visibility are unavailable;
- the vendor cannot support regulatory or audit requests;
- exit would create unacceptable operational or data risk.

## 71.11 Control library

| Control ID | Control objective | Owner | Frequency | Evidence |
|---|---|---|---|---|
| EUAI-TPRM-01 | Inventory all external AI products, models, and dependencies | AI Governance | Continuous | Vendor inventory, architecture records |
| EUAI-TPRM-02 | Assign risk tier before procurement or material change | Business Owner | Per event | Tiering record, rationale |
| EUAI-TPRM-03 | Determine AI Act and data-protection roles | Legal and Privacy | Per event | Role assessment, legal review |
| EUAI-TPRM-04 | Obtain and validate proportionate supplier evidence | Procurement and Assurance | Per event and annual | Questionnaire, evidence index, review notes |
| EUAI-TPRM-05 | Independently test higher-risk systems | Technical Assurance | Before use and after material change | Test plan, results, defects |
| EUAI-TPRM-06 | Track conditions and unresolved findings | Risk Owner | Monthly until closure | Remediation plan, status reports |
| EUAI-TPRM-07 | Reassess vendors after material changes or incidents | Vendor Manager | Event-driven | Change notices, reassessment |

## 71.12 Metrics

Useful measures include:

- percentage of AI vendors with completed risk tiering;
- percentage with documented role assessments;
- overdue evidence requests;
- unresolved high-risk findings;
- vendors lacking current dependency inventories;
- material changes received before implementation;
- incidents reported within required time;
- accessibility and bias defects by severity;
- conditional approvals past deadline;
- vendors without tested exit plans.

Metrics must not reward rapid approval at the expense of evidence quality.

## 71.13 Audit programme

Auditors should:

1. reconcile the AI inventory with procurement, accounts-payable, cloud, and software inventories;
2. sample vendors across risk tiers;
3. confirm that due diligence preceded production use;
4. verify the legal-role and classification rationale;
5. inspect source evidence rather than questionnaire answers alone;
6. reproduce selected technical, accessibility, privacy, or oversight tests;
7. trace findings to approval conditions and closure evidence;
8. confirm reassessment after material changes, incidents, or renewals;
9. verify that rejected or expired tools are no longer used;
10. report systemic weaknesses, not only individual missing documents.

## 71.14 Graphic specification

### Figure 71-1 — AI Vendor Due-Diligence Funnel

**Type:** Formal process diagram

**Flow:**

`Define use → Assign roles → Classify risk → Request evidence → Validate claims → Test system → Decide and monitor`

Each stage narrows the funnel. Red stop gates appear for prohibited use, unresolved classification, inadequate evidence, critical testing failures, and unacceptable exit risk.

**Caption:** A supplier should reach approval only after the proposed use, legal roles, evidence, testing, and residual risks have passed defined gates.

**Alt text:** A seven-stage funnel for AI vendor due diligence, with red stop gates for prohibited use, uncertain classification, insufficient evidence, critical test failures, and unacceptable exit risk.

### Figure 71-2 — “The Evidence Shelf”

**Type:** Professional human-concern graphic

A procurement reviewer stands before two shelves. One shelf contains glossy boxes labeled “Trustworthy,” “Secure,” “Fair,” and “Compliant.” The other contains test results, role assessments, data flows, incident records, accessibility findings, and change logs. The reviewer selects from the evidence shelf.

**Purpose:** Show that confidence must come from verifiable evidence rather than branding.

**Alt text:** A procurement reviewer ignores glossy marketing boxes and selects documented test results, legal assessments, data flows, incident records, accessibility findings, and change logs.

## 71.15 Management checklist

Before approval, confirm:

- [ ] The proposed use and affected persons are documented.
- [ ] The AI Act and privacy roles are supported by evidence.
- [ ] Prohibited-practice and high-risk screening are complete.
- [ ] The vendor and dependency inventory is complete.
- [ ] Evidence matches the exact product, model, version, configuration, and region.
- [ ] Security, privacy, accuracy, bias, accessibility, oversight, and resilience have been reviewed.
- [ ] Higher-risk claims have been independently tested.
- [ ] Open findings have owners, deadlines, and approval conditions.
- [ ] Contract requirements have been handed to Chapter 72’s contracting process.
- [ ] Monitoring, change reassessment, incident response, and exit are planned.

## 71.16 Key takeaway

AI vendor due diligence is not a questionnaire-completion exercise. It is a structured challenge process that connects the intended use, legal role, technical evidence, human impact, testing, and ongoing accountability.

GlobalWay may rely on external technology, but it must retain enough knowledge, evidence, control, and exit capability to remain responsible for how that technology affects travelers, employees, clients, and the public.
