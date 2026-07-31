# Chapter 110 — Corrective-Action Management

## Purpose

This chapter defines how AI-related findings, incidents, control failures, complaints, and regulatory issues should be converted into accountable corrective actions and verified through sustainable closure.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should maintain a corrective-action process that identifies root cause, assigns accountable ownership, defines measurable remediation, establishes deadlines based on severity, implements interim controls, verifies effectiveness, and prevents recurrence.

## Plain-language explanation

Closing a finding is not the same as fixing the problem. A corrective action is complete only when the underlying cause has been addressed, the control operates as intended, evidence supports closure, and related systems or processes have been checked for the same weakness.

## Corrective-action lifecycle

1. Record and classify the issue.
2. Contain immediate risk.
3. Determine root cause and contributing factors.
4. Define corrective and preventive actions.
5. Assign owner, resources, milestones, and due date.
6. Implement remediation.
7. Test design and operation.
8. Validate closure independently where appropriate.
9. Monitor for recurrence.
10. Share lessons learned.

## Root-cause analysis

Consider causes involving:

- governance and accountability;
- unclear requirements;
- process design;
- data quality or provenance;
- model design or configuration;
- software, infrastructure, or integration;
- human factors and training;
- vendor or fourth-party dependency;
- inadequate testing;
- weak monitoring;
- unauthorized change;
- resource or capacity constraints;
- incentives or organizational culture.

Do not accept “human error” as a complete root cause without examining why the process allowed the error to produce harm.

## Remediation-plan attributes

Each plan should include:

- issue and severity;
- affected systems and people;
- immediate containment;
- root cause;
- corrective action;
- preventive action;
- accountable owner;
- supporting teams;
- milestones and deadline;
- required evidence;
- testing and closure criteria;
- dependencies;
- interim risk and compensating controls;
- escalation triggers.

## Overdue actions

Overdue critical or high actions should trigger formal escalation, reassessment of residual risk, review of continued operation, and possible suspension. Repeated extensions require documented executive challenge and must not become indefinite acceptance.

## GlobalWay Travel Services example

GlobalWay discovers repeated hallucinated baggage-policy answers from its traveler chatbot. The initial correction changed the prompt but the issue returned. Root-cause analysis identifies stale supplier content, weak retrieval validation, and no threshold for escalating low-confidence answers. GlobalWay corrects the data feed, introduces source validation, adds confidence-based human escalation, tests affected routes, and monitors recurrence for 90 days before closure.

## Control activities

- Maintain one authoritative corrective-action register.
- Require root-cause analysis for material and recurring issues.
- Link deadlines to severity.
- Define interim controls and operating restrictions.
- Require objective closure criteria.
- Use independent validation for significant issues.
- Check for similar weaknesses across systems.
- Escalate overdue actions and repeated extensions.
- Feed lessons into policies, controls, training, and design standards.

## Evidence

- corrective-action register;
- containment decisions;
- root-cause analyses;
- remediation plans;
- milestone updates;
- implementation evidence;
- test and retest results;
- extension approvals;
- closure validation;
- recurrence monitoring;
- lessons-learned records.

## Audit tests

1. Sample corrective actions and trace them to the originating issue.
2. Verify root cause is supported and not merely a symptom.
3. Confirm deadlines and escalation align with severity.
4. Review interim controls for overdue actions.
5. Test whether closure criteria were met and independently validated where required.
6. Review recurring issues for systemic remediation.
7. Confirm lessons learned changed relevant controls or processes.

## Metrics

- open actions by severity;
- overdue critical and high actions;
- average time to contain and remediate;
- repeated extensions;
- recurrence rate;
- actions closed without independent validation;
- systemic issues affecting multiple systems;
- remediation effectiveness failures.

## Management checklist

- Is immediate risk contained?
- Does the plan address root cause rather than symptoms?
- Are owners, deadlines, evidence, and closure criteria explicit?
- Are overdue actions escalated?
- Has recurrence been monitored?
- Were similar systems checked?

## Figure specification — AI Corrective-Action Lifecycle

Create a closed-loop flow from issue identification and containment through root-cause analysis, remediation planning, implementation, validation, closure, recurrence monitoring, and lessons learned.

**Alt text:** AI corrective-action lifecycle from issue identification and containment through root-cause analysis, remediation, validation, closure, recurrence monitoring, and lessons learned.