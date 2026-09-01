# Manual 51 — Agentic AI Governance and Security Control Taxonomy

**Canonical stage:** 0 — controlled taxonomy / architecture preparation

## AG-01 — Agent identity

Every production agent or agent service that can access enterprise resources must have an attributable identity appropriate to the environment.

Evidence examples: identity record, service principal/workload identity, ownership metadata, credential lifecycle record.

## AG-02 — Authentication and credential control

Agents must authenticate to tools/services using controlled credentials; avoid embedded long-lived secrets and shared human accounts.

Evidence: auth configuration, secret-management records, token lifetime/scopes, rotation logs.

## AG-03 — Authorization and least privilege

Grant only the data, tools and actions necessary for the approved use case. Privilege must be reviewed as agent capabilities change.

Evidence: role/policy definitions, entitlement review, denied-action tests.

## AG-04 — Capability and autonomy bounding

Document permitted goals, actions, tools, data domains, transaction limits, external communications, code execution and prohibited activities.

Evidence: capability matrix, allowlist/denylist, policy-as-code, limit configuration.

## AG-05 — Significant human checkpoints

Define where human authorization is genuinely required before a material, high-impact or irreversible action.

Evidence: checkpoint catalogue, approval records, rejected actions, escalation logs.

## AG-06 — Tool and API trust boundaries

Treat tools, MCP servers, APIs, plugins and connectors as security boundaries with explicit trust, schema, permission and input/output controls.

Evidence: tool inventory, trust classification, API scopes, schema validation, server/provider assessment.

## AG-07 — Data and memory boundaries

Control what an agent may read, retain, retrieve, write or share across session memory, long-term memory, RAG stores and external services.

Evidence: data-flow map, access policies, retention rules, memory configuration, source allowlist.

## AG-08 — Instruction and prompt boundary integrity

Protect system instructions, tool-selection logic and trusted context from untrusted content and indirect prompt injection.

Evidence: trust-boundary model, content isolation, validation rules, adversarial tests.

## AG-09 — Action provenance

Material agent actions must be reconstructable from attributable logs including initiator/context, agent identity, selected tools, approvals, results and exceptions.

Evidence: immutable/event logs, correlation IDs, sampled reconstruction tests.

## AG-10 — Multi-agent delegation control

Explicitly define which agents may delegate to or instruct other agents, what authority transfers, and how shared memory/credentials are bounded.

Evidence: delegation graph, inter-agent permission matrix, cross-agent trace logs.

## AG-11 — Third-party agent and provider governance

Assess external agents/models/tools/providers for data handling, permissions, change notification, incidents, continuity and exit risk.

Evidence: vendor assessment, contract controls, provider-change log, contingency plan.

## AG-12 — Monitoring and anomaly detection

Monitor agent behavior, unusual tool use, privilege changes, policy denials, action velocity, high-impact decisions and unexpected delegation patterns.

Evidence: detections, dashboards, alerts, investigation records.

## AG-13 — Containment and kill capability

Provide tested mechanisms to halt the agent, revoke credentials, disable tools, isolate environments and prevent further harmful actions.

Evidence: containment runbook, kill-switch test, credential revocation test, rollback evidence.

## AG-14 — Incident response

Integrate agent incidents into enterprise incident response, including evidence preservation, scope reconstruction and provider coordination.

Evidence: AI/agent IR playbook, incident records, tabletop results.

## AG-15 — Change and revalidation

Material changes in model, prompt/system instruction, tools, permissions, autonomy, provider, data sources or orchestration must trigger risk reassessment and proportionate revalidation.

Evidence: trigger matrix, change tickets, before/after tests, approval.

## AG-16 — Testing and adversarial evaluation

Test normal and adversarial agent behavior, including unauthorized tool use, prompt injection, privilege escalation, cross-agent manipulation, data leakage, unsafe autonomy and containment response.

Evidence: test plan, red-team results, remediation, retest.

## AG-17 — Human competence and automation-bias control

People supervising agents must understand the agent's limits and retain independent judgment where human accountability is required.

Evidence: training, reviewer guidance, override/disagreement metrics, sampled reviews.

## AG-18 — End-user transparency and responsibility

Users should understand when they are interacting with an agent, the agent's role/limits, what actions it can take, and how to challenge/escalate problems where relevant.

Evidence: user notices, capability/limitation statement, feedback/escalation channel.

## AG-19 — Governance and risk acceptance

Deploy, restrict, suspend or retire agentic capability based on documented risk, test evidence and accountable decision-making.

Evidence: risk decision, exceptions, residual-risk acceptance, deployment gate.

## AG-20 — Auditability and continuous assurance

Maintain sufficient evidence to periodically test whether agent governance/security controls remain effective as systems and dependencies evolve.

Evidence: control testing, findings, remediation, revalidation schedule, management dashboard.

## Taxonomy rule

This taxonomy is an independently authored common-control structure. Source mappings to IMDA, NIST, OWASP, EU law, ISO/IEC 42001 or other material must preserve the source's actual status and may not imply automatic equivalence.