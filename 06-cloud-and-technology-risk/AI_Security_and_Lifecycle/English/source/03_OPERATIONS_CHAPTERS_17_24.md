# Manual 07 — AI Security and Lifecycle Controls
## Controlled English Source — Chapters 17–24

> Original defensive security implementation guidance. This material does not guarantee security or replace organization-specific risk decisions.

## Chapter 17 — Deployment hardening

Deployment should use approved configurations, least-privilege identities, protected secrets, controlled network paths, logging, monitoring, and rollback capability appropriate to risk.

The deployed system should be compared with the validated release candidate so security-relevant drift is not introduced during promotion.

## Chapter 18 — Monitoring and alerting

Monitoring should focus on indicators linked to known risk: unusual access, permission changes, repeated control failures, unexpected tool activity, sensitive-data handling, dependency changes, availability degradation, and policy exceptions.

Alerts should have owners, severity rules, escalation paths, and documented response expectations.

## Chapter 19 — Logging and evidence preservation

Security-relevant logs should preserve enough context to support investigation while respecting privacy and data-minimization requirements. Useful records may include identities, timestamps, model/configuration references, tool invocations, policy decisions, retrieval references, and change events.

Retention should be defined and access to logs controlled.

## Chapter 20 — Incident response

AI-related security events should integrate with the organization’s incident process. Response plans should identify containment options, evidence to preserve, supplier contacts, notification paths, recovery steps, and criteria for suspending or restricting the service.

## Chapter 21 — Rollback and stop mechanisms

Systems with material operational or security impact should have tested rollback or stop mechanisms. Authority to invoke them must be explicit.

A control that exists only on paper should not be credited until it has been technically and operationally validated.

## Chapter 22 — Change and configuration management

Changes to models, retrieval, prompts, system instructions, tools, permissions, data sources, hosting, guardrails, or suppliers can alter security posture. Change records should classify materiality and identify which previous validation remains valid.

## Chapter 23 — Exception governance

Security exceptions should record the unmet requirement, business rationale, compensating controls, owner, residual risk, approver, expiration date, and monitoring requirement.

High-risk exceptions should not become permanent through repeated administrative extension without reassessment.

## Chapter 24 — Periodic security reassessment

Periodic reassessment should examine whether threats, dependencies, access, data use, supplier state, operational behavior, and prior assumptions remain valid.

Evidence should show what was reviewed, what changed, what remains acceptable, and what additional action is required.