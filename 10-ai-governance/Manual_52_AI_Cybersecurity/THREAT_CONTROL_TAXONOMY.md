# Manual 52 — AI Cybersecurity Threat and Control Taxonomy

**Canonical stage:** 0 — authoritative-source and threat/control architecture

## AC-01 — AI asset and dependency inventory
Inventory models, APIs, agents, RAG stores, data pipelines, tools/connectors, identities, secrets, orchestration, hosting and third-party dependencies.

## AC-02 — Trust-boundary architecture
Document boundaries between users, untrusted content, prompts, model runtime, RAG sources, tools/APIs, agents, external services and privileged systems.

## AC-03 — Prompt and indirect prompt injection
Prevent untrusted content from silently acquiring instruction authority. Isolate trusted policy/context, validate tool calls, constrain actions and adversarially test indirect-injection paths.

## AC-04 — RAG/source poisoning
Control source approval, provenance, ingestion, authorization, tampering, freshness and retrieval. Test poisoned, unauthorized and misleading-source cases.

## AC-05 — Sensitive-data disclosure and exfiltration
Protect prompts, context, RAG data, model outputs, logs and tool responses using access controls, minimization, filtering, monitoring and leakage tests.

## AC-06 — Insecure output handling
Treat model output as untrusted when passed into shells, code interpreters, SQL, templates, browsers, APIs or other execution environments. Validate, escape and gate consequential operations.

## AC-07 — Excessive agency and tool abuse
Bound tools, permissions, transactions, autonomy and resources. Require human approval where warranted and preserve attributable action logs.

## AC-08 — Agent identity and delegation
Use attributable identities, scoped credentials and explicit delegation boundaries. Prevent privilege amplification across agents and tools.

## AC-09 — Secrets and credential security
Use managed secrets, short-lived/scoped credentials where practicable, rotation and rapid revocation. Do not embed durable secrets in prompts, code or memory.

## AC-10 — Model/data/software supply chain
Track model/provider versions, libraries, containers, data sources, plugins/tools, checksums/signatures where applicable, vulnerabilities and provider changes.

## AC-11 — Model/data poisoning
Protect training, tuning, evaluation and retrieval data against unauthorized modification or malicious content. Preserve provenance and integrity evidence.

## AC-12 — Model extraction, theft and abuse
Apply authentication, authorization, rate/resource limits, anomaly monitoring and contractual/technical controls appropriate to model exposure and value.

## AC-13 — Resource exhaustion / denial of service
Control token, compute, recursion, tool-call, API and transaction consumption. Monitor abnormal resource use and implement circuit breakers.

## AC-14 — Security monitoring and detection
Collect telemetry on authentication, tool use, policy denials, anomalous prompts/actions, RAG events, provider changes, security detections and containment actions.

## AC-15 — Adversarial testing and red teaming
Test representative OWASP/ATLAS-aligned scenarios, including prompt injection, RAG poisoning, tool abuse, data leakage, privilege escalation, unsafe output execution, model abuse and containment failure.

## AC-16 — Vulnerability and change management
Track vulnerabilities across AI components and dependencies. Treat model/provider/tool/permission changes as potential revalidation triggers.

## AC-17 — Third-party AI security
Assess external model/API/platform/agent/tool providers for security, identity, data handling, change notification, incidents, continuity and evidence access.

## AC-18 — AI security incident response
Preserve model/provider/version, prompts/context, RAG/tool/agent logs, identities, data exposure, detections and containment evidence. Integrate AI incidents into enterprise IR.

## AC-19 — Containment, rollback and emergency disablement
Provide tested capability to disable agents/tools, revoke credentials, isolate environments, block providers/endpoints and restore known-safe configuration.

## AC-20 — Secure retirement
Revoke credentials, remove access, archive required evidence, delete/retain data according to policy, decommission integrations and update inventory.

## Source-mapping rule
Each threat/control mapping must record: **source → source status → threat technique/scenario → control objective → implementation → telemetry → test/red-team method → residual risk → limitation**.

OWASP and MITRE ATLAS are practical security references, not legal compliance or certification. NIST framework/profile relationships retain their voluntary status. Specialist legal obligations remain in the corresponding regulatory manuals.

## Stage-0 completion criterion
Stage 0 is complete when authoritative-source anchors, threat categories, secure-lifecycle control families, telemetry/evidence expectations and source-status rules are controlled and ready for full training architecture.