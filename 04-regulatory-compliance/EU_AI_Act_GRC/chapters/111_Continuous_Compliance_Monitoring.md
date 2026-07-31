# Chapter 111 — Continuous Compliance Monitoring

## Purpose

This chapter explains how organizations should monitor AI systems, controls, obligations, evidence, vendors, and changes continuously or at risk-based intervals so compliance deterioration is detected before it becomes material harm.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should establish risk-based continuous compliance monitoring that links legal and policy requirements to measurable indicators, thresholds, alerts, ownership, investigation, escalation, and corrective action. Monitoring should cover both technical performance and governance operation.

## Plain-language explanation

A system may be compliant at launch and become noncompliant later because data changes, a vendor updates a model, notices disappear, human reviewers stop intervening, logs fail, or exceptions expire. Continuous monitoring detects those changes and provides evidence that controls continue to operate.

## Monitoring scope

Monitor as appropriate:

- inventory completeness and ownership;
- classification and role changes;
- prohibited-practice indicators;
- high-risk and transparency obligations;
- model and data drift;
- accuracy, robustness, and cybersecurity;
- bias, fairness, and accessibility;
- human-oversight activity and override patterns;
- logging and evidence completeness;
- incidents, complaints, and appeals;
- vendor and model changes;
- control failures and overdue actions;
- exceptions and risk acceptances;
- training and AI-literacy completion;
- regulatory and standards changes.

## Monitoring design

For each monitored obligation or risk, define:

- objective;
- data source;
- population and scope;
- metric or test;
- threshold;
- frequency;
- owner;
- alert recipient;
- investigation procedure;
- escalation requirement;
- evidence retention;
- limitations and data-quality controls.

## Thresholds and alerts

Thresholds should be risk-based and distinguish informational signals from conditions requiring investigation, restriction, suspension, or regulatory assessment. Avoid excessive alerts that cannot be reviewed effectively. Threshold changes should be approved and version controlled.

## Data reliability

Monitoring is only as reliable as its data. Validate completeness, accuracy, timeliness, lineage, access control, and reconciliation. Monitor the monitoring system itself, including missing feeds, disabled alerts, failed jobs, and unauthorized changes.

## GlobalWay Travel Services example

GlobalWay monitors its AI disruption assistant for stale airline data, low-confidence recommendations, human overrides, traveler complaints, inaccessible notices, vendor model changes, and failed logging. A spike in overrides for one carrier triggers investigation. GlobalWay restricts automated recommendations for that carrier until the data mapping is corrected and retested.

## Control activities

- Map monitoring to obligations, risks, and key controls.
- Define risk-based indicators and thresholds.
- Validate monitoring data and system integrity.
- Assign investigation and escalation ownership.
- Connect alerts to corrective-action workflows.
- Review threshold effectiveness and alert fatigue.
- Preserve monitoring evidence.
- Reassess monitoring after incidents and material changes.

## Evidence

- monitoring framework;
- obligation-to-indicator mapping;
- metric definitions;
- threshold approvals;
- dashboards and alerts;
- investigations;
- data-quality validations;
- escalation records;
- corrective actions;
- monitoring-system change history;
- periodic effectiveness reviews.

## Audit tests

1. Select key obligations and confirm each has appropriate monitoring or documented rationale.
2. Verify metrics, sources, thresholds, frequency, and ownership are defined.
3. Test data completeness and reconciliation.
4. Trace alerts to investigation, escalation, and remediation.
5. Review disabled or changed alerts for authorization.
6. Assess alert backlog and review capacity.
7. Confirm monitoring adapts after incidents, model changes, and regulatory updates.

## Metrics

- obligations covered by monitoring;
- key controls without monitoring;
- alerts by severity;
- investigation and closure time;
- false-positive and missed-event rates;
- disabled or failed monitors;
- stale data feeds;
- overdue alert investigations;
- incidents first detected through monitoring.

## Management checklist

- Which compliance conditions could deteriorate after launch?
- Are monitoring data reliable and complete?
- Do thresholds lead to clear action?
- Can material alerts restrict or stop operation?
- Is monitoring evidence retained and auditable?
- Are the monitors themselves protected and tested?

## Figure specification — Continuous AI Compliance Monitoring Loop

Create a loop connecting obligations and risks to indicators, data collection, thresholds, alerts, investigation, escalation, corrective action, validation, and control improvement. Show monitoring-data assurance as a cross-cutting layer.

**Alt text:** Continuous AI compliance monitoring loop from obligations and risks through indicators, alerts, investigation, corrective action, validation, and control improvement, with data assurance throughout.