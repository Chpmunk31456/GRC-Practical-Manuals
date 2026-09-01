# Manual 51 — Agentic AI Evidence Workbook

**Controlled stage:** 4 — release-depth evidence and accountability construction

## Evidence classes

| ID | Evidence | Minimum content |
|---|---|---|
| AG-E01 | Agent inventory | agent identity, owner, purpose, model, tools, data, autonomy tier, environments |
| AG-E02 | Action-boundary specification | allowed actions, prohibited actions, value/impact thresholds, approval requirements |
| AG-E03 | Identity and authorization design | service identity, user delegation, scopes, least privilege, token lifetime, secrets controls |
| AG-E04 | Tool and data allowlist | approved tools/APIs/data stores, purpose, permissions, restrictions, owner |
| AG-E05 | Human-accountability matrix | accountable human, approval checkpoints, intervention authority, escalation |
| AG-E06 | Agent action provenance | initiator, agent identity, context, tool call, parameters, decision, result, timestamp |
| AG-E07 | Safety/security evaluation | misuse cases, prompt injection, privilege escalation, cross-agent delegation, exfiltration, containment |
| AG-E08 | Change/revalidation record | model/tool/data/policy/autonomy change, materiality, retest, approval |
| AG-E09 | Monitoring record | denials, overrides, anomalous actions, policy violations, drift, incidents |
| AG-E10 | Kill/containment test | stop path, credential revocation, tool isolation, rollback, recovery evidence |

## Human approval and action-boundary controls

1. Define autonomy tiers before deployment.
2. Require explicit approval for actions with legal, financial, safety, employment, access-control, external-communication, or irreversible consequences unless a documented risk decision authorizes bounded automation.
3. Enforce technical action limits rather than relying only on prompts.
4. Bind delegated authority to an attributable user or accountable service owner.
5. Preserve the exact tool invocation and resulting side effect for consequential actions.
6. Deny actions outside the declared purpose, tool set, data scope, or authorization context.
7. Revalidate after material changes to tools, model/provider, memory, RAG, permissions, autonomy, or operating environment.
8. Test containment and credential revocation before production and periodically thereafter.

## Release-depth mapping rule

Each AG control must identify the source relationship as direct, partial, supporting, contextual, or none/N/A. IMDA, NIST, and OWASP guidance must retain their actual normative status. No crosswalk row may imply legal equivalence or certification.

## Completion criterion

Stage 4 is complete when the control taxonomy is connected to evidence classes, action-risk scenarios, human-accountability requirements, action boundaries, monitoring, containment, and source-qualified mapping rationale sufficient to prepare controlled localization and deterministic publication candidates.