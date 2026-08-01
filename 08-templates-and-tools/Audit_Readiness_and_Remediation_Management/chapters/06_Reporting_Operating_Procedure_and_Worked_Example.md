# Reporting, Operating Procedure, and Worked Example

## Executive reporting

Readiness and remediation reporting should support decisions about risk, resources, timing, and accountability. Avoid dashboards that show only counts without severity, age, exposure, ownership, or trend.

A useful executive view includes:

- assessment scope and current readiness confidence;
- open findings by severity and age;
- overdue and extended actions;
- critical dependencies and resource constraints;
- repeated or reopened findings;
- residual-risk concentration;
- upcoming audits, certifications, customer reviews, or regulatory milestones;
- decisions required from leadership.

## Operating cadence

A practical cadence may include:

- weekly action-owner review for critical and high findings;
- monthly remediation governance meeting;
- quarterly executive or risk-committee reporting;
- event-driven escalation for missed critical milestones, material scope changes, failed closure tests, or new exposure.

Meeting records should capture decisions, owners, due dates, and dissenting views.

## End-to-end operating procedure

### Step 1 — Authorize the readiness review

Confirm sponsor, objective, criteria, scope, period, systems, locations, stakeholders, independence expectations, and reporting route.

### Step 2 — Build the criteria and control universe

Map applicable requirements to control objectives, owners, systems, evidence sources, and assessment procedures. Record interpretation assumptions and exclusions.

### Step 3 — Perform readiness assessment

Review design, implementation, and available operating evidence. Use inquiry, inspection, observation, reperformance, population analysis, and sampling as appropriate.

### Step 4 — Record gaps and validate facts

Document criterion, condition, evidence, scope, cause, risk, compensating controls, and proposed owner. Allow factual challenge supported by evidence.

### Step 5 — Prioritize and approve findings

Apply approved severity definitions. Record final classification, accountable owner, acceptance date, and escalation requirements.

### Step 6 — Approve remediation plans

Require actions linked to causes, interim controls, milestones, resources, success measures, closure evidence, and residual-risk expectations.

### Step 7 — Monitor execution

Track milestones, blockers, extensions, scope changes, emerging risk, and evidence. Escalate according to severity and governance rules.

### Step 8 — Validate closure

Test completion and effectiveness against pre-agreed criteria. Record evidence, procedures, sample, results, residual risk, conclusion, and follow-up monitoring.

### Step 9 — Report and learn

Report trends, repeated causes, overdue exposure, resource constraints, closure failures, and lessons that should change control design or governance.

## Worked example

### Scenario

An organization’s access-control procedure requires terminated-user accounts to be disabled within one business day. A readiness review compares human-resources termination records with identity-platform accounts for the prior quarter.

### Evidence and result

The reviewer obtains the complete termination population from the HR system and the account-status export from the identity platform. Six of 120 terminated workers had active accounts more than one business day after termination. Two accounts remained active for more than ten days. No evidence of misuse was identified, but monitoring did not reliably detect overdue disablement.

### Finding

- Criterion: approved termination-access procedure requiring disablement within one business day.
- Condition: six of 120 accounts exceeded the approved timeframe.
- Cause: the process depended on manual email notification, lacked reconciliation, and did not assign ownership for failed notifications.
- Risk: former workers could retain unauthorized access to systems and data.
- Priority: high, based on access exposure, duration, and monitoring weakness.

### Remediation plan

1. Implement daily HR-to-identity reconciliation.
2. Assign exception ownership to identity operations.
3. Create an overdue-account alert and escalation rule.
4. Correct all current exceptions.
5. Test the full population weekly for eight weeks.
6. Report exceptions and response time to the security governance forum.

### Closure criteria

- all current overdue accounts corrected;
- automated daily reconciliation operating;
- documented ownership and escalation;
- eight weeks of population evidence;
- no unexplained overdue accounts;
- exceptions resolved within the approved timeframe or formally escalated.

### Validation conclusion

If the eight-week evidence supports the criteria, the finding may be closed with continuing quarterly monitoring. If overdue accounts remain or the reconciliation population is incomplete, validation fails and the finding remains open.

## Practical implementation roadmap

### First 30 days

- approve governance and severity definitions;
- inventory upcoming assurance activities;
- establish the criteria-to-control map;
- identify control and remediation owners;
- deploy the readiness and finding trackers.

### Days 31–60

- conduct risk-based readiness reviews;
- validate findings and causes;
- approve remediation plans;
- begin governance reporting;
- establish closure-evidence standards.

### Days 61–90

- validate early remediation results;
- analyze recurring causes and bottlenecks;
- refine metrics and escalation thresholds;
- schedule sustainability reviews;
- integrate lessons into continuous control monitoring.

## Final principle

Readiness is a continuous governance capability. The objective is not to create the appearance of compliance for an assessment date, but to maintain controls and evidence that remain credible before, during, and after independent review.
