# Chapter 107 — Evidence Standards

## Purpose

This chapter defines the standards for collecting, validating, retaining, protecting, and presenting evidence that demonstrates AI controls were designed and operated effectively.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should retain evidence that is sufficient, reliable, relevant, timely, complete, attributable, protected from unauthorized alteration, and traceable to the control, system, period, and decision it supports.

## Plain-language explanation

A control may have operated, but without reliable evidence the organization may be unable to prove it. Evidence standards ensure that records can support management review, internal audit, conformity readiness, incident response, litigation, and regulatory inquiry.

## Evidence-quality criteria

Evidence should be:

- sufficient to support the conclusion;
- relevant to the control objective;
- complete for the population and period;
- accurate and reproducible;
- timely;
- attributable to a person, system, or approved automated process;
- protected against unauthorized change;
- understandable without unsupported assumptions;
- retained according to applicable requirements.

## Evidence types

Examples include:

- approved policies and procedures;
- system inventories and classification records;
- risk and impact assessments;
- technical documentation;
- model, data, and system cards;
- test results and validation reports;
- logs, alerts, and monitoring records;
- approvals and decision records;
- training and competence records;
- contracts and supplier evidence;
- incident, complaint, and remediation records;
- screenshots, exports, configuration records, and source-controlled files.

## Evidence metadata

Record where practical:

- control identifier;
- system and version;
- period or event covered;
- evidence owner;
- creation date and source;
- reviewer and approval date;
- retention category;
- confidentiality classification;
- integrity or version information;
- relationship to findings, exceptions, or remediation.

## Automated evidence

Automated evidence should be validated for completeness, accuracy, access control, clock synchronization, retention, and resistance to unauthorized alteration. Dashboards alone are not sufficient when underlying data cannot be reproduced or exported.

## Sampling and populations

For controls operating over a population, preserve enough information to identify the full population and support reproducible sampling. Avoid retaining only selected successful examples.

## GlobalWay Travel Services example

GlobalWay’s deployment gate requires approvals from privacy, security, legal, and human-oversight reviewers. The release record stores the system version, approval timestamps, approver identities, linked assessments, test results, and deployment decision. A dashboard summary is retained together with the underlying export and source references.

## Control activities

- Establish an AI evidence standard and taxonomy.
- Define evidence requirements for each control.
- Protect integrity, confidentiality, and availability.
- Preserve populations and reproducible samples.
- Validate automated evidence sources.
- Apply retention and legal-hold requirements.
- Review evidence quality during control testing.

## Evidence

- evidence standard;
- evidence register;
- retention schedule;
- access-control records;
- source-system validation;
- integrity and version history;
- legal-hold records;
- quality-review results;
- evidence-deficiency remediation.

## Audit tests

1. Sample key controls and inspect whether evidence is sufficient, relevant, complete, and attributable.
2. Trace evidence to the correct system, version, period, and owner.
3. Test integrity and access protections.
4. Confirm automated evidence can be reproduced from source data.
5. Verify populations support complete and unbiased sampling.
6. Review retention, deletion, and legal-hold compliance.
7. Identify evidence gaps that could invalidate a control conclusion.

## Metrics

- controls without defined evidence;
- missing or incomplete evidence;
- evidence not attributable to an owner or system version;
- automated sources not validated;
- retention exceptions;
- evidence-access violations;
- audit findings caused by evidence weakness.

## Management checklist

- Can the organization prove the control operated?
- Is the evidence complete, reliable, and reproducible?
- Is it linked to the correct system, version, and period?
- Is integrity protected?
- Can it be retained, retrieved, and explained when needed?

## Figure specification — Evidence Reliability Chain

Create a chain from control execution to source record, metadata, integrity protection, review, retention, retrieval, and audit conclusion. Show failure points for missing, incomplete, altered, or nonreproducible evidence.

**Alt text:** Evidence reliability chain from control execution and source records through metadata, integrity protection, review, retention, retrieval, and audit conclusion, with common evidence-failure points.