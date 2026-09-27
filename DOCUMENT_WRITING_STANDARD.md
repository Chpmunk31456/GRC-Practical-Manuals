# Controlled Document Writing Standard

This standard governs editorial changes to the GRC Practical Manuals and is intended to be reusable for future professional documents in this repository.

## Objective

Write clear, natural, professional material that reads as if it was prepared and reviewed by an experienced practitioner. Improve grammar, spelling, punctuation, readability, consistency, and flow without changing the underlying legal, regulatory, technical, audit, security, risk, or governance meaning.

Editorial improvement is never authority to change a fact, source, citation, control requirement, legal interpretation, standard identifier, version, date, metric, scope statement, or publication status.

## Source-of-truth rule

For controlled manuals:

1. identify the controlled source before editing;
2. edit the controlled source first;
3. preserve authoritative citations and source boundaries;
4. rerun the manual's existing structural, legal, security, accessibility, localization, document, and publication QA;
5. regenerate derivative DOCX/PDF artifacts from the approved source rather than hand-editing generated artifacts.

Where English is the controlled source, approved substantive English changes must be propagated through the established localization process to neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) as applicable.

## Human professional voice

Prefer:

- direct sentences with clear subjects and actions;
- concrete implementation language;
- specific evidence and control language instead of promotional adjectives;
- natural variation in sentence length;
- accurate governance, risk, compliance, cybersecurity, privacy, audit, AI, OT/ICS, cloud, and resilience terminology;
- plain-language explanations before unnecessary specialist jargon;
- active voice when it improves accountability or clarity;
- explicit owners, triggers, evidence, tests, exceptions, and decisions when describing controls;
- cautious language when the underlying source or interpretation is conditional.

Avoid:

- generic AI-sounding phrases;
- inflated claims;
- repetitive introductions or conclusions;
- keyword stuffing;
- unnecessary synonyms for the same technical term;
- vague claims such as "best-in-class," "world-class," or "game-changing";
- filler such as "it is important to note" when the point can be stated directly;
- changing a defined legal or technical term merely to make prose sound different.

## Grammar and mechanics

Use correct grammar, spelling, punctuation, capitalization, and terminology for the document's controlled locale.

### English

Default editorial locale: professional U.S. English unless a specific manual or authoritative source requires another convention.

### Spanish

Use neutral professional Latin American Spanish (`es-419`) for controlled Spanish editions. Do not translate technical, regulatory, or legal terminology literally when an established Spanish-language term is available.

### Portuguese

Use professional Brazilian Portuguese (`pt-BR`) for controlled Portuguese editions. Preserve established Brazilian regulatory, technical, and professional terminology.

## Regulatory and standards language

Do not automatically rewrite:

- quotations from primary or authoritative sources;
- regulation, statute, rule, article, annex, section, control, requirement, or clause identifiers;
- official names of standards, frameworks, agencies, regulators, laws, certifications, or publications;
- exact source titles;
- DOI values, URLs, hashes, version identifiers, file names, code, commands, schemas, or machine-readable data;
- approved defined terms where wording consistency carries legal, audit, or control significance.

When an editorial tool flags one of these items, review it manually rather than accepting the proposed change automatically.

## Evidence and certainty

Match the strength of the sentence to the strength of the evidence.

Use distinctions such as:

- `requires` when an authoritative requirement actually requires it;
- `should` for a controlled recommendation or recognized good practice;
- `may` or `can` for options and capabilities;
- `typically` or `commonly` when describing patterns that are not universal.

Do not turn guidance into a legal requirement or weaken a mandatory requirement into optional guidance.

Do not promise compliance, certification, audit success, security, safety, privacy, or risk elimination.

## Controls and procedures

When practical, use a consistent evidence-oriented pattern:

**Requirement or Risk → Control Objective → Control Activity → Owner → Trigger/Frequency → Evidence → Test Procedure → Exception → Remediation → Residual-Risk Decision**

Not every paragraph needs every element, but control language should make accountability and evidence clear.

## Tables, diagrams, and structured material

Editorial changes must preserve:

- table meaning and header relationships;
- control mappings;
- crosswalk relationships;
- numbering and references;
- figure meaning and accessible descriptions;
- diagram labels;
- links between narrative, evidence, and test procedures.

Do not improve prose by collapsing distinctions that a table, crosswalk, or diagram intentionally preserves.

## AI-assisted editing

AI may assist with drafting, proofreading, consistency checking, localization support, and editorial suggestions. AI-assisted changes remain subject to the repository's controlled-source, source-verification, semantic-review, accessibility, security, and release controls.

Humanization tools are editorial aids only. They are not sources of facts and must never be allowed to invent evidence or silently change technical meaning.

## Automated writing QA

The repository writing-quality layer uses:

- local deterministic checks for repeated words, generic phrasing, and readability signals;
- local LanguageTool for grammar, spelling, punctuation, and usage;
- Vale for markup-aware style checks;
- an optional English editorial profile based on pinned Microsoft and proselint Vale packages;
- manual-specific end-to-end gates for source/localization/publication parity where a controlled publication package exists.

LanguageTool is local-first. Controlled manual text must not be sent to a public grammar API by repository automation.

Automated findings are triage signals. A tool suggestion does not override authoritative wording, technical terminology, citations, controlled translations, or professional judgment.

## End-to-end controlled publication validation

A controlled publication gate must validate the complete chain rather than only the source Markdown. For each supported locale it should verify, at minimum:

1. controlled source inventory and expected chapter/section structure;
2. protected framework identifiers and terminology;
3. localization-review evidence and semantic parity controls;
4. generated DOCX package integrity;
5. generated PDF file integrity;
6. publication-report and checksum agreement with the exact artifacts;
7. fail-closed release language and human-approval boundaries.

The gate must be non-destructive. It reports drift or stale artifacts; it does not silently regenerate or rewrite a controlled publication package.

## Ongoing maintenance

Writing and publication QA is maintained as a production control, not a one-time cleanup. The repository should:

- run the end-to-end gate on relevant pull requests;
- run a scheduled full maintenance check even when no writing pull request is open;
- pin external CI actions and downloaded tooling;
- checksum downloaded grammar tooling;
- compile-test publication generators and QA scripts;
- keep locale policies and terminology under version control;
- treat new false positives, terminology exceptions, and localization defects as controlled policy changes;
- require regenerated artifacts and refreshed hashes after approved source changes.

## Existing manuals

Existing manuals are improved in controlled batches rather than by repository-wide automatic rewriting. For each batch:

1. audit the controlled source;
2. separate true grammar/style defects from technical false positives;
3. make source-preserving edits;
4. rerun applicable manual QA;
5. propagate approved changes to controlled localizations;
6. regenerate derived documents;
7. complete semantic and visual review where required;
8. run the applicable source-to-publication integrity gate;
9. merge through the repository's normal controlled process.

This prevents an editorial cleanup from becoming an uncontrolled substantive revision.

## Future documents

New professional documents should use this standard from the first draft. Before release:

- run the writing-quality checker;
- resolve blocking grammar issues;
- review style warnings in context;
- verify sources and factual claims;
- confirm terminology and localization;
- run document-specific QA;
- regenerate and verify final DOCX/PDF artifacts where applicable;
- visually review final rendered artifacts;
- preserve the exact release evidence and hashes used for approval.

The target is not "perfectly polished AI text." The target is accurate, useful, human professional writing that can withstand technical, regulatory, editorial, localization, and publication review.
