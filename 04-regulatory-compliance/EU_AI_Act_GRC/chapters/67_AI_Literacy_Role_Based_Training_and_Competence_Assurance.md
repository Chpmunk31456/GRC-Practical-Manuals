# Chapter 67 — AI Literacy, Role-Based Training, and Competence Assurance

## 67.1 Purpose

This chapter establishes a practical governance framework for meeting the EU AI Act’s AI-literacy obligation and for demonstrating that people who operate, supervise, procure, approve, monitor, or rely on AI systems are prepared for their responsibilities.

The objective is not to turn every employee into a data scientist. It is to ensure that each person understands enough about the AI systems they encounter to use them safely, question them appropriately, recognize limits, escalate concerns, and preserve human accountability.

> **Core principle:** AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 67.2 Legal Requirement

Article 4 requires providers and deployers of AI systems to take measures supporting AI literacy for staff and other persons who operate or use AI systems on their behalf. The measures should reflect the person’s technical knowledge, experience, education and training, the context in which the AI system is used, and the people or groups affected by that use.

The obligation is contextual. A traveler-support agent using an AI assistant, a developer integrating a model, a procurement manager selecting an AI vendor, and an executive approving a high-impact deployment do not need identical training. Each needs competence appropriate to the role, risk, system, and affected population.

## 67.3 Plain-Language Explanation

An organization cannot responsibly say, “The system made the decision,” or “The employee completed a generic AI course,” and treat the matter as closed.

A defensible program must answer five questions:

1. Who interacts with each AI system?
2. What decisions or actions can that person take?
3. What can go wrong in that specific use case?
4. What must the person know and be able to do?
5. What evidence shows that the person remains competent?

Training attendance alone is not competence. Competence requires understanding, application, judgment, and the ability to recognize when normal use must stop.

## 67.4 GlobalWay Travel Services Example

GlobalWay Travel Services deploys several AI-enabled tools:

- a traveler-facing virtual assistant;
- an agent-assistance tool that drafts responses and rebooking options;
- a disruption-prediction system;
- a fraud-screening tool;
- an internal generative-AI assistant;
- a supplier-risk analysis tool;
- an AI-supported recruitment screening service.

A single annual awareness course would not address the different responsibilities involved.

GlobalWay therefore creates a role-based AI literacy matrix:

| Role | What AI may do | Human responsibility | Required competence |
|---|---|---|---|
| Traveler-support agent | Suggest itineraries, draft messages, summarize policy | Verify facts, approve communication, protect travelers, escalate exceptions | Hallucination recognition, source checking, override, accessibility, escalation |
| Operations manager | Prioritize disruption cases and recommend resource allocation | Approve operational decisions and monitor impact | Bias, performance drift, threshold effects, incident response, documentation |
| Procurement manager | Compare vendors and summarize questionnaire responses | Validate evidence, assess contractual obligations, reject unsupported claims | Vendor due diligence, model limitations, data rights, audit rights, subcontractor risk |
| Developer or integrator | Configure, test, and connect AI components | Implement safeguards and preserve technical controls | Testing, logging, security, data governance, marking, change control |
| Human reviewer | Review AI-supported decisions affecting people | Approve, correct, reject, or escalate | Automation bias, meaningful review, affected-person rights, evidence quality |
| Executive sponsor | Approve objectives, funding, risk appetite, and deployment | Own business accountability and stop unacceptable use | Governance duties, residual risk, legal exposure, human-impact assessment |
| Legal and compliance | Interpret obligations and challenge controls | Confirm regulatory treatment and evidence sufficiency | EU AI Act applicability, role classification, transparency, prohibited practices |
| Internal audit | Independently test control design and operation | Report deficiencies and verify remediation | Audit criteria, sampling, traceability, control effectiveness |

## 67.5 Control Objective

GlobalWay shall maintain a risk-based AI literacy and competence program that ensures personnel and third parties understand:

- the purpose and limits of the AI systems they use;
- their individual authority and accountability;
- what AI may and may not do;
- when human review is mandatory;
- how to identify unreliable, biased, unsafe, or manipulated outputs;
- how to stop, override, correct, challenge, and escalate;
- how to protect personal, confidential, and regulated information;
- how to document decisions and preserve evidence;
- how affected people may obtain help, correction, or human review.

## 67.6 Role-Based Learning Architecture

### 67.6.1 Foundation Level

Required for all personnel with access to AI-enabled tools.

Minimum topics:

- what qualifies as an AI-enabled system in the organization;
- approved and prohibited uses;
- confidentiality and data-handling rules;
- hallucinations and unreliable output;
- manipulation, phishing, and synthetic media;
- bias and unequal impact;
- human accountability;
- incident reporting;
- the right to stop and seek help.

### 67.6.2 Practitioner Level

Required for people who routinely operate or rely on AI systems.

Additional topics:

- system-specific purpose and limits;
- acceptable input and output handling;
- validation and source checking;
- override and escalation procedures;
- accessibility and vulnerable-person considerations;
- documentation and recordkeeping;
- known failure modes and operating boundaries.

### 67.6.3 Owner and Reviewer Level

Required for system owners, human reviewers, risk owners, and managers.

Additional topics:

- meaningful human oversight;
- automation bias;
- performance metrics and thresholds;
- incident and complaint trends;
- change management;
- impact on affected people;
- stop-use criteria;
- accountability and sign-off duties.

### 67.6.4 Specialist Level

Required for developers, integrators, security, privacy, legal, procurement, compliance, and audit specialists.

Training is tailored to function and may include:

- data governance;
- cybersecurity and adversarial misuse;
- model and system evaluation;
- vendor and supply-chain risk;
- technical documentation;
- transparency and content marking;
- logging and traceability;
- conformity, assurance, and audit evidence;
- legal-role classification and regulatory change.

### 67.6.5 Executive and Board Level

Required for senior leaders who approve AI strategy, risk appetite, material systems, or high-impact use cases.

Minimum topics:

- organizational accountability;
- material legal and reputational exposure;
- human-rights and consumer impacts;
- limits of assurance and testing;
- residual-risk acceptance;
- escalation from management to the board;
- conditions requiring suspension or withdrawal.

## 67.7 Competence Assurance

GlobalWay shall not rely only on completion certificates. It shall use evidence that demonstrates role-appropriate capability.

Acceptable methods include:

- scenario-based assessments;
- supervised practice;
- tabletop exercises;
- observed task performance;
- challenge-and-override simulations;
- incident-response exercises;
- periodic knowledge checks;
- role-specific attestations;
- manager confirmation;
- remedial training after errors or control failures.

A person should be able to demonstrate what they would do when:

- the AI output conflicts with authoritative information;
- the system recommends an action that appears unfair or unsafe;
- required data is missing;
- the traveler is vulnerable or needs accessibility support;
- the tool exposes confidential information;
- the system behaves differently after an update;
- a person challenges or disputes an AI-supported outcome.

## 67.8 Human Decision Boundary

For each AI-enabled role, GlobalWay documents:

| Required element | Example |
|---|---|
| What AI may do | Draft a rebooking recommendation |
| What remains human | Approve the final itinerary and communication |
| Review requirement | Verify fare rules, visa constraints, accessibility, and traveler preference |
| Stop condition | Conflicting data, vulnerable traveler, unclear policy, or unsafe recommendation |
| Escalation route | Senior agent, duty manager, legal, security, or emergency response |
| Accountable owner | Director of Traveler Operations |
| Challenge right | Traveler may request correction or human review |

No training program is complete unless employees understand this boundary in practice.

## 67.9 Third Parties and Contractors

The literacy obligation extends to persons operating or using AI systems on the organization’s behalf.

GlobalWay therefore requires relevant contractors, outsourced service providers, consultants, temporary staff, and managed-service personnel to complete role-appropriate training before access is granted.

Contractual controls should address:

- required competence;
- approved use;
- confidentiality;
- incident notification;
- subcontractor obligations;
- evidence retention;
- retraining after material changes;
- access suspension for non-compliance.

## 67.10 Training Triggers

Training must be assigned or refreshed when:

- a new AI system is introduced;
- a person’s role changes;
- system purpose, model, data, interface, or workflow materially changes;
- a new affected population is introduced;
- a control failure, complaint, incident, or near miss occurs;
- monitoring reveals recurring human error;
- legal or regulatory requirements change;
- a vendor changes a material feature;
- an audit identifies insufficient competence.

## 67.11 Stop and Escalation Conditions

Personnel must stop normal use and escalate when:

- the output may create significant harm;
- the system appears manipulated, compromised, or outside its intended use;
- mandatory human review cannot be performed;
- the user lacks sufficient information to validate the output;
- the system produces discriminatory, threatening, deceptive, or unsafe content;
- personal or confidential information is exposed improperly;
- a required notice, label, log, or control is missing;
- an affected person requests human intervention that the current workflow cannot provide.

Good AI literacy includes knowing when not to proceed.

## 67.12 Evidence

GlobalWay retains evidence proportionate to the system and role, including:

- AI literacy policy;
- role and system inventory;
- training-needs analysis;
- role-based curriculum;
- training materials and version history;
- attendance and completion records;
- assessment results;
- competency demonstrations;
- remedial actions;
- contractor training evidence;
- training-trigger records;
- exception approvals;
- management review minutes;
- links between incidents and training improvements.

## 67.13 Metrics

Management should review, at minimum:

- percentage of in-scope personnel assigned training;
- completion rate by role and system;
- assessment pass rate;
- overdue training;
- retraining after system changes;
- incidents involving human misunderstanding or misuse;
- override and escalation rates;
- repeated validation failures;
- contractor compliance;
- time from identified gap to remediation;
- employee confidence in challenging AI output.

Metrics must not reward blind acceptance. A healthy increase in overrides or escalations may show that people are exercising judgment.

## 67.14 Audit Test

An auditor should:

1. Select a sample of AI systems across risk levels and business functions.
2. Identify all roles that operate, supervise, approve, procure, maintain, audit, or rely on each system.
3. Compare assigned learning with the person’s authority, task, risk, and affected population.
4. Verify that training reflects the actual system and workflow.
5. Inspect assessment and competence evidence rather than completion records alone.
6. Test whether personnel can explain system limits, human decision boundaries, stop conditions, and escalation routes.
7. Trace recent system changes to training updates.
8. Review incidents and complaints for literacy-related root causes.
9. Verify contractor coverage.
10. Confirm that management reviews metrics and corrects deficiencies.

### Audit failure examples

- every employee receives the same generic course;
- training describes AI broadly but not the deployed system;
- human reviewers cannot explain when to override;
- contractor personnel are omitted;
- completion records exist but competence is not tested;
- material system changes do not trigger retraining;
- incidents repeat without curriculum changes;
- executives approve systems without understanding residual risk.

## 67.15 Formal Process Graphic Specification

**Figure 67-1 — Role-Based AI Literacy and Competence Lifecycle**

Process:

`AI system and use case identified → roles and affected people mapped → competence requirements defined → role-based learning delivered → scenario-based competence tested → access approved → performance monitored → change or incident triggers retraining`

The graphic should use two aligned tracks:

- **Organization track:** inventory, requirements, training, monitoring, evidence.
- **Human track:** understand, practice, question, override, escalate, improve.

**Human concern shown beneath the process:**

> “Does the person reviewing this system actually know when it is wrong?”

**Alt text:** A two-track lifecycle showing how an organization maps AI roles, delivers role-based training, tests competence, grants access, monitors performance, and retrains people after changes or incidents. The human track emphasizes understanding, questioning, overriding, and escalating rather than merely completing a course.

## 67.16 Original Workplace-Satire Graphic

**Figure 67-2 — “Everyone Passed the Training”**

Scene: A manager proudly points to a dashboard showing 100% training completion. Beside the dashboard, an employee asks an AI system whether a traveler needs a visa, receives three contradictory answers, and clicks “Approve All.”

Caption:

> “The course completion rate was excellent. The competence rate was still loading.”

Control lesson: Completion statistics do not prove that personnel can identify unreliable outputs, exercise judgment, or protect affected people.

**Alt text:** An office manager celebrates a dashboard showing full AI-training completion while an employee blindly approves contradictory AI answers about a traveler’s visa. The cartoon illustrates the difference between attendance and demonstrated competence.

## 67.17 Management Review Questions

Senior management should ask:

- Which roles can materially affect people through AI-supported work?
- Can those people explain when they must override or stop the system?
- Are training requirements tied to actual systems and decisions?
- Do contractors receive equivalent preparation?
- What recent incidents were caused or worsened by insufficient literacy?
- What changed in the curriculum as a result?
- Are employees rewarded for appropriate challenge and escalation?
- Can the organization demonstrate competence to an auditor or regulator?

## 67.18 Implementation Checklist

- [ ] Maintain an inventory of AI systems and in-scope roles.
- [ ] Map role authority, risk, and affected populations.
- [ ] Define role-specific competence requirements.
- [ ] Provide foundation, practitioner, owner, specialist, and executive learning.
- [ ] Test competence using realistic scenarios.
- [ ] Document human decision boundaries and stop conditions.
- [ ] Include contractors and third parties.
- [ ] Trigger retraining after material changes and incidents.
- [ ] Monitor literacy-related errors, overrides, and escalations.
- [ ] Retain evidence sufficient for management, audit, and regulatory review.

## 67.19 Key Takeaway

AI literacy is not a one-time awareness exercise. It is a governance control that connects each person’s knowledge and judgment to the real system, real decision, real risk, and real people affected.

A mature organization does not merely ask whether someone completed training. It asks whether that person can recognize when the AI is wrong, protect the affected person, and take accountable action.

## 67.20 Official Sources

- Regulation (EU) 2024/1689, Article 4 — AI literacy.
- European Commission, “AI Literacy — Questions & Answers.”
- European Commission, repository of AI literacy practices.

> **Legal update note:** EU AI Act implementation materials continue to evolve. The regulatory baseline and implementation dates should be verified against the current consolidated Regulation and official European Commission publications before final publication or reliance.