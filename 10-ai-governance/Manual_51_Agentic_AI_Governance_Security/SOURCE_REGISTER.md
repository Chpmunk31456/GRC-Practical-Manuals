# Manual 51 — Agentic AI Governance, Security & Human Accountability Source Register

**Verification date:** 1 September 2026  
**Canonical stage:** 0 — authoritative source collection / control taxonomy

## Primary governance and risk sources

1. Singapore IMDA — current AI governance ecosystem and Model AI Governance Framework for Agentic AI, May 2026 update identified by IMDA as v1.5  
   https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence

2. IMDA — Updated Model AI Governance Framework for Agentic AI, 20 May 2026  
   https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai

3. NIST AI RMF 1.0 / AIRC — voluntary risk-management operating baseline; AI RMF 1.0 is currently being revised  
   https://www.nist.gov/itl/ai-risk-management-framework

4. NIST AI 600-1 — Generative AI Profile  
   https://doi.org/10.6028/NIST.AI.600-1

## Agent-security and identity sources

5. NIST AI 800-5 — Summary Analysis of Responses to the Request for Information Regarding Security Considerations for AI Agents, published 18 May 2026  
   https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai

**Status note:** this NIST report summarises RFI responses and consensus themes; it is not treated as a final mandatory security standard.

6. NIST NCCoE concept paper — Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization, initial public draft, 5 February 2026  
   https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd

**Status note:** concept paper / initial public draft; useful for identity/authorization architecture, not a final standard.

7. OWASP Top 10 for Agentic Applications 2026  
   https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

8. OWASP Agentic AI — Threats and Mitigations  
   https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/

9. OWASP State of Agentic AI Security and Governance 2.01, 1 June 2026  
   https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/

**Status note:** OWASP resources are community/open-source security guidance, not law, certification, or government standard.

## Controlled source hierarchy

- Binding jurisdictional law controls legal obligations and is handled in specialist manuals.
- Official government/framework material controls its own stated guidance/status.
- NIST draft/concept/RFI-analysis material is labelled as such and must not be represented as final normative requirements.
- OWASP material is used as practical security/threat-model guidance and must not be represented as law or certification.
- Manual 46 and Manual 48 provide internal/common-control and Singapore-governance anchors but do not override external sources.

## Current control themes supported by the source set

- agent identity and attributable action;
- authentication and authorization;
- least privilege and scoped credentials;
- tool/API/data access boundaries;
- capability and autonomy bounding;
- meaningful human approval checkpoints;
- action provenance and reconstructability;
- multi-agent delegation/trust boundaries;
- third-party agent/provider governance;
- prompt/tool/data boundary security;
- monitoring and anomaly detection;
- containment / kill / credential revocation;
- incident response;
- model/tool/provider change and revalidation;
- end-user transparency and responsibility;
- automation-bias and overreliance controls.

## Release-source rule

Reverify fast-moving agentic security guidance and NIST draft/final status immediately before candidate freeze and publication. Any draft that becomes final must be reconciled as changed scope rather than silently assumed equivalent.