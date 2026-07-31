# Chapter 77 — Open-Source and Component Governance

## 1. Purpose

Open-source software, open-weight models, public datasets, community libraries, plug-ins, model adapters, prompts, orchestration frameworks, and other reusable components can accelerate AI delivery. They also create legal, security, quality, continuity, and accountability risks that may be difficult to see once the component is embedded in a production service.

This chapter establishes a controlled governance process for selecting, approving, integrating, monitoring, changing, and retiring open-source and reusable AI components.

> Open availability does not remove organizational accountability.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## 2. Scope

This chapter applies to:

- open-source software libraries;
- open-weight and openly licensed AI models;
- public model repositories and package registries;
- training, evaluation, retrieval, and fine-tuning datasets;
- model adapters, checkpoints, embeddings, prompts, agents, and plug-ins;
- community-maintained connectors and orchestration components;
- code copied from public repositories, forums, notebooks, or examples;
- transitive dependencies introduced through approved packages;
- internal forks of external open-source projects.

## 3. Governance principle

Open-source status is not a risk classification. A component may be freely available yet still create material risk because of:

- unknown provenance;
- restrictive or incompatible licensing;
- unverified maintainers;
- malicious or compromised code;
- hidden transitive dependencies;
- embedded personal, confidential, copyrighted, or unlawful data;
- weak documentation;
- undisclosed limitations;
- insecure defaults;
- model backdoors or poisoned weights;
- abandoned maintenance;
- uncontrolled updates;
- unclear downstream obligations.

## 4. EU AI Act considerations

The organization must determine the legal role it assumes when it integrates, modifies, brands, distributes, or places an AI model or AI system on the market or into service.

A free and open-source release may affect the application of certain documentation obligations for some general-purpose AI models when statutory conditions are met. It does not create a blanket exemption from the AI Act, and it does not remove obligations that remain applicable, including obligations concerning copyright policy, training-content summaries, systemic-risk models, prohibited practices, high-risk systems, transparency, safety, cybersecurity, or downstream provider responsibilities.

The legal team must assess:

- whether the component is software, an AI model, an AI system, or part of one;
- whether GlobalWay acts as deployer, provider, importer, distributor, or another value-chain actor;
- whether modification, fine-tuning, integration, own-brand placement, or changed intended purpose alters that role;
- whether the component contributes to a high-risk or transparency-regulated use case;
- whether open-source conditions relied upon for any exception are actually satisfied;
- whether the component is a general-purpose AI model with systemic risk;
- whether downstream information is sufficient for GlobalWay to meet its own obligations.

## 5. Open-source component inventory

Every approved component must be recorded in the AI component inventory before production use.

Minimum fields:

| Field | Required information |
|---|---|
| Component | Name and unique identifier |
| Type | Library, model, dataset, plug-in, adapter, prompt, framework, or other |
| Source | Repository, registry, provider, and canonical location |
| Version | Exact version, commit, digest, checksum, or model hash |
| License | License name, version, and obligations |
| Maintainer | Responsible external maintainer or project |
| Internal owner | Accountable GlobalWay owner |
| Use case | Approved business purpose |
| AI Act role | Provider, deployer, importer, distributor, or other assessment |
| Data exposure | Data sent to, processed by, or embedded in the component |
| Security status | Scan, signature, provenance, and vulnerability results |
| Quality status | Evaluation and limitation results |
| Approval | Decision, conditions, approver, and date |
| Monitoring | Review frequency and alert sources |
| Exit plan | Replacement, rollback, or removal approach |

## 6. Intake and approval process

### Step 1 — Business justification

The requester must document:

- the intended purpose;
- why the component is needed;
- alternatives considered;
- expected benefit;
- affected people and processes;
- proposed data use;
- production criticality.

### Step 2 — Source verification

The reviewer must confirm:

- the canonical repository or distribution channel;
- maintainer identity where reasonably available;
- release authenticity;
- digital signatures, hashes, or checksums;
- whether the package is a typosquatted, impersonated, or unofficial copy;
- whether binaries correspond to reviewed source where this can be verified.

### Step 3 — License and intellectual-property review

Review must cover:

- license compatibility with intended use and distribution;
- attribution and notice requirements;
- source-code disclosure obligations;
- copyleft implications;
- patent provisions;
- trademark restrictions;
- dataset and model-weight terms;
- restrictions on commercial use, field of use, geography, redistribution, or modification;
- copyright and database-right risks;
- training-data representations and unresolved claims.

No component may be approved merely because its repository labels it “open source.” The actual license text and use conditions control.

### Step 4 — Security and provenance review

The security review should include, where relevant:

- software composition analysis;
- vulnerability scanning;
- malware and secret scanning;
- dependency-tree analysis;
- package-signature verification;
- source and release-history review;
- model-weight integrity verification;
- sandbox execution;
- prompt, tool, and agent permission analysis;
- review for hidden network calls, telemetry, unsafe deserialization, arbitrary code execution, and insecure defaults;
- model backdoor, poisoning, and anomalous-behavior testing;
- maintainer and repository compromise indicators.

### Step 5 — Data and privacy review

The organization must determine:

- what data enters the component;
- what data leaves the controlled environment;
- whether prompts, outputs, logs, embeddings, or fine-tuning data are retained;
- whether personal or special-category data is involved;
- whether the component contains embedded personal, copyrighted, confidential, or unlawful content;
- whether international transfers occur;
- whether deletion and correction are technically possible;
- whether the component can expose memorized or training-derived content.

### Step 6 — Technical and human-impact evaluation

Evaluation must address:

- task performance;
- known limitations;
- robustness;
- bias and disparate impact;
- multilingual performance;
- accessibility;
- explainability;
- hallucination or fabrication risk;
- unsafe content generation;
- misuse potential;
- human-oversight requirements;
- stop, escalation, correction, and override mechanisms.

### Step 7 — Approval decision

Available decisions:

- approved;
- approved with conditions;
- approved for testing only;
- rejected;
- escalated for legal, security, privacy, technical, or executive review.

## 7. Component bill of materials

Each production AI system must maintain an AI component bill of materials sufficient to identify:

- direct and transitive software dependencies;
- models and model versions;
- datasets and dataset versions;
- adapters, fine-tunes, and checkpoints;
- prompts and orchestration logic;
- external APIs and services;
- licenses;
- hashes or immutable references;
- known vulnerabilities and exceptions;
- component owners;
- last-review dates.

The bill of materials must be updated through change management and retained as evidence.

## 8. Version pinning and change control

Production systems must use controlled, reproducible component versions wherever technically feasible.

Required controls include:

- pinning versions, commits, model revisions, or hashes;
- blocking uncontrolled “latest” dependencies;
- testing updates before release;
- comparing model behavior before and after change;
- documenting changed licenses, maintainers, dependencies, or limitations;
- reassessing AI Act role and substantial-modification risk;
- preserving rollback capability;
- approving emergency updates through a documented exception process.

A silent upstream update must not become a silent production change.

## 9. Forks and internal modifications

An internal fork creates additional responsibilities. The owner must document:

- why the fork exists;
- differences from upstream;
- responsible maintainers;
- security and quality testing;
- upstream changes not adopted;
- patch and vulnerability-management processes;
- license and attribution obligations;
- whether the modification changes the intended purpose, capabilities, risk, or legal role;
- long-term maintenance and exit plans.

## 10. Ongoing monitoring

Monitoring should cover:

- new vulnerabilities;
- maintainer or ownership changes;
- repository compromise;
- malicious releases;
- license changes;
- project abandonment;
- material issues or safety disclosures;
- model-performance drift;
- newly discovered bias, privacy, security, or misuse risks;
- regulatory or contractual changes;
- dependence on unsupported versions.

Critical alerts must route to accountable human owners with authority to restrict, suspend, replace, or remove the component.

## 11. Stop and escalation conditions

Use must stop or be restricted when:

- provenance cannot be established;
- the license is absent, incompatible, or unclear;
- a component contains malware, critical vulnerabilities, or untrusted code execution;
- model weights or releases fail integrity verification;
- the component creates an unmitigated prohibited-practice, safety, rights, privacy, or cybersecurity risk;
- required documentation is unavailable;
- a maintainer account or repository appears compromised;
- an update materially changes behavior without approval;
- the project is abandoned and continuity controls are inadequate;
- responsible owners cannot explain, monitor, override, or safely retire the component.

## 12. GlobalWay Travel Services example

GlobalWay proposes using an open-weight multilingual model to summarize airline disruption notices and draft traveler communications.

### AI may do

- summarize approved source notices;
- draft multilingual traveler messages;
- flag missing operational details;
- suggest a communication priority.

### Human decision

A travel-operations specialist decides whether the draft is accurate, appropriate, accessible, and safe to send.

### Required review

GlobalWay reviews:

- model and dataset provenance;
- license and redistribution terms;
- supported languages;
- known limitations;
- cybersecurity and model-integrity results;
- hallucination and mistranslation rates;
- accessibility of generated communications;
- data-retention and logging behavior;
- fallback capability.

### Stop and escalation

The workflow stops when the model invents itinerary details, mistranslates safety instructions, exposes traveler information, produces inaccessible content, or changes behavior after an unapproved model update.

### Accountable owner

The Director of Travel Operations owns the business decision. The AI product owner, security, privacy, legal, accessibility, and vendor-risk teams retain their assigned control responsibilities.

### Challenge, correction, and override

Travel specialists can edit, reject, or replace the draft. They can switch to approved templates or manual communications without relying on the model.

## 13. Control activities

| Control ID | Control activity | Evidence |
|---|---|---|
| EUAI-OSS-01 | Maintain an approved AI component inventory | Inventory and ownership records |
| EUAI-OSS-02 | Verify provenance, version, and integrity before use | Hashes, signatures, source records |
| EUAI-OSS-03 | Complete license and intellectual-property review | Legal assessment and notices |
| EUAI-OSS-04 | Perform security, privacy, quality, and rights testing | Test reports and approvals |
| EUAI-OSS-05 | Maintain an AI component bill of materials | Current bill of materials |
| EUAI-OSS-06 | Pin production versions and control updates | Configuration and change records |
| EUAI-OSS-07 | Monitor vulnerabilities, maintainers, licenses, and drift | Alerts, reviews, and tickets |
| EUAI-OSS-08 | Maintain rollback, replacement, and exit capability | Tested recovery and exit plans |

## 14. Evidence requirements

Evidence should include:

- approved intake request;
- component inventory record;
- canonical source and version information;
- hashes, signatures, or checksums;
- license analysis;
- attribution and notice records;
- security and provenance assessments;
- privacy and data-flow review;
- technical, bias, accessibility, and human-impact tests;
- AI Act role assessment;
- component bill of materials;
- approval decision and conditions;
- monitoring alerts and remediation records;
- change, rollback, and retirement evidence.

## 15. Audit test

Select a sample of production AI systems using open-source or reusable components.

For each sample:

1. Confirm every component is present in the approved inventory.
2. Trace the deployed version to an immutable reference, hash, or equivalent record.
3. Verify license and intellectual-property review.
4. Inspect security, privacy, quality, accessibility, and human-impact evidence.
5. Confirm direct and transitive dependencies are represented in the component bill of materials.
6. Test whether updates follow change-management controls.
7. Confirm monitoring identifies vulnerabilities, repository compromise, license changes, abandonment, and model drift.
8. Verify accountable humans can suspend, replace, roll back, or remove the component.
9. Confirm exceptions are approved, time-limited, and monitored.

## 16. Metrics

Suggested metrics:

- percentage of production AI components inventoried;
- percentage with immutable version references;
- percentage with completed license review;
- percentage with current security and vulnerability review;
- number of unsupported or abandoned components;
- number of critical open-source vulnerabilities past remediation target;
- percentage of systems with current component bills of materials;
- percentage of component updates tested before deployment;
- number of emergency rollbacks;
- average time to remove a prohibited or compromised component.

## 17. Management checklist

- [ ] Is the canonical component source known?
- [ ] Is the exact deployed version recorded?
- [ ] Is the license compatible with intended use?
- [ ] Are provenance and integrity verified?
- [ ] Are direct and transitive dependencies known?
- [ ] Have security, privacy, quality, bias, accessibility, and rights risks been tested?
- [ ] Is the AI Act role assessment current?
- [ ] Are updates controlled and reversible?
- [ ] Is ongoing monitoring active?
- [ ] Can accountable humans suspend, replace, and retire the component safely?

## 18. Figure specification

### Figure 77-1 — Open-Source AI Component Governance Gate

Create a formal process diagram showing:

`Business need → Source and provenance verification → License review → Security and data review → Technical and human-impact testing → Role assessment → Approval decision → Controlled integration → Monitoring → Update, rollback, or retirement`

Include visible stop gates for:

- unknown provenance;
- incompatible license;
- critical security risk;
- unlawful or unverified data;
- unacceptable performance or human impact;
- inadequate documentation;
- no safe exit capability.

**Accessibility text:** A left-to-right governance flow showing that open-source AI components must pass provenance, licensing, security, data, technical, human-impact, and legal-role reviews before controlled production use, followed by monitoring and safe retirement.

## 19. Key takeaway

Open source can improve transparency, flexibility, and innovation, but it does not transfer responsibility away from the organization that selects, modifies, integrates, deploys, or distributes the component. Effective governance requires verified provenance, lawful licensing, controlled versions, documented dependencies, tested human oversight, continuous monitoring, and a safe exit path.
