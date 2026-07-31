# Chapter 75 — Audit Rights and Incident Notification

## 1. Purpose

This chapter explains how an organization should obtain, exercise, and evidence contractual audit rights over AI providers and how it should govern incident notification across the AI supply chain.

The objective is not to transfer statutory accountability to a supplier. The objective is to ensure that GlobalWay Travel Services can obtain timely evidence, investigate failures, protect travelers and employees, support regulatory cooperation, and decide whether an AI service may remain in use.

> **Core principle:** Contractual audit and notification rights must be practical enough to support real oversight, not merely decorative language in a contract.

## 2. Requirement

Organizations using third-party AI should establish proportionate rights to:

- obtain compliance and assurance evidence;
- review controls, testing, limitations, and corrective actions;
- investigate incidents and material control failures;
- receive timely notification of relevant events;
- preserve evidence;
- cooperate with competent authorities;
- suspend, restrict, or terminate use when risk cannot be controlled.

Contractual rights do not replace legal obligations imposed directly on providers, deployers, importers, distributors, or other actors. They create an operational mechanism for meeting those obligations.

## 3. Plain-language explanation

A supplier may promise that its AI system is secure, accurate, compliant, and monitored. GlobalWay still needs a reliable way to verify those claims.

A useful audit-right clause answers four practical questions:

1. What evidence may GlobalWay obtain?
2. When may GlobalWay request it?
3. How quickly must the provider respond?
4. What happens when the evidence is incomplete or reveals unacceptable risk?

An incident-notification clause must answer equally practical questions:

1. What events must be reported?
2. How quickly must the initial alert be sent?
3. What information must follow?
4. Who decides whether the system should be stopped, restricted, or reported externally?

## 4. GlobalWay example

GlobalWay uses a third-party AI service to recommend flight alternatives during major disruptions.

The provider identifies a model update that causes the system to omit wheelchair-assistance constraints in some rerouting recommendations. The issue may affect accessibility, traveler safety, contractual service commitments, and regulatory obligations.

Under an effective agreement, the provider must:

- notify GlobalWay promptly;
- identify affected versions, dates, customers, and use cases;
- preserve logs and test evidence;
- explain containment and corrective action;
- support GlobalWay’s impact assessment;
- provide evidence needed for traveler remediation and regulatory cooperation.

GlobalWay’s accountable owner must decide whether to suspend automated recommendations, require human-only review, notify clients or travelers, and escalate to legal, privacy, security, accessibility, or regulatory teams.

## 5. Audit-right design

### 5.1 Evidence-access rights

The contract should permit access, subject to proportionate confidentiality and security controls, to evidence such as:

- system and model documentation;
- risk assessments;
- testing and validation reports;
- performance and limitation records;
- bias and accessibility testing;
- cybersecurity assessments;
- incident and vulnerability records;
- change logs and release notes;
- subcontractor and dependency information;
- business-continuity and recovery evidence;
- corrective-action plans;
- relevant independent assurance reports;
- records needed to support regulatory inquiries.

### 5.2 Audit methods

Audit rights may be exercised through a tiered model:

| Tier | Method | Typical use |
|---|---|---|
| 1 | Standard evidence review | Routine annual or onboarding assurance |
| 2 | Written clarification and targeted evidence request | Documentation gaps or control concerns |
| 3 | Remote interview or control walkthrough | Material ambiguity or elevated risk |
| 4 | Independent assessment or on-site audit | High-risk use, serious incident, repeated failure, or regulator request |
| 5 | Emergency investigation | Active harm, security compromise, prohibited use, or major control breakdown |

The contract should not limit GlobalWay to receiving only a generic certification when the underlying risk requires more specific evidence.

### 5.3 Trigger events

Enhanced audit rights should be available when:

- a serious or potentially serious incident occurs;
- the provider materially changes the model, service, data use, intended purpose, or architecture;
- a control failure or significant vulnerability is identified;
- evidence conflicts with observed system behavior;
- a regulator, client, insurer, or internal audit function requests support;
- the provider repeatedly misses service, security, transparency, or remediation commitments;
- the system may have been substantially modified;
- GlobalWay reasonably suspects prohibited, unsafe, discriminatory, deceptive, or noncompliant use.

### 5.4 Limits and safeguards

Audit activity should protect legitimate provider confidentiality and system security. Safeguards may include:

- need-to-know access;
- secure data rooms;
- independent assessors;
- redaction of unrelated customer information;
- restrictions on copying sensitive technical details;
- advance notice for routine audits;
- emergency exceptions when delay would increase harm.

These safeguards must not prevent access to evidence reasonably necessary for risk management, incident response, or regulatory cooperation.

## 6. Incident-notification taxonomy

The contract should define reportable events broadly enough to capture both confirmed incidents and material warning signs.

| Event class | Examples |
|---|---|
| Safety or fundamental-rights event | discriminatory output, accessibility failure, harmful recommendation, loss of meaningful human oversight |
| Security event | prompt injection, data leakage, model theft, unauthorized access, malicious manipulation |
| Privacy event | personal-data exposure, unauthorized retention, unexpected model training use |
| Reliability event | significant accuracy degradation, hallucination pattern, unavailable safeguards, failed fallback |
| Compliance event | prohibited use, missing disclosure, unsupported high-risk deployment, false documentation |
| Supply-chain event | critical subcontractor outage, dependency compromise, unapproved component change |
| Regulatory event | authority inquiry, enforcement action, required corrective measure, market restriction |
| Change-control event | material model, data, service, ownership, hosting, or intended-purpose change |

## 7. Notification timing

The agreement should define risk-based notification windows.

A practical structure is:

- **immediate alert:** active harm, critical security event, prohibited practice, major service integrity failure, or regulator intervention;
- **rapid preliminary notice:** suspected material event requiring investigation;
- **formal update:** known scope, affected systems, containment, evidence preservation, and interim risk assessment;
- **final report:** root cause, impact, corrective action, residual risk, and prevention measures.

Contractual timelines should support, not delay, any shorter statutory, regulatory, client, or internal reporting deadline.

## 8. Minimum notification content

The provider’s notice should include, as available:

- date and time discovered;
- date and time the event began;
- affected model, system, version, API, region, and environment;
- affected use cases and customers;
- nature of the event;
- known or suspected impact;
- categories of people and data affected;
- immediate containment;
- workarounds and recommended customer actions;
- evidence preserved;
- investigation owner;
- planned update cadence;
- regulator or other third-party notifications;
- root cause and corrective action when known.

The provider must clearly distinguish confirmed facts, preliminary findings, assumptions, and unresolved questions.

## 9. GlobalWay response workflow

```text
Provider or internal team detects event
                ↓
Initial triage and evidence preservation
                ↓
GlobalWay receives and validates notification
                ↓
Classify impact: safety | rights | privacy | security | operations | compliance
                ↓
Human decision: continue | restrict | human-only mode | suspend | terminate
                ↓
Notify accountable owners and affected stakeholders
                ↓
Determine external reporting and traveler/client remediation
                ↓
Verify corrective action and authorize controlled restoration
                ↓
Post-incident review, lessons learned, and contract/control updates
```

**Figure 75-1 — AI Supplier Audit and Incident Escalation Flow**  
*Alt text:* A formal process diagram showing detection, evidence preservation, notification, impact classification, accountable human decision, escalation, remediation, verification, and closure.

## 10. Human responsibility

AI may support incident detection, log analysis, pattern recognition, and prioritization. It must not make the final decision on whether to:

- suspend a production service;
- notify a regulator;
- notify an affected traveler, employee, or client;
- accept residual risk;
- close a serious finding;
- restore an AI system after a material incident.

| Element | Required definition |
|---|---|
| AI may do | Detect anomalies, correlate logs, summarize evidence, suggest severity |
| Human decision | Classify impact, stop or continue use, notify stakeholders, approve restoration |
| Review | Legal, compliance, security, privacy, accessibility, business, and technical review as applicable |
| Stop condition | Active harm, prohibited use, uncontrolled exposure, unreliable evidence, or ineffective oversight |
| Accountable owner | Named business executive or delegated accountable officer |
| Challenge and override | Authorized reviewers may reject automated severity, scope, or remediation recommendations |

## 11. Stop and escalation conditions

GlobalWay must suspend or materially restrict use when:

- the provider fails to report a material event promptly;
- evidence needed to assess impact is unavailable or unreliable;
- the provider refuses reasonable investigation support;
- harm may continue while the system remains active;
- human oversight or fallback controls are ineffective;
- a material vulnerability remains uncontrolled;
- a regulator or competent authority requires restriction;
- corrective action cannot be independently verified;
- the provider repeatedly breaches notification or remediation obligations.

## 12. Control activities

| Control ID | Control activity | Owner | Evidence |
|---|---|---|---|
| EUAI-TPRM-75-01 | Include proportionate audit rights in AI contracts | Procurement and Legal | Executed agreement, clause checklist |
| EUAI-TPRM-75-02 | Define reportable AI incidents and notification windows | Legal, Security, Compliance | Contract schedule, incident taxonomy |
| EUAI-TPRM-75-03 | Maintain supplier evidence-request and audit procedure | Third-Party Risk | Procedure, requests, responses, findings |
| EUAI-TPRM-75-04 | Preserve evidence for material AI incidents | Security and System Owner | Logs, legal hold, evidence register |
| EUAI-TPRM-75-05 | Require accountable human stop/continue decisions | Business Owner | Decision record, approvals, escalation log |
| EUAI-TPRM-75-06 | Track provider corrective actions to verified closure | Third-Party Risk | Corrective-action plan, validation results |
| EUAI-TPRM-75-07 | Exercise audit and incident clauses periodically | Internal Audit or Assurance | Test results, simulations, lessons learned |

## 13. Evidence requirements

Minimum evidence should include:

- executed audit-right and incident-notification clauses;
- provider contact and escalation matrix;
- supplier incident taxonomy;
- evidence requests and provider responses;
- audit reports and walkthrough notes;
- incident notices and update history;
- preserved logs and technical evidence;
- impact and legal assessments;
- stop, restriction, restoration, and closure decisions;
- traveler, employee, client, or regulator communications;
- corrective-action verification;
- lessons-learned records.

## 14. Audit test

Select a sample of material AI suppliers and determine whether:

1. contracts contain usable audit and incident-notification rights;
2. reportable events and time expectations are defined;
3. provider evidence can be obtained at the required level of detail;
4. emergency investigation rights are not blocked by routine notice restrictions;
5. incidents are escalated to accountable human owners;
6. stop and restoration decisions are documented;
7. corrective actions are independently verified;
8. records support regulatory and client cooperation;
9. confidentiality safeguards do not prevent necessary assurance;
10. repeated provider failures trigger stronger action.

## 15. Metrics

Useful measures include:

- percentage of material AI contracts with approved audit clauses;
- percentage with defined AI incident-notification terms;
- average provider notification delay;
- percentage of notices containing required minimum information;
- open supplier corrective actions by severity and age;
- percentage of high-risk suppliers audited during the review period;
- number of incidents requiring service restriction or suspension;
- percentage of restorations supported by documented verification;
- repeat incident rate by provider and system;
- unresolved evidence gaps.

## 16. Management checklist

- [ ] Audit rights are proportionate to AI risk.
- [ ] Rights cover documentation, controls, testing, incidents, and corrective action.
- [ ] Enhanced rights apply after material trigger events.
- [ ] Incident categories and timelines are defined.
- [ ] Initial and follow-up notification content is specified.
- [ ] Evidence preservation is required.
- [ ] Regulatory cooperation is addressed.
- [ ] Human stop, restriction, and restoration decisions are mandatory.
- [ ] Repeated provider failures trigger escalation.
- [ ] Audit rights are periodically exercised or tested.

## 17. Key takeaway

A contractual right that cannot be exercised quickly, cannot reach relevant evidence, or cannot support a stop decision is not an effective control. GlobalWay must combine practical audit access, timely incident notification, accountable human judgment, and verified corrective action throughout the AI supply chain.
