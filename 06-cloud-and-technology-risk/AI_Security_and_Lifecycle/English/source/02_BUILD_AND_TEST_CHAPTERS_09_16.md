# Manual 07 — AI Security and Lifecycle Controls
## Controlled English Source — Chapters 09–16

> Original defensive security implementation guidance. This material does not reproduce standards text or guarantee security.

## Chapter 09 — Retrieval and knowledge-source security

Retrieval sources should be treated as externally influenced inputs. Controls should address source admission, write authority, content validation, access control, tenant separation, stale content, sensitive-data exposure, and removal.

Vector stores and indexes should inherit appropriate data classification, access, retention, logging, and backup controls.

## Chapter 10 — Secrets and sensitive-data handling

Secrets should not be embedded in prompts, source code, notebooks, or model context when safer alternatives exist. Service credentials should be scoped, rotated, monitored, and stored using approved secret-management mechanisms.

Logs, traces, evaluations, and support artifacts must also be reviewed for unintended sensitive-data exposure.

## Chapter 11 — Model and component supply chain

Security review should include model origin, packages, containers, adapters, datasets, APIs, plugins, safety services, and hosting dependencies. Components should be versioned and traceable so security teams can assess supplier or component change impact.

Material supplier changes should trigger reassessment rather than being silently inherited.

## Chapter 12 — Evaluation and security validation

Security evaluation should use risk-based objectives and expected outcomes. Validation should cover whether access controls, data boundaries, tool permissions, retrieval controls, output handling, dependency behavior, and operational restrictions work as intended under representative and boundary conditions.

Test evidence should record configuration, scope, result, limitation, and remediation.

## Chapter 13 — Independent challenge

Independent challenge should test whether assumptions and control boundaries remain valid outside normal operating conditions. The review should be authorized, bounded, and evidence-driven.

Challenge activity without remediation ownership and follow-up validation should not be represented as assurance.

## Chapter 14 — Guardrails and deterministic controls

Guardrails can reduce risk but should be layered with deterministic security controls where consequences are significant. Authorization, input validation, output validation, allowlists, transaction limits, network controls, and human approval can provide stronger enforcement than model behavior alone.

## Chapter 15 — Human oversight for security-sensitive actions

Human approval should be required where automated actions can create material security or business impact and the system cannot reliably constrain risk through deterministic controls.

Reviewers need enough context, time, competence, and authority to reject or stop the action. A nominal approval step without meaningful information is not effective oversight.

## Chapter 16 — Pre-deployment security package

Before release, assemble the current threat model, architecture, asset inventory, validation results, open findings, supplier evidence, identity/permission review, monitoring thresholds, incident plan, rollback/stop plan, exceptions, and approvals.

The package must correspond to the exact release candidate and material changes must reopen affected evidence.