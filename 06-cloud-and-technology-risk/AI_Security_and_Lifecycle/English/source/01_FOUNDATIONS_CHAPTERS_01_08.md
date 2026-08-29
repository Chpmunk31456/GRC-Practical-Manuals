# Manual 07 — AI Security and Lifecycle Controls
## Controlled English Source — Chapters 01–08

> Original security implementation guidance. This material operationalizes the controlled source baseline without reproducing standards text. It does not guarantee security, safety, compliance, or absence of exploitable weaknesses.

## Chapter 01 — Security objective and lifecycle boundary

AI security must cover the full system lifecycle rather than only the model endpoint. The controlled boundary includes use-case definition, data and model acquisition, design, development, evaluation, deployment, operation, monitoring, incident response, change, and retirement.

Each system should have a documented security objective tied to its data, actions, users, autonomy, external connectivity, and consequence of failure.

## Chapter 02 — AI asset inventory

The inventory should identify models, datasets, prompts, retrieval sources, vector stores, tools, agents, APIs, service accounts, secrets, guardrails, monitoring components, hosting environments, suppliers, and critical downstream systems.

Inventory records should include owner, version, location, data classification, authentication boundary, supplier, exposure, change authority, and retirement status. Unknown components create unmanaged attack surface.

## Chapter 03 — Threat modeling

Threat modeling should identify assets, trust boundaries, actors, entry points, privileges, dependencies, and plausible abuse paths. AI-specific threats should be evaluated alongside conventional application, cloud, identity, data, and supply-chain threats.

Scenarios should include malicious users, compromised retrieval content, over-privileged agents, exposed secrets, insecure APIs, unsafe tool execution, poisoned data, model or prompt disclosure, supplier compromise, and unintended autonomous behavior where relevant.

## Chapter 04 — Secure development and change control

AI components should be developed and changed through controlled repositories, review, testing, dependency management, access control, and release processes. Prompt, policy, retrieval, tool, and guardrail changes can be security-significant and should not bypass change controls merely because they are not traditional code.

Material changes require reassessment of prior security evidence and may reopen release approval.

## Chapter 05 — Data and model provenance

Security teams should be able to identify where models, datasets, weights, adapters, packages, prompts, and external components came from and who approved their use.

Provenance records should include origin, version, integrity evidence where available, licensing or usage boundary, supplier, approval, transformation history, and known limitations. Provenance supports trust decisions but does not prove a component is safe.

## Chapter 06 — Identity, least privilege, and tool authorization

AI systems that invoke tools or external actions should use explicit identities and least-privilege permissions. The model should not receive broad credentials merely because the application needs access to multiple functions.

Authorization should be enforced outside the model whenever possible. High-impact actions should use policy checks, scoped credentials, transaction limits, human approval, or other deterministic controls appropriate to risk.

## Chapter 07 — Prompt injection and untrusted content

Direct and indirect prompt injection should be treated as security threats when untrusted input can influence privileged behavior, expose sensitive information, alter system instructions, or cause unsafe tool use.

Controls can include content isolation, permission boundaries, retrieval filtering, output validation, tool allowlists, context separation, reduced privileges, confirmation steps, and monitoring. No single prompt or classifier should be treated as a complete defense.

## Chapter 08 — Fail-closed release security gate

Release must fail closed when critical security evidence is missing, material findings are unresolved without approved treatment, required adversarial testing has not completed, rollback or containment is required but untested, or required human review is incomplete.

A green automated workflow supports the release decision but does not guarantee the system is secure. Final approval remains a human-controlled gate, and material post-review changes reopen affected security review.