# Chapter 70 — Testing, Monitoring, and Disclosure Assurance

## 70.1 Purpose

Transparency controls are only effective when they continue to work after deployment. This chapter establishes how GlobalWay Travel Services tests, monitors, documents, and improves AI disclosures so that people remain properly informed when they interact with AI systems or encounter AI-generated or manipulated content.

The objective is not simply to publish a notice once. The objective is to prove, over time, that the notice appears when required, is understandable, remains accessible, survives system changes, and supports meaningful human escalation.

## 70.2 Legal and governance context

Article 50 of Regulation (EU) 2024/1689 establishes transparency obligations for providers and deployers of certain AI systems. These duties apply from 2 August 2026, subject to the limited transitional treatment applicable to certain pre-existing systems for machine-readable marking and detection obligations.

The European Commission’s Article 50 guidance explains the scope of the obligations and how providers and deployers may demonstrate compliance. The Commission’s Code of Practice on Transparency of AI-Generated Content may also support compliance for marking and labelling obligations, while organisations that do not rely on the Code must demonstrate equivalent appropriate measures.

Testing and monitoring do not create a separate Article 50 obligation. They are the assurance mechanisms used to demonstrate that Article 50 controls remain effective, reliable, robust, accessible, and traceable.

## 70.3 Core principle

> A disclosure is not effective merely because it exists in a design file. It must appear at the right moment, reach the affected person, remain understandable and accessible, and continue to work after technical or operational change.

## 70.4 Scope

This chapter applies to:

- AI systems that interact directly with natural persons;
- generative AI systems that create or manipulate text, images, audio, or video;
- deepfake disclosures;
- AI-generated text concerning matters of public interest;
- emotion-recognition and biometric-categorisation notices;
- machine-readable marking and detection controls;
- accessibility and understandable-notice controls;
- human-escalation and challenge pathways linked to transparency notices.

## 70.5 Governance model

GlobalWay assigns the following accountability:

| Role | Responsibility |
|---|---|
| AI System Owner | Ensures the disclosure control is designed, implemented, funded, and maintained. |
| Product Owner | Ensures the notice appears in the correct user journey and release process. |
| Legal and Compliance | Determines the applicable disclosure obligation and approves legal wording. |
| Accessibility Lead | Verifies that notices and escalation routes are accessible. |
| Security and Engineering | Implements logging, monitoring, integrity checks, and technical safeguards. |
| Data Protection Officer | Reviews privacy interactions and data-minimisation concerns. |
| Human Oversight Owner | Ensures people can obtain meaningful human assistance or challenge. |
| Internal Audit | Tests design and operating effectiveness independently. |
| Vendor Management | Obtains evidence from external providers and monitors contractual compliance. |

No single function may self-certify the entire disclosure-control lifecycle.

## 70.6 Disclosure control inventory

Every applicable system must have a disclosure-control record containing:

- system and use-case identifier;
- provider, deployer, or combined role;
- applicable Article 50 paragraph;
- affected-person population;
- disclosure trigger;
- disclosure wording and language variants;
- channel and placement;
- machine-readable marking method, where applicable;
- accessibility requirements;
- human-escalation path;
- control owner;
- test frequency;
- evidence source;
- known limitations;
- last successful test date;
- unresolved defects and remediation status.

## 70.7 Testing lifecycle

### 70.7.1 Design testing

Before release, GlobalWay verifies that:

- the legal trigger has been correctly identified;
- the notice is presented before or at the first relevant interaction or exposure;
- the wording clearly identifies the AI involvement;
- the notice is not hidden in terms and conditions or a secondary help page;
- the disclosure remains visible long enough to be perceived;
- the user can reach a human or alternative channel where required;
- the notice is available in the relevant language;
- accessibility requirements are satisfied;
- machine-readable marks are present and detectable where required.

### 70.7.2 Functional testing

Functional tests should confirm that the control operates in realistic conditions, including:

- new and returning users;
- authenticated and unauthenticated journeys;
- desktop, mobile, app, kiosk, email, voice, and messaging channels;
- slow networks and interrupted sessions;
- translated interfaces;
- assistive technologies;
- third-party integrations;
- content export, download, reposting, and format conversion;
- fallback and degraded-service modes.

### 70.7.3 Negative testing

GlobalWay must test what happens when the control fails. Negative scenarios include:

- the disclosure does not render;
- the wrong disclosure appears;
- the notice is displayed after the AI interaction has already occurred;
- a model or vendor update removes machine-readable marking;
- a translation omits or weakens the disclosure;
- a screen reader cannot detect the notice;
- a user cannot reach a human escalation route;
- a deepfake or synthetic-media label is stripped during publishing;
- a content-management system changes the layout or hides the notice;
- an emergency communication bypasses the normal review workflow.

### 70.7.4 User comprehension testing

A notice should be tested with representative users to determine whether they understand:

- that AI is being used;
- what the AI is doing;
- whether content was generated or manipulated;
- whether a human reviewed the output;
- what choices or challenge rights are available;
- how to obtain human assistance;
- what the notice does not mean.

Comprehension testing should include people with varied language, disability, literacy, age, device, and digital-confidence profiles.

### 70.7.5 Accessibility testing

Testing must cover, as appropriate:

- keyboard-only navigation;
- screen-reader output and reading order;
- focus visibility;
- colour contrast;
- text resizing and reflow;
- captions and transcripts;
- voice-interface alternatives;
- cognitive load and plain language;
- touch-target size;
- timeout and motion controls;
- compatibility with common assistive technologies.

Accessibility testing should combine automated checks, expert review, and user testing. Automated tools alone are not sufficient.

## 70.8 Monitoring in production

GlobalWay should monitor both the presence and effectiveness of disclosures.

### 70.8.1 Technical monitoring

Technical controls may include:

- synthetic user journeys that confirm notice rendering;
- telemetry showing whether notices were delivered;
- integrity checks for machine-readable marks;
- alerts when templates, model versions, or content pipelines change;
- automated detection of missing disclosure elements;
- monitoring for broken escalation links;
- retention of release and configuration evidence;
- comparison of approved wording against production wording.

### 70.8.2 Operational monitoring

Operational monitoring should include:

- complaints that people were unaware they were interacting with AI;
- accessibility complaints;
- escalation abandonment rates;
- reports of misleading or missing labels;
- vendor incidents;
- translation defects;
- repeated user confusion;
- content reposting that strips labels;
- regulator or consumer-protection enquiries.

### 70.8.3 Outcome monitoring

The organisation should assess whether disclosure controls are achieving their intended outcome. Useful indicators include:

- percentage of applicable interactions with a verified disclosure;
- percentage of synthetic content with verified machine-readable marking;
- disclosure comprehension rate;
- human-escalation completion rate;
- accessibility defect rate;
- mean time to repair a disclosure failure;
- repeat-defect rate;
- vendor evidence completion rate;
- percentage of releases that completed disclosure regression testing.

Metrics must not be used to imply compliance where the underlying control evidence is incomplete.

## 70.9 Change-management triggers

Disclosure controls must be retested when any of the following occurs:

- model or system replacement;
- major model-version change;
- new use case or audience;
- new language or jurisdiction;
- interface redesign;
- vendor or subcontractor change;
- content-publishing workflow change;
- new output modality;
- new accessibility requirement;
- material complaint or incident;
- legal or regulatory guidance change;
- substantial modification assessment;
- new integration that may remove or obscure labels.

## 70.10 Stop and escalation conditions

Deployment or publication must stop when:

- a legally required disclosure is absent;
- the notice is materially misleading;
- the human-escalation route does not work;
- required machine-readable marking is absent or unreliable;
- accessibility defects prevent affected users from perceiving or acting on the notice;
- a translation changes the legal meaning;
- monitoring shows repeated undisclosed AI interaction;
- a vendor cannot provide required evidence;
- a change has occurred without required regression testing.

Emergency exceptions must be documented, time-limited, approved by an accountable human, and reviewed after the event.

## 70.11 GlobalWay examples

### Example 1 — Traveler-support chatbot

**Requirement:** Inform travelers that they are interacting with AI.

**Control activity:** The notice appears before the first chatbot response, remains available during the conversation, and includes a visible human-agent option.

**Monitoring:** A synthetic test runs daily across web, mobile, and messaging channels. Failure creates a high-priority incident.

**Evidence:** Screenshots, test logs, release records, accessibility results, and escalation-path logs.

**Audit test:** Select a sample of channels and languages, reproduce the user journey, verify timing and wording, and confirm the human route operates.

### Example 2 — AI-generated disruption notice

**Requirement:** Assess whether disclosure is required for AI-generated public-interest text and whether meaningful human editorial responsibility applies.

**Control activity:** The publishing workflow records the authoring source, human reviewer, substantive edits, approval time, and disclosure decision.

**Monitoring:** Weekly sampling compares published messages with approval records.

**Evidence:** Draft history, reviewer identity, change log, final message, and disclosure rationale.

**Audit test:** Determine whether the human review was meaningful rather than nominal and whether editorial responsibility was clearly assigned.

### Example 3 — Synthetic destination video

**Requirement:** Label manipulated or synthetic content and preserve machine-readable marking where applicable.

**Control activity:** The content pipeline adds a visible label and an approved machine-readable mark before publication.

**Monitoring:** Automated checks test whether both survive export and platform upload.

**Evidence:** Original asset, marked asset, detection-test result, publishing record, and platform screenshot.

**Audit test:** Download the published content and verify both visible and machine-readable disclosures remain effective.

## 70.12 Vendor assurance

Contracts with AI providers should require:

- disclosure-support functionality;
- machine-readable marking capability where applicable;
- documentation of known limitations;
- change notifications;
- testing evidence;
- cooperation with audits and incidents;
- accessibility information;
- retention of relevant logs;
- remediation timeframes;
- prohibition on silently removing required labels or notices.

Vendor assurances must be validated. A contractual statement alone is not sufficient evidence of operating effectiveness.

## 70.13 Evidence register

Recommended evidence includes:

- legal applicability assessment;
- approved notice wording;
- screenshots and recordings;
- automated and manual test results;
- accessibility reports;
- machine-readable detection results;
- release approvals;
- change tickets;
- model and vendor version records;
- user-comprehension study results;
- complaints and incident records;
- remediation evidence;
- audit workpapers;
- management reporting.

Evidence must be dated, attributable, protected from unauthorised alteration, and retained according to the organisation’s legal and records-management requirements.

## 70.14 Control library

| Control ID | Control objective | Control activity | Owner | Frequency | Evidence |
|---|---|---|---|---|---|
| TRA-70-01 | Identify all disclosure controls | Maintain a complete disclosure-control inventory | Compliance | Quarterly and on change | Approved inventory |
| TRA-70-02 | Verify pre-release effectiveness | Perform functional, negative, accessibility, and comprehension testing | Product and Accessibility | Every release | Test pack and approval |
| TRA-70-03 | Detect production failures | Monitor disclosure rendering, marking integrity, and escalation paths | Engineering | Continuous | Monitoring logs and alerts |
| TRA-70-04 | Control changes | Trigger regression testing after defined changes | Change Manager | Every relevant change | Change record and test result |
| TRA-70-05 | Address defects | Triage, contain, remediate, and retest disclosure failures | System Owner | As needed | Incident and closure evidence |
| TRA-70-06 | Assure vendors | Obtain and validate provider evidence | Vendor Management | Annually and on change | Due-diligence file |
| TRA-70-07 | Provide independent assurance | Test design and operating effectiveness | Internal Audit | Risk-based | Audit workpapers |

## 70.15 Audit programme

Internal Audit should:

1. obtain the AI and disclosure-control inventories;
2. select a risk-based sample of systems and channels;
3. confirm the legal role and applicable Article 50 duty;
4. inspect approved wording and placement;
5. reproduce user journeys;
6. test accessibility and human escalation;
7. inspect machine-readable marking where applicable;
8. review monitoring alerts and defect closure;
9. verify change-triggered regression testing;
10. assess vendor evidence;
11. inspect management reporting;
12. determine whether control failures were disclosed, contained, and remediated appropriately.

Audit conclusions should distinguish:

- design effectiveness;
- operating effectiveness;
- evidence sufficiency;
- residual risk;
- unresolved legal judgment;
- accessibility limitations;
- vendor dependency.

## 70.16 Formal process diagram

### Figure 70-1 — Disclosure Testing, Monitoring, and Assurance Lifecycle

**Diagram sequence:**

1. Determine applicable disclosure duty.
2. Approve wording, placement, accessibility, and escalation.
3. Perform functional, negative, comprehension, and accessibility testing.
4. Release only after accountable approval.
5. Monitor rendering, marking, complaints, and outcomes.
6. Detect defect or change.
7. Stop, contain, remediate, and retest where required.
8. Record evidence and report to governance.
9. Conduct independent assurance.
10. Feed lessons into design and training.

**Alt text:** Circular assurance lifecycle showing legal assessment, design approval, multidimensional testing, controlled release, production monitoring, defect response, evidence retention, independent audit, and continuous improvement.

**Explanation:** The lifecycle prevents transparency from becoming a one-time drafting exercise. It links legal interpretation, engineering, accessibility, operations, monitoring, and independent assurance.

## 70.17 Human-concern graphic

### Figure 70-2 — “The Notice Worked in Testing”

**Concept:** A professional travel-service interface shows a disclosure perfectly in a test environment. Beside it, the live mobile interface hides the same notice behind a cookie banner, language selector, and floating promotion.

**Caption:** A control that works only in the test environment is not an effective control.

**Alt text:** Side-by-side comparison of a clear AI notice in a controlled test screen and an obscured notice in the live mobile interface, illustrating the difference between laboratory success and real-world effectiveness.

## 70.18 Management checklist

Before approving continued operation, management should confirm:

- [ ] all applicable systems are in the disclosure inventory;
- [ ] legal roles and duties are documented;
- [ ] wording and placement are approved;
- [ ] accessibility and comprehension tests are complete;
- [ ] machine-readable marking is tested where applicable;
- [ ] monitoring is active;
- [ ] escalation routes work;
- [ ] change triggers are configured;
- [ ] vendor evidence is current;
- [ ] defects are tracked and retested;
- [ ] management receives meaningful metrics;
- [ ] independent assurance is scheduled.

## 70.19 Key lesson

Transparency is an operational control, not a label added at the end of a project. Effective compliance requires continuous proof that disclosures remain visible, understandable, accessible, technically reliable, and supported by accountable human action.

## 70.20 Authoritative sources

- Regulation (EU) 2024/1689, especially Article 50.
- European Commission, Guidelines on the implementation of transparency obligations for providers and deployers of AI systems under Article 50.
- European Commission, Code of Practice on Transparency of AI-Generated Content.
- European Commission, Quick Facts: Transparency rules for AI systems.

Legal requirements, guidance, codes, and organisational best practices must remain clearly distinguished during future editorial and legal review.
