# Chapter 40 — Logs and Recordkeeping

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 40 draft language.

## Requirement

High-risk AI systems must be designed to enable automatic recording of events over the system lifetime to the extent appropriate to the intended purpose. Providers and deployers must retain logs and related records for the periods required by Regulation (EU) 2024/1689, as amended, and other applicable law.

## Plain-English explanation

Logs are the operational evidence trail for how a high-risk AI system behaved. They support monitoring, incident investigation, human oversight, conformity assessment, corrective action, and regulatory review. Logging must be useful, proportionate, secure, and linked to the correct system version.

The AI Act does not create one universal retention period for every record. Retention must be determined by actor role, record type, applicable article, sector law, data-protection requirements, contractual obligations, limitation periods, and litigation or regulatory holds.

## Logging requirements

The logging design should address, as applicable:

1. system and model version;
2. date and time of operation;
3. input source and relevant processing context;
4. output, score, recommendation, or decision;
5. confidence or threshold information where relevant;
6. human-review, intervention, override, or escalation;
7. errors, anomalies, failed controls, and security events;
8. configuration, prompt, retrieval, and dependency changes;
9. identity or role of authorized operators where lawful and necessary;
10. linkages to complaints, incidents, corrective actions, and monitoring records.

## Data-protection and security controls

Logging must not become uncontrolled surveillance or excessive personal-data collection. The organization must define lawful purpose, data minimisation, access restrictions, integrity protection, retention, deletion, and secure export procedures.

## GlobalWay example

GlobalWay’s high-risk recruitment system records the production model version, candidate-processing timestamp, relevant scoring outcome, threshold applied, reviewer identity, reviewer decision, override reason, and any system error. Access is restricted to authorized HR, compliance, audit, and security personnel.

## Control activity

The provider must define logging capabilities during design, and the deployer must ensure logs are enabled, protected, reviewed, and retained according to an approved schedule. Any logging gap that prevents effective monitoring, oversight, investigation, or regulatory response must block deployment or trigger corrective action.

## Evidence

- logging specification;
- data dictionary;
- sample event records;
- access-control configuration;
- retention schedule;
- deletion and legal-hold procedures;
- integrity and tamper-evidence controls;
- monitoring and review records;
- incident and corrective-action linkages;
- privacy assessment.

## Audit test

Select a sample of high-risk system events and confirm that logs are generated, complete, version-linked, protected from unauthorized change, accessible to authorized reviewers, retained under an approved schedule, and used in monitoring and incident investigation.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 12 and applicable actor obligations concerning log retention and access.
- GDPR and sector-specific retention rules where personal data or regulated records are involved.
- Current consolidated EUR-Lex text controls over older summaries.
