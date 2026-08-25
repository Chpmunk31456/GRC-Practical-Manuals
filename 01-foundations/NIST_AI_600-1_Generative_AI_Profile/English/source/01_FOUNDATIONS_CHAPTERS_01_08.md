# Manual 04 — NIST AI 600-1 Generative AI Profile Implementation
## Controlled English Source — Chapters 01–08

> Original implementation guidance based on the controlled NIST AI 600-1 / AI RMF source baseline. This text does not reproduce NIST publication text and does not create certification, legal compliance, or an audit opinion.

## Chapter 01 — Purpose, scope, and applicability

This manual operationalizes generative-AI risk management for organizations that design, acquire, integrate, deploy, operate, or retire generative-AI capabilities. The implementation boundary is deliberately risk-based: not every control, test, evidence item, or operating practice applies to every use case.

Each implementation begins with a documented applicability decision covering the use case, affected parties, deployment context, data handled, autonomy, external dependencies, and the consequences of error or misuse. The applicability record becomes controlled evidence and must be revisited when the system, model, data, tooling, supplier, or operating context materially changes.

Minimum evidence:
- use-case description and business owner;
- system/model/component inventory reference;
- affected-party and stakeholder identification;
- risk-tier or equivalent classification;
- applicability rationale;
- reviewer and approval date.

## Chapter 02 — Relationship to AI RMF 1.0

NIST AI 600-1 is treated as a generative-AI profile and companion to the AI RMF rather than as a stand-alone universal checklist. The operating model therefore retains GOVERN, MAP, MEASURE, and MANAGE as the management cycle while adding generative-AI-specific risk families, testing expectations, provenance considerations, and incident signals.

Organizations should map each GAI implementation decision to the relevant AI RMF function and preserve traceability from risk statement to evidence, decision, action, and residual risk.

Required control behavior:
- GOVERN sets policy, accountability, authority, and escalation;
- MAP defines context, use, actors, dependencies, and plausible harms;
- MEASURE evaluates performance, safety, security, privacy, integrity, and uncertainty;
- MANAGE selects treatments, accepts residual risk, monitors operation, and triggers stop/rollback when thresholds are exceeded.

## Chapter 03 — Implementation paths

Three proportional paths are supported.

### Essential
For lower-complexity or lower-impact uses. Requires inventory, ownership, basic risk screening, minimum testing, human oversight, incident handling, and documented approval.

### Structured
For material business, customer, workforce, security, privacy, financial, or operational use. Requires formal risk registers, evidence matrices, test plans, supplier review, change controls, monitoring thresholds, incident playbooks, and periodic reassessment.

### Enhanced
For high-impact, high-autonomy, safety-sensitive, regulated, externally exposed, or otherwise consequential uses. Requires independent challenge, deeper adversarial testing, formal release criteria, stronger provenance, explicit stop/rollback authority, enhanced monitoring, and documented residual-risk acceptance by accountable management.

Implementation path selection must be justified and may only be downgraded through documented approval.

## Chapter 04 — Governance and accountability

Every GAI system must have named business, technical, security, privacy/data, and risk owners appropriate to its scope. Accountability cannot be delegated solely to a model provider or implementation vendor.

Governance should define:
- who may approve a new use case;
- who may approve model, prompt, retrieval, tool, or data changes;
- who owns testing and evidence;
- who can suspend or roll back deployment;
- who accepts residual risk;
- who receives incident notifications;
- who conducts periodic review.

Conflicts of interest should be identified where the same person designs, tests, and approves a high-impact system. Enhanced implementations should add independent review or challenge.

## Chapter 05 — Inventory and system decomposition

Treat the GAI capability as a system, not merely a model. The inventory should identify the model, hosting environment, retrieval layer, vector store, prompts/system instructions, tools, APIs, data sources, fine-tuning artifacts, guardrails, monitoring components, external services, and human decision points.

The inventory should capture version, owner, supplier, deployment location, data classification, authentication boundary, change authority, and retirement status. Dependencies that can materially alter output or behavior must be separately traceable.

A system change is material when it can alter risk, capability, exposure, output quality, safety, security, privacy, compliance posture, or affected-party impact.

## Chapter 06 — GAI risk-family model

The controlled Manual 04 baseline preserves twelve generative-AI risk families:

1. CBRN Information or Capabilities
2. Confabulation
3. Dangerous, Violent, or Hateful Content
4. Data Privacy
5. Environmental Impacts
6. Harmful Bias and Homogenization
7. Human-AI Configuration
8. Information Integrity
9. Information Security
10. Intellectual Property
11. Obscene, Degrading, and/or Abusive Content
12. Value Chain and Component Integration

These risk families are screening categories, not automatic findings. Each use case must determine which families are applicable, the credible scenarios involved, existing controls, evidence, residual risk, and monitoring indicators.

## Chapter 07 — Risk statements and impact pathways

Risk records should be scenario-based rather than generic. A useful structure is:

**Condition or threat → system behavior → affected asset/person/process → consequence → control/evidence → residual risk.**

For example, a retrieval-enabled assistant may ingest untrusted content, follow malicious embedded instructions, invoke an external tool, and expose restricted information. The risk statement should describe the complete pathway rather than only labeling the issue “prompt injection.”

Impact analysis should consider direct, indirect, cumulative, and foreseeable misuse effects. Where impacts are uncertain, uncertainty must be recorded rather than silently converted into a low-risk conclusion.

## Chapter 08 — Release authority and fail-closed gates

No GAI use case should move to production merely because automated tests pass. Release requires documented evidence sufficient for the selected implementation path, unresolved exceptions within approved tolerance, responsible-owner sign-off, and any required human review.

A release gate must fail closed when:
- required evidence is missing or stale;
- mandatory testing is incomplete or failed;
- critical findings remain open without approved treatment;
- a required human review is missing, rejected, or invalidated by material change;
- legal, security, privacy, safety, or operational applicability is unresolved;
- rollback/stop capability is required but not validated.

Material change after approval reopens the affected review and release gates.