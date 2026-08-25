# AI Governance and Audit Toolkit — Controlled Template Field Guide

> Original implementation guidance for the toolkit. This guide defines the minimum evidence intent for each controlled template and does not replace organization-specific legal, audit, security, privacy, safety, or regulatory requirements.

## Shared field principles

Every template should identify, where applicable:
- unique record identifier;
- system/use-case/vendor/change reference;
- owner;
- status;
- evidence references;
- decision and decision authority;
- reviewer;
- findings or exceptions;
- remediation owner and due date;
- residual risk;
- material-change indicator;
- review/approval date.

Missing mandatory human review must keep the associated release or closure gate open.

## 1. AI System and Use Case Register

Purpose: establish the authoritative inventory of AI systems and material use cases.

Minimum intent:
- business purpose;
- accountable business and technical owners;
- model/provider/component references;
- data classifications;
- user populations and affected parties;
- autonomy and external-action capability;
- deployment status;
- risk tier;
- applicable frameworks or obligations;
- last review date.

## 2. AI Risk and Impact Register

Purpose: record scenario-based risk and impact pathways.

Minimum intent:
- risk statement;
- initiating condition/threat;
- affected asset/person/process;
- consequence;
- inherent risk;
- existing controls;
- evidence;
- residual risk;
- treatment decision;
- owner;
- monitoring indicator.

## 3. AI Control and Evidence Matrix

Purpose: map requirements or risk treatments to implemented controls and evidence.

Minimum intent:
- criterion/control objective;
- control owner;
- implementation description;
- system/component scope;
- evidence source;
- test method;
- test result;
- exception;
- remediation;
- reviewer conclusion.

## 4. AI Audit Workpaper Index

Purpose: provide traceability across planning, evidence, testing, findings, and conclusions.

Minimum intent:
- workpaper ID;
- audit objective/criterion;
- procedure performed;
- population/sample reference;
- evidence links;
- preparer;
- reviewer;
- result;
- cross-reference to finding or conclusion.

## 5. AI Findings and Remediation Log

Purpose: control findings from identification through validated closure.

Minimum intent:
- finding statement;
- criterion;
- condition;
- cause;
- consequence/risk;
- severity;
- management response;
- remediation action;
- owner;
- target date;
- validation evidence;
- residual risk;
- closure approver.

## 6. AI Vendor and Component Register

Purpose: record external AI dependencies and third/fourth-party exposure.

Minimum intent:
- supplier/component;
- service provided;
- criticality;
- data handled;
- model/API/tool dependency;
- subprocessors/fourth parties;
- due-diligence status;
- contract and notification requirements;
- monitoring tier;
- renewal/exit date;
- current exceptions.

## 7. AI Change and Reassessment Log

Purpose: determine whether change invalidates prior evidence or approvals.

Minimum intent:
- change description;
- component affected;
- reason;
- materiality;
- risk effect;
- tests required;
- reviews reopened;
- rollback plan;
- approval;
- deployment date;
- post-change validation.

## 8. Human Review and Approval Record

Purpose: preserve the mandatory human decision gate.

Required fields:
- reviewer;
- review date;
- decision;
- evidence reviewed;
- findings;
- remediation, if applicable;
- limitations;
- material-change validity statement;
- final approval authority where relevant.

Automated QA must never populate this record as though it were a human decision.

## 9. Release Evidence Manifest

Purpose: identify the exact controlled package approved for release.

Minimum intent:
- release identifier/version;
- included artifacts;
- source commit/reference;
- SHA-256 or equivalent integrity values where used;
- language/format inventory;
- QA results;
- unresolved accepted exceptions;
- human review references;
- Final Human Release Approval reference;
- publication date;
- superseded release, if any.

## Fail-closed usability rule

A template is not complete merely because every field contains text. Required fields must contain meaningful, reviewable evidence. Placeholder values, unresolved references, missing approvers, or stale review dates keep the associated control open.