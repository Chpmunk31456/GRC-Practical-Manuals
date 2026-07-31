# Chapter 98 — Explainability and Transparency Risk

## Purpose

This chapter establishes a practical method for assessing and controlling the risk that people cannot understand, challenge, supervise, or appropriately rely on an AI system.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should assess whether information about an AI system is sufficient, accurate, timely, accessible, and appropriate for each audience. The assessment should distinguish between legal disclosure, operational transparency, technical explainability, user communication, and evidence required for governance or audit.

## Plain-language explanation

Transparency means more than telling someone that AI is being used. Different people need different information. A traveler may need a simple notice and a path to human help. An operator may need confidence indicators, limitations, and escalation rules. A regulator or auditor may need technical documentation, logs, test results, and decision records.

Explainability risk arises when a system’s operation or output cannot be understood well enough for its consequence. A technically complex model may still be acceptable when controls, validation, oversight, and user communication make its use understandable and accountable.

## Transparency audiences

Identify the information needs of:

- affected persons;
- customers and users;
- human reviewers and operators;
- business owners;
- risk, compliance, privacy, and security teams;
- internal audit;
- vendors and downstream deployers;
- regulators and market-surveillance authorities;
- incident responders and legal counsel.

## Risk questions

Assess whether each audience can determine:

- that AI is being used;
- the system’s purpose and role;
- what information it uses;
- what the output means and does not mean;
- the principal limitations and uncertainty;
- whether a human reviews or can override the result;
- how to ask for help, challenge, or appeal;
- what records are retained;
- who is accountable;
- when the system or model last changed.

## Explainability dimensions

Consider:

1. **Global explainability** — how the system generally works, including purpose, inputs, logic, and limitations.
2. **Local explainability** — why a particular output or recommendation occurred.
3. **Procedural explainability** — how people can contest, correct, escalate, or seek human review.
4. **Operational explainability** — what an operator needs to use the system safely.
5. **Technical explainability** — information needed by engineers, validators, auditors, and regulators.
6. **Outcome explainability** — whether the explanation is meaningful for the actual consequence.

## Common risk scenarios

- users do not know they are interacting with AI;
- notices are hidden, overly technical, or presented too late;
- an output appears certain when it is probabilistic;
- operators cannot identify low-confidence or out-of-scope cases;
- an explanation does not match the actual system behavior;
- reasons are generic, misleading, or generated after the fact without validation;
- model or data changes invalidate earlier explanations;
- explanations reveal personal, confidential, security-sensitive, or proprietary information;
- affected persons cannot obtain human review;
- logs are insufficient to reconstruct a consequential decision;
- vendor documentation is incomplete or not passed downstream.

## Assessment factors

Rate risk based on:

- consequence of the output;
- affected-person vulnerability;
- degree of automation;
- complexity and opacity;
- availability of meaningful local explanations;
- human-review quality;
- notice timing and prominence;
- accessibility and language needs;
- ability to contest or correct;
- documentation completeness;
- consistency between documented and actual behavior;
- change frequency;
- vendor dependency.

## Control expectations

Controls may include:

- approved transparency notices;
- plain-language explanations;
- confidence, uncertainty, and limitation indicators;
- reason codes or validated explanation methods;
- user-accessible human escalation;
- operator instructions and decision-support guidance;
- accessibility and language testing;
- documentation standards by audience;
- logging sufficient for decision reconstruction;
- version-controlled model, prompt, and policy records;
- change-triggered notice and documentation review;
- validation that explanations are faithful and not merely plausible;
- safeguards against disclosure of sensitive information.

## Human oversight

Human reviewers should receive enough information to:

- understand the system’s intended purpose;
- recognize uncertainty and known limitations;
- identify inputs that materially influenced the result;
- detect anomalies or manipulation;
- obtain additional context;
- override, reject, or stop the system;
- document the reason for consequential decisions;
- avoid automation bias.

## GlobalWay Travel Services example

GlobalWay uses an AI engine to recommend alternative flights during disruptions. Early testing shows that travel consultants receive a ranked list but cannot see whether options were excluded because of policy, availability, traveler preference, accessibility needs, or low data confidence.

GlobalWay introduces validated reason codes, confidence indicators, a summary of relevant constraints, and an option to display excluded alternatives. Travelers receive a plain-language notice that recommendations are AI-assisted and may request a human review. The company tests whether explanations remain accurate after model and supplier-data changes.

## Control activities

- Define transparency requirements by audience and consequence.
- Validate notices, explanations, and operator guidance before release.
- Ensure explanations are faithful to system behavior.
- Provide meaningful human escalation and contestability.
- Protect sensitive information while maintaining accountability.
- Reassess transparency after material change.
- Retain evidence supporting disclosure and explanation design.

## Evidence

- audience and transparency assessment;
- approved notices and instructions;
- explanation-method documentation;
- faithfulness and usability test results;
- accessibility and language reviews;
- screenshots and user-interface records;
- operator training materials;
- human-review and appeal records;
- model, prompt, and policy versions;
- decision logs;
- change-review records;
- vendor documentation.

## Audit tests

1. Select AI uses by consequence and identify applicable transparency audiences.
2. Confirm notices are timely, prominent, accurate, and understandable.
3. Test whether operators can interpret uncertainty, limitations, and escalation triggers.
4. Review a sample of consequential outputs and verify explanations are supported by system records.
5. Confirm affected persons can obtain human assistance or review where required.
6. Verify changes trigger review of notices, explanations, and documentation.
7. Assess whether transparency controls avoid disclosing protected or security-sensitive information.

## Metrics

- systems with approved transparency assessments;
- notices tested for readability and accessibility;
- explanation accuracy or faithfulness test results;
- human-review requests;
- successful challenges or corrections;
- operator override rates;
- complaints related to unclear AI use;
- documentation gaps;
- overdue transparency reviews after change;
- vendor systems lacking adequate downstream information.

## Management checklist

- Do users know when they are interacting with AI?
- Can operators understand and challenge outputs?
- Are explanations meaningful for the consequence?
- Are uncertainty and limitations communicated?
- Can affected persons obtain human assistance?
- Are explanations validated rather than assumed?
- Are notices and documentation updated after change?

## Figure specification — Transparency and Explainability Audience Map

Create a concentric or role-based map showing affected persons, users, operators, owners, assurance teams, vendors, and regulators. For each audience, show the information needed, the format, the timing, and the evidence retained. Include a validation loop ensuring explanations remain faithful after change.

**Alt text:** Transparency and explainability audience map showing information needs for affected persons, users, operators, owners, assurance teams, vendors, and regulators, with a validation loop after system changes.