# Manual 04 — NIST AI 600-1 Generative AI Profile Implementation
## Controlled English Source — Chapters 09–16

> Original implementation guidance. This material operationalizes the controlled Manual 04 baseline and does not reproduce NIST publication text.

## Chapter 09 — Confabulation and output reliability

Confabulation risk is managed through use-case-specific evaluation rather than a single accuracy percentage. Teams should identify statements that must be factual, the acceptable error rate, the consequences of false confidence, and the controls used when the model lacks reliable support.

Useful controls include retrieval-grounding, source display, constrained generation, abstention behavior, human validation, deterministic downstream checks, and restrictions on high-consequence autonomous actions.

Evidence should include evaluation datasets, acceptance thresholds, observed failure modes, representative examples, remediation decisions, and residual-risk approval.

## Chapter 10 — Harmful, abusive, and dangerous content

Organizations should define categories of content that are prohibited, restricted, context-dependent, or acceptable for the specific use case. Policy must distinguish user-input handling from model-output handling and should address adversarial attempts to bypass safeguards.

Testing should include expected use, misuse, boundary conditions, prompt manipulation, multilingual variation where relevant, and escalation behavior. A refusal mechanism that can be trivially bypassed should not be treated as an effective control.

## Chapter 11 — Data privacy and sensitive information

Privacy review should trace data across prompts, retrieval stores, logs, training or fine-tuning pipelines, external APIs, observability platforms, support channels, and retained conversation history.

The minimum control set should address data minimization, purpose limitation, access, retention, deletion, redaction, secrets handling, logging, third-party processing, and user disclosure where applicable.

Testing should intentionally look for memorization, data leakage, retrieval overexposure, cross-user contamination, and unauthorized disclosure through tools or connectors.

## Chapter 12 — Harmful bias, homogenization, and human impact

Bias evaluation should be tied to the decisions, recommendations, classifications, content, or experiences produced by the system. Teams should identify populations or stakeholder groups that could experience different failure rates or harms.

Controls may include dataset analysis, outcome testing, subgroup evaluation, human escalation, alternative workflows, monitoring, and restrictions on the use of generated content in consequential decisions.

Where measurement is limited by data or sample size, that uncertainty should be documented rather than represented as evidence of fairness.

## Chapter 13 — Human-AI configuration and oversight

Human oversight must be designed, not assumed. The organization should determine what the human is expected to notice, what evidence is available, whether there is enough time and authority to intervene, and how automation bias will be reduced.

For consequential uses, define:
- decisions the system may make or recommend;
- decisions reserved for humans;
- escalation triggers;
- override authority;
- logging of human review;
- competency requirements;
- fallback procedures when the system is unavailable or unreliable.

## Chapter 14 — Information integrity and provenance

Information-integrity controls should help users distinguish generated, retrieved, transformed, and authoritative information. Provenance should be preserved where it materially affects trust, review, attribution, or downstream use.

Depending on the system, evidence may include source references, content metadata, signed artifacts, transformation history, prompt/version identifiers, model/version records, and traceability from output to supporting material.

Provenance claims must be bounded: metadata or labels improve traceability but do not by themselves prove truth or authenticity.

## Chapter 15 — Information security and adversarial testing

GAI security testing should cover the full system attack surface: prompts, retrieval sources, vector databases, model endpoints, plugins/tools, identities, secrets, APIs, user interfaces, logs, orchestration layers, and supplier integrations.

Testing should include prompt injection, indirect prompt injection, unauthorized tool use, privilege escalation, sensitive-data extraction, malicious retrieval content, model or system prompt disclosure, abuse of external actions, and denial or degradation scenarios where relevant.

Findings should be linked to concrete controls, owners, remediation, retest evidence, and residual-risk decisions.

## Chapter 16 — Intellectual property, value chain, and component integration

The organization should identify licensed, proprietary, third-party, open-source, and externally hosted components that influence the system. Supplier terms, usage restrictions, output rights, data-processing terms, and component dependencies should be documented where relevant.

Value-chain review should include model providers, hosting platforms, datasets, retrieval sources, plugins, APIs, safety services, monitoring providers, and subprocessors. A supplier questionnaire alone is not sufficient evidence for high-risk dependencies.

Material supplier or component change should trigger reassessment when it can alter capability, data handling, contractual exposure, security posture, availability, or output behavior.