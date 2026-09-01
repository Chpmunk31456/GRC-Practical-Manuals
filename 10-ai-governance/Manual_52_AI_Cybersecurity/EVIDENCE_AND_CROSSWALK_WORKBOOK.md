# Manual 52 — AI Cybersecurity Evidence and Crosswalk Workbook

**Controlled stage:** 4 — detailed threat/control mapping and evidence construction

## Evidence register

| ID | Evidence | Supports |
|---|---|---|
| AC-E01 | AI asset and dependency inventory | model, provider, RAG, vector DB, tools, agents, hosting, APIs |
| AC-E02 | AI threat model | trust boundaries, attack paths, misuse cases, threat actors, assumptions |
| AC-E03 | Prompt/RAG security test pack | injection, indirect injection, retrieval poisoning, exfiltration |
| AC-E04 | Agent authorization design | identities, scopes, tool permissions, delegation, least privilege |
| AC-E05 | Supply-chain assessment | model/provider/library/package provenance, integrity, change notice |
| AC-E06 | Adversarial evaluation results | jailbreak, tool abuse, unsafe execution, cross-agent attack, evasion |
| AC-E07 | Telemetry and detection map | model, app, agent, tool, identity, data, network, policy logs |
| AC-E08 | Incident evidence package | event chronology, affected assets, prompts/actions, containment, root cause |
| AC-E09 | Change/revalidation record | model/provider/data/tool/policy changes and required retesting |
| AC-E10 | Recovery/containment test | isolation, credential revocation, rollback, safe-mode, restoration |

## OWASP / MITRE ATLAS relationship method

Each threat/control row must record: enterprise control → OWASP relationship → MITRE ATLAS technique/tactic relationship where applicable → NIST supporting relationship → evidence → limitations → residual risk. OWASP remains community guidance; MITRE ATLAS remains a living knowledge base; NIST remains voluntary framework/profile guidance. None is represented as legal certification.

## Manual 46 / Manual 51 crosswalk

- Manual 46 supplies enterprise AI-governance ownership, inventory, risk, assurance, monitoring, incident, and change-management spine.
- Manual 51 supplies agent identity, autonomy, action-boundary, delegated-authority, tool-use, provenance, and human-accountability controls.
- Manual 52 adds adversarial threat modeling, attack-path controls, detection, red-team validation, technical containment, and AI-specific incident evidence.

## Required technical control families

1. AI asset and dependency discovery.
2. Secure design and trust-boundary analysis.
3. Data/RAG integrity and retrieval security.
4. Prompt and instruction-channel isolation.
5. Model/provider and software supply-chain integrity.
6. Agent/tool least privilege and authorization.
7. Output handling and unsafe-action prevention.
8. Abuse, jailbreak, and adversarial testing.
9. Telemetry, detection, and forensic provenance.
10. Incident containment, recovery, and revalidation.

## Stage completion criterion

Stage 4 is complete when the AC control taxonomy, adversarial scenarios, source-qualified OWASP/ATLAS relationships, evidence register, Manual 46/51 dependencies, and localization-ready control language are sufficient to prepare deterministic publication candidates.