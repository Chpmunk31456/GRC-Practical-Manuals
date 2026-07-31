# Chapter 82 — Special-Category Data

## Purpose

This chapter establishes controls for AI systems that collect, generate, infer, transform, expose, or rely on special-category personal data. It integrates GDPR Article 9 controls with EU AI Act risk management, data governance, transparency, human oversight, security, and accountability requirements.

Special-category data requires heightened protection because misuse, inaccuracy, disclosure, or automated inference may cause discrimination, exclusion, physical harm, reputational damage, or loss of access to essential services.

> **Core principle:** AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 82.1 Requirement

An organisation must not process special-category personal data through an AI system unless it can document:

1. a valid GDPR Article 6 lawful basis;
2. a specific GDPR Article 9 condition permitting the processing;
3. necessity and proportionality;
4. compliance with applicable Union and Member State law;
5. data-minimisation and purpose-limitation controls;
6. appropriate technical and organisational safeguards;
7. an assessment of discrimination, fundamental-rights, and security risks;
8. effective human review, escalation, challenge, and correction mechanisms; and
9. an accountable owner authorised to stop or restrict the processing.

The EU AI Act applies alongside the GDPR. Compliance with one instrument does not replace obligations under the other.

## 82.2 What counts as special-category data

GDPR Article 9 covers personal data revealing or concerning:

- racial or ethnic origin;
- political opinions;
- religious or philosophical beliefs;
- trade-union membership;
- genetic data;
- biometric data processed for uniquely identifying a person;
- health data; and
- a person’s sex life or sexual orientation.

For AI governance, the organisation must also treat **inferred special-category data** as high sensitivity when an AI system predicts, classifies, scores, or derives such characteristics from other information. Examples include inferring health status from travel behaviour, religion from meal preferences, ethnicity from names or images, or disability from assistance requests.

The fact that an attribute was inferred rather than directly collected does not remove the risk or the need for legal and governance review.

## 82.3 Plain-language explanation

Special-category data is information that can expose a person to serious harm if it is used incorrectly. AI systems may create this information even when nobody explicitly entered it. For example, a model may infer a medical condition from a pattern of airport-assistance requests.

Before using such data, the organisation must answer two separate questions:

1. **Is ordinary personal-data processing lawful under Article 6?**
2. **Which Article 9 exception permits processing this sensitive category?**

Both answers must be documented. A general business benefit, convenience, or model-performance improvement is not enough.

## 82.4 Article 9 condition assessment

The privacy owner and legal counsel must identify the precise Article 9 condition relied upon. Depending on the use case, this may include explicit consent, employment and social-protection law, protection of vital interests, substantial public interest, legal claims, healthcare, public health, or qualifying research and statistical purposes.

The assessment must record:

- the exact Article 9 condition;
- the Article 6 lawful basis;
- the applicable Union or Member State legal provision, where required;
- why the processing is necessary;
- why a less intrusive method is insufficient;
- whether consent is freely given, specific, informed, explicit, and withdrawable, where consent is relied upon;
- safeguards required by law;
- retention and deletion rules; and
- the approval and review date.

### Prohibited shortcuts

The organisation must not:

- rely on implied consent for Article 9 processing;
- treat acceptance of general terms as explicit consent;
- infer that publicly available sensitive data may be used without restriction;
- reuse special-category data for model training merely because it was collected lawfully for another purpose;
- assume that pseudonymisation removes GDPR obligations; or
- use broad labels such as “legitimate interest” as an Article 9 condition.

## 82.5 Direct, observed, and inferred data

The AI use-case record must distinguish among:

| Data form | Description | Example | Required control |
|---|---|---|---|
| Directly provided | Supplied by the person or authorised representative | A traveller discloses a mobility impairment | Validate purpose, legal basis, Article 9 condition, access, retention, and notice |
| Observed | Captured from behaviour, devices, transactions, or interactions | Repeated requests for wheelchair assistance | Prevent unauthorised profiling and test whether sensitive inference is occurring |
| Derived | Created by combining existing data | A risk marker generated from assistance and itinerary data | Document derivation logic, accuracy, purpose, and human review |
| Inferred | Predicted by a model | A model predicts pregnancy or medical vulnerability | Treat as high sensitivity; require explicit approval, necessity, validation, and challenge rights |

## 82.6 Biometric data and categorisation

Biometric processing requires a separate assessment covering:

- whether the data is used for unique identification or verification;
- whether the system performs biometric categorisation;
- whether it infers sensitive attributes;
- whether the use is prohibited, high-risk, or otherwise regulated under the EU AI Act;
- the Article 6 and Article 9 grounds;
- accuracy and demographic-performance testing;
- spoofing, replay, template-theft, and presentation-attack risks;
- storage of raw images versus protected templates;
- retention and deletion;
- human fallback and alternative access methods; and
- the ability to challenge incorrect matches or classifications.

AI systems must not assign people to sensitive categories based on biometric data where the practice is prohibited by applicable law. Where a biometric use is legally permitted, the organisation must still determine whether the system is high-risk and apply all corresponding controls.

## 82.7 Health, disability, and accessibility data

Health and disability information must be used only for a clearly defined and lawful purpose. Accessibility support must not become a hidden source of profiling, eligibility scoring, marketing segmentation, fraud suspicion, or adverse treatment.

Controls must ensure that:

- assistance requests are separated from commercial profiling where possible;
- only personnel with a genuine need can access the data;
- health indicators are not exposed in ordinary customer-service screens;
- free-text notes are minimised and structured safely;
- the AI does not diagnose or make clinical claims unless the system is lawfully designed and authorised for that purpose;
- travellers can correct inaccurate information;
- support is not withheld solely because an AI confidence score is low; and
- a trained human can intervene immediately.

## 82.8 Data-quality and bias controls

Special-category data can magnify discrimination risks. Data governance must therefore include:

- provenance and collection-context review;
- representativeness analysis;
- subgroup performance testing;
- missing-data analysis;
- label-quality review;
- proxy-variable detection;
- false-positive and false-negative analysis;
- intersectional testing where appropriate;
- controls against feedback loops;
- documented thresholds and limitations; and
- approval before deployment or material change.

High aggregate accuracy does not prove fair or safe performance. Results must be reviewed across relevant populations and operating conditions.

## 82.9 Human oversight

Every use case involving special-category data must define:

### AI may do

- identify records requiring specialist review;
- support accessibility routing;
- summarise information for authorised personnel;
- detect possible data-quality or security anomalies; and
- recommend, but not independently impose, a consequential action.

### Human decision

A qualified human must decide whether to:

- approve or deny a consequential action;
- rely on a sensitive inference;
- disclose or share the data;
- override a model result;
- suspend processing;
- correct or delete information; or
- escalate to privacy, legal, security, or safeguarding teams.

### Review requirements

The reviewer must have:

- appropriate training and authority;
- access to relevant context and model limitations;
- enough time to conduct a real review;
- the ability to disagree with the AI;
- a documented escalation path; and
- protection from automation bias or performance targets that make review merely symbolic.

### Stop and escalation conditions

Processing must stop or be restricted when:

- no valid Article 9 condition is documented;
- the purpose materially changes;
- sensitive attributes appear unexpectedly in prompts, outputs, logs, or embeddings;
- the model produces discriminatory or clinically unsafe inferences;
- data lineage cannot be established;
- access controls fail;
- deletion cannot be completed across all data layers;
- a vendor reuses the data outside authorised purposes;
- meaningful human review is unavailable; or
- legal, privacy, or security owners direct suspension.

## 82.10 GlobalWay Travel Services example

### Scenario

GlobalWay uses an AI assistant to help agents coordinate disrupted travel. A passenger requests wheelchair assistance and mentions medication that must remain refrigerated. The assistant summarises the case, identifies suitable alternative flights, and alerts a specialist support agent.

### AI may do

- extract the assistance requirement from the passenger’s message;
- identify operational constraints relevant to rebooking;
- present available options;
- flag urgency; and
- draft a response for human review.

### AI must not do

- diagnose the passenger;
- infer unrelated medical conditions;
- use the information for pricing, marketing, fraud scoring, or customer-value segmentation;
- disclose the information to staff without a need to know;
- deny travel or assistance automatically; or
- retain the information longer than the authorised purpose requires.

### Human decision

A trained support agent verifies the passenger’s needs, confirms the preferred option, coordinates necessary assistance, corrects any inaccurate AI summary, and approves all external communications.

### Control activity

GlobalWay documents the lawful basis and Article 9 condition, limits collection to operationally necessary facts, separates accessibility records from marketing profiles, restricts access, applies short retention, logs human approval, and offers a correction route.

### Evidence

- approved use-case and privacy assessment;
- Article 6 and Article 9 determination;
- data-flow diagram;
- role-based access list;
- prompt and output controls;
- retention configuration;
- human-approval logs;
- vendor restrictions;
- training records; and
- periodic bias and access reviews.

### Audit test

Select a sample of disruption cases involving accessibility or medical information. Confirm that each case had a documented lawful basis and Article 9 condition, limited data collection, authorised access, human approval, proper retention, no secondary marketing use, and an available correction process.

## 82.11 Control activities

| Control ID | Control activity | Accountable owner | Evidence | Audit test |
|---|---|---|---|---|
| SCD-01 | Maintain an inventory of AI uses involving direct, observed, derived, or inferred special-category data | Privacy Officer | AI inventory, data classification | Reconcile sampled systems to data flows and records of processing |
| SCD-02 | Document Article 6 and Article 9 grounds before processing | Legal and Privacy | Lawful-basis assessment | Verify the exact grounds and supporting law |
| SCD-03 | Prohibit unapproved sensitive inference | AI Governance Lead | Design standards, model tests | Test whether models infer sensitive attributes outside scope |
| SCD-04 | Apply strict access control and segregation | Security Owner | Access matrix, logs | Sample access and verify need-to-know approval |
| SCD-05 | Perform DPIA and fundamental-rights review where required | Privacy and AI Risk | DPIA, FRIA, approvals | Confirm completion before deployment and after material change |
| SCD-06 | Test subgroup performance and proxy discrimination | Model Risk Owner | Validation reports | Reperform selected subgroup tests and inspect thresholds |
| SCD-07 | Provide meaningful human review and override | Business Owner | Workflow records, training | Sample decisions and assess whether review was substantive |
| SCD-08 | Enforce retention and deletion across all data layers | Data Owner | Retention schedule, deletion logs | Trace deletion through source, logs, cache, embeddings, and vendors |
| SCD-09 | Restrict vendor use and onward transfer | Procurement and Legal | Contract, subprocessor list | Verify purpose limits, deletion, incident, and audit terms |
| SCD-10 | Monitor for leakage into prompts, outputs, logs, and analytics | Security and Privacy | DLP alerts, monitoring reports | Review alerts and remediation evidence |

## 82.12 Evidence package

The minimum evidence package should include:

- use-case description and owner;
- system and data-flow diagrams;
- Article 6 lawful-basis decision;
- Article 9 condition and supporting legal analysis;
- DPIA and, where applicable, fundamental-rights assessment;
- data inventory and classification;
- purpose and necessity analysis;
- data-minimisation record;
- inference and proxy-variable assessment;
- bias and subgroup testing;
- human-oversight procedure;
- privacy notice and rights procedure;
- access-control matrix and logs;
- retention and deletion evidence;
- vendor contract and subprocessor records;
- incident and breach procedures;
- training records; and
- periodic management review.

## 82.13 Metrics

Management should monitor:

- number of AI systems processing special-category data;
- percentage with current Article 6 and Article 9 assessments;
- number of unexpected sensitive-inference events;
- percentage with completed DPIA and required rights assessments;
- subgroup performance variance;
- sensitive-data access exceptions;
- deletion completion rate across all data layers;
- number of human overrides and escalations;
- vendor-policy exceptions;
- sensitive-data incidents and near misses; and
- overdue corrective actions.

Metrics must not encourage reviewers to approve cases quickly at the expense of meaningful oversight.

## 82.14 Management checklist

- [ ] Have we identified direct, observed, derived, and inferred special-category data?
- [ ] Is an Article 6 lawful basis documented?
- [ ] Is the exact Article 9 condition documented and supported?
- [ ] Is the processing necessary and proportionate?
- [ ] Have we checked applicable Member State law?
- [ ] Have we prevented unapproved sensitive inference and proxy use?
- [ ] Are biometric uses separately classified under the EU AI Act?
- [ ] Are accessibility and health details separated from marketing and scoring?
- [ ] Have we completed required DPIA and fundamental-rights reviews?
- [ ] Are subgroup accuracy and discrimination risks tested?
- [ ] Is human review meaningful, trained, and empowered?
- [ ] Can affected people challenge and correct results?
- [ ] Are access, retention, deletion, vendor, and incident controls operating?
- [ ] Is there a clear stop authority and escalation route?

## 82.15 Graphic specification

**Title:** Special-Category Data Decision Gate

**Type:** Formal decision-flow diagram

**Flow:**

1. Does the AI system collect, use, generate, or infer personal data?
2. Does the data fall within, or reveal, a GDPR Article 9 category?
3. Is there a documented Article 6 lawful basis?
4. Is there a valid and specific Article 9 condition?
5. Is the processing necessary, proportionate, and permitted by applicable law?
6. Have DPIA, fundamental-rights, bias, security, and vendor reviews been completed?
7. Are minimisation, access, retention, deletion, transparency, and human-oversight controls effective?
8. Authorise with conditions, redesign, restrict, or stop.

**Visual treatment:** Restrained corporate colours, high contrast, clear decision diamonds, visible stop paths, and an accountable-human approval gate before deployment.

**Alt text:** Decision flow for determining whether an AI system may process special-category personal data, requiring lawful bases, necessity, risk assessments, safeguards, and accountable human approval.

## 82.16 Key takeaway

Special-category data is not an ordinary AI input. It requires a documented legal permission, strict necessity, controlled architecture, strong security, tested fairness, meaningful human authority, and continuous evidence that the processing remains lawful and safe.

Where those conditions cannot be demonstrated, the organisation must redesign, restrict, or stop the AI use.