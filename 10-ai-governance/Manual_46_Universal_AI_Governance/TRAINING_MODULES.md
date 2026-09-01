# Manual 46 — Universal AI Governance Foundation
## Controlled Training Modules

**Status:** CONTROLLED DEVELOPMENT  
**Relationship:** Substantive training companion to the Manual 46 controlled-English master.

## Learning design

Manual 46 is intended to create practitioner capability, not memorization. Each module follows a repeatable pattern:

**Concept → Decision → Control → Evidence → Challenge → Exercise**

A learner should be able to apply the governance model to predictive AI, machine learning, generative AI, RAG, foundation-model services, embedded AI and agentic systems without depending on one legal regime or framework.

---

## Module 1 — Establish the governance mandate

### Objective
Define why the organization governs AI and where accountability sits.

### Practitioner tasks
- Identify executive sponsorship.
- Define AI-governance scope and boundaries.
- Connect AI governance to enterprise risk appetite.
- Establish decision rights and escalation authority.
- Distinguish first-line ownership, second-line oversight and third-line assurance.

### Required evidence
- AI governance charter.
- Approved policy hierarchy.
- Committee terms of reference.
- Decision-rights matrix.
- Risk-appetite linkage.

### Challenge questions
- Who can stop deployment?
- Who may accept residual AI risk?
- What happens when business and control functions disagree?
- Is internal audit independent from control ownership?

### Exercise
Design a governance charter for an organization introducing AI across HR, customer service, software development and finance.

---

## Module 2 — Build the AI inventory

### Objective
Create a reliable system of record for governed AI.

### Practitioner tasks
- Define what qualifies as an AI use case or AI system.
- Identify shadow AI and embedded vendor AI.
- Record business and technical ownership.
- Capture models, providers, data, tools, integrations and deployment geography.
- Track lifecycle and approval state.

### Minimum inventory record
- unique identifier;
- business purpose;
- business owner;
- technical owner;
- model/provider/version;
- deployment environment;
- users and affected populations;
- data categories and provenance;
- third parties;
- jurisdictional footprint;
- risk tier;
- autonomy level;
- validation state;
- human oversight;
- approval state;
- monitoring state;
- last material change;
- retirement state.

### Evidence test
A reviewer should be able to identify every production AI use case and its accountable owner without relying on tribal knowledge.

---

## Module 3 — Classify risk, impact and autonomy

### Objective
Determine governance intensity before detailed controls are selected.

### Classification dimensions
- potential impact on people and rights;
- health and safety impact;
- business criticality;
- financial exposure;
- data sensitivity;
- cybersecurity privilege;
- autonomy;
- reversibility;
- scale;
- external versus internal use;
- legal/regulatory classification;
- dependency and concentration risk;
- transparency/contestability need.

### Practical outcome
The classification determines:
- assessment depth;
- required control functions;
- validation independence;
- approval authority;
- human-oversight requirements;
- monitoring frequency;
- revalidation triggers.

### Anti-pattern
Do not classify an AI system as low risk merely because it is purchased from a major vendor.

---

## Module 4 — Perform AI risk and impact assessment

### Objective
Translate context into explicit risks and treatment decisions.

### Assessment domains
- strategic/business;
- legal/regulatory;
- human-rights and societal impact;
- safety;
- model performance;
- data quality/provenance;
- privacy;
- cybersecurity;
- misuse/abuse;
- bias/fairness where relevant;
- transparency/explainability;
- intellectual property;
- third-party/supply chain;
- resilience;
- autonomy/agentic action;
- fraud/financial;
- reputation.

### Assessment output
For each material risk record:
**Scenario → Cause → Impact → Inherent Risk → Control → Residual Risk → Owner → Decision**

### Quality criterion
Risk statements must describe plausible adverse outcomes, not vague labels such as “AI risk.”

---

## Module 5 — Govern data and knowledge

### Objective
Ensure AI data and knowledge sources are authorized, traceable and fit for purpose.

### Control topics
- lineage and provenance;
- authorized purpose;
- quality and representativeness;
- minimization;
- sensitive-data handling;
- retention and deletion;
- training/evaluation separation where relevant;
- RAG corpus approval;
- retrieval authorization;
- correction and withdrawal;
- vendor data-use terms.

### GenAI extension
Treat prompts, context windows, vector stores, retrieval indexes, embeddings and fine-tuning datasets as governed information assets where appropriate.

---

## Module 6 — Secure the AI system

### Objective
Integrate security throughout the AI lifecycle.

### Threat surfaces
- model endpoints;
- APIs;
- identity and authorization;
- secrets and credentials;
- training/inference pipelines;
- prompts and system instructions;
- retrieval sources;
- tool/plugin connections;
- agent permissions;
- model and dependency supply chains;
- telemetry and logs.

### Security outcomes
- least privilege;
- secure secrets handling;
- input/output validation;
- prompt-injection resistance;
- data-exfiltration prevention;
- dependency integrity;
- attack detection;
- containment and recovery.

---

## Module 7 — Design meaningful human oversight

### Objective
Avoid ceremonial “human in the loop” claims.

### Oversight test
A human overseer must have:
1. sufficient information;
2. relevant competence;
3. practical time to review;
4. authority to intervene;
5. a functioning intervention mechanism.

### Controls
- defined approval checkpoints;
- override authority;
- escalation criteria;
- stop/suspend capability;
- override logging;
- reviewer training;
- workload/capacity controls.

### Failure mode
A human who is expected to approve thousands of AI decisions without meaningful review capacity is not an effective control.

---

## Module 8 — Test, evaluate, verify and validate

### Objective
Demonstrate that the AI system is fit for its intended use and controlled for foreseeable failure modes.

### Test domains
- intended performance;
- robustness;
- edge cases;
- misuse/abuse;
- security;
- privacy;
- fairness where relevant;
- explainability;
- human factors;
- failure recovery;
- GenAI factuality/confabulation;
- RAG retrieval quality;
- agent action boundaries.

### Validation independence
Independence should increase with materiality. High-impact systems require meaningful challenge beyond the development team.

---

## Module 9 — Establish lifecycle approval gates

### Objective
Convert governance from advice into enforceable decisions.

### Core gates
**Intake → Inventory → Classification → Assessment → Design/Acquisition Review → Validation → Approval → Deployment → Monitoring → Change/Revalidation → Retirement**

### Gate decision types
- approve;
- approve with conditions;
- reject;
- defer pending evidence;
- exception with time-bound risk acceptance;
- suspend;
- retire.

### Evidence requirement
Each decision records the approver, date, scope, conditions, evidence considered and residual-risk disposition.

---

## Module 10 — Govern third-party AI

### Objective
Manage AI risk even when the organization does not build the model.

### Due-diligence areas
- provider governance;
- security and privacy;
- data use;
- model limitations;
- subcontractors;
- geographic processing;
- change notification;
- incident notification;
- assurance evidence;
- service continuity;
- contractual allocation of responsibility;
- exit and portability.

### Key principle
Vendor adoption changes the control allocation; it does not eliminate organizational accountability.

---

## Module 11 — Govern generative AI

### Objective
Extend the universal model for probabilistic content generation and retrieval-based systems.

### Additional control areas
- hallucination/confabulation;
- prompt injection and indirect injection;
- sensitive-data leakage;
- retrieval governance;
- output verification;
- content provenance and labeling where applicable;
- intellectual-property considerations;
- red teaming;
- guardrails;
- safe fallback behavior.

---

## Module 12 — Govern agentic AI

### Objective
Control systems that can choose and execute actions.

### Core control areas
- agent identity;
- bounded purpose;
- authorization;
- least privilege;
- tool/API allowlists;
- credential isolation;
- transaction/resource limits;
- human approval checkpoints;
- separation of duties;
- action provenance;
- runtime monitoring;
- emergency stop capability;
- multi-agent delegation controls;
- revalidation after model, prompt, tool, permission or data changes.

### Practitioner rule
For agents, evaluate both **what the system can say** and **what the system can do**.

---

## Module 13 — Monitor AI continuously

### Objective
Detect when assumptions, performance or risk conditions change.

### Example KRIs/KPIs
- performance drift;
- error/failure rates;
- override rates;
- harmful-output rates;
- security events;
- privacy events;
- unauthorized tool use;
- exception volume;
- unresolved findings;
- vendor/model-version changes;
- overdue revalidation;
- incident recurrence.

### Monitoring design
Every monitored metric should have an owner, threshold, cadence, evidence source and predefined response.

---

## Module 14 — Manage incidents and change

### Objective
Ensure AI failures and material changes trigger controlled response.

### Incident lifecycle
**Detect → Contain → Preserve Evidence → Assess Impact → Escalate/Notify → Remediate → Validate → Learn**

### Material-change triggers
- model change;
- model-version change;
- provider change;
- prompt/system-instruction change;
- data-source change;
- retrieval change;
- tool/API addition;
- permission increase;
- new user population;
- new geography;
- new business purpose;
- autonomy increase.

---

## Module 15 — Build evidence and assurance

### Objective
Make governance demonstrable.

### Universal evidence chain
**Requirement or Risk → Control Objective → Control Activity → Owner → Trigger/Frequency → Evidence → Test Procedure → Exception → Remediation → Residual-Risk Decision**

### Assurance levels
- first-line self-assessment;
- second-line challenge/testing;
- independent validation;
- internal audit;
- external assurance where appropriate.

### Completion standard
A learner can defend not only that a control exists, but that it operated and produced evidence.

---

## Module 16 — Executive and board governance

### Objective
Translate detailed AI control data into decision-useful governance information.

### Executive reporting themes
- inventory growth and materiality;
- high-risk/high-impact use cases;
- exceptions and residual-risk acceptances;
- overdue validation/revalidation;
- incidents;
- vendor concentration;
- regulatory exposure;
- control failures;
- emerging GenAI/agentic risk;
- risk trends against appetite.

### Board-level question
Can leadership determine where the organization is taking material AI risk and whether that risk remains within appetite?

---

## Capstone exercise

Given a proposed customer-facing AI assistant that uses a third-party foundation model, RAG over internal knowledge, personal customer data and tools capable of modifying customer records:

1. Define the system boundary.
2. Identify accountable owners.
3. Populate the inventory record.
4. Classify impact and autonomy.
5. Identify material risks.
6. Define security/privacy/data controls.
7. Define human oversight.
8. Design validation evidence.
9. Define approval gates.
10. Define runtime monitoring.
11. Define incident/change triggers.
12. Identify third-party requirements.
13. Specify evidence retained.
14. State conditions under which deployment should be suspended.

The exercise should be answerable using the universal model without relying on any one jurisdiction or standard.