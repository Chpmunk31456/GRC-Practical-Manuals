# Manual 51 — Agentic AI Governance, Security, Identity & Human Accountability

**Status:** CONTROLLED DEVELOPMENT  
**Version:** 0.2.0-draft  
**Source verification date:** 1 September 2026  
**Canonical stage:** 0 — authoritative source baseline and control taxonomy

## Purpose

Provide a practical governance and security model for AI agents that can plan, invoke tools, access data, delegate tasks, persist memory, interact with other agents and take actions in enterprise environments.

## Governing principle

Agentic AI must be governed by the consequences of its actions, not only by the quality of its generated text.

## Stage-0 controlled package

- current source register covering IMDA Agentic AI governance, NIST AI RMF/GenAI, NIST 2026 agent-security/identity material and OWASP 2026 agentic security guidance;
- explicit status labels distinguishing government framework, RFI-analysis/concept draft and community security guidance;
- AG-01 through AG-20 independently authored control taxonomy covering identity, authorization, tools, data/memory, human checkpoints, provenance, multi-agent boundaries, containment, incident response, testing and continuous assurance.

## Core control questions

1. Who or what is the agent and who owns it?
2. What objective is it authorized to pursue?
3. What data, tools, systems and credentials can it access?
4. Which actions are explicitly prohibited?
5. Which actions require human authorization?
6. What limits apply to transactions, cost, time, recursion and resource use?
7. Can every consequential action be reconstructed from logs?
8. Can the organization contain, suspend or disable the agent quickly?
9. What changes trigger revalidation?
10. Who accepts residual risk?

## Architecture

1. Agentic AI concepts and system boundaries.
2. Capability and autonomy classification.
3. Intended, permitted and prohibited actions.
4. Agent identity and authentication.
5. Authorization and least privilege.
6. Tool/API allowlisting and policy enforcement.
7. Credential, token and secret isolation.
8. Data access and privacy controls.
9. Human approval checkpoints.
10. Separation of duties and dual control.
11. Transaction, cost, resource and rate limits.
12. Memory, persistence and retention governance.
13. Prompt/context integrity and indirect prompt injection.
14. Agent-to-agent delegation and trust boundaries.
15. Multi-agent coordination and emergent-risk controls.
16. Baseline testing and red teaming.
17. Runtime monitoring and anomaly detection.
18. Complete action logging and provenance.
19. Emergency stop, containment and rollback.
20. Incident response and forensics.
21. Change management and revalidation.
22. Third-party agent and agent-platform risk.
23. Singapore Agentic AI framework mapping.
24. NIST AI RMF/GenAI mapping.
25. ISO/IEC 42001 management-system relationship.
26. EU AI Act applicability and role analysis.
27. Executive/board risk reporting.
28. Scenario exercises and tabletop testing.

## Source/currentness caveats

- NIST AI 800-5 is an analysis of RFI responses, not a final mandatory agent-security standard.
- The NIST agent identity/authorization concept paper is an initial public draft, not a final standard.
- OWASP Agentic Security Initiative material is practical community guidance, not law or certification.
- Fast-moving agentic guidance must be reverified immediately before candidate freeze and publication.

## Publication gates

- [x] Current Stage-0 agentic-governance/security sources verified.
- [x] Initial identity/authorization and agent security source architecture established.
- [x] AG-01 through AG-20 control taxonomy established.
- [ ] Full controlled training architecture at next eligible stage.
- [ ] Detailed threat/control mappings and scenarios.
- [ ] Accountable-human technical review where genuinely required.
- [ ] Cross-framework mappings complete.
- [ ] Accessibility/localization preparation complete.
- [ ] Artifact/provenance/security gates complete.

**Fail-closed:** Manual 51 remains one controlled stage behind Manual 50. Draft/concept/community sources retain their actual status and may not be promoted to final normative requirements.