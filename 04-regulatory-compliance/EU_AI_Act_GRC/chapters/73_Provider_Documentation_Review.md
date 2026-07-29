# 73. Provider Documentation Review

## 73.1 Purpose

Provider documentation is a primary source of evidence for understanding an AI system’s intended purpose, capabilities, limitations, risks, controls, dependencies, and change history. It must be reviewed critically rather than accepted as a complete or neutral description of the system.

This chapter establishes a practical method for assessing whether provider documentation is sufficient, internally consistent, current, usable, and traceable to the organization’s own risk and compliance decisions.

## 73.2 Core principle

**Documentation may support a decision, but it does not replace independent judgment, testing, or accountability.**

A deployer remains responsible for determining whether the system is appropriate for its intended use, whether additional controls are necessary, and whether deployment should stop when provider evidence is incomplete or unreliable.

## 73.3 Documentation in scope

The review should cover, where applicable:

- instructions for use;
- intended purpose and prohibited uses;
- model cards and system cards;
- technical documentation;
- architecture and dependency descriptions;
- data sources and data-governance information;
- performance, accuracy, robustness, and bias evaluations;
- cybersecurity and adversarial-testing results;
- human-oversight requirements;
- logging and monitoring specifications;
- transparency and accessibility information;
- conformity and registration records;
- post-market monitoring information;
- serious-incident and vulnerability notices;
- change logs, release notes, and deprecation notices;
- subcontractor and downstream-provider information;
- retention, deletion, and model-training terms;
- certificates, attestations, and independent audit reports.

## 73.4 Provider documentation review workflow

### Step 1 — Inventory required documents

The business owner, procurement team, legal function, privacy function, security function, and AI governance lead define the minimum evidence package based on the use case, risk tier, and GlobalWay’s role.

### Step 2 — Confirm identity and version

Verify:

- provider legal entity;
- system and model name;
- model or service version;
- release date;
- document version and date;
- applicable region and deployment environment;
- whether the document applies to the contracted configuration.

### Step 3 — Test completeness

Compare the received package with the evidence requirements. Missing documents must be recorded explicitly rather than treated as not applicable without justification.

### Step 4 — Test internal consistency

Identify contradictions among marketing claims, instructions, model cards, contracts, security documents, test reports, and release notes.

### Step 5 — Test relevance

Confirm that the evidence addresses GlobalWay’s actual intended use, affected people, data, interfaces, languages, operating conditions, and foreseeable misuse.

### Step 6 — Test credibility

Assess whether claims are supported by reproducible methods, meaningful samples, stated limitations, qualified reviewers, dates, and traceable results.

### Step 7 — Identify gaps and compensating controls

Classify gaps as:

- acceptable with documented rationale;
- acceptable only with compensating controls;
- requiring provider remediation;
- deployment-blocking.

### Step 8 — Approve, conditionally approve, or reject

The accountable owner records the decision, conditions, evidence relied upon, unresolved limitations, review date, and required monitoring.

## 73.5 Documentation-quality criteria

| Criterion | Review question | Evidence |
|---|---|---|
| Completeness | Are all required documents present? | Evidence checklist |
| Currency | Do the documents match the current service version? | Version and release records |
| Consistency | Do documents contradict one another? | Reconciliation log |
| Specificity | Do claims address the actual use case? | Use-case mapping |
| Traceability | Can claims be linked to tests, data, or controls? | Test IDs, reports, references |
| Reproducibility | Can important results be repeated or independently checked? | Methodology and test materials |
| Limitations | Are known weaknesses stated clearly? | Limitations register |
| Accessibility | Can intended users understand and use the documentation? | Accessibility review |
| Accountability | Are owners, contacts, and escalation routes identified? | Responsibility matrix |

## 73.6 Red flags

Escalate when documentation:

- relies primarily on marketing language;
- makes broad claims without methods or test evidence;
- omits known limitations;
- uses outdated model or service versions;
- reports only aggregate performance that hides subgroup variation;
- excludes relevant languages, regions, disability contexts, or edge cases;
- conflicts with contractual terms or observed system behaviour;
- uses unexplained proprietary scores;
- refers to unavailable attachments or external reports;
- changes materially without notification;
- treats provider confidentiality as a reason to withhold evidence necessary for safe use;
- fails to identify material subcontractors or dependencies.

## 73.7 GlobalWay example — traveler recommendation platform

GlobalWay considers a provider’s AI itinerary-recommendation platform. The provider supplies a model card claiming high recommendation quality, but the report:

- covers only English-language users;
- does not include travelers requiring accessible accommodation;
- does not describe disruption or emergency scenarios;
- uses a model version older than the contracted service;
- provides no evidence for the claim that recommendations are unbiased.

GlobalWay does not accept the model card as sufficient. It requires current evidence, runs its own multilingual and accessibility tests, limits initial deployment, adds human review for complex itineraries, and records the residual risk.

## 73.8 Contradiction management

Contradictions must be logged and resolved before approval. Examples include:

- a model card says customer data is not used for training, while the service terms allow reuse;
- instructions say a human must approve certain outputs, while the interface provides no practical review step;
- marketing material claims real-time accuracy, while technical documentation states delayed data refresh;
- a security report covers one hosting region while the contracted service uses another.

The stricter interpretation should govern temporarily until the provider supplies reliable clarification.

## 73.9 Change control

Provider documentation must be reassessed when there is a material change to:

- model version;
- intended purpose;
- data sources;
- training or fine-tuning process;
- hosting region;
- subcontractors;
- safety controls;
- performance or bias profile;
- human-oversight design;
- API behaviour;
- retention or training terms;
- cybersecurity posture;
- known limitations.

No material provider change should be treated as routine merely because the commercial service name remains unchanged.

## 73.10 Control activities

| Control ID | Control activity | Owner | Frequency | Evidence |
|---|---|---|---|---|
| EUAI-DOC-73-01 | Maintain a required-document checklist by vendor risk tier | AI Governance | Annual and on change | Checklist |
| EUAI-DOC-73-02 | Verify document identity, version, and applicability | Technical Owner | Each review | Version record |
| EUAI-DOC-73-03 | Perform completeness and contradiction review | Procurement and Legal | Pre-contract and renewal | Review log |
| EUAI-DOC-73-04 | Map provider claims to independent evidence | Risk and Security | Pre-deployment | Evidence matrix |
| EUAI-DOC-73-05 | Record limitations and compensating controls | Business Owner | Pre-deployment and on change | Limitations register |
| EUAI-DOC-73-06 | Reassess documentation after material change | Change Advisory Function | On change | Change assessment |
| EUAI-DOC-73-07 | Track unresolved provider evidence requests | Vendor Management | Monthly | Gap tracker |

## 73.11 Evidence package

Retain:

- received provider documents;
- document inventory and version record;
- completeness checklist;
- contradiction log;
- provider questions and responses;
- independent test results;
- limitations and residual-risk register;
- compensating-control approvals;
- deployment decision;
- change assessments;
- review and renewal history.

Evidence should preserve the exact provider document version relied upon. A live web page alone is insufficient where content may change without notice.

## 73.12 Audit tests

Auditors should:

1. select a sample of active AI vendors;
2. obtain the documentation package used for approval;
3. confirm the package matches the deployed version and configuration;
4. compare required and received evidence;
5. test whether contradictions and limitations were documented;
6. verify independent testing where provider claims were material;
7. confirm approval conditions were implemented;
8. inspect change records for later provider updates;
9. verify unresolved evidence gaps were escalated;
10. assess whether the final decision was supported and traceable.

## 73.13 Metrics

Track:

- percentage of vendors with complete evidence packages;
- average age of critical provider documents;
- unresolved documentation gaps by severity;
- contradictions identified and resolved;
- percentage of material claims independently tested;
- provider changes reviewed before deployment;
- conditional approvals overdue for reassessment;
- incidents linked to undocumented provider limitations.

## 73.14 Stop and escalation conditions

Stop deployment or materially restrict use when:

- the intended purpose is unclear;
- the deployed version cannot be identified;
- critical safety, security, bias, privacy, or oversight evidence is absent;
- documentation conflicts with observed behaviour;
- provider limitations prevent responsible operation;
- change history is unavailable;
- the provider refuses evidence necessary for lawful or safe deployment;
- compensating controls cannot reduce risk to an approved level.

## 73.15 Graphic specification

### Figure 73-1 — Provider Documentation Evidence Funnel

**Type:** Formal process diagram.

**Flow:**

`Document intake → Identity and version check → Completeness review → Contradiction review → Relevance and credibility testing → Gap classification → Independent validation → Approve / condition / reject → Continuous change monitoring`

**Purpose:** Show that provider documentation is filtered through progressively stronger assurance steps before it can support a deployment decision.

**Accessibility:** Use numbered stages, high contrast, text labels in addition to icons, and a linear reading order. Do not rely on colour alone.

**Alt text:** A nine-stage assurance funnel showing provider documents moving from intake through version verification, completeness, contradiction, relevance, credibility, gap analysis, independent testing, decision, and ongoing monitoring.

## 73.16 Practical conclusion

Provider documentation is necessary but not self-validating. The organization must verify what the documentation covers, what it omits, whether it matches the deployed system, and whether important claims withstand independent scrutiny.

GlobalWay may use provider evidence to inform its decision, but responsibility for deployment remains with the people who approve, operate, monitor, and govern the system.