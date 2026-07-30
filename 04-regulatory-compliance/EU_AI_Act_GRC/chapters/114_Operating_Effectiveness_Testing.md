# Chapter 114 — Operating-Effectiveness Testing

## Purpose

This chapter explains how to determine whether suitably designed AI controls operated consistently, completely, accurately, and on time during the period under review.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should test the operating effectiveness of key AI controls using sufficient and appropriate evidence. Testing should confirm that the control was performed by authorized personnel, covered the intended population, used reliable information, produced required evidence, and triggered escalation or correction when exceptions occurred.

## Plain-language explanation

A well-designed control provides assurance only when it actually operates. A policy may require approval before model deployment, but assurance depends on evidence that every applicable deployment received complete and timely approval and that missing approvals blocked release.

## Preconditions

Before operating-effectiveness testing:

- confirm the control design is effective;
- define the test period;
- identify the full population;
- validate population completeness and accuracy;
- understand control frequency and triggers;
- identify control owners and performers;
- define expected evidence and exceptions;
- determine whether system-generated information is reliable.

## Testing methods

Use one or more of the following:

- inspection of records;
- reperformance;
- observation;
- system-query validation;
- configuration testing;
- sample testing;
- full-population analytics;
- exception-log review;
- inquiry supported by corroborating evidence;
- tracing from trigger through approval, execution, evidence, and closure.

## Attributes to test

Determine whether:

- the control operated at the required frequency or trigger;
- the performer was authorized and competent;
- the complete population was covered;
- required review steps were completed;
- thresholds were applied consistently;
- evidence was generated and retained;
- exceptions were identified and escalated;
- remediation occurred within defined timelines;
- approvals were obtained before the relevant action;
- override or bypass activity was detected and reviewed.

## Automated controls

For automated or hybrid controls, assess:

- configuration and rule logic;
- change-management controls;
- access to modify rules;
- input-data completeness and accuracy;
- interface and job failures;
- alert routing;
- exception handling;
- continued operation after releases or vendor changes.

When effective general IT controls cannot be relied upon, perform additional direct testing.

## Deviations and conclusions

For each deviation, determine:

- nature and cause;
- population affected;
- duration;
- risk and requirement impacted;
- whether the deviation is isolated or systemic;
- whether compensating controls operated;
- whether additional sampling is required;
- whether the control conclusion changes.

Conclude effective, partially effective, or ineffective, with a clear basis.

## GlobalWay Travel Services example

GlobalWay tests its mandatory human-review control for low-confidence itinerary recommendations. A complete system report identifies 480 triggered cases. Testing finds that 17 were released without documented review because weekend staffing was insufficient.

GlobalWay expands testing, confirms the issue is systemic during two weekend periods, suspends automated release for affected cases, adds coverage controls, and treats the control as ineffective for the period.

## Control activities

- Define the period, population, attributes, and test method.
- Validate source-data reliability.
- Select representative samples or use full-population testing.
- Reperform key control steps where appropriate.
- Evaluate deviations individually and in aggregate.
- expand testing when exceptions indicate systemic failure.
- document conclusions and management responses.
- retest remediation before closure.

## Evidence

- complete control populations;
- sample-selection records;
- approvals and review records;
- system logs and reports;
- configuration evidence;
- exception and escalation records;
- reperformance results;
- deviation analyses;
- control conclusions;
- remediation and retest evidence.

## Audit tests

1. Verify that design effectiveness was established before reliance.
2. Validate the completeness and accuracy of the control population.
3. Select samples appropriate to frequency, risk, and expected deviation.
4. Test performer authority, timeliness, evidence, and required attributes.
5. Review deviations and determine whether testing should be expanded.
6. Inspect automated-control configuration and change history.
7. Confirm the final conclusion is supported by the results.

## Metrics

- key controls tested;
- controls rated effective, partially effective, or ineffective;
- deviation rate;
- late or missing control performance;
- unauthorized performers;
- automated-control failures;
- repeat operating deficiencies;
- remediation retest pass rate.

## Management checklist

- Did the control operate throughout the period?
- Was the complete population covered?
- Was performance timely and properly authorized?
- Are records sufficient to demonstrate operation?
- Were exceptions escalated and corrected?
- Do deviations indicate an isolated or systemic problem?

## Figure specification — Operating-Effectiveness Test Cycle

Create a cycle showing design reliance, population validation, sampling or analytics, attribute testing, deviation evaluation, expanded testing, conclusion, remediation, and retesting.

**Alt text:** Operating-effectiveness testing cycle from design reliance and population validation through testing, deviation evaluation, conclusion, remediation, and retesting.