# Chapter 65 — AI-Generated and Manipulated Content Marking

**Status:** Draft for owner review  
**Primary legal basis:** Regulation (EU) 2024/1689, Article 50(2), 50(4), and 50(5)  
**Official implementation guidance:** European Commission Article 50 transparency guidelines and the Code of Practice on Transparency of AI-Generated Content  
**Application date:** 2 August 2026, subject to applicable transitional provisions

> **Human concern:** “How will I know whether this image, recording, video, or message is authentic?”

## 1. Requirement

Providers of AI systems that generate or manipulate synthetic audio, image, video, or text content must ensure that the output is marked in a machine-readable format and can be detected as artificially generated or manipulated, as far as technically feasible. The marking must be effective, interoperable, robust, and reliable, taking account of the characteristics and limitations of the relevant content type, implementation cost, and generally acknowledged technical standards.

Deployers must clearly disclose when they use AI systems to create or manipulate content that qualifies as a deepfake. They must also clearly disclose AI-generated or manipulated text published to inform the public on matters of public interest when that text has not undergone human review or editorial control and no natural or legal person holds editorial responsibility for it.

The duties are related but distinct:

- **Provider duty:** make synthetic content technically identifiable.
- **Deployer duty:** make specified synthetic content meaningfully understandable to people.

Technical marking does not, by itself, satisfy every human-facing disclosure obligation.

## 2. Plain-English explanation

A hidden technical marker helps systems, platforms, investigators, and downstream organizations check where content came from. A visible disclosure helps an ordinary person understand what they are seeing, hearing, or reading.

Organizations need both controls when both duties apply. A technically detectable file with no understandable notice can still mislead a traveler, employee, customer, regulator, or member of the public. Conversely, a visible label alone may be lost when content is copied, cropped, converted, compressed, or redistributed.

The control objective is therefore:

> **Preserve reliable provenance through the content lifecycle and give people a clear disclosure at the point where the content may influence them.**

## 3. Scope assessment

For every AI-generated or manipulated item, the content owner should determine:

1. Was an AI system used to generate or materially manipulate the content?
2. What content type is involved: text, image, audio, video, or a combination?
3. Is GlobalWay acting as provider, deployer, or both?
4. Does the provider-side machine-readable marking duty apply?
5. Does the content qualify as a deepfake?
6. Is text being published to inform the public on a matter of public interest?
7. Did qualified human review or editorial control occur?
8. Is a person or organization accepting editorial responsibility?
9. Does an exception or special treatment apply?
10. What visible disclosure, technical marker, evidence, and monitoring are required?

A documented answer is required before publication or distribution.

## 4. GlobalWay Travel Services example

GlobalWay uses generative AI to prepare traveler communications during a major volcanic-ash disruption affecting European airspace.

The AI system produces:

- a route map showing affected airports;
- a short video narrated by a synthetic voice;
- personalized traveler alerts;
- an executive client briefing;
- social-media posts explaining expected delays;
- draft public statements about safety and disruption response.

### What the AI may do

- summarize approved operational data;
- draft text and visual layouts;
- generate alternative wording;
- produce synthetic narration from approved scripts;
- insert machine-readable provenance data supported by the provider;
- flag low-confidence or conflicting source information.

### What remains a human decision

A qualified GlobalWay employee must:

- verify safety, routing, airport, and regulatory information;
- approve all public-interest communications;
- determine whether a visible AI disclosure is required;
- approve the placement and wording of the disclosure;
- confirm that technical markers remain present in final published files;
- accept editorial responsibility;
- stop publication where facts cannot be verified.

### Stop and escalation conditions

Publication must stop and escalate when:

- a safety claim cannot be validated;
- the AI output conflicts with an authoritative source;
- the content may impersonate a real person;
- synthetic audio or video could reasonably be mistaken for authentic footage;
- required metadata is missing or stripped;
- the disclosure is obscured, unreadable, or removed by the publishing platform;
- there is uncertainty about whether the material concerns a matter of public interest;
- no qualified person is prepared to accept editorial responsibility.

## 5. Control framework

### Control 65.1 — Content-origin classification

**Control activity:** Before publication, the content owner records whether the item is human-created, AI-assisted, AI-generated, or AI-manipulated and identifies the applicable Article 50 obligations.

**Owner:** Content owner or business process owner  
**Frequency:** Per item or approved content batch  
**Evidence:** Classification record, source files, model or tool identifier, reviewer decision

### Control 65.2 — Machine-readable marking

**Control activity:** Where the provider duty applies, the system applies an effective machine-readable marker or provenance mechanism to relevant synthetic content.

**Owner:** AI provider or technical platform owner  
**Frequency:** At generation or export  
**Evidence:** Configuration, technical specification, sample outputs, detection test results, version records

### Control 65.3 — Marker-preservation testing

**Control activity:** GlobalWay tests whether markers remain detectable after normal processing, including resizing, compression, transcoding, document conversion, platform upload, and download.

**Owner:** Technical owner  
**Frequency:** Before deployment and after material change  
**Evidence:** Test plan, test files, results, defects, remediation records

### Control 65.4 — Deepfake disclosure

**Control activity:** Deepfake content is clearly and distinguishably disclosed as artificially generated or manipulated, with appropriate treatment for evidently artistic, satirical, fictional, or analogous content.

**Owner:** Communications, legal, or content owner  
**Frequency:** Per item  
**Evidence:** Published content, disclosure wording, approval, screenshot, accessibility check

### Control 65.5 — Public-interest text review

**Control activity:** AI-generated or manipulated public-interest text either receives documented human editorial review with an accountable publisher or carries the required disclosure.

**Owner:** Editorial owner  
**Frequency:** Per publication  
**Evidence:** Reviewer identity, review checklist, tracked changes, approval, editorial-responsibility record

### Control 65.6 — Disclosure quality

**Control activity:** Disclosures are clear, perceivable, understandable, accessible, and presented no later than the first exposure to the relevant content.

**Owner:** User-experience or communications owner  
**Frequency:** Before publication and during periodic review  
**Evidence:** Approved language, placement screenshots, readability and accessibility testing, localized versions

### Control 65.7 — Distribution-channel validation

**Control activity:** The organization verifies that each intended channel preserves the required label and technical marker and does not hide, crop, or strip them.

**Owner:** Channel owner  
**Frequency:** Before channel use and after platform change  
**Evidence:** Channel test results, sample publications, exception log

### Control 65.8 — Correction and takedown

**Control activity:** GlobalWay can rapidly correct, relabel, withdraw, or replace content when a disclosure or provenance control fails.

**Owner:** Communications incident owner  
**Frequency:** Event-driven  
**Evidence:** Incident record, takedown evidence, corrected version, notification record, root-cause analysis

## 6. Human-facing disclosure standard

A compliant disclosure should be:

- easy to notice;
- understandable without technical expertise;
- accessible to people with disabilities;
- appropriate to the language and context;
- placed before or at first exposure;
- preserved during redistribution where feasible;
- specific enough to explain whether the content was generated or materially manipulated;
- linked to a human contact or correction route when the content could materially affect a person.

### Example disclosure language

**AI-generated image:**  
“This image was generated using artificial intelligence and was reviewed by GlobalWay before publication.”

**Synthetic narration:**  
“This recording uses an AI-generated voice reading a script approved by GlobalWay.”

**Materially altered video:**  
“This video contains imagery materially altered using artificial intelligence.”

**Public-interest text without editorial review:**  
“This text was generated using artificial intelligence and was published without human editorial review.”

The final wording must reflect the actual process. An organization must not claim human review where the reviewer merely clicked an approval button without examining the substance.

## 7. Formal process graphic specification

**Figure 65-1 — From generation to trustworthy publication**

Process:

`AI creates or modifies content → classify content and organizational role → apply machine-readable marker → determine visible-disclosure duty → human factual/editorial review → approve, correct, reject, or escalate → publish with marker and disclosure → monitor redistribution and complaints → correct or withdraw when necessary`

### Human checkpoints

- factual verification;
- deepfake determination;
- public-interest determination;
- disclosure decision;
- accessibility review;
- editorial responsibility;
- final publication approval.

### Alt text

A process diagram showing AI-generated content moving through classification, technical marking, legal assessment, human review, publication, monitoring, and correction, with human decision points before content is released.

### Written explanation

The figure demonstrates that transparency is not a label added at the end. It is a controlled lifecycle combining technical provenance, legal classification, human judgment, accessible communication, and post-publication monitoring.

## 8. Original workplace-satire illustration specification

**Figure 65-2 — “Technically Disclosed”**

### Scene

A communications manager proudly points to a large synthetic travel poster. The poster carries a microscopic label hidden in the decorative border. A traveler is using a magnifying glass while an auditor asks, “Was the disclosure intended for people or for ants?”

### Concept explained

A disclosure can exist and still fail if it is not perceivable or understandable.

### Human concern

“Are you genuinely telling me this is artificial, or merely protecting the organization with fine print?”

### Caption

**A disclosure that ordinary people cannot notice is not meaningful transparency.**

### Alt text

An original office cartoon shows a traveler using a magnifying glass to find an extremely small AI disclosure on a synthetic travel advertisement while an auditor questions whether the notice was designed for people.

### Publication note

The illustration must be original workplace satire. It must not imitate or reproduce copyrighted characters, panels, dialogue, or a living or deceased cartoonist’s distinctive style.

## 9. Evidence requirements

GlobalWay should retain, as applicable:

- content classification and legal assessment;
- AI system and model version;
- prompts or generation instructions where appropriate;
- original and final content files;
- machine-readable marker configuration;
- marker-detection results;
- disclosure wording and placement approval;
- human review and tracked changes;
- evidence of editorial responsibility;
- accessibility and localization testing;
- distribution-channel tests;
- publication screenshots or recordings;
- complaint, correction, and takedown records;
- exceptions and legal advice;
- vendor documentation and contractual commitments.

Evidence must show what actually happened, not merely what the policy required.

## 10. Audit tests

### Design-effectiveness testing

The auditor should determine whether:

1. the organization distinguishes provider and deployer duties;
2. the classification process covers all relevant content types;
3. machine-readable marking is technically defined;
4. deepfake and public-interest disclosure decisions are documented;
5. human review and editorial responsibility are meaningful;
6. disclosure standards address placement, accessibility, language, and timing;
7. channel testing and correction procedures exist;
8. exceptions are defined and legally reviewed.

### Operating-effectiveness testing

For a sample of AI-generated or manipulated content, the auditor should:

1. trace the item to its source system and model version;
2. verify the classification decision;
3. test whether the technical marker is detectable;
4. confirm that ordinary processing did not remove the marker;
5. inspect the visible disclosure for clarity and placement;
6. verify the identity and competence of the reviewer;
7. examine evidence of substantive review and editorial responsibility;
8. compare approved and published versions;
9. confirm that publication-channel behavior was tested;
10. inspect complaints, corrections, or takedowns connected with the item.

### Failure indicators

- labels hidden in metadata when a visible disclosure is required;
- visible notices placed after the content has already influenced the user;
- disclosures removed during platform upload;
- undetectable or unreliable technical markers;
- synthetic media impersonating a person without escalation;
- “human reviewed” claims unsupported by substantive review evidence;
- no accountable editor for public-interest text;
- inconsistent labels across languages or channels;
- no method to correct or withdraw misleading content.

## 11. Metrics and management reporting

Recommended measures include:

- percentage of synthetic-content items classified before publication;
- percentage with required technical markers successfully detected;
- marker survival rate after common transformations;
- percentage with required visible disclosures;
- percentage receiving documented substantive human review;
- disclosure accessibility pass rate;
- channel-preservation failure rate;
- number of synthetic-content complaints;
- number and age of open transparency defects;
- correction and takedown response time;
- repeated failures by system, vendor, content owner, or distribution channel.

Metrics should distinguish technical success from human comprehension. A 100% metadata-marking rate does not prove that people received a meaningful disclosure.

## 12. Management questions

Leaders should ask:

- Which of our systems generate or materially manipulate content?
- Where are we the provider, deployer, or both?
- Can we prove that technical markers survive real distribution channels?
- Which publications require visible disclosure?
- Who decides whether content qualifies as a deepfake or concerns a matter of public interest?
- Who accepts editorial responsibility?
- Can a traveler easily identify synthetic content without special tools?
- How quickly can we correct or withdraw misleading material?
- What happens when a vendor’s marking technology fails?
- Are our labels equally clear in every supported language and format?

## 13. GlobalWay implementation checklist

- [ ] Inventory content-generating and content-manipulating AI systems.
- [ ] Assign provider and deployer roles.
- [ ] Define machine-readable marking requirements.
- [ ] Test marking across normal transformations.
- [ ] Create deepfake and public-interest decision criteria.
- [ ] Define meaningful human editorial review.
- [ ] Approve accessible disclosure language and placement.
- [ ] Test all publication channels.
- [ ] Establish correction, relabeling, and takedown procedures.
- [ ] Train content, marketing, communications, legal, and technical teams.
- [ ] Monitor complaints and marker failures.
- [ ] Reassess after system, vendor, model, format, or channel changes.

## 14. Legal-status and publication control

This chapter distinguishes:

- **binding obligations:** Article 50 of Regulation (EU) 2024/1689 and any binding amending instrument;
- **official nonbinding interpretation:** Commission guidelines;
- **voluntary compliance support:** the Code of Practice on Transparency of AI-Generated Content;
- **recommended organizational practice:** controls that go beyond the minimum legal text to create reliable, auditable, and human-centered compliance.

Before publication, the legal editor must reverify:

- the current consolidated Article 50 text;
- applicable transitional dates;
- the status and adequacy assessment of the Code of Practice;
- Commission guidance and official FAQs;
- any relevant harmonised standards or technical specifications;
- enforcement guidance from competent authorities.

## 15. Official sources

- Regulation (EU) 2024/1689, Article 50 and Recitals 133–135: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European Commission, Guidelines on transparency obligations for providers and deployers of AI systems: https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- European Commission, Guidelines on Transparency of AI-Generated Content: https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content
- European Commission, Code of Practice on Transparency of AI-Generated Content: https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
- European Commission, Quick Facts: Transparency rules for AI systems: https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems
