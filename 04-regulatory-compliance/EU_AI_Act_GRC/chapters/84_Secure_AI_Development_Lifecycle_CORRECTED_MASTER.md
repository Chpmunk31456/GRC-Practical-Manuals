# Chapter 84 — Secure AI Development Lifecycle

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 84 draft language.

## Requirement

Providers and organizations developing, integrating, configuring, or materially modifying AI systems must embed security, safety, privacy, robustness, data governance, human oversight, documentation, and change control throughout the lifecycle. Controls must be proportionate to the system's intended purpose, risk classification, foreseeable misuse, value-chain dependencies, and production environment.

## Plain-English explanation

Security review cannot be postponed until the end of development. AI-specific threats can enter through data, models, prompts, tools, APIs, integrations, logs, deployment pipelines, and downstream use. The lifecycle must produce evidence that controls were designed, tested, approved, monitored, and updated for the actual production version.

## Lifecycle controls

The secure lifecycle should include:

1. intake, intended-purpose, role, and risk classification;
2. security and abuse-case requirements;
3. architecture, data-flow, and trust-boundary review;
4. data provenance, integrity, quality, and access controls;
5. secure coding, dependency, model, and infrastructure controls;
6. prompt, retrieval, agent, tool, and API safeguards;
7. privacy, bias, safety, robustness, and human-oversight testing;
8. adversarial testing and vulnerability management;
9. release criteria, segregation of duties, approvals, and rollback;
10. logging, monitoring, incident response, and post-market feedback;
11. version-linked documentation and evidence retention;
12. retirement, data deletion, model disposal, and continuity planning.

## GlobalWay example

GlobalWay develops an AI travel-policy assistant that can query booking systems and draft traveler recommendations. The secure lifecycle limits tool permissions, validates retrieval sources, tests prompt injection and data leakage, requires human approval for consequential actions, records production versions, and blocks release until security and compliance gates are complete.

## Control activity

Engineering must operate a documented secure-AI lifecycle with mandatory gates appropriate to risk. High-risk or material systems require independent security, privacy, legal, and AI-governance approval. Exceptions must identify the owner, rationale, compensating controls, expiration date, and residual risk.

## Evidence

- lifecycle standard and control gates;
- threat model and abuse cases;
- architecture and data-flow reviews;
- secure-development and dependency records;
- test plans and results;
- vulnerability and remediation records;
- release approvals and exception records;
- version-linked technical documentation;
- monitoring and post-release review evidence;
- retirement and disposal records.

## Audit test

Select a sample of production AI releases. Trace each release through intake, design, development, testing, approval, deployment, and monitoring. Confirm that required gates were completed, exceptions were authorised and time-bound, and evidence matches the deployed version.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Articles 9–15, 17, 20, 24–26, 55, 72–73, and Annex IV as applicable.
- Regulation (EU) 2016/679: Articles 25, 32, 35, and related accountability provisions where personal data are processed.
- Current consolidated EUR-Lex texts control over summaries and earlier drafts.
