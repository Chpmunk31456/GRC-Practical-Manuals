# Chapter 114 — Operating Effectiveness Testing

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 114 draft language.

## Requirement

Operating effectiveness testing must determine whether AI controls operated consistently, completely, accurately, timely, and by authorized competent personnel throughout the period under review.

## Plain-English explanation

A well-designed control may fail in practice. Operating testing examines actual transactions, releases, decisions, incidents, changes, and records to confirm that the control worked repeatedly and that exceptions were handled properly.

## Testing requirements

The tester should evaluate:

1. the defined review period and relevant population;
2. completeness and reliability of the population used for sampling;
3. evidence that the control operated at the required frequency;
4. timeliness, accuracy, and completeness of execution;
5. performer authorization, competence, and independence;
6. application of thresholds, approvals, and escalation rules;
7. treatment of exceptions, overrides, failures, and missing evidence;
8. consistency across systems, models, versions, vendors, and jurisdictions;
9. remediation and retesting of identified failures;
10. whether compensating controls operated where the primary control failed.

## GlobalWay example

GlobalWay tests a sample of AI release approvals over six months. The tester verifies that every sampled release used the approved model version, completed required legal and technical reviews, resolved blocking issues, obtained authorized approval, and retained evidence before production deployment.

## Control activity

Control owners must retain evidence sufficient to reconstruct operation. Independent testers must use reliable populations, defensible samples, clear exception criteria, and documented conclusions supported by the evidence reviewed.

## Evidence

- population and completeness validation;
- sample-selection record;
- executed control evidence;
- timestamps, approvals, and reviewer identity;
- exception and escalation records;
- compensating-control evidence;
- remediation and retest results;
- testing conclusion and quality review.

## Audit test

Select key controls and independently validate the population. Test a risk-based sample across the review period, document all deviations, assess whether failures are isolated or systemic, and determine whether the control operated effectively.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable quality-management, documentation, recordkeeping, risk-management, monitoring, incident, corrective-action, and governance provisions.
- Current consolidated official texts control over older summaries.