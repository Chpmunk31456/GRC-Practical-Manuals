# Chapter 66 — Deepfake Disclosure and Synthetic-Media Governance

**Status:** Draft for owner review  
**Primary legal basis:** Regulation (EU) 2024/1689, Article 50(4) and related official European Commission guidance  
**Application date:** 2 August 2026, subject to applicable transitional provisions and final publication verification

> **Human concern:** “Am I looking at something that really happened, or at content created or altered by AI?”

## 1. Requirement

Deployers of AI systems that generate or manipulate image, audio, or video content constituting a deepfake must disclose that the content has been artificially generated or manipulated. Limited exceptions and adapted disclosure rules apply in specific legally authorised or evidently artistic, creative, satirical, fictional, or analogous contexts.

The disclosure duty is separate from provider-side machine-readable marking. A technical marker may help systems detect synthetic content, but it does not replace a clear disclosure to the person who sees or hears the content.

## 2. Plain-language explanation

People should not have to investigate metadata, inspect source code, or guess whether a realistic video, voice recording, or image is authentic. When an organisation uses AI to create or materially alter realistic media, the disclosure should be visible, timely, understandable, and appropriate to the context.

A label that is technically present but hidden, ambiguous, or displayed only after the content has influenced the viewer is not meaningful transparency.

## 3. GlobalWay Travel Services example

GlobalWay creates an AI-generated video showing a fictional traveler receiving support during a major airport disruption. The video uses synthetic narration and digitally generated people.

Before publication, GlobalWay must:

1. classify the content as synthetic media;
2. determine whether it constitutes a deepfake under the applicable legal definition;
3. preserve provider-side machine-readable marking where available;
4. add a clear visible and, where relevant, audible disclosure;
5. obtain human editorial and legal approval;
6. retain the source, prompt, model, approval, and publication evidence;
7. monitor whether downstream platforms remove or obscure the disclosure.

**Example disclosure:**

> This video contains AI-generated people and voices. It illustrates a fictional travel-support scenario and does not depict an actual event.

## 4. What AI may do and what remains a human decision

| Activity | AI may perform | Human responsibility |
|---|---|---|
| Generate images, voices, or video | Create draft media from approved instructions | Approve the purpose, audience, and permitted use |
| Suggest disclosure text | Draft plain-language wording | Confirm legal sufficiency, clarity, placement, and accessibility |
| Detect possible synthetic media | Flag content for review | Determine classification and required action |
| Apply technical markers | Embed supported machine-readable signals | Verify preservation and test detectability |
| Publish content | Prepare a publication package | Authorise release and remain accountable for the outcome |

AI must not make the final decision that disclosure is unnecessary.

## 5. Control activities

### 5.1 Synthetic-media intake and classification

All externally distributed AI-generated or materially manipulated image, audio, and video content must enter a documented review process before release.

The reviewer must determine:

- whether the content is wholly or partly AI-generated;
- whether it realistically depicts people, objects, places, entities, or events;
- whether viewers could reasonably mistake it for authentic content;
- whether it qualifies as a deepfake;
- whether an exception or adapted disclosure rule may apply;
- whether other laws, contractual duties, platform rules, or internal policies impose stricter requirements.

### 5.2 Dual-layer transparency

GlobalWay must use both layers where applicable:

1. **Technical layer:** machine-readable marking, provenance metadata, watermarking, or comparable detection support.
2. **Human layer:** visible, audible, or otherwise directly perceivable disclosure appropriate to the format.

The human-facing notice must not depend solely on metadata or a link hidden in terms and conditions.

### 5.3 Placement and timing

Disclosures should appear before or at the first meaningful exposure to the synthetic content. They should remain visible or accessible long enough to be understood.

For video, the control owner should consider:

- opening-frame notice;
- persistent or recurring on-screen label;
- spoken notice where audio is central;
- description-field disclosure;
- accessible text alternative.

### 5.4 Artistic, satirical, and fictional content

Where content is evidently artistic, creative, satirical, fictional, or analogous, disclosure may be adapted so it does not unreasonably interfere with the work. The organisation must still document why the adapted form is appropriate and how viewers are informed that AI-generated or manipulated content exists.

An “artistic” label must not be used to conceal deceptive commercial, political, reputational, or operational communications.

### 5.5 Impersonation and voice-cloning safeguards

Synthetic media involving a real person’s likeness or voice requires heightened review. At minimum, GlobalWay must verify:

- identity and authority of the requester;
- consent or other lawful basis;
- permitted purpose and distribution channels;
- contractual and personality-right restrictions;
- fraud, social-engineering, and reputational risks;
- revocation, correction, and takedown procedures.

### 5.6 Human editorial review

A qualified reviewer must assess whether the content:

- could mislead a reasonable person;
- creates an inaccurate impression of a real event;
- falsely attributes statements or conduct;
- could affect safety, employment, travel decisions, reputation, or public trust;
- uses a disclosure that is clear and proportionate;
- remains suitable after translation, cropping, reposting, or platform conversion.

### 5.7 Downstream preservation

GlobalWay must test whether labels and technical markers survive common processing steps, including:

- resizing and compression;
- format conversion;
- clipping or excerpting;
- reposting to social-media platforms;
- screenshotting or screen recording;
- audio extraction;
- translation and localisation.

If the disclosure is removed or weakened, the content owner must correct, withdraw, relabel, or republish the material.

## 6. Stop and escalation conditions

Publication must stop and escalate when:

- the identity or authority of the requester is uncertain;
- consent or lawful basis is unresolved;
- the content imitates a real person in a sensitive context;
- disclosure would materially reduce the intended persuasive effect and the sponsor resists including it;
- the content concerns safety, emergencies, elections, public-interest events, or other high-impact matters;
- provider marking cannot be preserved and no compensating control exists;
- legal, communications, privacy, security, or ethics reviewers disagree;
- testing shows that a reasonable viewer may still believe the content is authentic.

## 7. Evidence

Required evidence should include, as applicable:

- synthetic-media intake record;
- business purpose and intended audience;
- model and provider details;
- prompts, source files, and editing history;
- classification and legal analysis;
- consent or authority documentation;
- approved disclosure wording;
- screenshots or recordings showing placement;
- accessibility and localisation test results;
- technical-marker detection results;
- editorial, legal, privacy, security, and communications approvals;
- publication record and distribution channels;
- monitoring, complaints, corrections, and takedown evidence.

## 8. Audit tests

### Design effectiveness

The auditor should verify that the organisation has controls for:

- identifying synthetic media before release;
- determining deepfake status;
- applying both technical and human-facing transparency;
- reviewing impersonation and voice-cloning risk;
- preserving labels through publication workflows;
- approving exceptions and adapted disclosures;
- correcting or removing misleading content.

### Operating effectiveness

Select a sample of published AI-generated image, audio, and video content and test whether:

1. the content entered the intake process;
2. classification was complete and supportable;
3. disclosure appeared at the appropriate time and location;
4. technical marking was preserved where applicable;
5. human approval occurred before publication;
6. consent and authority were documented for real-person likeness or voice;
7. monitoring detected label loss, complaints, or misuse;
8. corrective actions were timely and complete.

## 9. Metrics

Management should monitor:

- percentage of synthetic-media items reviewed before release;
- percentage with documented deepfake classification;
- percentage with successful technical-marker detection;
- disclosure accessibility pass rate;
- number of impersonation or voice-cloning requests rejected;
- number of downstream label-loss events;
- number and age of unresolved complaints;
- correction and takedown completion time.

## 10. Formal process graphic specification

**Figure 66-1 — Synthetic-media disclosure decision process**

`Content created or altered with AI → realistic depiction test → deepfake classification → exception/adapted-disclosure analysis → technical marking → human-facing disclosure → human approval → publish → monitor preservation → correct or withdraw`

**Human concern callout:**

> “Will I know this is synthetic before I rely on it?”

**Alt text:** A flow diagram shows AI-generated or manipulated media moving through classification, technical marking, visible disclosure, human approval, publication, monitoring, and correction.

## 11. Original workplace-satire illustration concept

**Figure 66-2 — “The Authenticity Committee”**

A corporate team watches a highly realistic synthetic executive announce a major travel-policy change. One employee asks, “Should we tell people he isn’t real?” The project manager replies, “Legal put it in the file name.”

**Concept explained:** A disclosure that exists only in metadata or internal records does not meaningfully inform the affected person.

**Alt text:** Office workers watch a realistic synthetic executive on a screen while a manager points to an obscure file name as proof of disclosure.

## 12. Management questions

- Can a viewer recognise synthetic media before relying on it?
- Are technical markers and visible disclosures both present where required?
- Who can approve use of a real person’s likeness or voice?
- How are artistic or satirical adaptations documented?
- What happens when a platform strips the label or metadata?
- Can GlobalWay quickly correct or remove misleading synthetic content?

## 13. Legal and publication note

This chapter distinguishes binding legal duties from implementation recommendations. Article 50, official Commission guidance, the approved transparency Code of Practice, and any applicable amending or transitional measures must be reverified immediately before publication.

## Official sources

- Regulation (EU) 2024/1689, Article 50: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- European Commission guidelines on Article 50 transparency obligations: https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems
- European Commission overview of AI-generated-content transparency: https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content
- Commission opinion on the Transparency Code of Practice: https://digital-strategy.ec.europa.eu/en/library/commission-opinion-assessment-code-practice-transparency-ai-generated-content
