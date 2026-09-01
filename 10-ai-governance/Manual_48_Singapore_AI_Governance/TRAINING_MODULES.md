# Manual 48 — Singapore AI Governance Training Modules

**Controlled English draft — Stage 3**  
**Currentness baseline:** 1 September 2026  
**Purpose:** convert Singapore's practical AI-governance ecosystem into an enterprise operating model without treating voluntary guidance or assurance tools as binding law or certification.

## Module 1 — Singapore's practical AI-governance ecosystem

### Learning objective
Distinguish the roles of the Model AI Governance Framework, the Generative AI framework, AI Verify, the Agentic AI framework and related assurance/testing initiatives.

### Operating rule
For every source used in a control decision, label it as one of: governance guidance, assurance/testing framework, implementation example, proposed standardisation work, or binding law from another jurisdiction. Do not collapse those categories.

### Evidence
- framework inventory;
- source/version register;
- applicability note;
- non-equivalence statement.

## Module 2 — Foundational Model AI Governance Framework

Operationalise four enduring organisational themes:

1. internal governance structures and accountability;
2. appropriate human involvement in AI-augmented decisions;
3. operations management across the AI lifecycle; and
4. stakeholder interaction and communication.

### Control pattern
**Policy → accountable owner → risk assessment → lifecycle control → evidence → testing → remediation.**

### Minimum evidence
- AI policy and governance charter;
- RACI / accountable executive and system owner;
- AI inventory and use-case classification;
- documented human-oversight model;
- data/model lifecycle procedures;
- stakeholder communication plan.

## Module 3 — Human involvement and decision accountability

### Training outcome
Participants must be able to justify the selected level of human involvement rather than merely state that a human is 'in the loop'.

### Control questions
- What decision or action is the AI influencing?
- What harm could occur if the AI is wrong?
- Is the human able, trained and authorised to intervene?
- Is the review point early enough to prevent harm?
- Is the information presented to the reviewer sufficient for meaningful judgment?
- Is automation bias monitored?

### Evidence
- decision-rights matrix;
- approval thresholds;
- override/stop procedure;
- reviewer training record;
- sampled approval logs;
- override and exception metrics.

## Module 4 — Operations management and lifecycle controls

Establish controls for data quality, model/system validation, robustness, monitoring, tuning/change, incident response and retirement.

### Required operating artifacts
- lifecycle control plan;
- data lineage and quality evidence;
- validation/test report;
- monitoring thresholds;
- change/revalidation triggers;
- incident and rollback procedure;
- retirement/decommission record.

## Module 5 — Stakeholder interaction and communication

Train teams to communicate AI use clearly, provide understandable information, maintain feedback channels where appropriate and avoid claims that exceed evidence.

### Evidence
- user notices;
- model/system limitations statement;
- feedback/complaint process;
- communications approval record;
- claims register.

## Module 6 — Generative AI governance

Treat the GenAI framework as an ecosystem extension to foundational governance. Enterprise training focuses on the dimensions most directly actionable by deployers and developers:

- accountability and governance;
- data and provenance;
- trusted development and deployment;
- incident reporting and monitoring;
- testing and assurance;
- security and safety;
- content provenance and transparency;
- third-party/supply-chain responsibility; and
- societal/user impact considerations.

### GenAI control questions
- What training, retrieval, prompt and tool data enter the system?
- How are sensitive data and confidential sources constrained?
- What evaluation set demonstrates acceptable performance?
- What hallucination, toxicity, security and privacy failure modes are tested?
- How are generated outputs identified or qualified where appropriate?
- How are model/provider changes detected and revalidated?

## Module 7 — AI Verify assurance and testing

### Training principle
AI Verify is used as an assurance/testing mechanism, not as proof that an AI system is universally safe, unbiased, compliant or certified.

### Enterprise workflow
1. define the claims to be assessed;
2. identify applicable process checks and technical tests;
3. document data, test conditions and limitations;
4. execute reproducible tests where feasible;
5. review failures and residual risk;
6. record management disposition;
7. re-test after material change.

### Evidence
- test plan;
- process-check responses;
- technical test outputs;
- reproducibility record;
- exception log;
- remediation plan;
- management sign-off.

## Module 8 — Agentic AI: assess and bound risks upfront

Use the current Agentic AI framework as the primary operating reference for systems that can plan, select tools, interact with other agents or execute actions.

### Required assessment dimensions
- intended use and prohibited use;
- autonomy level;
- tool/API access;
- data access and sensitivity;
- financial/operational authority;
- external communication capability;
- code execution capability;
- multi-agent interaction;
- third-party-agent dependency;
- reversibility of actions;
- potential blast radius.

### Controls
- capability inventory;
- least-privilege access;
- action allowlist/denylist;
- transaction/value thresholds;
- environment segmentation;
- rate/volume limits;
- safe default on uncertainty.

## Module 9 — Agentic AI: meaningful human accountability

Human approval must be tied to **significant checkpoints** rather than cosmetic review.

### Examples of significant checkpoints
- release to production;
- access to a new high-impact tool or dataset;
- external payment or contractual action;
- privileged system change;
- irreversible deletion;
- safety/security exception;
- material model/toolchain change;
- escalation after abnormal behaviour.

### Evidence
- checkpoint catalogue;
- approval policy;
- identity of approver;
- approval timestamp and context;
- rejected/overridden action log;
- escalation record.

## Module 10 — Agentic AI: lifecycle technical and process controls

### Baseline controls
- authenticated agent/service identity;
- least privilege and scoped credentials;
- tool allowlisting;
- input/output validation;
- prompt/tool boundary protection;
- sandboxing where appropriate;
- action logging and provenance;
- anomaly monitoring;
- rate limiting;
- kill switch / containment mechanism;
- dependency inventory;
- third-party-agent risk assessment;
- change control and revalidation.

### Multi-agent emphasis
Document delegation chains, inter-agent permissions, shared-memory boundaries, conflict-resolution logic and how responsibility is reconstructed across agent interactions.

## Module 11 — Agentic AI: end-user transparency and responsibility

Users should understand when they are interacting with an agent, the agent's role and limits, the kinds of actions it can take, what review is expected of the user and where to report problems.

### Evidence
- agent identity disclosure;
- capability/limitation notice;
- user training;
- feedback channel;
- escalation instructions;
- sampled interaction review.

## Module 12 — Third-party AI and agent supply chain

### Control objectives
- know which provider/model/agent/tool is being used;
- understand material dependencies and data flows;
- contract for security, privacy, change notification and incident cooperation;
- monitor provider changes;
- revalidate after material model, API, policy or capability changes;
- prevent inherited credentials or excessive privileges.

### Evidence
- vendor risk assessment;
- architecture/data-flow diagram;
- contract/control mapping;
- provider-change log;
- exit/continuity plan.

## Module 13 — Automation bias and operational challenge

The May 2026 Agentic AI update specifically strengthens practical attention to automation bias.

### Training exercises
- identify decisions where users are likely to defer to AI output;
- design counter-signals, independent checks or forced review;
- measure override rates and reviewer disagreement;
- investigate near-zero override rates where independent judgment is expected.

## Module 14 — Assurance, evidence and auditability

Every major control must be testable.

### Evidence rule
For each control maintain:

**Source concept → organisational interpretation → control objective → control owner → implementation → evidence → test method → result → finding → remediation → residual risk.**

## Module 15 — Cross-framework mapping without false equivalence

Map Singapore guidance to Manual 46 universal controls and, where useful, to EU AI Act, ISO/IEC 42001 and NIST AI RMF control themes. Mapping is for operational reuse, not a statement that satisfying one framework automatically satisfies another.

### Required mapping fields
- Singapore source concept;
- target framework concept;
- relationship type: direct / partial / supporting / contextual;
- important differences;
- additional evidence required;
- legal/standards caveat.

## Module 16 — Enterprise implementation blueprint

### 30-day foundation
- establish AI governance owner and inventory;
- classify active AI/GenAI/agentic use cases;
- identify highest-risk agentic deployments;
- define significant human checkpoints;
- establish evidence repository.

### 60-day operating model
- implement lifecycle controls;
- perform vendor and tool-access reviews;
- establish testing/assurance cadence;
- formalise incident and containment procedures;
- train reviewers and end users.

### 90-day assurance cycle
- execute independent sampling/testing;
- validate high-risk agent/tool permissions;
- review automation-bias indicators;
- close findings;
- produce governance dashboard and management attestation.

## Completion standard
A learner completes Manual 48 when they can take a Singapore governance concept and produce a defensible enterprise control, evidence set, test procedure and limitation statement without claiming legal equivalence or certification.