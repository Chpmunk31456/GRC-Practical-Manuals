# Chapter 113 — Design Effectiveness Testing

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 113 draft language.

## Requirement

Design effectiveness testing must determine whether each AI control, individually and collectively, is suitably designed to prevent, detect, correct, or escalate the relevant legal and operational risk when implemented as intended.

## Plain-English explanation

A control can exist on paper and still be incapable of achieving its purpose. Design testing examines whether the control has the right trigger, owner, authority, inputs, logic, frequency, evidence, escalation, and relationship to other controls.

## Design-testing requirements

For each control, assess:

1. the legal duty, risk, or objective addressed;
2. scope across systems, models, versions, actors, and jurisdictions;
3. trigger, frequency, timing, and preventive or detective nature;
4. accountable owner, competence, authority, and segregation of duties;
5. required inputs, data quality, tools, and dependencies;
6. decision criteria, thresholds, exceptions, and escalation paths;
7. retained evidence and traceability;
8. linkage to upstream and downstream controls;
9. ability to address foreseeable misuse, change, failure, and incident conditions;
10. alignment with policies, technical documentation, contracts, and operating procedures.

## GlobalWay example

GlobalWay tests the design of its high-risk recruitment-system release gate. The review confirms that classification, risk management, data governance, human oversight, testing, supplier evidence, and legal approval are mandatory inputs and that unresolved critical issues block deployment.

## Control activity

Control owners must document control objectives and design attributes before implementation. Independent reviewers must challenge whether the control could achieve the intended outcome under normal, changed, and failure conditions.

## Evidence

- control description and objective;
- legal and risk mapping;
- process flow and decision logic;
- RACI and competency requirements;
- thresholds and escalation design;
- evidence specification;
- dependency and failure-mode analysis;
- design review and approval.

## Audit test

Select key controls. Trace each to the relevant legal duty and risk, inspect the documented design, walk through normal and exception scenarios, and determine whether the control could reasonably achieve its stated objective if operated as designed.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable quality-management, risk-management, data-governance, documentation, human-oversight, accuracy, robustness, cybersecurity, monitoring, incident, and corrective-action provisions.
- Current consolidated official texts control over older summaries.