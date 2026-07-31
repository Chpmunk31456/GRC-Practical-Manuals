# Chapter 104 — Control Library Design

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 104 draft language.

## Requirement

Organizations must maintain a structured AI control library that translates applicable legal obligations, risk treatments, governance decisions, technical safeguards, and operational practices into clear, assignable, testable, and evidence-producing controls.

## Plain-English explanation

A control library is the operational bridge between law, policy, risk, and day-to-day execution. Controls must state who performs the activity, what must be done, when it must occur, which systems and versions are covered, what evidence is retained, and how failures are escalated.

## Design requirements

Each control record should include:

1. unique control identifier and title;
2. linked legal, regulatory, contractual, policy, and risk sources;
3. objective and risk addressed;
4. regulated actor, business owner, control owner, and operator;
5. scope by system, model, version, geography, supplier, and lifecycle stage;
6. control activity, trigger, frequency, and timing;
7. preventive, detective, corrective, or governance classification;
8. manual, automated, or hybrid execution method;
9. required inputs, outputs, systems, and dependencies;
10. evidence standard, retention, and access requirements;
11. exception, escalation, and compensating-control process;
12. design and operating-effectiveness test procedures;
13. change history, approval, and next-review date.

## GlobalWay example

GlobalWay creates a control for high-risk recruitment systems requiring pre-release classification confirmation, approved human-oversight procedures, validation results, provider documentation, logging readiness, and executive release approval. The control record identifies evidence, frequency, owners, and testing steps.

## Control activity

The AI Governance function must maintain a controlled master library, map every material AI obligation and risk to one or more controls, prevent duplicate or contradictory controls, and require review after regulatory, system, model, supplier, purpose, or organizational change.

## Evidence

- approved control-library methodology;
- master control register;
- source-to-control mappings;
- ownership and RACI records;
- control narratives and procedures;
- evidence specifications;
- testing scripts and results;
- exception and change records.

## Audit test

Select a sample of legal obligations and material AI risks. Trace each to an approved control, responsible owner, operating procedure, retained evidence, and test method. Confirm that obsolete controls are retired and material changes trigger reassessment.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable governance, quality-management, risk-management, documentation, recordkeeping, monitoring, incident, corrective-action, and actor-specific provisions.
- Current consolidated EUR-Lex text controls over older summaries.
- Control frameworks and standards are non-binding unless incorporated through law, contract, certification, or organizational policy.