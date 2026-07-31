# Chapter 81 — Privacy by Design and Data Minimisation

## 1. Purpose

Privacy must be designed into an AI system before data is collected, integrated, inferred, retained, or shared. It cannot be added only after deployment.

This chapter establishes controls for limiting personal data throughout the AI lifecycle while preserving necessary accuracy, safety, fairness, security, traceability, and regulatory evidence.

> Collecting more data “just in case” is not a privacy strategy.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 2. Legal and governance basis

GDPR Article 5 requires personal data to be adequate, relevant, and limited to what is necessary for the stated purpose. Article 25 requires appropriate technical and organisational measures to implement data-protection principles effectively and to ensure that, by default, only necessary personal data are processed.

The EU AI Act does not replace the GDPR. Where AI design, development, testing, deployment, or monitoring involves personal data, both regimes may apply. High-risk AI data-governance duties may require sufficient, relevant, representative, and suitably governed data, but they do not authorize unnecessary personal-data collection.

The organization must therefore balance:

- necessity and proportionality;
- accuracy and representativeness;
- bias detection and mitigation;
- safety and robustness;
- traceability and auditability;
- privacy, confidentiality, and data-subject rights.

## 3. Scope

This chapter applies to:

- training, validation, testing, fine-tuning, and evaluation data;
- prompts, outputs, feedback, and conversation histories;
- retrieval-augmented generation stores;
- embeddings and vector databases;
- operational logs and monitoring data;
- identity, profile, preference, loyalty, and travel records;
- inferred attributes and risk scores;
- synthetic and pseudonymised data;
- vendor-hosted AI services and subprocessors;
- archived datasets, backups, and evidence repositories.

## 4. Privacy-by-design lifecycle

Privacy controls must be applied at each lifecycle stage.

| Lifecycle stage | Required privacy question |
|---|---|
| Idea and intake | Is personal data necessary for the proposed outcome? |
| Design | Can the purpose be achieved with less data or lower identifiability? |
| Acquisition | Are source, legal basis, notice, and collection limits documented? |
| Development | Are development environments and test datasets appropriately protected? |
| Evaluation | Is the minimum data needed for accuracy, bias, safety, and robustness testing used? |
| Deployment | Are default settings privacy-protective? |
| Monitoring | Are logs, feedback, and telemetry proportionate and time-limited? |
| Change | Does the change introduce new data, purposes, recipients, or inferences? |
| Retirement | Are data, models, embeddings, logs, and backups deleted or retained lawfully? |

## 5. Data minimisation decision test

Before approving a personal-data field or source, the owner must document:

1. **Purpose** — What specific approved purpose requires this data?
2. **Necessity** — Can the purpose reasonably be achieved without it?
3. **Proportionality** — Is the privacy impact proportionate to the benefit and risk reduction?
4. **Granularity** — Can less precise, aggregated, masked, or categorical data be used?
5. **Identifiability** — Can direct identifiers be removed, tokenised, or separated?
6. **Access** — Which people, systems, vendors, and subprocessors need access?
7. **Retention** — What is the shortest defensible retention period?
8. **Deletion** — Can the data be located and deleted across all system layers?
9. **Alternatives** — Could synthetic, anonymised, local, or sampled data work?
10. **Evidence** — What demonstrates that the decision was reviewed and approved?

Data must not be approved solely because it is available, inexpensive, or potentially useful later.

## 6. Data-category controls

### 6.1 Direct identifiers

Names, passport numbers, loyalty identifiers, account numbers, contact details, and booking references must be excluded unless directly required.

Where needed, controls should include:

- tokenisation;
- separation from model inputs;
- masking in logs;
- role-based access;
- restricted export;
- shorter retention;
- explicit deletion workflows.

### 6.2 Special-category and highly sensitive data

Health, disability, biometric, racial or ethnic origin, religion, sexual orientation, union membership, political opinion, and similar data require enhanced legal and risk review.

The system must not infer or use such attributes merely because technical methods make inference possible.

### 6.3 Location and travel-pattern data

Travel history and real-time location can expose health, religion, relationships, employment, political activity, or security risks. Collection and retention must be narrowly tied to operational need.

### 6.4 Inferred data

Predictions, classifications, embeddings, profiles, and risk scores may be personal data even when the original identifiers are not displayed. Inferences must be inventoried, justified, reviewable, and subject to correction or challenge where applicable.

## 7. Minimisation by architecture

Privacy-protective design patterns include:

- local or edge processing where feasible;
- purpose-specific data stores;
- separation of identity from analytical features;
- attribute filtering before prompts or API calls;
- retrieval filters that prevent unnecessary record access;
- ephemeral processing;
- field-level encryption;
- pseudonymisation and tokenisation;
- aggregation and sampling;
- privacy-preserving analytics;
- synthetic data for development and testing;
- configurable logging levels;
- automatic retention and deletion enforcement;
- restricted administrative access;
- tenant and client segregation.

Pseudonymised data remain personal data when re-identification is reasonably possible.

## 8. Privacy-protective defaults

Default settings must:

- disable unnecessary data collection;
- minimize prompt and conversation retention;
- prevent provider training on customer data unless specifically approved;
- restrict public sharing;
- limit user profiling;
- minimize telemetry;
- mask sensitive content in logs;
- apply shortest approved retention;
- restrict broad administrator access;
- require deliberate approval for expanded data use.

A user or administrator should not have to locate obscure settings to obtain the most privacy-protective configuration.

## 9. Training, validation, and testing data

Data-governance teams must document:

- dataset purpose;
- source and provenance;
- original collection purpose;
- legal basis;
- necessity of each major data category;
- representativeness and known gaps;
- bias and discrimination risks;
- data-cleaning and exclusion rules;
- retention and deletion rules;
- access and transfer restrictions;
- relationship to model or system versions.

Removing unnecessary attributes must not conceal material bias. Where sensitive attributes are legitimately required to test discrimination, access must be restricted and the use narrowly documented.

## 10. Prompts, outputs, logs, and feedback

Operational AI data must be governed independently from training data.

Controls must address:

- sensitive-data detection before submission;
- prompt redaction;
- output filtering;
- log minimisation;
- retention limits;
- human-review notes;
- user feedback;
- vendor storage;
- provider reuse;
- support-ticket replication;
- export and deletion capability.

Logs must capture enough information for security, incident response, oversight, and audit without becoming an uncontrolled duplicate of sensitive business and traveler data.

## 11. Retrieval and embeddings

Retrieval-augmented generation creates additional risks because data may be copied into indexes, chunks, caches, embeddings, and backups.

Required controls include:

- approved source repositories;
- document-level access inheritance;
- tenant segregation;
- filtering before retrieval;
- identity-aware authorization;
- deletion propagation;
- embedding and index retention rules;
- source traceability;
- stale-data removal;
- prevention of cross-client retrieval;
- testing for sensitive-data leakage.

Deletion from the original source is incomplete if copies remain in retrieval or embedding layers without a documented lawful basis.

## 12. Vendor and API controls

Before sending personal data to an external AI service, the organization must confirm:

- controller and processor roles;
- approved purpose;
- data fields transferred;
- provider retention;
- provider training and reuse terms;
- logging and support access;
- subprocessor chain;
- international transfers;
- deletion and return capability;
- model and service change controls;
- incident and breach notification;
- evidence and audit rights.

Vendor defaults must not override GlobalWay’s approved privacy configuration.

## 13. Retention and deletion

Retention must be defined separately for:

- source data;
- training and evaluation datasets;
- prompts and outputs;
- monitoring logs;
- human-review records;
- embeddings and indexes;
- model checkpoints and fine-tunes;
- backups;
- incident and audit evidence.

Deletion procedures must identify all locations and dependencies. Legal hold, regulatory evidence, safety, or security needs may justify retention, but the exception must be documented, access-restricted, and periodically reviewed.

## 14. Change control

A fresh privacy review is required when a change introduces:

- new personal-data categories;
- a new purpose;
- a new model or provider;
- expanded retention;
- broader sharing;
- new inferences or profiling;
- biometric, health, location, or special-category data;
- cross-border processing;
- new retrieval sources;
- provider training or reuse;
- reduced deletion capability;
- material changes to human impact.

## 15. Stop and escalation conditions

Deployment or processing must stop or be restricted when:

- necessity cannot be demonstrated;
- data are collected for undefined future use;
- provider reuse is unclear or unauthorized;
- sensitive data are exposed in prompts, logs, outputs, or support systems;
- deletion cannot be completed across material system layers;
- access controls permit cross-client or unauthorized retrieval;
- data are materially inaccurate and cannot be corrected;
- minimisation would be defeated by uncontrolled vendor defaults;
- required privacy, legal, security, or rights review is incomplete;
- accountable owners cannot explain or defend the data used.

## 16. GlobalWay Travel Services example

GlobalWay proposes an AI assistant that recommends disruption options using itinerary, traveler profile, loyalty status, location, health-assistance requests, and prior support history.

### AI may do

- identify relevant itinerary constraints;
- retrieve approved disruption options;
- prioritize options using necessary travel preferences;
- draft a recommendation for a travel consultant.

### Human decision

A travel consultant decides which option to present or book and whether sensitive traveler circumstances are necessary for the decision.

### Minimisation controls

GlobalWay:

- excludes passport and payment details;
- tokenises the booking identifier;
- uses broad location rather than continuous precise tracking;
- retrieves health-assistance details only when required for accessibility or safety;
- prevents provider training on traveler data;
- masks prompts and logs;
- deletes session content after the approved retention period;
- keeps loyalty data separate unless needed for eligibility;
- provides a manual alternative.

### Stop and escalation

The workflow stops if the model accesses unrelated traveler history, exposes another client’s records, infers sensitive traits without approval, or retains session data contrary to policy.

### Accountable owner

The VP of Traveler Experience owns the business purpose. Privacy, legal, security, data governance, accessibility, and the AI product owner retain their assigned control responsibilities.

### Challenge, correction, and override

Travelers and consultants can correct relevant data, reject the recommendation, request human handling, or use a manual workflow.

## 17. Control activities

| Control ID | Control activity | Evidence |
|---|---|---|
| EUAI-PRV-01 | Apply a documented necessity and proportionality test | Data-field assessment |
| EUAI-PRV-02 | Implement privacy-protective defaults | Configuration records and tests |
| EUAI-PRV-03 | Minimize prompts, outputs, logs, and telemetry | Data-flow and logging review |
| EUAI-PRV-04 | Separate identity from analytical features where feasible | Architecture and tokenisation evidence |
| EUAI-PRV-05 | Govern retrieval stores and embeddings | Access, deletion, and leakage tests |
| EUAI-PRV-06 | Restrict vendor use, retention, and training | Contract and configuration evidence |
| EUAI-PRV-07 | Enforce retention and deletion across all layers | Retention schedule and deletion tests |
| EUAI-PRV-08 | Reassess privacy upon material change | Change assessment and approval |

## 18. Evidence requirements

Evidence should include:

- approved purpose statement;
- data inventory and field-level necessity assessment;
- data-flow diagram;
- privacy architecture decision record;
- default-configuration screenshots or exports;
- pseudonymisation or tokenisation design;
- prompt and log filtering tests;
- vendor data-use terms;
- retrieval authorization and deletion tests;
- retention schedule;
- deletion and backup procedures;
- DPIA and related rights assessments;
- exception approvals;
- monitoring and remediation records.

## 19. Audit test

Select a sample of AI systems processing personal data.

For each sample:

1. Confirm the purpose and legal basis are documented.
2. Trace each material personal-data category to a necessity decision.
3. Verify privacy-protective defaults.
4. Inspect prompts, logs, outputs, retrieval stores, embeddings, and vendor systems for unnecessary duplication.
5. Confirm direct identifiers and sensitive data are restricted.
6. Test role-based and tenant access.
7. Verify provider training and reuse settings.
8. Test retention and deletion across source, index, cache, log, vendor, and backup layers.
9. Confirm changes trigger renewed privacy review.
10. Verify accountable humans can restrict, stop, correct, and override processing.

## 20. Metrics

Suggested metrics:

- percentage of AI systems with field-level minimisation review;
- percentage using privacy-protective defaults;
- percentage of external AI services with provider training disabled or approved;
- number of unnecessary data fields removed;
- percentage of AI logs with masking enabled;
- percentage of retrieval stores with tested deletion propagation;
- number of expired data records awaiting deletion;
- number of privacy exceptions past review date;
- number of unauthorized sensitive-data submissions;
- average time to complete AI data-subject deletion requests.

## 21. Management checklist

- [ ] Is every personal-data category necessary for an approved purpose?
- [ ] Are defaults privacy-protective?
- [ ] Are direct identifiers removed or separated where feasible?
- [ ] Are sensitive and inferred data subject to enhanced review?
- [ ] Are prompts, outputs, logs, and feedback minimized?
- [ ] Are retrieval stores and embeddings included in deletion processes?
- [ ] Is provider training or reuse prohibited unless explicitly approved?
- [ ] Are retention periods specific to each data layer?
- [ ] Can accountable humans stop or restrict processing?
- [ ] Is evidence sufficient to demonstrate GDPR and AI-governance compliance?

## 22. Graphic specification

### Figure 81-1 — Privacy-by-Design Data Reduction Funnel

A formal process diagram showing:

1. proposed data universe;
2. purpose and legal-basis review;
3. necessity and proportionality test;
4. identifier removal and granularity reduction;
5. access, retention, and vendor restrictions;
6. approved minimum dataset;
7. monitored production use and deletion.

The figure must show human approval gates at design, deployment, material change, and exception stages.

**Alt text:** A funnel narrows a broad proposed dataset through purpose, necessity, proportionality, de-identification, access, retention, and vendor controls until only the approved minimum dataset remains, with human approval gates throughout.

## 23. Key takeaway

Privacy by design means proving why each category of personal data is needed, configuring the system to use less by default, and retaining only what remains necessary. Effective minimisation must extend beyond source databases to prompts, logs, outputs, embeddings, retrieval stores, vendors, backups, and evidence repositories.