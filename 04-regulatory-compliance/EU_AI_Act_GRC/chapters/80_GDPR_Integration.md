# Chapter 80 — GDPR Integration

## 1. Purpose

AI governance and data-protection governance must operate as one coordinated control environment whenever an AI system processes personal data.

The EU AI Act does not replace the General Data Protection Regulation. An organization may satisfy an AI Act requirement and still breach the GDPR, or satisfy a GDPR requirement and still fail an AI Act obligation.

> AI compliance and data-protection compliance must be assessed together, but evidenced separately.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 2. Scope

This chapter applies when an AI system or model:

- collects or receives personal data;
- infers information about an identifiable person;
- profiles travelers, employees, applicants, suppliers, or customers;
- uses identity, behavior, location, itinerary, loyalty, payment, device, health, accessibility, biometric, or communication data;
- trains, fine-tunes, evaluates, retrieves, or monitors using personal data;
- generates outputs linked to an identifiable person;
- supports or influences decisions about individuals;
- transfers personal data to providers, subprocessors, or locations outside the European Economic Area.

## 3. Integrated legal principle

The organization must identify and document both:

1. its role under the EU AI Act, such as provider, deployer, importer, distributor, or another value-chain actor; and
2. its role under the GDPR, such as controller, joint controller, processor, or subprocessor.

These role assessments are related but not interchangeable.

For example, GlobalWay may be a deployer of a third-party AI system while acting as the controller for traveler data processed through that system. A provider may act as a processor for one activity and as an independent controller for another, such as service-security telemetry or model-improvement data.

## 4. GDPR principles applied to AI

### 4.1 Lawfulness, fairness, and transparency

Every personal-data processing activity must have an appropriate legal basis and must be fair and transparent.

The organization must document:

- the specific processing purpose;
- the legal basis;
- whether additional conditions apply to special-category or criminal-offence data;
- what information is given to affected people;
- whether the use is within their reasonable expectations;
- whether the AI creates hidden, manipulative, discriminatory, or disproportionate effects;
- how people can challenge, correct, or obtain human review.

An AI-interaction notice does not by itself satisfy the GDPR transparency obligation. Notices must also explain the personal-data processing in a concise, intelligible, accessible, and sufficiently specific manner.

### 4.2 Purpose limitation

Personal data collected for one purpose must not be reused for an incompatible AI purpose without a documented legal assessment.

Examples requiring review include:

- reusing booking data to train a recommendation model;
- using customer-service transcripts for employee-performance scoring;
- using travel-risk data for marketing segmentation;
- using accessibility requests to infer health conditions;
- using fraud indicators to make unrelated commercial decisions.

### 4.3 Data minimisation

AI teams must not collect or retain personal data merely because it may improve a model.

Required controls include:

- defining the minimum necessary fields;
- removing unnecessary identifiers;
- limiting historical depth;
- excluding sensitive attributes unless justified;
- restricting prompts, logs, embeddings, and retrieval indexes;
- using aggregation, pseudonymisation, anonymisation, or synthetic data where appropriate;
- preventing production data from entering unapproved training or evaluation workflows.

### 4.4 Accuracy

The organization must take reasonable steps to keep personal data and person-specific AI outputs accurate.

Controls should address:

- source-data quality;
- stale profile data;
- incorrect identity matching;
- inferred attributes;
- hallucinated personal facts;
- correction propagation across systems;
- contested data and outputs;
- suppression or deletion from retrieval stores, caches, indexes, and downstream records.

### 4.5 Storage limitation

Retention must be defined for:

- source data;
- prompts and outputs;
- model inputs;
- embeddings and vector-store content;
- training and fine-tuning datasets;
- monitoring logs;
- human-review records;
- incident evidence;
- challenge and correction records.

Retention must distinguish operational need, legal obligation, security evidence, model improvement, and convenience.

### 4.6 Integrity and confidentiality

Personal data used by AI systems must be protected through appropriate technical and organizational measures.

Controls should include:

- access control and least privilege;
- encryption;
- tenant and environment isolation;
- secure APIs;
- prompt and output filtering;
- secret management;
- logging and alerting;
- protection against data leakage, prompt injection, model extraction, and membership inference;
- secure deletion;
- incident response;
- supplier and subprocessor controls.

### 4.7 Accountability

The organization must be able to demonstrate compliance.

Evidence must show not only that a policy exists, but also that the specific AI use case was assessed, approved, tested, monitored, challenged, and corrected where necessary.

## 5. Processing inventory and AI inventory alignment

The AI inventory and the GDPR record of processing activities must be linked.

Minimum cross-references should include:

| AI inventory field | GDPR record field |
|---|---|
| AI system and version | Processing activity and systems used |
| Business purpose | Purpose of processing |
| AI Act role | Controller/processor role |
| Data categories | Categories of personal data |
| Affected people | Categories of data subjects |
| Provider and subprocessors | Recipients and processors |
| Data locations | International transfers |
| Retention | Erasure schedule |
| Human oversight | Decision and challenge process |
| Risk classification | DPIA and rights-risk status |
| Monitoring | Ongoing compliance controls |

Changes to either inventory must trigger reconciliation.

## 6. Legal-basis assessment

The legal team and data-protection function must document the legal basis for each distinct processing purpose.

The assessment must not rely on broad labels such as “service improvement” or “AI optimization.”

Where legitimate interests are relied upon, the organization should document:

- the legitimate interest;
- necessity;
- impact on individuals;
- reasonable expectations;
- safeguards;
- opt-out or objection handling;
- residual risk.

Consent must be freely given, specific, informed, unambiguous, and capable of withdrawal. It should not be used where a genuine choice is absent or where service access is improperly conditioned on unnecessary AI processing.

## 7. Special-category and sensitive data

AI systems may infer or expose sensitive information even when it was not explicitly collected.

Examples include:

- health or disability inferred from assistance requests;
- religion inferred from meal, destination, or calendar patterns;
- political views inferred from travel or event attendance;
- biometric information derived from images, voice, or behavior;
- sexual orientation inferred from relationship or travel patterns;
- trade-union status inferred from corporate travel or communications.

The organization must assess both explicit and inferred sensitive data, document the applicable legal condition, apply strict access controls, and prohibit unsupported inference or secondary use.

## 8. Data protection impact assessment

A data protection impact assessment should be initiated where AI processing is likely to create high risk to individuals, including through systematic profiling, large-scale sensitive-data processing, monitoring, novel technology, vulnerable populations, or decisions with significant effects.

The DPIA should address:

- processing purposes and necessity;
- proportionality;
- data flows and recipients;
- model and system behavior;
- foreseeable misuse;
- bias and discrimination;
- opacity and explainability;
- data leakage and re-identification;
- automated decision-making;
- affected-person rights;
- security and resilience;
- human oversight;
- residual risk;
- consultation and approval.

Where an AI Act fundamental-rights impact assessment is also required or voluntarily performed, the organization should coordinate the assessments, reuse reliable evidence, and preserve the distinct legal conclusions and approvals.

## 9. Automated decision-making and profiling

The organization must determine whether an AI-supported process produces a decision based solely on automated processing that has legal or similarly significant effects.

The assessment must consider the real operating model, not merely the documented workflow.

A nominal human step is not meaningful human involvement when the reviewer:

- lacks authority to change the outcome;
- lacks time or information;
- routinely accepts the recommendation;
- is measured against agreement with the AI;
- cannot understand the relevant factors;
- cannot investigate conflicting evidence.

Where applicable, controls must support:

- human intervention;
- expression of the person’s viewpoint;
- challenge and contestability;
- review of relevant data and reasoning;
- correction of errors;
- reversal or remediation;
- communication of the outcome.

## 10. Transparency and notice integration

AI Act and GDPR notices should be coordinated but must cover their distinct purposes.

An integrated notice may include:

- that AI is being used;
- whether the person is interacting with AI;
- the processing purpose;
- categories of personal data;
- legal basis;
- source of the data;
- significant logic or factors where required and appropriate;
- expected consequences;
- provider and recipient information;
- transfer information;
- retention;
- human-review options;
- rights and contact routes;
- accessibility and alternative formats.

Layered notices should present critical information at the point of interaction and provide access to fuller detail.

## 11. Data-subject rights

AI systems must support operational handling of:

- access;
- rectification;
- erasure;
- restriction;
- portability;
- objection;
- withdrawal of consent;
- rights related to automated decision-making.

The organization must know where person-related data exists across:

- source systems;
- prompts and outputs;
- logs;
- embeddings;
- retrieval indexes;
- training or fine-tuning sets;
- evaluation sets;
- caches;
- vendor systems;
- backups;
- monitoring and incident records.

A request must not be closed merely because the primary database was updated while derived AI stores remain unchanged.

## 12. Controller–processor governance

Contracts and operating procedures must define:

- processing instructions;
- confidentiality;
- security obligations;
- subprocessors;
- data location and transfers;
- retention and deletion;
- assistance with rights requests;
- incident and breach notification;
- audit and evidence rights;
- restrictions on provider training or independent reuse;
- model-improvement settings;
- exit and return of data;
- responsibility for correction across derived stores.

The organization must identify processing that the provider performs for its own purposes and determine whether separate controller obligations apply.

## 13. International transfers

Where personal data is accessed or processed outside the European Economic Area, the organization must document:

- the transfer mechanism;
- destination countries;
- onward transfers;
- subprocessor locations;
- supplementary safeguards;
- government-access risks;
- encryption and key control;
- remote-support access;
- data-residency limitations;
- changes requiring reassessment.

Data location must be verified through evidence rather than relying solely on marketing statements.

## 14. Security incidents and personal-data breaches

An AI incident may also be a personal-data breach.

Examples include:

- prompts exposed to another customer;
- model outputs revealing traveler data;
- unauthorized provider training on customer content;
- retrieval systems returning another person’s records;
- compromised model or plug-in exfiltrating data;
- membership-inference or model-extraction attacks exposing personal information;
- logs retaining sensitive data beyond the approved period.

Incident triage must assess both AI Act and GDPR notification duties. Different authorities, thresholds, time limits, evidence, and affected-person communications may apply.

## 15. Stop and escalation conditions

Processing must stop or be restricted when:

- no valid legal basis is documented;
- the purpose is incompatible with the original collection;
- unnecessary personal or sensitive data is used;
- required DPIA or legal review is incomplete;
- individuals cannot exercise applicable rights;
- the system produces uncorrectable person-specific errors;
- automated decisions lack meaningful human review;
- provider reuse or training is unauthorized;
- transfer safeguards are inadequate;
- a serious privacy or security risk remains unmitigated;
- accountable owners cannot explain or control the processing.

## 16. GlobalWay Travel Services example

GlobalWay proposes an AI service that predicts which travelers may need proactive assistance during major disruptions.

### AI may do

- identify itineraries affected by disruption;
- prioritize outreach using approved operational factors;
- draft assistance messages;
- flag travelers with recorded service needs.

### Human decision

A travel-operations specialist decides the outreach priority, assistance offered, and final communication.

### GDPR review

GlobalWay documents:

- the operational purpose and legal basis;
- the minimum data fields required;
- whether accessibility information reveals health or disability data;
- the provider’s processor role and any independent use;
- retention of prompts, outputs, and logs;
- international transfers;
- the DPIA outcome;
- objection, correction, and human-review routes.

### Stop and escalation

The workflow stops when the model infers unsupported sensitive information, uses marketing data for emergency prioritization, exposes another traveler’s details, or makes outreach decisions without meaningful human control.

### Accountable owner

The Director of Travel Operations owns the operational decision. The Data Protection Officer, privacy counsel, AI product owner, security, accessibility, and vendor-risk teams retain their assigned responsibilities.

### Challenge, correction, and override

Travelers can correct relevant information, object where applicable, request human review, and use non-AI support channels. Staff can reject the AI priority, correct the record, and switch to manual disruption procedures.

## 17. Control activities

| Control ID | Control activity | Evidence |
|---|---|---|
| EUAI-GDPR-01 | Link the AI inventory to the record of processing activities | Reconciled inventories |
| EUAI-GDPR-02 | Document controller, processor, and AI Act roles | Role assessment |
| EUAI-GDPR-03 | Establish purpose and legal basis for each processing activity | Legal-basis assessment |
| EUAI-GDPR-04 | Apply data minimisation and retention controls | Data specification and retention schedule |
| EUAI-GDPR-05 | Complete DPIA and coordinated rights-risk review where required | Approved assessments |
| EUAI-GDPR-06 | Implement meaningful human review for significant decisions | Oversight plan and review records |
| EUAI-GDPR-07 | Provide integrated, accessible transparency information | Approved notices and tests |
| EUAI-GDPR-08 | Operationalize data-subject rights across AI data stores | Procedures and request evidence |
| EUAI-GDPR-09 | Govern processors, subprocessors, reuse, and transfers | Contracts and transfer assessments |
| EUAI-GDPR-10 | Coordinate AI incidents and personal-data breach response | Triage and notification records |

## 18. Evidence requirements

Evidence should include:

- linked AI and processing inventories;
- role assessments;
- purpose and legal-basis records;
- legitimate-interest or consent assessments where applicable;
- data-category and minimisation specifications;
- retention and deletion schedules;
- DPIAs and coordinated impact assessments;
- automated-decision assessments;
- privacy and AI transparency notices;
- accessibility testing;
- rights-request procedures and completed cases;
- controller–processor agreements;
- subprocessor records;
- transfer assessments;
- security testing;
- incident and breach records;
- monitoring, correction, and remediation evidence.

## 19. Audit test

Select a sample of AI systems processing personal data.

For each sample:

1. Confirm the AI inventory links to the correct processing record.
2. Verify AI Act and GDPR roles are documented.
3. Test whether the purpose and legal basis are specific and supported.
4. Confirm only necessary data is processed and retention is enforced.
5. Determine whether a DPIA was required and, where applicable, completed before deployment.
6. Inspect automated-decision and meaningful-human-review assessments.
7. Review the accuracy and accessibility of notices.
8. Trace a sample rights request across source, derived, vendor, and retrieval stores.
9. Verify processor, subprocessor, reuse, and transfer controls.
10. Confirm incidents are assessed under both AI and data-protection requirements.
11. Verify accountable humans can suspend, correct, override, or terminate the processing.

## 20. Metrics

Suggested metrics:

- percentage of personal-data AI systems linked to processing records;
- percentage with documented legal basis;
- percentage with current DPIAs where required;
- percentage with tested rights-request procedures;
- number of AI data stores outside the retention schedule;
- number of unauthorized provider-training or reuse events;
- percentage of significant AI decisions with tested meaningful human review;
- average time to correct person-specific AI errors;
- number of unresolved transfer or subprocessor gaps;
- number of AI incidents also classified as personal-data breaches.

## 21. Management checklist

- [ ] Are AI Act and GDPR roles documented separately?
- [ ] Is each personal-data purpose specific and lawful?
- [ ] Is only necessary data processed?
- [ ] Are sensitive and inferred sensitive data controlled?
- [ ] Is retention defined for prompts, outputs, logs, embeddings, and training data?
- [ ] Has the DPIA requirement been assessed?
- [ ] Is human review meaningful rather than nominal?
- [ ] Are notices clear, layered, and accessible?
- [ ] Can rights requests reach all relevant AI data stores?
- [ ] Are provider reuse and model training contractually controlled?
- [ ] Are international transfers and subprocessors documented?
- [ ] Are AI incidents triaged for personal-data breach obligations?
- [ ] Can accountable humans stop, correct, or override the processing?

## 22. Graphic specification

### Figure 80.1 — Integrated AI Act and GDPR Governance Flow

A formal process diagram showing:

1. AI use-case intake;
2. AI Act role and risk classification;
3. GDPR role, purpose, and legal-basis assessment;
4. data minimisation and data-flow review;
5. DPIA and fundamental-rights coordination;
6. human-oversight and transparency design;
7. vendor, transfer, security, and rights controls;
8. approval or stop decision;
9. monitoring, correction, incident response, and reassessment.

The diagram must make clear that AI Act approval does not substitute for GDPR approval and that both control paths converge at an accountable human decision gate.

Alt text: A dual-track governance flow in which EU AI Act and GDPR assessments proceed in parallel, share evidence, and converge at a human approval, restriction, or stop decision.

## 23. Authoritative legal sources

- Regulation (EU) 2024/1689 — Artificial Intelligence Act, official EUR-Lex text.
- Regulation (EU) 2016/679 — General Data Protection Regulation, official EUR-Lex text.

Legal requirements, regulator guidance, and organizational interpretations must be reviewed by qualified legal and data-protection professionals before publication or operational reliance.
