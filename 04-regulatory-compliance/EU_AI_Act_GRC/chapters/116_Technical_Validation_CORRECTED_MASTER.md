# Chapter 116 — Technical Validation

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 116 draft language.

## Requirement

Providers of high-risk AI systems must establish and document validation and testing appropriate to the system’s intended purpose and risks, including the information required by Article 11 and Annex IV and the performance, robustness, cybersecurity, and human-oversight requirements applicable to the system. Other organizations developing, procuring, integrating, or deploying material AI systems should apply proportionate technical validation before release and after material change so they can demonstrate that the production configuration operates within approved boundaries and that their own legal and operational duties can be met.

## Plain-English explanation

The EU AI Act does not impose one universal validation procedure on every AI system and actor. The exact duty depends on classification and role. For high-risk AI systems, providers must maintain risk management, technical documentation, testing, accuracy, robustness, cybersecurity, and quality-management evidence. Deployers and other value-chain actors need sufficient validation evidence to use the system according to instructions, exercise oversight, monitor operation, and reassess changes. Validation should test the actual production configuration, not only a laboratory prototype.

## Validation requirements

The validation plan should address, as applicable:

1. the regulated actor, classification, intended purpose, and legal trigger;
2. system, model, data, prompt, tool, software, firmware, and configuration version;
3. foreseeable misuse and reasonably foreseeable operating conditions;
4. accuracy, robustness, reliability, consistency, and error boundaries;
5. representative and context-appropriate test data and performance metrics;
6. subgroup, accessibility, and context-specific performance where relevant;
7. human-oversight, override, stop, escalation, and safe-failure controls;
8. cybersecurity, abuse, leakage, manipulation, and dependency resistance;
9. logging, traceability, monitoring, evidence capture, and version linkage;
10. integration, latency, availability, failover, and degraded-mode behaviour;
11. acceptance criteria, unresolved limitations, corrective action, and residual risk;
12. independent review and authorized release decision.

## GlobalWay example

GlobalWay validates a travel-disruption recommendation system using production-equivalent data, degraded network conditions, unusual itineraries, multilingual inputs, human-override scenarios, and supplier-failure simulations. It records the provider and deployer roles, the production version tested, applicable instructions, limitations, acceptance criteria, unresolved deviations, and the basis for release.

## Control activity

A high-risk AI system must not be released by its provider until the applicable risk-management, documentation, testing, conformity, and quality-management requirements are satisfied. GlobalWay must not place any material AI system into production until it has obtained and evaluated validation evidence sufficient for its actual role, intended use, oversight responsibilities, and risk. Material changes require proportionate reassessment and, where applicable, revalidation and renewed conformity activity.

## Evidence

- legal-role and classification assessment;
- approved validation plan;
- version and configuration record;
- test data, representativeness rationale, and environment description;
- metrics, test results, logs, and defect records;
- acceptance criteria, limitations, and exceptions;
- independent review and approval;
- conformity and release evidence where applicable;
- post-release monitoring and revalidation records.

## Audit test

Select released systems and significant changes. Confirm that validation covered the actual production version, matched the actor and classification, used appropriate data and metrics, tested relevant legal and operational risks, documented limitations and deviations, and linked the results to conformity, release, monitoring, and reassessment decisions as applicable.

## Primary legal references

- Regulation (EU) 2024/1689, as amended, including Articles 9–15, 16–18, 26, 43, 72, and Annex IV, as applicable.
- Regulation (EU) 2026/1744, where its amendments affect the relevant requirements, application dates, or procedures.
- Applicable harmonised standards and common specifications, when legally available and relevant; otherwise they must not be described as binding law merely because they are useful validation references.
- Current consolidated EUR-Lex text controls over older summaries and drafts.
