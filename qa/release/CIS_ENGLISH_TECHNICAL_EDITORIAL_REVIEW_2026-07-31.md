# CIS Controls v8.1 English Master — Technical and Editorial Review

## Candidate

- Repository: `Chpmunk31456/GRC-Practical-Manuals`
- Branch: `production/multilingual-grc-editions`
- Source: `01-foundations/CIS_Controls_v8.1/English_Source_CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`
- Pull request: `#3` — remains draft and unmerged

## Review result

**PASS WITH LICENSING REVIEW ITEM**

The English master passed the configured structural and framework-fact audit after one bounded editorial correction to the Word table-of-contents instruction.

## Verified technical points

The following statements were checked against current official CIS primary sources:

- CIS Controls v8.1 remains the current published Controls edition.
- Version 8.1 is an iterative update to v8 and includes revised asset classes, clarification changes, NIST CSF 2.0 mapping realignment, and the Govern security function.
- The framework contains 18 Controls and 153 Safeguards.
- IG1 contains 56 Safeguards; IG2 adds 74; IG3 adds 23, totaling 153.
- The Controls Assessment Specification includes Safeguard metadata, assumptions, inputs, operations, measures, metrics, and procedure review.
- Framework mappings do not by themselves prove compliance with another requirement.

## Editorial and structural evidence

- All expected Sections 1–30 are present exactly once.
- No configured conversion markers, malformed headings, placeholders, empty Markdown links, or raw separator corruption remain.
- Required framework facts are present.
- The malformed label `True Word contents` was corrected to `Word table of contents`.
- Official CIS references are included in Section 30.5.
- Technical-tool guidance consistently requires authorization, controlled scope, evidence retention, remediation, and retesting.

## Licensing review item

Current CIS terms state conditions relating to attribution, linking to the applicable license, noncommercial redistribution, modified materials, and commercial-use approval. The manual already identifies itself as an independent educational work, attributes CIS trademarks, and directs readers to official CIS resources. However, final public distribution should include an explicit owner review of the applicable CIS licensing terms and the manual's permitted distribution model.

This record does not provide legal advice or licensing certification. No licensing language was changed without an owner decision.

## Remaining gates

- Full visual inspection of generated English DOCX/PDF: not yet completed.
- Accessibility and assistive-technology review: not yet completed.
- Link execution check in generated formats: not yet completed.
- Final licensing/distribution decision: pending owner review at release stage.
- Broader PR #3 merge authorization: not granted.

## Status

The English CIS Markdown master is technically and editorially suitable to proceed to generated-document QA, subject to the documented licensing review item and repository-wide release gates.
