# Manual 49 — NIST AI RMF + GenAI Control and Evidence Workbook

| ID | Function/domain | Control objective | Minimum evidence | Test / assurance method |
|---|---|---|---|---|
| N-AI-01 | GOVERN | Assign accountable AI ownership and decision rights | charter, RACI, approvals | sample decisions and ownership |
| N-AI-02 | GOVERN | Maintain AI/GenAI inventory and risk tier | inventory, tier rationale | reconcile against procurement/cloud/repos |
| N-AI-03 | GOVERN | Establish policy, risk tolerance and exceptions | policy, standards, exceptions | inspect exceptions and expiry/remediation |
| N-AI-04 | GOVERN | Govern model/provider and third parties | assessment, contract, change notices | sample material provider changes |
| N-AI-05 | MAP | Document intended purpose and prohibited/misuse cases | use-case statement, misuse analysis | compare production use to approved purpose |
| N-AI-06 | MAP | Identify actors, users and affected parties | stakeholder map | sample impacts and escalation paths |
| N-AI-07 | MAP | Map data, RAG and technical dependencies | architecture, lineage/source map | trace sampled data/retrieval flows |
| N-AI-08 | MAP | Record assumptions, limitations and foreseeable harms | limitations/risk register | challenge assumptions against evidence |
| N-AI-09 | MEASURE | Define measurable acceptance criteria | evaluation plan, thresholds | reproduce selected tests |
| N-AI-10 | MEASURE | Preserve test/version provenance | model/provider version, test config | verify reproducibility |
| N-AI-11 | MEASURE | Test robustness and adversarial behavior | red-team/test report | retest remediated findings |
| N-AI-12 | MEASURE | Evaluate security/privacy risks | security/privacy tests | attack/leakage sampling |
| N-AI-13 | MEASURE | Evaluate human overreliance where relevant | user study/override metrics | analyze disagreement/override rates |
| N-AI-14 | MANAGE | Tie material risks to treatment decisions | treatment plan, owners, due dates | sample open/closed risks |
| N-AI-15 | MANAGE | Establish deployment/exception gate | decision record, residual risk | verify authority/evidence basis |
| N-AI-16 | MANAGE | Monitor KRIs, incidents and drift | dashboard, alerts, incident log | sample alert-to-action trace |
| N-AI-17 | MANAGE | Trigger revalidation after material change | trigger matrix, change tickets | sample model/provider/RAG changes |
| N-GEN-01 | GenAI | Control confabulation/information integrity | groundedness/factuality tests | sample high-impact responses |
| N-GEN-02 | GenAI | Govern RAG source provenance and access | allowlist, lineage, access rules | poison/unauthorized retrieval tests |
| N-GEN-03 | GenAI | Control sensitive-data leakage | DLP/privacy config and tests | adversarial leakage testing |
| N-GEN-04 | GenAI | Manage harmful/unsafe outputs | policy, filters, evaluations | safety test set / red team |
| N-GEN-05 | GenAI | Govern provider/model changes | version/change register | regression/revalidation sampling |
| N-GEN-06 | GenAI | Preserve content/source provenance where relevant | source/citation metadata | trace selected output to sources |
| N-TEVV-01 | Assurance | Scale independent challenge to materiality | assurance plan, reviewer independence | verify reviewer separation/competence |
| N-IR-01 | Incident | Reconstruct AI/GenAI incidents | version, prompt/context, RAG/tool logs | tabletop or incident reconstruction |
| N-XW-01 | Crosswalk | Prevent false equivalence | mapping rationale/caveats | review claims against source status |

## Evidence register

For each control record:

- system/use case;
- control ID and owner;
- evidence location/date;
- model/provider/tool version;
- test procedure and test data;
- result and uncertainty/limitation;
- finding/exception;
- remediation owner/date;
- residual-risk decision;
- next revalidation date.

## GOVERN-MAP-MEASURE-MANAGE case worksheet

### GOVERN
Who owns risk? What policy/risk tolerance applies? What provider/third-party dependencies exist?

### MAP
What is the intended use? Who is affected? What data/RAG/tools/dependencies exist? What harms/misuse are foreseeable?

### MEASURE
Which claims must be tested? What metrics, test sets and adversarial cases apply? What uncertainty remains?

### MANAGE
What risks require treatment? Who accepts residual risk? What monitoring, change triggers, incident and rollback controls apply?

## Release caveat

This workbook operationalises voluntary NIST AI RMF / AI 600-1 guidance. Completion does not constitute NIST certification and does not by itself establish compliance with law or another standard.