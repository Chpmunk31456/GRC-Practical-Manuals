# Manual 51 — Agentic AI Governance, Security & Human Accountability Training Architecture

**Canonical stage:** 1 — controlled training architecture  
**Currentness baseline:** 1 September 2026

## Module 1 — What makes an AI system agentic

Distinguish generation from action. Characterise planning, tool invocation, persistence, delegation, memory, environment interaction and autonomous execution. Governance depth scales with consequences and authority, not marketing labels.

## Module 2 — Agent capability and autonomy classification

Create a capability matrix covering goals, tools, data, external systems, code execution, transactions, communications, persistence, multi-agent delegation and reversibility. Establish permitted, prohibited and human-gated actions.

## Module 3 — Identity and authentication

Require attributable agent/service identities. Separate workload identities from shared human credentials. Govern credential issuance, lifetime, storage, rotation and revocation.

## Module 4 — Authorization and least privilege

Scope tool, API, data and environment permissions to approved purpose. Apply deny-by-default for consequential actions where appropriate. Reassess entitlement after capability/tool changes.

## Module 5 — Tool/API and MCP-style trust boundaries

Treat every tool server/API/connector as a security boundary. Validate provider, schema, permissions, transport, input/output, secrets handling and failure behavior. Prevent a trusted agent from becoming a confused deputy for untrusted content.

## Module 6 — Data, RAG and memory governance

Control read/write access, source provenance, memory scope, retention, sensitive data, cross-session persistence and cross-agent sharing. Prevent untrusted retrieved content from silently gaining instruction authority.

## Module 7 — Prompt/context integrity and indirect prompt injection

Separate system policy from untrusted content. Test indirect prompt injection through web pages, documents, tickets, emails and RAG sources. Validate tool calls and consequential outputs independently of natural-language instructions.

## Module 8 — Significant human checkpoints

Define checkpoints before high-impact or irreversible actions such as payments, privileged changes, external commitments, destructive operations, policy exceptions and production deployment. Human review must be timely, informed and empowered to stop the action.

## Module 9 — Action provenance and reconstruction

Record initiator, identity, context, plans/decisions where appropriate, tool calls, permissions, approvals, results, exceptions and downstream effects. Test whether a material event can be reconstructed end-to-end.

## Module 10 — Multi-agent delegation and trust

Document delegation chains, authority transfer, shared memory, cross-agent permissions, identity propagation and conflict handling. Limit recursive delegation and prevent privilege amplification.

## Module 11 — Third-party agents, models and platforms

Assess data handling, identity integration, tool permissions, model/provider changes, incident notification, service continuity, subcontractors and exit. Treat capability expansion as a revalidation trigger.

## Module 12 — Runtime monitoring

Monitor abnormal tool use, privilege denials, action velocity, unusual delegation, repeated failed approvals, cost/resource consumption, security alerts, model/provider changes and policy exceptions.

## Module 13 — Containment and kill capability

Provide tested mechanisms to stop agent execution, revoke credentials, disable tools/connectors, isolate environments, freeze workflows and roll back harmful actions where possible.

## Module 14 — Agent incident response and forensics

Preserve model/version, system policy, tool definitions, identities, prompts/context, RAG/memory evidence, approval logs and action traces. Coordinate with third-party providers when evidence or containment depends on them.

## Module 15 — Change and revalidation

Trigger reassessment after material model, tool, permission, memory, orchestration, prompt/policy, provider, data-source, autonomy or intended-use change.

## Module 16 — Adversarial testing

Test prompt injection, tool abuse, excessive agency, credential misuse, privilege escalation, malicious delegation, data exfiltration, unsafe recursion, multi-agent manipulation, resource exhaustion and containment failure.

## Module 17 — Human competence and automation bias

Train approvers and operators on system limits and failure modes. Monitor override/disagreement patterns. A human checkpoint is ineffective if volume, interface or incentives make independent judgment impractical.

## Module 18 — End-user transparency and responsibility

Where relevant, communicate that the user is interacting with an agent, what it can do, what it cannot decide, what actions require confirmation, and how to challenge or escalate outcomes.

## Module 19 — Governance and residual-risk decision

Use evidence to approve, conditionally approve, restrict, suspend or retire agentic capabilities. Record the accountable decision-maker and residual risk.

## Module 20 — Continuous assurance

Periodically retest permissions, human checkpoints, containment, provider changes, action provenance and security controls. Track findings to closure.

## Source-to-control mapping method

For each AG control record:

**AG control → supporting source(s) → source status → organisational implementation → evidence → test/adversarial case → limitation/non-equivalence note**

Draft/concept/community sources retain their actual status and do not become mandatory standards merely because they support a control.

## Scenario architecture

The controlled scenario set will include:

1. finance agent with payment authority;
2. coding agent with repository/CI/CD access;
3. customer-support agent exposed to indirect prompt injection;
4. multi-agent travel or procurement workflow;
5. third-party agent capability expansion;
6. malicious/compromised tool server;
7. shared-memory data leakage;
8. automation-bias approval failure;
9. failed kill switch during incident;
10. post-incident reconstruction and board reporting.

## Stage-1 completion criterion

Stage 1 is complete when AG-01 through AG-20 are organised into a coherent training sequence, source-status rules are explicit, trust boundaries and evidence/test concepts are defined, and scenario architecture is ready for controlled full drafting.