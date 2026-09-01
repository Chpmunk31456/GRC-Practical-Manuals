# Manual 48 — Control and Evidence Workbook

Use this workbook to translate Singapore AI-governance guidance into auditable enterprise controls. Each row should be completed for the organisation's actual AI system and retained with evidence.

| ID | Control objective | Implementation expectation | Minimum evidence | Test / assurance method | Common failure |
|---|---|---|---|---|---|
| SG-AI-01 | Governance accountability | Named accountable executive, system owner and control owners | charter, RACI, committee terms | verify ownership and sampled decisions | ownership exists only on paper |
| SG-AI-02 | AI inventory | Maintain current inventory of AI, GenAI and agents | inventory, owner, purpose, provider, status | reconcile against procurement/cloud/repos | shadow AI omitted |
| SG-AI-03 | Use-case risk assessment | Assess impact, data, autonomy, users and failure modes before deployment | risk assessment, disposition | sample completeness and approvals | generic risk template with no use-case analysis |
| SG-AI-04 | Human involvement | Define meaningful review/approval where harm or irreversible action warrants it | decision-rights matrix, approval logs | test whether reviewer can intervene | rubber-stamp human in the loop |
| SG-AI-05 | Data governance | Control collection, retrieval, sensitive data, lineage and retention | data-flow map, source list, retention rules | trace sampled data paths | unrestricted RAG/data sources |
| SG-AI-06 | Lifecycle operations | Define validation, monitoring, change, incident and retirement controls | lifecycle plan, test reports, monitoring | inspect material changes and revalidation | model/provider changes not detected |
| SG-AI-07 | Stakeholder transparency | Communicate AI use, role and limitations accurately | notices, user guidance, claims register | compare claims to evidence | overstated capability or compliance claims |
| SG-GEN-01 | GenAI evaluation | Evaluate hallucination, harmful output, security/privacy and task performance | evaluation plan/results | reproduce selected tests | only benchmark accuracy measured |
| SG-GEN-02 | Prompt/RAG boundary | Bound prompt, retrieval and tool inputs | source allowlist, filters, prompt controls | adversarial retrieval/prompt tests | confidential or poisoned sources admitted |
| SG-GEN-03 | Content provenance | Identify or qualify generated content where relevant | metadata/notice policy | sample outputs | no traceability for high-impact content |
| SG-ASSURE-01 | Assurance claims | Tie every assurance statement to actual checks/tests and limitations | test scope, report, limitation note | trace claims to evidence | 'passed AI Verify = compliant' |
| SG-ASSURE-02 | Reproducible testing | Preserve test conditions, data/version and results | test config, versions, logs | rerun selected tests | results cannot be reproduced |
| SG-AG-01 | Agent capability inventory | Record autonomy, tools, data, actions and external communication | capability matrix | compare with live permissions | undocumented tool capability |
| SG-AG-02 | Bound agent powers | Apply least privilege, allowlists, limits and safe defaults | IAM policy, tool policy, thresholds | attempt prohibited action | broad inherited credentials |
| SG-AG-03 | Significant human checkpoints | Require approval at high-impact/irreversible boundaries | checkpoint catalogue, approval records | sample transactions | approval occurs after action |
| SG-AG-04 | Agent identity | Give agents/services attributable identities | identity records, auth config | trace sampled action to identity | shared human/service account |
| SG-AG-05 | Action provenance | Record requests, plans, tool calls, results and material actions | immutable/event logs | reconstruct sampled event | fragmented or missing logs |
| SG-AG-06 | Containment | Provide tested disable/kill/credential-revocation mechanisms | runbook, test evidence | tabletop or controlled test | kill switch exists but untested |
| SG-AG-07 | Multi-agent boundaries | Define delegation, trust and shared-memory boundaries | architecture diagram, permissions | trace cross-agent action | implicit privilege propagation |
| SG-AG-08 | Third-party agent risk | Assess external agent/provider changes and dependencies | vendor assessment, contract, change log | review update notification/revalidation | silent capability expansion |
| SG-AG-09 | Automation-bias control | Preserve independent human judgment where required | reviewer training, override metrics | analyze override/disagreement rates | near-zero overrides ignored |
| SG-AG-10 | End-user responsibility | Disclose agent identity, role, limits and escalation | user notice/training | sample user journeys | user believes agent has authority it lacks |
| SG-AG-11 | Change/revalidation | Define material changes that trigger new assessment/testing | trigger list, change tickets | sample model/tool/provider updates | no revalidation after capability change |
| SG-AG-12 | Incident response | Detect, contain, investigate and remediate AI/agent incidents | IR playbook, incident records | tabletop/sample incident | AI incidents handled outside IR process |
| SG-XW-01 | Cross-framework non-equivalence | Map overlaps without claiming automatic legal/standards equivalence | crosswalk, caveat column | review mappings | framework alignment misrepresented as compliance |

## Evidence register template

For every implemented control record:

- Control ID
- AI system / use case
- Accountable owner
- Control operator
- Evidence location
- Evidence period / timestamp
- Model/provider/tool versions
- Test procedure
- Test result
- Exception / finding
- Remediation owner and due date
- Residual risk decision
- Revalidation date

## Agent action review sample

For a sample of material agent actions, verify:

1. attributable agent/service identity;
2. authenticated user or upstream initiator where applicable;
3. relevant instruction/context;
4. selected tool/API;
5. permission decision;
6. human checkpoint if required;
7. action result;
8. error/exception handling;
9. downstream consequences;
10. rollback/containment availability.

## Management dashboard minimums

- AI systems by risk tier;
- GenAI/agentic systems by business owner;
- overdue risk assessments;
- overdue access reviews;
- high-impact actions requiring approval;
- approval override/rejection rates;
- unresolved assurance findings;
- provider/model changes awaiting revalidation;
- AI/agent incidents and near misses;
- tested/untested containment mechanisms;
- third-party-agent dependencies;
- overdue remediation items.

## Release caveat

This workbook operationalises Singapore governance guidance. Completion of the workbook is not certification and does not by itself establish compliance with Singapore law, the EU AI Act, ISO/IEC 42001, NIST AI RMF, or any other external requirement.