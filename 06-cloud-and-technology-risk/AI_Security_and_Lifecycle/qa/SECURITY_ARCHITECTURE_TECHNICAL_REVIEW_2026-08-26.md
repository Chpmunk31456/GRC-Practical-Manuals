# Manual 07 — Security Architecture and Technical Review

**Manual:** AI Security and Lifecycle Controls  
**Review date:** 2026-08-26  
**Review type:** model-assisted technical/security review supporting the controlled release process  
**Human release status:** not satisfied by this record

## Scope reviewed

The complete controlled English 32-chapter master, implementation-path architecture, controlled baseline, authoritative-source verification record, and current source registry were reviewed for internal consistency, security overstatement, lifecycle gaps, and source-state leakage.

## Findings and disposition

### 1. ISO/IEC 27090 source state — remediated

The shared source registry previously described ISO/IEC 27090 as `final`. ISO currently lists the first edition at stage 60.00, International Standard under publication. The registry has been corrected to `under-development`, with stage 60.00 retained in the version field. Manual 07 already treats this source as a source-state watch rather than a published normative baseline.

**Disposition:** PASS after registry correction. Reverify at the exact final candidate because publication may occur during the release cycle.

### 2. Lifecycle security coverage — PASS

The controlled master addresses concept/use-case definition, acquisition, design/development, evaluation/testing, release, operation/monitoring, incident/change management, and retirement/decommissioning. It treats prompts, retrieval, tools, agents, models, data, infrastructure, identities, suppliers, and monitoring components as security-relevant system elements rather than reducing security to a model endpoint.

### 3. Authorization and privilege boundaries — PASS

The master requires explicit identities, least privilege, external/deterministic authorization where possible, bounded tool permissions, high-impact approval controls, credential scoping, and observable execution. It does not rely on model instructions as the sole authorization mechanism.

### 4. Prompt injection, RAG, and untrusted-content boundary — PASS

Direct and indirect prompt injection, poisoned or compromised retrieval content, vector-store access, context separation, retrieval filtering, output validation, tool allowlists, and permission boundaries are represented as layered controls. The manual does not claim that a single classifier, prompt, or guardrail eliminates the threat.

### 5. Secure development and supply chain — PASS

The manual treats model, dataset, adapter, package, container, API, plugin, safety service, hosting, prompt, retrieval, and supplier changes as security-significant. Provenance supports trust decisions but is explicitly not represented as proof of safety.

### 6. Security testing and independent challenge — PASS

The master distinguishes risk-based validation, independent challenge, adversarial evaluation/red-team scenarios, configuration-specific evidence, limitations, remediation ownership, and follow-up validation. Testing is not represented as proof of absence of exploitable weakness.

### 7. Runtime detection, response, containment, rollback, and stop — PASS

Monitoring, alert ownership, evidence-preserving logs, incident integration, explicit stop/rollback authority, tested recovery, degraded operation, and periodic reassessment are covered. The manual correctly states that a paper-only stop mechanism cannot be credited before validation.

### 8. Assurance and release boundary — PASS

The material repeatedly states that automated QA, testing, checklists, or repository workflows do not guarantee security, safety, compliance, or absence of weaknesses. Exact-candidate evidence and human release review remain mandatory, and material changes reopen affected gates.

## Security/editorial conclusions

No release-blocking defect was identified in the controlled English security architecture after correction of the ISO/IEC 27090 registry status. The current content is suitable to proceed to controlled localization and publication-candidate generation.

This record is supporting technical evidence. It is not penetration testing of a deployed AI system, a certification, a conformity assessment, an audit opinion, or Final Human Release Approval.
