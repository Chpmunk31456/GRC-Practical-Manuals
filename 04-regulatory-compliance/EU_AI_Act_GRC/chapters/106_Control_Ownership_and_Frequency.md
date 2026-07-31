# Chapter 106 — Control Ownership and Frequency

## Purpose

This chapter defines how to assign accountable ownership, performance responsibility, review responsibility, and operating frequency for AI controls.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Every material AI control should have a named accountable owner, an identified performer, a defined frequency or trigger, documented evidence, and an escalation path for failure or delay.

## Plain-language explanation

A control without a clear owner is unlikely to operate consistently. A control without a defined frequency may occur too late or not at all. Ownership and timing should reflect the control’s purpose, risk, system lifecycle, and the speed at which conditions can change.

## Responsibility model

For each control, identify:

- accountable owner;
- control performer;
- reviewer or approver;
- escalation authority;
- backup owner or delegate;
- required competence;
- segregation-of-duties constraints.

The accountable owner remains responsible even when performance is delegated or automated.

## Frequency types

Controls may be:

- continuous;
- per transaction or decision;
- daily, weekly, monthly, quarterly, or annual;
- before deployment;
- after material change;
- after incident or complaint;
- at contract renewal;
- on regulatory change;
- at model retraining, replacement, or retirement.

Frequency should be risk based and should consider how quickly harm, drift, noncompliance, or control failure could emerge.

## Trigger design

Event-triggered controls should define observable triggers such as:

- new use case;
- role or classification change;
- model or data update;
- performance threshold breach;
- security vulnerability;
- material vendor change;
- serious incident;
- regulatory update;
- repeated complaint;
- control failure;
- exception expiry.

## Ownership conflicts

Avoid arrangements where the same person can initiate, approve, evidence, and close a high-impact control without independent challenge. Increase separation and review for high-risk, rights-sensitive, safety-critical, or financially material systems.

## GlobalWay Travel Services example

GlobalWay assigns the AI product owner responsibility for completing deployment-readiness controls, but release approval is performed by a separate release authority after legal, privacy, security, and human-oversight approvals are verified. Monitoring runs continuously, while formal risk reassessment occurs quarterly and after material change or incident.

## Control activities

- Assign owners and performers for every key control.
- Define competence and delegation rules.
- Set risk-based frequencies and event triggers.
- Establish backup coverage.
- Enforce segregation of duties.
- Track missed, late, or failed controls.
- Review ownership after organizational or system change.

## Evidence

- control-owner register;
- responsibility matrix;
- job descriptions;
- delegation records;
- control calendar;
- automated schedules and alerts;
- completed control evidence;
- escalation and overdue reports;
- segregation-of-duties reviews.

## Audit tests

1. Sample key controls and verify ownership, performance, and review roles.
2. Confirm frequencies and triggers align with risk and lifecycle events.
3. Review overdue or missed controls and escalation.
4. Test backup coverage and delegation.
5. Inspect segregation of duties for high-impact controls.
6. Confirm ownership records were updated after organizational change.

## Metrics

- key controls without owners;
- overdue control executions;
- failed controls by owner;
- controls without backup coverage;
- segregation-of-duties conflicts;
- missed event-triggered reviews;
- average time to reassign ownership after change.

## Management checklist

- Is one person clearly accountable for each key control?
- Is the performer competent and appropriately independent?
- Does the frequency match the speed of risk?
- Are event triggers observable and monitored?
- Are missed controls escalated promptly?

## Figure specification — AI Control Responsibility and Timing Model

Create a matrix connecting accountable owner, performer, reviewer, escalation authority, frequency, event triggers, evidence, and backup coverage. Distinguish continuous, periodic, and lifecycle-gate controls.

**Alt text:** AI control responsibility and timing matrix showing accountable owners, performers, reviewers, escalation, frequencies, event triggers, evidence, and backup coverage.