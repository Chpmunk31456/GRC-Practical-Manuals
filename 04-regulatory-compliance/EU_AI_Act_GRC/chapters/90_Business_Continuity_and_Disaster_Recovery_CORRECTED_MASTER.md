# Chapter 90 — Business Continuity and Disaster Recovery

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 90 draft language.

## Requirement

Organizations must maintain proportionate continuity and recovery arrangements for material AI systems so that outages, corruption, supplier failure, cyber incidents, unsafe behavior, or loss of supporting services do not create unmanaged harm or prevent compliance.

## Plain-English explanation

Continuity is not limited to restoring servers. The organization must preserve safe decision-making, human oversight, records, model and data integrity, approved configurations, and affected-person protections while the AI service is degraded or unavailable.

## Continuity requirements

The plan should address:

1. critical processes, dependencies, recovery priorities, and impact tolerances;
2. safe degradation, manual fallback, suspension, and emergency shutdown;
3. recovery-time and recovery-point objectives;
4. model, prompt, configuration, data, log, and documentation backup;
5. integrity validation before restoration;
6. cloud, API, model-provider, identity, network, and data-source dependencies;
7. alternate suppliers, regions, endpoints, or human processes;
8. incident command, communications, authority, and affected-person notifications where required;
9. recovery testing, rollback, reconciliation, and post-restoration monitoring;
10. lessons learned and corrective action.

## GlobalWay example

GlobalWay's recruitment-screening service becomes unavailable after a supplier outage. Automated ranking is suspended, trained reviewers use an approved manual process, pending decisions are tracked, required evidence is preserved, and the AI workflow is restored only after version, data, configuration, and control validation.

## Control activity

Every material AI system must have a version-linked continuity and recovery plan before production approval. High-risk systems require tested manual alternatives, defined suspension authority, evidence-preservation procedures, and recovery exercises covering supplier and cyber-failure scenarios.

## Evidence

- business-impact and dependency analysis;
- continuity and recovery plan;
- backup and restoration records;
- manual fallback procedure;
- exercise scenarios and results;
- integrity and reconciliation testing;
- communications and escalation records;
- remediation and lessons-learned actions.

## Audit test

Select material systems and continuity exercises. Verify that plans cover AI-specific assets and dependencies, manual fallback protects affected persons, recovery objectives were tested, restored systems were validated before use, and identified gaps were remediated.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, human-oversight, accuracy, robustness, cybersecurity, logging, monitoring, incident, corrective-action, and systemic-risk provisions.
- Applicable sector resilience and continuity law.
- Current consolidated EUR-Lex text controls over older summaries.