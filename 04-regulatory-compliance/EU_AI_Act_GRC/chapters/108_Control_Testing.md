# Chapter 108 — Control Testing

## Purpose

This chapter defines how to test whether AI controls are suitably designed, implemented, and operating effectively.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should test key AI controls using a documented, risk-based methodology. Testing should evaluate design effectiveness, implementation, operating effectiveness, evidence quality, exceptions, and remediation.

## Plain-language explanation

A control can exist on paper and still fail in practice. Control testing determines whether the activity is capable of preventing or detecting the intended risk, whether it was implemented, and whether it operated consistently during the period reviewed.

## Testing objectives

Testing should answer:

- Is the control clearly defined?
- Does the design address the stated requirement or risk?
- Is the control implemented in the relevant process and system?
- Did it operate at the required frequency or trigger?
- Was the population complete?
- Is evidence reliable and attributable?
- Were exceptions identified and escalated?
- Did failures result in corrective action?

## Test planning

Document:

- control and objective;
- requirement and risk addressed;
- scope and period;
- systems and populations;
- test method;
- sample approach;
- evidence required;
- tester competence and independence;
- expected result;
- rating criteria;
- reporting and escalation.

## Test methods

Use one or more of:

- inquiry, supported by corroborating evidence;
- observation;
- inspection;
- reperformance;
- configuration review;
- data analysis;
- automated testing;
- transaction or decision sampling;
- walkthrough;
- scenario or failure testing.

Inquiry alone is generally insufficient for a key control conclusion.

## Sampling

Sampling should consider population size, control frequency, risk, expected deviation, prior findings, automation, and system change. Preserve the population, selection method, sample items, exceptions, and evaluation rationale.

## Automated controls

For automated controls, test:

- configuration and logic;
- access and change management;
- input completeness and accuracy;
- processing integrity;
- exception handling;
- monitoring and alerting;
- relevant supporting general controls.

## Deficiency evaluation

A test exception should be evaluated for:

- cause;
- frequency and duration;
- affected systems and decisions;
- legal, safety, privacy, security, and rights impact;
- compensating controls;
- evidence reliability;
- likelihood of recurrence;
- need for suspension, escalation, or notification.

## GlobalWay Travel Services example

GlobalWay tests the deployment-approval control for its traveler-assistance systems. The tester obtains the complete release population, samples releases across the review period, verifies required approvals and evidence, and reperforms the release-blocking logic. One release used an expired privacy approval, resulting in a control deficiency, expanded testing, and remediation of the approval-expiry alert.

## Control activities

- Maintain a risk-based control-testing plan.
- Define test methods and rating criteria.
- Preserve complete populations and samples.
- Require competent and sufficiently independent testers.
- Test automated logic and supporting controls.
- Evaluate exceptions consistently.
- Track findings through validated closure.
- Increase testing after material change or repeated failure.

## Evidence

- testing methodology;
- annual or periodic test plan;
- control narratives and walkthroughs;
- population and sampling records;
- test scripts and workpapers;
- evidence reviewed;
- exceptions and deficiency ratings;
- reports and management responses;
- remediation and retest results;
- tester competence and independence records.

## Audit tests

1. Review the testing universe and confirm key controls receive proportionate coverage.
2. Inspect test plans for scope, method, population, sample, and criteria.
3. Reperform selected tests.
4. Confirm inquiry was corroborated.
5. Review automated-control logic and supporting controls.
6. Trace exceptions to deficiency evaluation, escalation, and remediation.
7. Confirm closure was supported by successful retesting.

## Metrics

- key controls tested;
- design and operating failures;
- repeat deficiencies;
- overdue testing;
- unsupported control conclusions;
- population or sampling defects;
- failed automated controls;
- average remediation and retest time;
- findings reopened after closure.

## Management checklist

- Are the most important controls tested often enough?
- Is testing independent and evidence based?
- Are populations complete and samples defensible?
- Are automated controls tested beyond screenshots?
- Do failures lead to timely remediation and validated closure?

## Figure specification — AI Control Testing Workflow

Create a workflow showing planning, population validation, sampling, evidence collection, inspection and reperformance, exception evaluation, deficiency rating, remediation, retest, and closure. Include separate paths for manual and automated controls.

**Alt text:** AI control testing workflow from planning and population validation through sampling, evidence review, exception evaluation, deficiency rating, remediation, retest, and closure, with manual and automated control paths.