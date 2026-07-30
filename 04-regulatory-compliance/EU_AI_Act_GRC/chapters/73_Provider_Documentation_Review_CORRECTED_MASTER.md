# Chapter 73 — Provider Documentation Review

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 73 draft language.

## Requirement

Organizations must review provider-supplied documentation before deployment and after material change to determine whether it is complete, current, internally consistent, applicable to the intended use, and sufficient to support the organization's legal and operational obligations.

## Plain-English explanation

Receiving documents is not the same as reviewing them. Instructions for use, technical summaries, conformity records, model cards, test reports, and security materials must be checked against the deployed version, actual configuration, and use case.

## Review criteria

Confirm as applicable:

1. provider identity, role, system or model version, and intended purpose;
2. applicability of the documents to the exact product and release;
3. high-risk, transparency, GPAI, and systemic-risk classification statements;
4. instructions, limitations, performance metrics, thresholds, and foreseeable misuse;
5. human-oversight, logging, monitoring, and incident procedures;
6. data, privacy, security, robustness, bias, and accessibility evidence;
7. conformity assessment, declaration, registration, and marking evidence where required;
8. material assumptions, exclusions, unresolved limitations, and customer responsibilities;
9. document-control, approval, language, accessibility, and update status;
10. contradictions between contractual, technical, assurance, and marketing claims.

## GlobalWay example

GlobalWay receives a vendor's model card and conformity package for a recruitment system. The review identifies that the model card covers an earlier version and omits the threshold configuration used by GlobalWay. Deployment remains blocked until corrected, version-specific documentation is supplied.

## Control activity

The system owner must maintain a provider-documentation index and obtain approval from Legal, Compliance, Security, Privacy, and relevant technical reviewers before production use. Missing, stale, or contradictory documentation must result in remediation, restricted use, compensating controls, or rejection.

## Evidence

- provider-documentation index;
- version and configuration mapping;
- completed review checklist;
- identified gaps and contradictions;
- supplier clarifications and replacements;
- risk decisions and approvals;
- update and reassessment history.

## Audit test

Select a sample of third-party AI systems and confirm that provider documents match the deployed release and intended use, that gaps were resolved before approval, and that material changes triggered renewed review.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable provider information, instructions, technical documentation, conformity, transparency, GPAI, and value-chain provisions.
- Current consolidated EUR-Lex text controls over older summaries.
