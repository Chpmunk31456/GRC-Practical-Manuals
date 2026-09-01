# Manual 49 — NIST AI RMF 1.0 + NIST AI 600-1 GenAI Training Modules

**Controlled English draft — Stage 3**  
**Currentness baseline:** 1 September 2026

## Module 1 — NIST AI RMF as an operating system

Treat GOVERN, MAP, MEASURE and MANAGE as a continuous risk-management cycle. GOVERN is cross-cutting; MAP establishes context; MEASURE tests and evaluates; MANAGE prioritises and treats risk. Every function feeds the others as the system, provider, data, environment and use case change.

### Evidence
- AI governance charter and risk policy;
- AI inventory and risk tiers;
- use-case/context records;
- evaluation/TEVV records;
- risk-treatment decisions;
- monitoring and incident evidence;
- change/revalidation records.

## Module 2 — GOVERN: accountability and risk culture

Establish accountable ownership, decision rights, policies, risk tolerance, competence, lifecycle governance, third-party governance, exception handling and management reporting.

### Control questions
- Who owns the AI system and its residual risk?
- Which roles can approve, restrict or suspend deployment?
- How are security, privacy, safety, model risk, legal/compliance and business perspectives integrated?
- What evidence shows governance actually operates?

## Module 3 — MAP: purpose, context and impacts

Document intended purpose, deployment context, users, affected parties, data, dependencies, assumptions, benefits, foreseeable harms and misuse.

### Evidence
- context/system diagram;
- intended-use statement;
- stakeholder/impact analysis;
- data and RAG source map;
- dependency inventory;
- misuse/abuse cases;
- limitations register.

## Module 4 — MEASURE: evaluation and TEVV

Define acceptance criteria and test performance, robustness, security, privacy, uncertainty and control effectiveness under representative and adversarial conditions.

### TEVV record
**claim → metric/test → data/test set → environment/version → result → uncertainty/limitation → finding → remediation → retest**

## Module 5 — MANAGE: risk treatment and lifecycle decisions

Prioritise identified risks and decide whether to deploy, restrict, remediate, accept, monitor, suspend or retire. Link every material risk to a disposition and owner.

### Evidence
- treatment plan;
- deployment/exception decision;
- residual-risk acceptance;
- monitoring thresholds;
- remediation tracking;
- rollback/retirement plan.

## Module 6 — Trustworthiness characteristics

Use NIST trustworthiness characteristics as design and evaluation considerations rather than a single composite score. Relevant considerations include validity/reliability, safety, security/resilience, accountability/transparency, explainability/interpretablity, privacy enhancement and fairness with harmful bias managed where applicable.

### Training rule
Trade-offs must be explicit. Improving one characteristic may create cost, performance, privacy or operational effects elsewhere.

## Module 7 — NIST AI 600-1 GenAI profile

Use AI 600-1 as a GenAI companion profile to extend AI RMF outcomes/actions for generative-AI risks. Maintain source status: voluntary NIST profile, not law or certification.

## Module 8 — Confabulation and information integrity

### Risks
- plausible false output;
- invented citations/facts;
- stale or misleading information;
- downstream automation based on incorrect content.

### Controls
- task-specific evaluation;
- source grounding/RAG where appropriate;
- confidence/limitation communication;
- human validation for consequential outputs;
- output verification against authoritative sources;
- monitoring of known failure classes.

## Module 9 — RAG and knowledge-source governance

Control approved sources, provenance, authorisation, freshness, access inheritance, poisoning/tampering, sensitive data, retrieval quality and deletion/re-indexing.

### Tests
- retrieval relevance;
- groundedness;
- poisoned-source resistance;
- unauthorised-source retrieval;
- stale-version detection;
- sensitive-data leakage.

## Module 10 — Information security

Threat model the complete system: model, prompts, RAG, agents/tools, APIs, identities, secrets, providers, runtime and downstream actions.

### Controls
- identity and least privilege;
- prompt/context boundary controls;
- tool/API restrictions;
- secrets protection;
- data validation;
- rate/resource limits;
- logging/monitoring;
- red teaming;
- incident response.

## Module 11 — Privacy and sensitive data

Map collection, prompts, retrieval sources, logs, provider processing, retention and model/data reuse. Apply minimisation, purpose/authority controls, access restrictions, retention and privacy testing as applicable.

## Module 12 — Human-AI configuration and overreliance

Assess where users may defer excessively to model output. Define training, review thresholds, independent checks, override mechanisms and monitoring of disagreement/override rates.

## Module 13 — Harmful bias and representational risk

Where relevant to the use case, evaluate performance and impacts across appropriate populations/contexts. Avoid unsupported fairness claims and document limitations in data, metrics and interpretation.

## Module 14 — Intellectual property and provenance

Track material source provenance and contractual/usage restrictions where relevant. Separate legal conclusions from technical provenance controls. Escalate legal ambiguity rather than encoding an unsupported rule into the model workflow.

## Module 15 — Third-party model/provider risk

Maintain model/provider identity, material version, data-processing commitments, security/privacy controls, incident/change notification, continuity/exit provisions and revalidation triggers.

### Change triggers
- provider/model replacement;
- capability expansion;
- changed safety policy;
- new training/data-use commitment;
- API/tool behavior change;
- changed geography/hosting;
- material performance shift.

## Module 16 — Red teaming and adversarial evaluation

Scale adversarial testing to materiality. Include prompt injection, jailbreak/unsafe content where relevant, data leakage, RAG poisoning, privilege/tool abuse, denial/resource exhaustion, misleading outputs and containment/recovery.

## Module 17 — Monitoring and KRIs

Monitor operational performance, safety/security events, evaluation drift, provider changes, user complaints, override patterns, policy denials, incidents and unresolved findings.

### Example KRIs
- evaluation failure rate;
- groundedness/citation failure;
- security-policy denials;
- high-impact human overrides;
- unresolved critical findings;
- provider changes awaiting revalidation;
- AI incidents/near misses.

## Module 18 — Incident response

Integrate AI/GenAI incidents into enterprise incident response. Preserve model/provider/version, prompts/context, RAG/tool evidence, affected users/data, containment actions and root-cause/remediation records.

## Module 19 — Change management and revalidation

Material changes to model, prompt/system instructions, provider, RAG sources, tools, permissions, data, evaluation assumptions, use case or population trigger proportionate reassessment and revalidation.

## Module 20 — Independent challenge and assurance

Scale independence to risk. Developer self-testing may be adequate for low-risk routine use; high-impact systems may require independent internal review, specialist red teaming or external assurance where applicable.

### Assurance rule
NIST does not certify implementation through AI RMF alignment. Assurance claims must describe the actual scope, evidence, tests, limitations and residual risk.

## Module 21 — Cross-framework mapping

Map NIST outcomes/actions to Manual 46 common controls and, where useful, to EU AI Act, ISO/IEC 42001 and Singapore governance. Every mapping records relationship type and differences. Similar language does not imply identical obligations.

## Module 22 — 30/60/90-day enterprise implementation

### 30 days
- establish governance ownership;
- inventory AI/GenAI systems;
- define risk tiering;
- document highest-risk use cases and dependencies;
- establish evaluation/evidence repository.

### 60 days
- complete MAP records;
- implement TEVV/evaluation plans;
- establish provider/RAG controls;
- define monitoring and incident procedures;
- close critical control gaps.

### 90 days
- execute independent challenge for material systems;
- test revalidation/change process;
- report KRIs and residual risk;
- complete remediation cycle;
- institutionalise continuous GOVERN/MAP/MEASURE/MANAGE feedback.

## Completion standard

A learner completes Manual 49 when they can take an AI/GenAI use case through GOVERN, MAP, MEASURE and MANAGE, produce auditable evidence and testing, treat GenAI-specific risks through NIST AI 600-1, and explain limitations without claiming legal compliance or certification from NIST alignment.