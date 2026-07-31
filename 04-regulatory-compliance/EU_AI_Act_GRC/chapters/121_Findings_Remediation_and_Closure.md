# Chapter 121 — Findings, Remediation, and Closure

## Purpose

This chapter explains how organizations should classify AI-related findings, assign accountable owners, implement corrective action, verify completion, and close issues only when evidence demonstrates that the underlying risk or control failure has been addressed.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should maintain a documented process for recording, prioritizing, remediating, validating, escalating, and closing findings arising from audits, control testing, technical validation, incidents, complaints, regulatory reviews, vendor assessments, and management monitoring.

## Plain-language explanation

A finding is not closed because a team says the work is finished. Closure requires evidence that the agreed action was completed, the affected control now works, residual risk is acceptable, and no related issue remains hidden elsewhere.

## Finding record

Each finding should include:

- unique identifier;
- source and date identified;
- affected system, process, model, vendor, and jurisdiction;
- requirement or control affected;
- condition observed;
- root cause;
- risk and affected people;
- severity and rationale;
- accountable owner;
- remediation plan and target date;
- interim or compensating controls;
- escalation status;
- closure criteria;
- evidence required for validation.

## Severity and prioritization

Prioritize using factors such as:

- legal or regulatory breach;
- prohibited-practice exposure;
- safety or fundamental-rights harm;
- scale and duration of impact;
- data sensitivity;
- likelihood of recurrence;
- control dependency;
- exploitability or abuse potential;
- customer, employee, or public impact;
- regulator, litigation, and reputational exposure;
- absence of effective compensating controls.

## Root-cause analysis

Distinguish symptoms from causes. Root causes may include:

- unclear accountability;
- inadequate requirement interpretation;
- weak design or testing;
- poor data governance;
- vendor dependency;
- insufficient training;
- ineffective monitoring;
- change-management failure;
- unrealistic procedures;
- resource or capacity constraints;
- incentive or governance conflicts.

## Remediation planning

A corrective-action plan should define:

- specific actions;
- responsible owner and contributors;
- milestones;
- target completion date;
- dependencies;
- interim safeguards;
- required approvals;
- validation method;
- rollback or suspension conditions;
- communication needs.

## Closure validation

Before closure, confirm that:

- actions are complete;
- evidence is authentic, current, and version matched;
- the control design is adequate;
- operating effectiveness is demonstrated where required;
- affected populations and related systems were considered;
- regression or unintended consequences were tested;
- residual risk is approved;
- temporary controls are removed or formally retained;
- documentation, training, and monitoring are updated.

## GlobalWay Travel Services example

An audit finds that GlobalWay’s recruitment-screening system does not consistently record human overrides. The issue affects traceability and oversight. GlobalWay changes the interface, requires a reason code, updates procedures, trains reviewers, and monitors completion rates.

Closure occurs only after validation confirms that override records are complete across a representative period and that missing records trigger escalation.

## Control activities

- Maintain a centralized findings register.
- Apply consistent severity criteria.
- Require root-cause analysis for material issues.
- Assign accountable owners and due dates.
- Implement interim controls where needed.
- Escalate overdue and high-severity findings.
- Validate remediation independently.
- Reopen findings when evidence is incomplete or controls fail again.

## Evidence

- findings register;
- risk and severity assessments;
- root-cause analyses;
- corrective-action plans;
- interim-control records;
- progress reports;
- test and validation results;
- closure approvals;
- residual-risk acceptances;
- reopened-finding records;
- management and board reporting.

## Audit tests

1. Sample findings and verify condition, cause, risk, owner, due date, and closure criteria are documented.
2. Confirm severity is consistent with defined methodology.
3. Review overdue findings for escalation.
4. Trace remediation actions to reliable evidence.
5. Verify closure testing addressed both design and operation where required.
6. Confirm related systems and recurrence risk were considered.
7. Review reopened or repeated findings for management challenge.

## Metrics

- open findings by severity;
- overdue findings;
- average remediation time;
- repeated and reopened findings;
- findings without root-cause analysis;
- findings closed without independent validation;
- interim controls beyond expiry;
- high-severity findings reported to executives or the board.

## Management checklist

- Are material findings prioritized correctly?
- Is the actual root cause understood?
- Are interim controls protecting affected people?
- Is the remediation plan specific and achievable?
- Is closure supported by independent evidence?
- Could the same issue exist elsewhere?

## Figure specification — AI Finding-to-Closure Lifecycle

Create a lifecycle from identification, validation, severity, root cause, ownership, remediation, interim controls, retesting, residual-risk decision, closure, and recurrence monitoring. Show escalation and reopening as mandatory side paths.

**Alt text:** AI finding lifecycle from identification and severity through root-cause analysis, remediation, retesting, residual-risk approval, closure, monitoring, escalation, and reopening.