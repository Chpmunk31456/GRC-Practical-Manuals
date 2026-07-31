# Chapter 43 — Accuracy, Robustness, Cybersecurity, and Resilience

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 43 draft language.

## Requirement

High-risk AI systems must achieve an appropriate level of accuracy, robustness, and cybersecurity and perform consistently throughout their lifecycle. The design must address errors, faults, inconsistencies, malicious interference, feedback loops, and reasonably foreseeable misuse in light of the intended purpose and risk.

## Plain-English explanation

Compliance does not require perfect performance. It requires defensible performance targets, risk-based testing, transparent limitations, secure design, monitoring, and corrective action. Metrics must reflect the real deployment context rather than only laboratory averages.

## Required control areas

The provider should address, as applicable:

1. defined accuracy and performance metrics linked to intended purpose;
2. acceptance thresholds and decision limits;
3. subgroup and context-specific performance;
4. robustness to noise, missing data, distribution shift, and component failure;
5. resilience to errors, faults, outages, and dependency failures;
6. protection against data poisoning, adversarial examples, prompt injection, model manipulation, extraction, and unauthorized access;
7. secure development, testing, vulnerability management, and change control;
8. feedback-loop risks for systems that continue learning or influence future data;
9. fallback, degradation, rollback, and safe-stop behavior;
10. monitoring, incident response, and corrective-action triggers.

## Metrics and disclosure

Accuracy and robustness metrics must be documented in the technical file and instructions for use where required. Aggregate scores must not conceal material failure modes, affected-group disparities, unsafe operating conditions, or uncertainty.

## GlobalWay example

GlobalWay validates its recruitment system using role-relevant datasets and measures false-positive and false-negative patterns across relevant applicant groups. It also tests missing information, unusual résumé formats, malicious prompt content, vendor outages, model changes, and rollback procedures.

## Control activity

The provider must approve measurable performance, robustness, and cybersecurity requirements before release and repeat testing after material changes or emerging threats. The deployer must monitor real-world performance, maintain required operating conditions, report serious anomalies, and suspend use when defined thresholds are breached.

## Evidence

- performance requirements and thresholds;
- validation and test plans;
- subgroup and edge-case results;
- robustness and stress-test results;
- threat model and security architecture;
- vulnerability and penetration-test records;
- dependency and resilience testing;
- monitoring dashboards;
- incident and corrective-action records;
- release and rollback approvals.

## Audit test

Select a high-risk system and verify that performance and security requirements are documented, tests reflect the intended deployment context, material failure modes are disclosed, vulnerabilities and anomalies are tracked, and threshold breaches trigger investigation, correction, restriction, or suspension.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 15 and related lifecycle, monitoring, and provider/deployer obligations.
- Current consolidated EUR-Lex text controls over older summaries.
