# Manual 04 — NIST AI 600-1 Generative AI Profile Implementation

**Current controlled baseline:** NIST AI 600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, published 26 July 2024

**Development status:** controlled build — version-aware implementation intake

**Author and accountable human creator:** Alberto “Al” Leiva

[Main repository](../../README.md) | [GRC foundations](../README.md) | [AI-assistance disclosure](../../AI_ASSISTANCE_DISCLOSURE.md) | [Visual-learning standard](../../VISUAL_LEARNING_STANDARD.md)

## Important scope and version notice

NIST AI 600-1 is a published cross-sectoral profile of and companion resource for AI RMF 1.0. It is intended for voluntary use. The profile describes risks that are unique to or exacerbated by generative AI and provides suggested actions organized against selected AI RMF functions, categories, and subcategories.

Manual 04 will not treat the profile as a universal checklist. NIST states that not every AI RMF subcategory is included, not every suggested action applies to every AI actor or task, and applicability depends on the organization, its GAI use, lifecycle stage, context, risk tolerance, requirements, and resources. The manual will therefore preserve an explicit applicability decision for every adopted, tailored, deferred, or non-applicable action.

AI RMF 1.0 remains the parent framework for this profile and is under revision. Any NIST change to the parent framework or this profile will trigger source-state review and impact analysis before the controlled baseline changes.

## Start here

1. Read [Manual 04 implementation paths](./MANUAL_04_IMPLEMENTATION_PATHS.md).
2. Establish a GAI inventory that distinguishes models, systems, applications, use cases, integrations, data flows, users, affected parties, and value-chain dependencies.
3. Identify the relevant AI actors and tasks across design, development, deployment, operation, monitoring, procurement, oversight, TEVV, incident response, and decommissioning.
4. Screen the twelve NIST GAI risk families at model, system, use-case, and ecosystem levels.
5. Select and tailor suggested actions through the organization’s actual requirements, risk tolerance, resources, lifecycle stage, and actor responsibilities.
6. Define evidence, thresholds, stop/rollback conditions, release decisions, continuous monitoring, incident disclosure, and reassessment triggers.

## Controlled risk families

Manual 04 preserves the twelve risk families identified by NIST AI 600-1:

1. CBRN Information or Capabilities
2. Confabulation
3. Dangerous, Violent, or Hateful Content
4. Data Privacy
5. Environmental Impacts
6. Harmful Bias and Homogenization
7. Human-AI Configuration
8. Information Integrity
9. Information Security
10. Intellectual Property
11. Obscene, Degrading, and/or Abusive Content
12. Value Chain and Component Integration

The presence of a risk-family label does not prove that a risk is material in a particular deployment. Each assessment must record the relevant source, context, affected asset or party, plausible event, likelihood or uncertainty, consequence, existing controls, residual risk, and accountable decision.

## Four primary considerations

NIST AI 600-1 was informed by work focused on four primary considerations. Manual 04 will keep each operationally visible:

- **Governance:** authority, accountability, policies, risk tolerance, acceptable use, documentation, independent challenge, and decision rights.
- **Content Provenance:** origin, history, authenticity, labeling, metadata, disclosure, chain of custody, and limits of provenance methods.
- **Pre-deployment Testing:** risk-based TEVV, red-teaming, structured human feedback, representative conditions, capability evaluation, safety thresholds, and independent review.
- **Incident Disclosure:** detection, triage, containment, notification, affected-party communication, supplier coordination, evidence retention, corrective action, and learning.

## Implementation model

Manual 04 will apply the profile through the AI RMF functions:

- **GOVERN** establishes authority, policy, accountability, risk tolerance, acceptable-use rules, supplier controls, and independent review.
- **MAP** records the context of use, actors, affected parties, dependencies, intended and reasonably foreseeable uses, risk sources, benefits, harms, and assumptions.
- **MEASURE** uses proportionate qualitative and quantitative methods, TEVV, red-teaming, provenance checks, bias/privacy/security evaluation, uncertainty analysis, and human feedback.
- **MANAGE** prioritizes and treats risk, makes go/no-go/conditional decisions, monitors residual risk, activates stop or rollback conditions, responds to incidents, and improves controls.

## Evidence model

The controlled build will require evidence that can support both management decisions and independent review:

- GAI inventory and actor/responsibility map;
- applicability and tailoring register for suggested actions;
- risk-family assessment with model/system/use-case/ecosystem scope;
- data, model, prompt, tool, retrieval, output, and downstream-use lineage;
- content-provenance design and effectiveness records;
- test strategy, datasets, environments, acceptance thresholds, limitations, and results;
- red-team and structured-feedback plans, findings, triage, and closure evidence;
- human-oversight design, competence, workload, escalation, and override evidence;
- supplier due diligence, contract, change-notice, monitoring, incident, and exit evidence;
- release, stop, rollback, containment, decommissioning, and residual-risk decisions; and
- incident disclosure, affected-party communication, corrective action, and lessons learned.

## Assurance boundary

Passing repository QA will mean that the controlled structure, official-source references, profile relationship, risk-family coverage, applicability logic, accessibility, and evidence expectations are internally consistent. It will **not** certify a GAI system, establish legal compliance, prove that all suggested actions apply, determine that an organization has achieved trustworthy AI, or provide an audit opinion.

The profile and AI RMF are voluntary guidance. Organizations remain responsible for applicable law, regulation, contract, policy, safety, security, privacy, intellectual-property, sector, and product obligations.

## Controlled source identifiers

- `nist-ai-600-1` — NIST AI 600-1 Generative AI Profile; status `final`
- `nist-ai-rmf-1-0` — AI RMF 1.0 parent framework; status `final-under-revision`

## Development roadmap

- [x] Establish Manual 04 as the next controlled series item behind Manual 03.
- [x] Verify the current profile title, publication date, cross-sectoral scope, companion relationship, and voluntary-use boundary through official NIST sources.
- [x] Establish the controlled baseline, applicability boundary, risk-family set, and dedicated fail-closed QA workflow.
- [x] Build Essential, Structured, and Enhanced intake paths with accessible memory graphics.
- [ ] Build the controlled English chapter master and practical workpapers.
- [ ] Perform official-source, terminology, copyright, accessibility, security, and visual QA.
- [ ] Produce semantically localized Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) sources.
- [ ] Complete qualified human semantic review for both localized editions.
- [ ] Generate and page-review accessible DOCX/PDF publication candidates.
- [ ] Complete final human release approval only after the full evidence package is reviewed.

## Official starting points

- NIST AI 600-1 publication page and DOI `10.6028/NIST.AI.600-1`
- NIST AI 600-1 official PDF
- NIST AI Risk Management Framework page
- NIST AI Resource Center (AIRC)

Verify the official NIST publication state immediately before publication or release packaging.
