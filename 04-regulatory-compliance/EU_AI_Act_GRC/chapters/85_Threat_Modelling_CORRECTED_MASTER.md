# Chapter 85 — Threat Modelling

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 85 draft language.

## Requirement

Organizations must perform proportionate threat modelling for AI systems and general-purpose AI components where security, safety, resilience, privacy, fundamental-rights, or operational risks could be materially affected by malicious or accidental misuse.

## Plain-English explanation

AI threat modelling identifies how attackers, insiders, users, dependencies, data pipelines, prompts, models, tools, and interfaces could cause harmful outcomes. It should cover the full lifecycle and be updated when the system, model, intended purpose, data, deployment environment, or threat landscape changes.

## Threat-modelling scope

Assess at minimum:

1. assets, trust boundaries, actors, and attack surfaces;
2. training, fine-tuning, retrieval, prompt, and inference pipelines;
3. data poisoning, prompt injection, model manipulation, extraction, and theft;
4. unauthorized tool use, privilege escalation, and agentic abuse;
5. supply-chain, API, plugin, open-source, and cloud dependencies;
6. privacy leakage, memorisation, confidential-information exposure, and model inversion;
7. safety bypass, harmful-content generation, evasion, and misuse;
8. logging, monitoring, detection, containment, rollback, and recovery;
9. affected-person, operational, and regulatory consequences;
10. residual risk, assumptions, and required controls.

## GlobalWay example

Before releasing an AI travel-assistance agent that can access booking systems, GlobalWay maps the agent's tool permissions, prompt channels, external APIs, user inputs, data stores, and escalation paths. The review identifies prompt injection, unauthorized itinerary changes, data leakage, and supplier-model substitution as priority scenarios.

## Control activity

Security and system owners must complete a version-linked threat model before production release and after material change. High-risk findings must be assigned controls, owners, deadlines, validation tests, and release-blocking criteria.

## Evidence

- approved threat model;
- architecture and data-flow diagrams;
- asset and trust-boundary inventory;
- abuse cases and attack trees;
- control mapping and residual-risk decisions;
- validation and red-team results;
- change-triggered reassessment records.

## Audit test

Select a sample of material AI systems and verify that threat models reflect the deployed architecture, current dependencies, realistic misuse scenarios, assigned mitigations, tested control effectiveness, and documented residual-risk acceptance.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, accuracy, robustness, cybersecurity, post-market, incident, and systemic-risk provisions.
- Current consolidated EUR-Lex text controls over older summaries.
- Recognized security frameworks and guidance are non-binding unless incorporated through another binding requirement.