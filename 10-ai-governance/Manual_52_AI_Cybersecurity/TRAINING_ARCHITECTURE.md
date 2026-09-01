# Manual 52 — AI Cybersecurity Training Architecture

**Canonical stage:** 3 — release-depth training, mapping, scenario and evidence construction  
**Currentness baseline:** 1 September 2026

This architecture operationalizes the existing AC-01 through AC-20 threat/control taxonomy into a practical training system. It preserves source status: OWASP guidance is community guidance, MITRE ATLAS is a living adversary knowledge base, and NIST material is voluntary framework/profile guidance rather than legal certification.

## Module 1 — AI attack surface and system boundaries
Learners identify models, RAG stores, embeddings, orchestration, agents, tools, APIs, identities, secrets, data paths, provider dependencies and administrative surfaces. Output: current attack-surface inventory and trust-boundary diagram.

## Module 2 — Prompt, retrieval and context attacks
Covers direct/indirect prompt injection, retrieval poisoning, context manipulation, malicious documents, instruction hierarchy abuse and unsafe tool invocation. Output: threat cases, mitigations, test evidence and residual-risk decision.

## Module 3 — Model and supply-chain security
Covers provider/model provenance, model changes, dependency compromise, insecure packages, model theft, artifact integrity, signing/checksums and provider notification controls. Output: supply-chain risk register and validation evidence.

## Module 4 — Agentic identity, permissions and action control
Covers attributable agent identity, least privilege, scoped credentials, tool allowlists, transaction limits, human checkpoints, policy enforcement, cross-agent delegation and revocation. Output: action-permission matrix and action-provenance evidence.

## Module 5 — Sensitive-data and privacy attack paths
Covers memorization/extraction, RAG exfiltration, over-broad retrieval, secret leakage, cross-tenant exposure, logging hazards and unauthorized training/use. Output: data-flow map, exposure tests and control evidence.

## Module 6 — Insecure output handling and downstream execution
Covers unsafe code/content consumption, command execution, browser/tool actions, database queries, document generation, business-process automation and approval bypass. Output: safe-output handling standard and test cases.

## Module 7 — Evasion, abuse and model-behavior manipulation
Covers jailbreaks, adversarial examples, capability misuse, policy circumvention, obfuscation and multi-step attack chains. Output: red-team findings, detection coverage and remediation record.

## Module 8 — Monitoring, detection and incident response
Covers telemetry from prompts, agents, tools, identity systems, DLP, gateways, model/provider changes and safety/security policy events. Output: AI incident playbook, detection catalogue and escalation matrix.

## Module 9 — Red-team and adversarial validation
Defines controlled test objectives, authorization, safe data, success/failure criteria, evidence capture, retest and independent challenge. Output: reproducible adversarial test package.

## Module 10 — Governance integration and continuous assurance
Connects AI cybersecurity controls to governance, risk acceptance, change management, third-party oversight, audit, secure SDLC and Manual 46/51 control families. Output: management evidence pack and revalidation schedule.

## Required training outcomes
By completion, practitioners must be able to: map an AI attack surface; distinguish model, retrieval, agent, tool and supply-chain risks; design least-privilege action boundaries; conduct controlled adversarial tests; trace findings to controls and evidence; and define change triggers requiring revalidation.

## Release-depth completion criterion
Stage 3 is complete when the training modules are paired with detailed OWASP/ATLAS/NIST relationship mappings, practical red-team scenarios, evidence requirements and crosswalk links sufficient to begin controlled localization and deterministic candidate tooling.