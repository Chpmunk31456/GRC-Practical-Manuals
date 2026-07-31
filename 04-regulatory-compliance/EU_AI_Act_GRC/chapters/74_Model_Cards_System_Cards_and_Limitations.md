# Chapter 74 — Model Cards, System Cards, and Limitations

## 74.1 Purpose

Model cards, system cards, technical fact sheets, service descriptions, and limitation statements help an organization understand what an AI capability is designed to do, where it may fail, and how it should be governed.

These artifacts may support compliance, procurement, deployment, oversight, and audit. They do not replace legally required technical documentation, instructions for use, contractual commitments, conformity documentation, risk-management records, or the organization’s own validation.

**Core principle:** A polished document is not evidence that an AI system is safe, suitable, compliant, or effective. Claims must be tested against the actual system, intended use, operating environment, and affected people.

## 74.2 Governance objective

The organization shall establish a controlled process to:

1. obtain current model and system documentation;
2. identify the artifact’s author, scope, version, and intended audience;
3. distinguish provider claims from independently verified facts;
4. extract stated capabilities, limitations, assumptions, exclusions, and dependencies;
5. test whether the documentation applies to the contracted and deployed configuration;
6. convert relevant limitations into operational controls;
7. identify documentation gaps, contradictions, and unsupported claims;
8. reassess the artifacts after material changes; and
9. retain review evidence for audit and regulatory response.

## 74.3 Model card and system card distinctions

### Model card

A model card commonly describes a model-level capability. It may include:

- model name and version;
- developer or provider;
- intended uses;
- out-of-scope uses;
- training or evaluation information;
- performance results;
- known limitations;
- bias or fairness observations;
- safety and security testing;
- environmental or resource information; and
- contact or reporting channels.

### System card

A system card commonly describes a complete AI-enabled service or application, including model, prompts, retrieval components, filters, interfaces, business rules, human review, monitoring, and deployment constraints.

A system card should help reviewers understand how the full system behaves in context rather than evaluating the underlying model in isolation.

### Other equivalent artifacts

Providers may use different names, including:

- AI service description;
- technical fact sheet;
- responsible-AI report;
- safety report;
- deployment guide;
- transparency report;
- product specification;
- evaluation report; or
- limitations and acceptable-use statement.

The review process should assess content and evidence, not the document title.

## 74.4 Legal and compliance position

Model cards and system cards are useful governance artifacts, but they are not automatically equivalent to documentation required by law or contract.

The organization must determine whether the provider has supplied all information needed for the organization’s role and use case, including, where applicable:

- intended purpose;
- system capabilities and limitations;
- required input characteristics;
- expected output characteristics;
- performance and accuracy information;
- human-oversight measures;
- logging and monitoring information;
- cybersecurity and resilience information;
- foreseeable misuse;
- maintenance and update information;
- data-governance information;
- transparency information; and
- instructions necessary for safe and compliant use.

A voluntary provider artifact may contribute to this evidence set, but it must not be treated as a substitute without a documented legal and technical assessment.

## 74.5 Minimum artifact inventory

For every material AI system, maintain an artifact register containing:

| Field | Required record |
|---|---|
| Artifact title | Exact title supplied by provider |
| Artifact type | Model card, system card, fact sheet, report, or other |
| Provider | Legal entity and product owner |
| Model/system | Exact product, model, service, and configuration |
| Version | Version number, release, or publication date |
| Deployment mapping | Where the model or system is used internally |
| Intended audience | Technical, compliance, customer, regulator, or public |
| Source | Provider portal, contract repository, API documentation, or other |
| Reviewer | Named accountable reviewer |
| Review date | Date of assessment |
| Status | Accepted, conditionally accepted, incomplete, rejected, or expired |
| Next review | Scheduled reassessment date or change trigger |

## 74.6 Required content review

### 74.6.1 Identity and version

Confirm that the artifact identifies the exact model or system being procured or deployed.

Review questions:

- Does the name match the contracted service?
- Is the version identifiable?
- Does the provider use silent or automatic updates?
- Does the artifact cover the production configuration?
- Are regional, language, or customer-specific variants documented?
- Does the artifact apply to hosted, API, embedded, and fine-tuned versions equally?

### 74.6.2 Intended purpose

Determine whether the stated intended purpose matches the approved business use.

The review must identify:

- permitted decisions and recommendations;
- intended users;
- intended affected populations;
- operating environment;
- input types;
- output types;
- expected human involvement; and
- explicitly excluded uses.

A mismatch between provider intended purpose and organizational use must trigger escalation before deployment.

### 74.6.3 Performance claims

Performance claims must be specific enough to evaluate.

Review:

- metric definitions;
- test datasets;
- sample sizes;
- confidence intervals or uncertainty;
- benchmark relevance;
- language and regional coverage;
- population coverage;
- conditions under which testing occurred;
- performance degradation scenarios;
- known failure rates; and
- whether results were independently reproduced.

Do not accept an aggregate score when the use case depends on performance for a specific language, population, route, transaction type, or operational condition.

### 74.6.4 Limitations

Limitations should be converted into enforceable controls.

Common limitation categories include:

- hallucination or unsupported output;
- outdated knowledge;
- poor performance for certain languages or dialects;
- reduced performance for uncommon cases;
- sensitivity to prompt wording;
- vulnerability to adversarial input;
- inability to verify facts;
- insufficient explainability;
- bias or uneven performance;
- lack of accessibility;
- limited context window;
- inconsistent output;
- unreliable confidence scores;
- dependence on external tools or data sources;
- inability to handle emergencies; and
- unsuitable use in legally or operationally sensitive decisions.

For each material limitation, define:

| Required control field | Example |
|---|---|
| Limitation | The model may generate incorrect visa-entry requirements |
| Risk | Traveler receives inaccurate compliance information |
| Preventive control | Use approved authoritative travel-rule data source |
| Detective control | Sample and compare responses against source records |
| Human decision | Travel consultant confirms exceptions and complex cases |
| Stop condition | Disable automated advice when source data is unavailable |
| Owner | Director, Traveler Operations |
| Evidence | Test results, override logs, monitoring reports |

### 74.6.5 Training and data information

Where relevant and available, review:

- high-level training-data description;
- data sources and collection methods;
- rights and licensing statements;
- geographic and language representation;
- personal or special-category data considerations;
- data-quality controls;
- filtering and deduplication;
- known gaps;
- customer-data use;
- retention;
- whether prompts or outputs are used for model improvement; and
- mechanisms for deletion, restriction, or opt-out.

Absence of detailed training-data disclosure does not automatically prohibit use, but it may increase legal, privacy, bias, security, and evidentiary risk.

### 74.6.6 Safety, security, and misuse

Review whether the provider documents:

- abuse and misuse scenarios;
- prompt injection;
- data leakage;
- model extraction;
- malicious content generation;
- jailbreak resistance;
- tool or plugin risks;
- external-data poisoning;
- access controls;
- logging;
- vulnerability reporting;
- incident history;
- red-team results; and
- residual risk.

High-level assurances without evidence should be classified as unverified claims.

### 74.6.7 Human oversight

Confirm that the artifact explains how people can:

- understand the system’s role;
- review material outputs;
- detect abnormal behavior;
- challenge or correct results;
- override or disregard output;
- stop use safely;
- escalate uncertainty; and
- receive training appropriate to their responsibilities.

Human oversight must be operationally realistic. A statement that a person remains “in the loop” is insufficient when the person lacks time, information, authority, competence, or an effective override mechanism.

## 74.7 Claim classification

Every material provider statement should be classified as one of the following:

| Classification | Meaning |
|---|---|
| Verified | Supported by applicable independent or internal testing |
| Corroborated | Supported by multiple credible sources but not fully reproduced |
| Provider-attested | Stated by the provider without independent verification |
| Conditional | True only under documented assumptions or configurations |
| Contradicted | Inconsistent with testing, contracts, other documentation, or observed behavior |
| Unknown | Insufficient evidence to assess |

This classification must be visible in the review record. Provider-attested claims must not be represented internally or externally as independently verified facts.

## 74.8 Documentation quality criteria

Evaluate each artifact against the following criteria:

1. **Specificity:** Does it identify exact models, configurations, populations, and conditions?
2. **Completeness:** Does it cover material capabilities, limitations, risks, and dependencies?
3. **Consistency:** Does it agree with contracts, technical documentation, test reports, and observed behavior?
4. **Currency:** Is it current for the deployed version?
5. **Traceability:** Can claims be traced to evidence or responsible owners?
6. **Usability:** Can business, technical, compliance, and oversight personnel understand and apply it?
7. **Accessibility:** Is the information accessible to intended users?
8. **Change visibility:** Are changes documented and communicated?
9. **Auditability:** Can the organization demonstrate review, challenge, decision, and remediation?

## 74.9 Contradiction and gap management

### Contradictions

Examples include:

- contract says customer data are not used for training, while product documentation permits such use;
- model card lists English-only evaluation, while sales materials claim multilingual reliability;
- system card states human review is required, while the configured workflow automatically acts on output;
- provider says logs are retained, while the service tier does not expose them;
- documentation states a fixed model version, while the API routes requests dynamically.

Each contradiction must have:

- a unique issue identifier;
- affected documents and versions;
- risk assessment;
- accountable owner;
- provider clarification request;
- interim control;
- target resolution date; and
- closure evidence.

### Gaps

Classify documentation gaps as:

- **Critical:** prevents lawful, safe, or controlled deployment;
- **High:** materially limits risk assessment or oversight;
- **Medium:** requires remediation but can be controlled temporarily;
- **Low:** administrative or nonmaterial deficiency.

## 74.10 Acceptance decisions

### Accept

Use when documentation is sufficiently complete, applicable, and supported for the approved use.

### Conditional acceptance

Use only when:

- gaps are understood;
- interim controls are documented;
- the residual risk is accepted by authorized management;
- remediation has an owner and deadline; and
- the condition does not conceal a legal or safety blocker.

### Reject or stop

Reject or suspend deployment when:

- the artifact does not apply to the deployed version;
- material limitations are concealed or contradicted;
- intended use is outside the provider’s supported purpose;
- required oversight cannot be implemented;
- significant performance claims cannot be substantiated;
- critical safety, security, privacy, discrimination, or rights risks remain uncontrolled;
- the provider refuses essential clarification or evidence; or
- the organization cannot determine its legal or operational responsibilities.

## 74.11 Change-management triggers

Re-review model and system documentation when:

- the model version changes;
- the provider changes architecture, training, safety controls, or data practices;
- the organization fine-tunes, adapts, or materially modifies the system;
- the intended purpose changes;
- a new language, market, population, or channel is added;
- a material incident or complaint occurs;
- performance drifts;
- an external dependency changes;
- provider documentation is revised;
- regulation or authoritative guidance changes; or
- contractual terms change.

A material change must not be accepted solely through a provider release note. The organization must reassess impact and required controls.

## 74.12 GlobalWay Travel Services example

### Scenario

GlobalWay purchases a generative-AI service to assist travel consultants with itinerary summaries and traveler communications.

The provider supplies a model card stating that the model performs well on general English-language summarization but may produce unsupported factual details and has limited evaluation for airline disruption, visa, medical, and accessibility scenarios.

### Requirement

GlobalWay must assess whether the documentation supports the intended use and convert material limitations into controls.

### Plain-language explanation

The model may help draft a clear itinerary summary, but it must not become the authoritative source for travel restrictions, medical advice, accessibility commitments, refund rights, or emergency instructions.

### Control activity

GlobalWay shall:

1. restrict the model to drafting and summarization;
2. retrieve itinerary data from approved booking systems;
3. require travel consultants to verify material facts;
4. prohibit unsourced visa, medical, legal, and safety advice;
5. display source information where feasible;
6. test English, Spanish, and Portuguese outputs separately;
7. monitor unsupported factual additions;
8. provide an accessible correction and escalation channel;
9. suspend automated generation when authoritative data are unavailable; and
10. reassess the service after provider model updates.

### Evidence

- approved use-case record;
- model and system cards;
- provider-documentation review;
- limitation-to-control mapping;
- multilingual test results;
- human-review procedure;
- sampled output reviews;
- incident and correction logs;
- change assessments; and
- approval decision.

### Audit test

Select the deployed version of the itinerary-assistance service. Confirm that the reviewed artifact matches the actual model and configuration. Trace each material limitation to an implemented control. Sample generated summaries and verify that required human review occurred, factual sources were used, and prohibited advice was not issued without escalation.

## 74.13 Control library

| Control ID | Control | Frequency | Owner | Evidence |
|---|---|---|---|---|
| EUAI-MSC-01 | Maintain current model/system artifact register | Continuous | AI Governance | Artifact register |
| EUAI-MSC-02 | Map artifacts to deployed versions and configurations | At intake and change | Technical Owner | Configuration mapping |
| EUAI-MSC-03 | Classify provider claims by evidence status | At review | Risk/Compliance | Claim assessment |
| EUAI-MSC-04 | Convert material limitations into controls | Before deployment and change | Business Owner | Limitation-control map |
| EUAI-MSC-05 | Resolve contradictions and material gaps | Before approval | Procurement/Legal/Technical | Issue log and closure evidence |
| EUAI-MSC-06 | Independently validate critical claims | Risk-based | Validation Team | Test reports |
| EUAI-MSC-07 | Reassess after material changes | Event-driven | Change Authority | Change assessment |
| EUAI-MSC-08 | Retain review and approval evidence | Continuous | Records Owner | Evidence repository |

## 74.14 Metrics

Recommended metrics include:

- percentage of material AI systems with current model or system documentation;
- percentage of artifacts mapped to exact deployed versions;
- number of provider-attested claims awaiting validation;
- number and age of unresolved contradictions;
- number of critical and high documentation gaps;
- percentage of material limitations mapped to controls;
- percentage of model changes reviewed before production use;
- number of incidents associated with undocumented limitations;
- average provider response time to documentation requests; and
- percentage of expired artifacts removed or renewed.

Metrics must not reward superficial document collection. Quality, applicability, evidence, and control effectiveness matter more than artifact count.

## 74.15 Audit programme

Auditors should:

1. select a risk-based sample of AI systems;
2. identify the actual model, service, and configuration in production;
3. obtain the corresponding model card, system card, and related documentation;
4. confirm version and scope alignment;
5. evaluate completeness and consistency;
6. trace material claims to evidence;
7. review limitation-to-control mappings;
8. test whether controls operate in practice;
9. inspect contradictions, gaps, exceptions, and approvals;
10. review change events and reassessment records; and
11. determine whether provider claims were represented accurately to management, customers, auditors, and regulators.

## 74.16 Formal process diagram

### Figure 74-1 — Model and System Documentation Assurance Flow

```text
Receive provider artifact
          |
          v
Identify model, system, version, configuration, and intended use
          |
          v
Confirm artifact applies to deployed service
          |
          +---- No ----> Stop / obtain correct documentation
          |
         Yes
          |
          v
Extract claims, assumptions, exclusions, limitations, and dependencies
          |
          v
Classify evidence: verified / corroborated / provider-attested / unknown
          |
          v
Compare with contracts, testing, observed behavior, and other documents
          |
          +---- Contradiction or critical gap ----> Escalate / control / reject
          |
          v
Map material limitations to operational controls
          |
          v
Approve / conditionally approve / reject
          |
          v
Monitor changes, incidents, drift, and documentation updates
```

**Accessibility description:** The flow begins with receipt of a provider artifact, verifies that it matches the deployed model and configuration, extracts and classifies claims, compares them with independent evidence, escalates contradictions or critical gaps, maps limitations to controls, records an approval decision, and continues monitoring for changes.

## 74.17 Human-concern graphic specification

### Figure 74-2 — “The Polished Card and the Real Trip”

An original professional workplace illustration shows a procurement team viewing a polished model card on one screen while a travel consultant handles a real disruption involving a canceled flight, a wheelchair request, a visa question, and a stranded family. A compliance reviewer connects each documented limitation to a visible operational safeguard.

The message is: **Documentation becomes useful only when limitations are translated into protections for real people.**

The graphic must be respectful, accessible, non-comedic, and free of copied characters or recognizable commercial styles.

## 74.18 Management checklist

Before approving reliance on a model card, system card, or equivalent artifact, confirm:

- [ ] Exact model, system, version, and configuration are identified.
- [ ] Intended purpose matches the approved use.
- [ ] Material claims are classified by evidence status.
- [ ] Performance claims are relevant to the actual population and environment.
- [ ] Limitations, exclusions, and foreseeable misuse are documented.
- [ ] Material limitations are mapped to controls and owners.
- [ ] Human oversight is practical and testable.
- [ ] Security, privacy, data-use, bias, and accessibility issues are addressed.
- [ ] Contradictions and gaps are logged and resolved or formally accepted.
- [ ] Provider updates trigger reassessment.
- [ ] The artifact is not being treated as a substitute for required legal or technical documentation.
- [ ] Evidence is retained for audit and regulatory response.

## 74.19 Key takeaway

Model cards and system cards can improve transparency, but their value depends on disciplined review. The organization must verify that the artifact applies to the deployed system, distinguish claims from evidence, convert limitations into controls, and reassess the documentation whenever the model, system, use, or risk changes.
