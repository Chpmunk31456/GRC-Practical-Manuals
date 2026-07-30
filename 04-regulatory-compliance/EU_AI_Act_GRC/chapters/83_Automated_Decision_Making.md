# Chapter 83 — Automated Decision-Making

## Purpose

Automated decision-making creates a distinct governance risk because an AI system may move from supporting a person to determining an outcome for that person. This chapter establishes controls for identifying, approving, operating, monitoring, challenging, and stopping AI-enabled decisions that may produce legal or similarly significant effects.

The governing principle is:

> AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

This chapter should be read together with the chapters on GDPR integration, privacy by design, special-category data, human oversight, transparency, logging, incident management, and fundamental-rights impact assessment.

## 1. Requirement

Organizations must determine whether an AI-enabled process:

1. makes a decision about an identifiable person;
2. is based solely or materially on automated processing, including profiling;
3. produces a legal effect or similarly significant effect;
4. falls within a permitted legal basis or exception;
5. provides effective safeguards, including human intervention, the ability to express a view, and the ability to contest the outcome;
6. is subject to meaningful human oversight rather than ceremonial approval;
7. records the evidence necessary to explain, review, challenge, correct, suspend, and audit the decision.

The GDPR and the EU AI Act must be assessed separately and then integrated. A process may comply with one instrument while still failing the other.

## 2. Plain-language explanation

An automated decision is not limited to a system that displays a final “approve” or “deny” result. It may also exist where:

- a score automatically determines eligibility;
- a recommendation is followed by staff almost every time;
- a workflow hides or deprioritizes people without a realistic review route;
- a model determines price, access, priority, service level, employment outcome, fraud status, creditworthiness, insurance treatment, or another consequential result;
- a human technically clicks “approve” but lacks the time, information, authority, competence, or independence to disagree.

The presence of a human in the workflow does not automatically make the decision human. The review must be real, informed, and capable of changing the outcome.

## 3. Travel-agency example

GlobalWay Travel Services uses an AI system to prioritize customers during widespread flight disruption. The system assigns a service-priority score using ticket class, loyalty status, connection risk, traveler location, recorded accessibility needs, and predicted rebooking difficulty.

### AI may do

- identify disrupted itineraries;
- estimate missed-connection risk;
- rank cases for operational attention;
- propose rebooking options;
- identify missing information;
- flag cases for urgent review.

### AI may not do alone

- deny assistance;
- remove a traveler from the service queue;
- reduce legally required assistance;
- infer a disability or health condition and act on it without an approved basis;
- impose a materially worse itinerary solely because of a score;
- make a final decision that significantly affects the traveler without the required safeguards.

### Human decision

A trained disruption specialist reviews the relevant facts, verifies the proposed action, considers accessibility and customer-protection obligations, and decides whether to accept, modify, reject, or escalate the recommendation.

### Stop and escalation conditions

The workflow must stop or escalate when:

- the system uses prohibited or unapproved data;
- the recommendation conflicts with contractual, legal, accessibility, or safety obligations;
- the customer disputes a material fact;
- the confidence level is below the approved threshold;
- the output is inconsistent with available evidence;
- the system cannot provide sufficient decision context;
- a pattern of adverse outcomes appears for a protected or vulnerable group;
- the human reviewer cannot independently assess the case.

### Accountable owner

The accountable business owner remains responsible for the decision process, even when a vendor provides the model or platform.

### Challenge, correction, and override

The traveler must have an accessible route to:

- obtain information about the decision process;
- correct inaccurate personal data;
- provide additional context;
- request human review;
- contest the outcome;
- receive a corrected decision where appropriate.

## 4. Decision classification

Every AI-enabled decision process should be classified before deployment.

### 4.1 Decision categories

| Category | Description | Minimum governance response |
|---|---|---|
| Informational | AI provides information without ranking, recommendation, or decision influence | Accuracy, transparency, monitoring |
| Assistive | AI proposes options but a human independently decides | Documented human-review controls |
| Influential | AI score or recommendation materially shapes the likely outcome | Enhanced oversight, bias testing, challenge route |
| Solely automated | No meaningful human involvement before the decision takes effect | Article 22 analysis and legal approval |
| Prohibited or unacceptable | The use violates applicable law, policy, or fundamental-rights constraints | Do not deploy; stop immediately if detected |

### 4.2 Significant-effect indicators

A decision should be treated as potentially significant where it materially affects:

- access to employment, education, insurance, credit, housing, healthcare, travel, public services, or essential private services;
- price, eligibility, ranking, priority, or contractual terms;
- a person’s reputation, livelihood, safety, mobility, legal position, or ability to exercise rights;
- a child, worker, consumer, patient, person with a disability, or other vulnerable individual;
- a person through repeated lower-level decisions whose cumulative effect becomes significant.

## 5. Solely automated processing test

The organization must assess actual operation, not merely the process diagram.

A decision may be effectively solely automated when:

- reviewers normally accept the output without analysis;
- productivity targets discourage challenge;
- reviewers see only the model result and not the underlying evidence;
- the interface makes override difficult;
- staff lack authority to alter the outcome;
- the decision takes effect before human review;
- review occurs only after harm has already occurred;
- human participation is limited to administrative confirmation.

Evidence should include observation, override rates, decision time, interface design, reviewer interviews, training records, and sampled case files.

## 6. Lawful pathway and approval

Before using solely automated decision-making with legal or similarly significant effects, the organization must document:

1. the precise decision and affected population;
2. whether Article 22 applies;
3. the applicable exception or authorization, where relied upon;
4. the separate Article 6 lawful basis;
5. any Article 9 condition for special-category data;
6. applicable Member State law;
7. contractual necessity analysis, where relevant;
8. explicit-consent validity, where relevant;
9. safeguards for rights, freedoms, and legitimate interests;
10. DPIA and fundamental-rights assessment results;
11. DPO, legal, compliance, security, accessibility, and business approvals;
12. residual risk acceptance by an authorized owner.

Contractual necessity must not be interpreted as mere convenience, efficiency, or cost reduction. Explicit consent must be specific, informed, freely given, demonstrable, and capable of withdrawal where consent is relied upon.

## 7. Meaningful human intervention

Meaningful human intervention requires more than a nominal checkpoint.

The reviewer must have:

- appropriate competence and training;
- sufficient time;
- access to relevant evidence and limitations;
- authority to disagree with the system;
- freedom from automation bias and improper performance pressure;
- an understandable explanation of the output;
- the ability to obtain additional information;
- an accessible override, correction, escalation, and stop mechanism;
- accountability for the final decision.

The reviewer must actively consider the person’s circumstances and not merely repeat the model result.

## 8. Required human-review design

Each governed workflow must define:

| Element | Required definition |
|---|---|
| AI role | What the system may calculate, rank, recommend, or flag |
| Prohibited AI action | What the system must never decide or execute alone |
| Human decision | The exact judgment reserved for the reviewer |
| Evidence available | Facts, source records, confidence, limitations, and alternatives |
| Review standard | Questions the reviewer must answer before deciding |
| Override authority | Who may change or reject the output |
| Stop authority | Who may suspend the individual decision or whole system |
| Escalation route | Legal, privacy, security, safety, accessibility, or management path |
| Challenge route | How the affected person can contest or correct the outcome |
| Accountable owner | Named business role responsible for the process |

## 9. Transparency and explanation

Information provided to affected persons should be concise, accessible, and appropriate to the context. It should explain, as applicable:

- that automated processing or profiling is used;
- the purpose of the processing;
- the categories of data used;
- the role of the AI system in the outcome;
- the main factors that materially influenced the decision;
- significant limitations or uncertainty;
- whether a human reviewed the result;
- how to correct data, request review, express a view, or contest the decision;
- how to contact the controller or responsible organization.

An explanation should be specific enough to support understanding and challenge. A generic statement that “an algorithm was used” is not sufficient.

## 10. Data and profiling controls

Automated decision-making controls must address:

- purpose limitation;
- data minimisation;
- accuracy and freshness;
- representativeness and known gaps;
- inferred and proxy attributes;
- special-category data;
- children and vulnerable persons;
- lawful data acquisition;
- retention and deletion;
- vendor reuse;
- international transfers;
- correction propagation across models, features, logs, and downstream systems.

A lawful source does not make every later use lawful. Data must be assessed in the context of the specific decision.

## 11. Bias, discrimination, and outcome testing

Testing must examine both model performance and decision outcomes.

At minimum, the organization should evaluate:

- false positives and false negatives;
- error rates by relevant group;
- selection, approval, denial, prioritization, and override rates;
- proxy discrimination;
- intersectional effects;
- accessibility impacts;
- effects on vulnerable groups;
- cumulative impacts from repeated decisions;
- drift after deployment;
- human-review consistency;
- whether overrides correct or reinforce model error.

Testing should use legally permitted data and approved safeguards. Where sensitive data is needed for bias monitoring, the organization must document the legal basis, necessity, access restrictions, retention, and separation from operational decision-making.

## 12. Logging and evidence

The organization must retain sufficient evidence to reconstruct a consequential decision, subject to lawful retention limits.

Relevant evidence may include:

- system and model version;
- decision timestamp;
- input categories and source systems;
- material features or factors;
- output, score, confidence, and thresholds;
- known limitations presented to the reviewer;
- reviewer identity and role;
- review actions and decision rationale;
- override or escalation activity;
- notices provided;
- challenge and correction history;
- downstream actions;
- incident or complaint linkage.

Logs should support accountability without creating unnecessary surveillance or indefinite retention.

## 13. Contestability and redress

The challenge mechanism must be real and usable.

It should provide:

- accessible channels;
- reasonable response times;
- trained human reviewers;
- independence from the original decision where appropriate;
- ability to correct inaccurate data;
- consideration of new evidence;
- suspension of harmful action where justified;
- documented reasons for the reviewed outcome;
- correction of downstream records;
- escalation to the DPO, legal, compliance, or complaints function;
- protection against retaliation.

Repeated successful challenges should trigger system-level investigation, not only individual correction.

## 14. Vendor and third-party controls

Where a third party supplies an AI decision system, the organization must obtain enough information and contractual rights to govern its use.

Required controls may include:

- intended-purpose and prohibited-use statements;
- model and version identification;
- performance and limitation documentation;
- data-use and reuse restrictions;
- explanation and logging capability;
- human-oversight configuration;
- bias and subgroup testing evidence;
- incident notification;
- material-change notification;
- audit and access rights;
- support for data-subject requests;
- correction, deletion, export, and exit assistance;
- subcontractor and model-provider transparency.

A vendor’s assertion of compliance does not replace the deployer’s own assessment.

## 15. Monitoring and material change

Automated decision-making processes require ongoing monitoring.

Review triggers include:

- model, prompt, threshold, feature, or data-source changes;
- new affected populations;
- new jurisdictions;
- changes in legal basis or purpose;
- increased automation;
- lower human-override rates;
- complaint or challenge trends;
- adverse subgroup outcomes;
- incidents or near misses;
- vendor changes;
- significant performance drift;
- expansion from recommendation to execution.

A material change requires reassessment before continued use where risk may increase.

## 16. Stop and suspension criteria

The organization must suspend an individual decision, workflow, or system when appropriate, including where:

- the legal basis or Article 22 pathway is uncertain;
- meaningful human review is not functioning;
- required explanations cannot be produced;
- decisions rely on inaccurate or unlawfully processed data;
- significant discriminatory effects appear;
- override or challenge mechanisms fail;
- the model operates outside its intended purpose;
- logs are insufficient to reconstruct decisions;
- an unapproved material change has occurred;
- continued use creates unacceptable risk to rights, safety, or lawful treatment.

Restoration requires documented corrective action, validation, authorization, and monitoring.

## 17. Control activities

| Control ID | Control activity | Owner | Frequency |
|---|---|---|---|
| ADM-01 | Inventory AI-enabled decisions and classify their level of automation and effect | AI governance lead | At onboarding and quarterly |
| ADM-02 | Complete GDPR Article 22, lawful-basis, and special-category analysis | Privacy and legal | Before deployment and material change |
| ADM-03 | Define meaningful human-review requirements and authority | Business owner | Before deployment |
| ADM-04 | Test interface, reviewer behavior, override capability, and automation bias | Product, UX, compliance | Before launch and periodically |
| ADM-05 | Provide accessible transparency, correction, challenge, and redress routes | Privacy and customer operations | Continuous |
| ADM-06 | Monitor performance, subgroup outcomes, overrides, complaints, and drift | Model-risk owner | Monthly or risk-based |
| ADM-07 | Maintain decision reconstruction evidence and retention controls | System owner | Continuous |
| ADM-08 | Review vendor documentation, contractual rights, and material changes | Procurement and AI governance | Before contract and annually |
| ADM-09 | Exercise suspension, fallback, and restoration procedures | Business continuity and system owner | At least annually |
| ADM-10 | Report significant failures and corrective actions to governance bodies | Accountable executive | Risk-based |

## 18. Evidence

Evidence may include:

- decision inventory;
- Article 22 assessments;
- lawful-basis and Article 9 analyses;
- DPIAs and fundamental-rights impact assessments;
- system instructions and limitations;
- human-oversight design;
- reviewer training and competency records;
- sampled decision files;
- override and escalation logs;
- transparency notices;
- challenge and redress records;
- bias and performance reports;
- vendor documentation and contracts;
- incident records;
- suspension and restoration approvals;
- management-review minutes.

## 19. Audit tests

Auditors should:

1. select a sample of AI-enabled decision processes;
2. verify classification of automation and significance;
3. inspect Article 22, lawful-basis, and special-category analyses;
4. trace sampled decisions from input through final outcome;
5. determine whether human review was meaningful;
6. verify reviewer competence, time, information, and authority;
7. test override, escalation, correction, and challenge mechanisms;
8. compare notices with actual operation;
9. review subgroup outcomes, complaints, and successful challenges;
10. verify logs can reconstruct the decision;
11. inspect vendor evidence and material-change controls;
12. confirm stop criteria and restoration approvals are operational.

An audit should not conclude that human oversight is effective merely because a human approval field exists.

## 20. Metrics

Useful metrics include:

- number of consequential AI decision processes;
- percentage with current Article 22 assessments;
- percentage with approved human-oversight designs;
- reviewer override rate;
- reviewer decision time;
- challenge and complaint rate;
- percentage of challenges upheld;
- correction completion time;
- adverse-outcome rates by relevant group;
- unexplained decision rate;
- decisions lacking complete reconstruction evidence;
- material changes awaiting approval;
- number and duration of suspensions;
- repeated failure rate after corrective action.

Metrics must be interpreted carefully. A very low override rate may reflect high model quality, but it may also indicate automation bias or ineffective review.

## 21. Management checklist

Management should confirm that:

- every significant AI-enabled decision is inventoried;
- solely automated processing is explicitly identified;
- Article 22 and related legal conditions are documented;
- special-category and inferred sensitive data are controlled;
- meaningful human intervention is designed and tested;
- reviewers have competence, information, time, authority, and independence;
- affected persons receive usable information and challenge rights;
- decisions can be reconstructed;
- bias and outcome monitoring are active;
- vendors provide sufficient transparency and support;
- material changes trigger reassessment;
- stop, fallback, correction, and restoration procedures work;
- an accountable executive owns the residual risk.

## 22. Graphic specification — Automated Decision Governance Gate

**Type:** Formal process diagram.

**Purpose:** Show the decision path from AI use-case identification through legal classification, human oversight, execution, challenge, monitoring, and suspension.

**Flow:**

1. Identify AI-influenced decision.
2. Determine whether a natural person is affected.
3. Assess legal or similarly significant effect.
4. Determine whether processing is solely or effectively automated.
5. Complete GDPR, AI Act, and sector-law assessment.
6. Apply prohibited-use and high-risk screening.
7. Define AI role and reserved human judgment.
8. Configure meaningful human review.
9. Validate data, performance, bias, transparency, and contestability.
10. Authorize deployment.
11. Record decision evidence.
12. Provide challenge and correction route.
13. Monitor outcomes and material changes.
14. Continue, correct, restrict, suspend, or retire.

**Decision diamonds:**

- Does the decision significantly affect a person?
- Is the decision solely or effectively automated?
- Is there a lawful pathway?
- Is human review meaningful?
- Can the person understand and contest the outcome?
- Has a material change or unacceptable risk occurred?

**Accessibility:**

- do not rely on color alone;
- use high contrast;
- label every arrow and decision outcome;
- provide a text equivalent;
- maintain logical reading order;
- ensure all labels remain readable in grayscale.

**Caption:** Figure 83-1. Automated Decision Governance Gate.

**Alt text:** Process diagram showing how an organization identifies an AI-influenced decision, assesses significance and automation, verifies a lawful pathway, implements meaningful human review and contestability, authorizes use, monitors outcomes, and suspends the process when unacceptable risk or material change occurs.

## 23. Key takeaway

The central question is not whether a person appears somewhere in the workflow. The question is whether that person genuinely understands the AI output, can independently evaluate it, has authority to change it, and remains accountable for the final outcome.

A well-governed automated decision process is lawful, transparent, reviewable, contestable, evidence-based, monitored, and stoppable.