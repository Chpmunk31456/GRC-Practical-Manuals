# Chapter 12 — AI Literacy, Role-Based Training, and Competence Assurance

## 12.1 Purpose

This chapter establishes a practical governance framework for meeting the EU AI Act’s AI-literacy obligation and for demonstrating that people who operate, supervise, procure, approve, monitor, audit, or rely on AI systems are prepared for their responsibilities.

The objective is not to turn every employee into a data scientist. It is to ensure that each person understands enough about the AI systems they encounter to use them safely, question them appropriately, recognize limits, escalate concerns, and preserve human accountability.

> **Core principle:** AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 12.2 Legal Requirement

Article 4 requires providers and deployers of AI systems to take measures supporting AI literacy for staff and other persons who operate or use AI systems on their behalf. The measures should reflect the person’s technical knowledge, experience, education and training, the context in which the AI system is used, and the people or groups affected by that use.

The obligation is contextual. A traveler-support agent, developer, procurement manager, human reviewer, executive sponsor, and internal auditor do not need identical training. Each needs competence appropriate to the role, system, decision authority, risk, and affected population.

## 12.3 Plain-Language Explanation

A defensible program must answer five questions:

1. Who interacts with each AI system?
2. What decisions or actions can that person take?
3. What can go wrong in that use case?
4. What must the person know and be able to do?
5. What evidence shows that the person remains competent?

Training attendance alone is not competence. Competence requires understanding, application, judgment, and the ability to recognize when normal use must stop.

## 12.4 GlobalWay Travel Services Example

GlobalWay Travel Services uses a traveler-facing virtual assistant, agent-assistance tools, disruption prediction, fraud screening, internal generative AI, supplier-risk analysis, and AI-supported recruitment screening.

GlobalWay therefore maintains a role-based AI literacy matrix.

| Role | What AI may do | Human responsibility | Required competence |
|---|---|---|---|
| Traveler-support agent | Suggest itineraries and draft messages | Verify facts, approve communications, protect travelers, escalate exceptions | Hallucination recognition, source checking, accessibility, override, escalation |
| Operations manager | Prioritize disruption cases | Approve operational decisions and monitor impact | Bias, drift, thresholds, incident response, documentation |
| Procurement manager | Summarize vendor responses | Validate evidence and assess contractual risk | Due diligence, model limits, data rights, audit rights, subcontractor risk |
| Developer or integrator | Configure and connect AI components | Implement safeguards and preserve controls | Testing, logging, security, marking, change control |
| Human reviewer | Review AI-supported decisions | Approve, correct, reject, or escalate | Automation bias, meaningful review, challenge rights, evidence quality |
| Executive sponsor | Approve objectives, funding, and risk acceptance | Own business accountability | Governance duties, residual risk, human impact, stop-use criteria |
| Legal and compliance | Interpret obligations and challenge controls | Confirm regulatory treatment and evidence sufficiency | Role classification, transparency, prohibited practices, documentation |
| Internal audit | Independently test controls | Report deficiencies and verify remediation | Audit criteria, sampling, traceability, operating effectiveness |

## 12.5 Control Objective

GlobalWay shall maintain a risk-based AI literacy and competence program ensuring that personnel and third parties understand:

- the purpose and limits of the AI systems they use;
- their authority and accountability;
- what AI may and may not do;
- when human review is mandatory;
- how to identify unreliable, biased, unsafe, or manipulated outputs;
- how to stop, override, correct, challenge, and escalate;
- how to protect personal, confidential, and regulated information;
- how to document decisions and preserve evidence;
- how affected people may obtain help, correction, or human review.

## 12.6 Role-Based Learning Architecture

### Foundation level

Required for all personnel with access to AI-enabled tools. Topics include approved and prohibited uses, confidentiality, hallucinations, synthetic media, bias, human accountability, incident reporting, and the right to stop and seek help.

### Practitioner level

Required for routine users. Topics include system-specific purpose and limits, input and output handling, source validation, override procedures, accessibility, documentation, and known failure modes.

### Owner and reviewer level

Required for system owners, human reviewers, risk owners, and managers. Topics include meaningful human oversight, automation bias, performance thresholds, incidents, complaints, change management, affected-person impact, and stop-use criteria.

### Specialist level

Required for developers, integrators, security, privacy, legal, procurement, compliance, and audit. Topics may include data governance, adversarial misuse, model evaluation, vendor risk, technical documentation, transparency marking, logging, conformity, and evidence.

### Executive and board level

Required for leaders approving AI strategy, material systems, or risk acceptance. Topics include organizational accountability, legal exposure, human-rights impact, limits of assurance, residual-risk acceptance, and suspension or withdrawal conditions.

## 12.7 Competence Assurance

GlobalWay shall not rely only on completion certificates. It shall use scenario-based assessments, supervised practice, tabletop exercises, observed task performance, challenge-and-override simulations, periodic knowledge checks, manager confirmation, and remedial training.

Personnel should be able to demonstrate what they would do when:

- AI output conflicts with authoritative information;
- a recommendation appears unfair or unsafe;
- required data is missing;
- a traveler is vulnerable or needs accessibility support;
- confidential information is exposed;
- a system behaves differently after an update;
- an affected person challenges an AI-supported outcome.

## 12.8 Human Decision Boundary

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

## 12.9 Third Parties and Contractors

Relevant contractors, consultants, temporary staff, managed-service personnel, and outsourced providers must complete role-appropriate training before access is granted. Contracts should address competence, approved use, confidentiality, incident notification, subcontractors, evidence retention, retraining, and access suspension.

## 12.10 Training Triggers

Training must be assigned or refreshed when a new AI system is introduced, a role changes, the model or workflow materially changes, a new affected population is introduced, an incident or complaint occurs, monitoring reveals recurring error, law changes, a vendor changes a material feature, or an audit identifies insufficient competence.

## 12.11 Stop and Escalation Conditions

Personnel must stop normal use and escalate when output may cause significant harm, the system appears compromised, mandatory human review cannot be performed, information is insufficient to validate output, content is discriminatory or unsafe, confidential information is exposed, a required notice or log is missing, or an affected person requests human intervention that the workflow cannot provide.

## 12.12 Evidence

Retain the AI literacy policy, role inventory, training-needs analysis, curriculum, version history, completion records, assessment results, competence demonstrations, remedial actions, contractor evidence, training-trigger records, exception approvals, management review minutes, and links between incidents and training improvements.

## 12.13 Metrics

Management should review assignment and completion rates, assessment pass rates, overdue training, retraining after changes, incidents involving misuse or misunderstanding, override and escalation rates, repeated validation failures, contractor compliance, remediation time, and employee confidence in challenging AI output.

Metrics must not reward blind acceptance. Appropriate increases in overrides or escalations may show that personnel are exercising judgment.

## 12.14 Audit Test

An auditor should sample AI systems across risk levels and functions; identify all operating, reviewing, approving, procuring, maintaining, and auditing roles; compare learning with actual authority and risk; verify system-specific training; inspect competence evidence; test knowledge of limits and stop conditions; trace system changes to retraining; review incidents for literacy-related root causes; verify contractor coverage; and confirm management remediation.

## 12.15 Formal Process Graphic Specification

**Figure 12-1 — Role-Based AI Literacy and Competence Lifecycle**

`AI system identified → roles and affected people mapped → competence requirements defined → role-based learning delivered → realistic competence tested → access approved → performance monitored → change or incident triggers retraining`

Use two aligned tracks:

- **Organization track:** inventory, requirements, training, monitoring, evidence.
- **Human track:** understand, practice, question, override, escalate, improve.

**Human concern:**

> “Does the person reviewing this system actually know when it is wrong?”

**Alt text:** A two-track lifecycle showing how an organization maps AI roles, delivers role-based training, tests competence, grants access, monitors performance, and retrains people after changes or incidents. The human track emphasizes questioning, overriding, and escalating rather than merely completing a course.

## 12.16 Original Workplace-Satire Graphic

**Figure 12-2 — “Everyone Passed the Training”**

Scene: A manager points proudly to a dashboard showing 100% training completion. Beside it, an employee asks an AI system whether a traveler needs a visa, receives three contradictory answers, and clicks “Approve All.”

Caption:

> “The course completion rate was excellent. The competence rate was still loading.”

Control lesson: Completion statistics do not prove that personnel can identify unreliable outputs, exercise judgment, or protect affected people.

**Alt text:** An office manager celebrates full AI-training completion while an employee blindly approves contradictory AI answers about a traveler’s visa.

## 12.17 Key Takeaway

AI literacy is not a one-time awareness exercise. It is a governance control connecting each person’s knowledge and judgment to the real system, decision, risk, and people affected.

## 12.18 Official Sources

- Regulation (EU) 2024/1689, Article 4 — AI literacy.
- European Commission, AI literacy questions, answers, and practice materials.

> **Legal update note:** Verify the regulatory baseline and official Commission implementation materials immediately before publication.