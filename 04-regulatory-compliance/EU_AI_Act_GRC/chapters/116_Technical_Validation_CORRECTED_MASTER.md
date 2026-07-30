# Chapter 116 — Technical Validation

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 116 draft language.

## Requirement

Organizations must perform risk-based technical validation before release and after material change to confirm that an AI system operates within its approved intended purpose, documented performance boundaries, safety constraints, cybersecurity controls, and human-oversight design.

## Plain-English explanation

Validation must test the actual production configuration, not only a laboratory prototype. It should establish whether the system works as claimed, fails safely, produces reproducible evidence, and remains suitable for the people, environments, and decisions affected.

## Validation requirements

Validate at minimum:

1. system, model, data, prompt, tool, and configuration version;
2. intended purpose and foreseeable misuse;
3. accuracy, robustness, reliability, and error boundaries;
4. subgroup and context-specific performance;
5. human-oversight, override, stop, and escalation controls;
6. cybersecurity, abuse, leakage, and manipulation resistance;
7. logging, traceability, monitoring, and evidence capture;
8. integration, dependency, latency, availability, and failover behaviour;
9. acceptance criteria, unresolved limitations, and residual risk;
10. independent review and release decision.

## GlobalWay example

GlobalWay validates a travel-disruption recommendation system using production-equivalent data, degraded network conditions, unusual itineraries, multilingual inputs, human override scenarios, and supplier-failure simulations before approving release.

## Control activity

No material AI system may enter production until validation results satisfy approved acceptance criteria or residual deviations receive documented risk acceptance from authorized leadership. Material changes require proportionate revalidation.

## Evidence

- approved validation plan;
- version and configuration record;
- test data and environment description;
- test results and defect log;
- acceptance criteria and exceptions;
- independent review;
- release decision;
- post-release validation monitoring.

## Audit test

Select released systems and significant changes. Confirm that validation covered the actual production version, tested relevant legal and operational risks, documented limitations, resolved or accepted deviations, and linked results to release approval.

## Primary legal references

- Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 where applicable: risk management, data governance, technical documentation, human oversight, accuracy, robustness, cybersecurity, conformity, and post-market monitoring provisions.
- Current consolidated EUR-Lex text controls over older summaries.