# Manual 52 — AI Cybersecurity: Secure AI Lifecycle, OWASP GenAI & MITRE ATLAS

**Status:** CONTROLLED DEVELOPMENT  
**Version:** 0.2.0-draft  
**Source verification date:** 31 August 2026  
**Canonical stage:** 0 — source baseline and threat/control taxonomy

## Purpose

Establish a practical security program for AI systems across design, development, integration, deployment, operation and retirement, with special treatment for generative and agentic AI.

## Stage-0 controlled package

- OWASP GenAI LLM Top 10 2026 source anchor;
- OWASP Agentic Applications 2026 source anchor;
- OWASP agentic/data-security guidance anchors;
- MITRE ATLAS living threat-knowledge-base anchor;
- NIST AI RMF / AI 600-1 dependencies;
- AC-01 through AC-20 independently authored AI cybersecurity threat/control taxonomy;
- explicit distinction between community security guidance, living threat intelligence, voluntary NIST framework material and legal requirements.

## Security operating model

**AI asset → threat scenario → attack path → security objective → preventive/detective/corrective controls → telemetry → test method → response playbook → evidence**

## Core architecture

1. AI asset inventory and trust boundaries.
2. Secure architecture and threat modeling.
3. Model/data/software supply-chain security.
4. Identity, authentication and authorization.
5. Secrets and credential management.
6. Prompt injection and indirect prompt injection.
7. Retrieval/RAG poisoning and authorization failures.
8. Sensitive-data disclosure and exfiltration.
9. Insecure output handling and downstream execution.
10. Model extraction, theft and abuse.
11. Data/model poisoning.
12. Excessive agency and tool abuse.
13. Agent identity, delegation and tool/MCP-style boundaries.
14. Denial-of-service and resource-consumption controls.
15. Logging, detection and behavioral monitoring.
16. Adversarial testing and red teaming.
17. MITRE ATLAS threat mapping.
18. OWASP GenAI/Agentic control mapping.
19. Third-party AI security.
20. Security incident response and forensics.
21. Recovery, containment and emergency disablement.
22. Secure retirement and cleanup.
23. Evidence and audit procedures.

## Publication gates

- [x] Stage-0 OWASP/ATLAS/NIST source anchors registered.
- [x] GenAI/agentic threat taxonomy established.
- [x] Secure-lifecycle control families established.
- [ ] Reverify fast-moving OWASP and MITRE ATLAS source state at later controlled stages.
- [ ] Full training architecture and red-team scenarios.
- [ ] Detailed OWASP/ATLAS source-to-control mappings.
- [ ] Crosswalk to Manual 46 and Manual 51.
- [ ] Accountable-human technical review where genuinely required.
- [ ] Accessibility/localization preparation.
- [ ] Artifact/provenance/security gates.

**Fail-closed:** Manual 52 remains one controlled stage behind Manual 51. Community guidance and living knowledge-base material retain their actual status and do not become legal/certification requirements.