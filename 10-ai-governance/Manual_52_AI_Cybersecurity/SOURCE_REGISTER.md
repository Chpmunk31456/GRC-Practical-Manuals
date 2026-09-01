# Manual 52 — AI Cybersecurity Authoritative Source Register

**Verification date:** 31 August 2026  
**Status:** CONTROLLED DEVELOPMENT

## OWASP GenAI Security Project

1. **OWASP GenAI LLM Top 10 2026** — published 3 August 2026  
   https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/  
   Use: current critical security risks for LLM-powered applications, attack scenarios, mitigations and framework mappings.

2. **OWASP Top 10 for Agentic Applications for 2026** — published 9 December 2025 as the 2026 edition  
   https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/  
   Use: current critical security risks for autonomous and agentic applications.

3. **OWASP Agentic Security Initiative**  
   https://genai.owasp.org/initiatives/agentic-security-initiative/  
   Use: current agentic-security guidance, including MCP and related operational resources.

4. **OWASP AI Data Security initiative**  
   https://genai.owasp.org/initiative/ai-data-security/  
   Use: AI/LLM data-security practices and current GenAI security resources.

## MITRE ATLAS

5. **MITRE ATLAS — Adversarial Threat Landscape for AI Systems**  
   https://atlas.mitre.org/  
   Use: living adversary tactics/techniques knowledge base and mitigations for AI-enabled systems. Current ATLAS matrix supports predictive AI, generative AI and agentic AI platforms.

## NIST dependencies

6. **NIST AI RMF 1.0**  
   https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10

7. **NIST AI 600-1 Generative AI Profile**  
   https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

## Preflight source-control note

The repository's current `.compliance/authoritative-sources.json` validator only permits a fixed domain set that does not yet include `genai.owasp.org` or `atlas.mitre.org`. These official sources must not be forced into the central registry until the allowlist is expanded through an explicit reviewed repository-security change.

## Release-source rules

- Recheck OWASP edition currency immediately before release.
- Treat MITRE ATLAS as a living knowledge base and record the verification date used for mappings.
- Distinguish community security guidance from legal/regulatory requirements.
- Do not claim OWASP or ATLAS alignment establishes certification or regulatory compliance.
