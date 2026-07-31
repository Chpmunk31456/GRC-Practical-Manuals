# Chapter 103 — Residual Risk, Acceptance, and Exceptions

## Purpose

This chapter defines how organizations should identify residual AI risk, decide whether it is acceptable, approve exceptions, impose compensating controls, and monitor conditions until closure or renewal.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Residual AI risk should be accepted only by an authorized decision maker who understands the remaining exposure, affected people, legal constraints, control limitations, duration, monitoring requirements, and alternatives. Risk acceptance must never be used to authorize prohibited conduct or waive a binding legal obligation.

## Plain-language explanation

Controls rarely reduce risk to zero. The remaining exposure is residual risk. Management may accept some residual risk when the business need is legitimate and the remaining exposure is within approved tolerance. That decision must be explicit, evidence-based, time-limited where appropriate, and subject to review.

## Residual-risk determination

Document:

- inherent risk;
- implemented controls;
- control design and operating effectiveness;
- remaining likelihood and impact;
- affected people and rights;
- legal and contractual constraints;
- uncertainty and evidence limitations;
- dependencies and assumptions;
- proposed monitoring;
- fallback, suspension, and exit options.

## Acceptance criteria

A residual-risk decision should confirm that:

- the use case remains lawful and consistent with policy;
- prohibited practices are excluded;
- mandatory controls and obligations are satisfied;
- material harms have been considered;
- the decision maker has appropriate authority;
- alternatives were evaluated;
- the exposure is within approved risk appetite or formally escalated;
- monitoring and escalation triggers are defined;
- the decision has an expiry or review date.

## Exceptions

An exception is a temporary, formally approved departure from an internal control, standard, or procedure. Each exception record should state:

- the specific requirement affected;
- business justification;
- scope and systems covered;
- start and expiry dates;
- risk assessment;
- affected stakeholders;
- compensating controls;
- remediation owner and target date;
- monitoring and reporting frequency;
- approval authority;
- renewal and closure criteria.

## Non-acceptable exceptions

Do not approve an exception that would:

- permit a prohibited AI practice;
- bypass a binding legal duty;
- conceal a material incident or known harm;
- remove required human oversight without lawful justification;
- authorize unbounded use of sensitive or special-category data;
- suppress evidence, logs, complaints, or audit findings;
- continue a system that cannot fail or degrade safely;
- transfer accountability to an unqualified or unauthorized person.

## Compensating controls

Examples include:

- reduced functionality;
- narrower user population;
- lower transaction or decision limits;
- mandatory dual approval;
- increased human review;
- enhanced logging and monitoring;
- additional testing;
- restricted data access;
- temporary manual processing;
- more frequent management reporting;
- predefined suspension triggers.

Compensating controls should reduce the specific risk created by the exception rather than merely add unrelated activity.

## Renewal and closure

Before renewal, verify:

- the business need still exists;
- the original assumptions remain valid;
- no incident or regulatory change alters the decision;
- compensating controls operated effectively;
- remediation progressed;
- the exception remains within tolerance;
- continued acceptance is preferable to suspension or replacement.

Close the exception when the underlying requirement is met, the system is retired, the use case changes, or risk can no longer be accepted.

## GlobalWay Travel Services example

GlobalWay’s disruption assistant cannot initially provide the planned automated confidence explanation for one legacy airline feed. The feature is not legally prohibited, but the gap could mislead consultants.

GlobalWay approves a 60-day exception limited to internal users. It disables automated traveler-facing output for that feed, requires manual validation, adds a warning banner, increases sampling, and sets a hard expiry. The exception owner must either deliver the control, remove the feed, or suspend the feature before expiry.

## Control activities

- Define risk-acceptance and exception authorities.
- Separate legal obligations from internal requirements that may permit exceptions.
- Use a standard approval record.
- Require risk-based compensating controls.
- Set expiry and review dates.
- Monitor conditions and trigger early reassessment after incidents or change.
- Escalate overdue exceptions.
- Report material acceptances and exceptions to senior management or the board.

## Evidence

- residual-risk assessments;
- risk-acceptance records;
- exception requests and approvals;
- authority matrix;
- compensating-control evidence;
- monitoring reports;
- expiry and renewal records;
- remediation plans;
- escalation records;
- closure verification;
- management and board reporting.

## Audit tests

1. Sample residual-risk acceptances and verify the approver had appropriate authority.
2. Confirm prohibited practices and binding obligations were not treated as waivable.
3. Trace the assessment from inherent risk through controls to residual risk.
4. Verify exceptions are scoped, justified, time-limited, and monitored.
5. Test whether compensating controls address the actual control gap.
6. Review overdue or repeatedly renewed exceptions for escalation and challenge.
7. Confirm closure evidence demonstrates the requirement was met or the exposure ended.

## Metrics

- open AI risk acceptances by severity;
- open exceptions by risk tier;
- overdue exceptions;
- repeatedly renewed exceptions;
- exceptions without effective compensating controls;
- incidents involving accepted risk;
- average exception age;
- time to remediation;
- material acceptances reported to executives or the board.

## Management checklist

- Is the remaining exposure clearly understood?
- Is the decision lawful and within authority?
- Are affected people and rights considered?
- Are compensating controls specific and effective?
- Is there a clear expiry, owner, and remediation path?
- What event would require immediate suspension or reassessment?

## Figure specification — Residual-Risk Decision Gate

Create a decision flow from inherent risk through controls and effectiveness testing to residual risk. Branch to accept, remediate, transfer, restrict, suspend, or reject. Show approval authority, expiry, monitoring, and reassessment as mandatory governance gates.

**Alt text:** Residual-risk decision flow from inherent risk and control effectiveness to acceptance, remediation, transfer, restriction, suspension, or rejection, with approval authority, expiry, monitoring, and reassessment gates.
