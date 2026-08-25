# Manual 02 Source Verification and Citation Review Report 01

**Repository:** `Chpmunk31456/GRC-Practical-Manuals`

**Pull request:** [#89](https://github.com/Chpmunk31456/GRC-Practical-Manuals/pull/89)

**Branch:** `build/iso-iec-42001-manual-02-2026`

**Base branch observed:** `maintenance/eu-ai-act-manual-01-2026`

**Starting revision verified:** `9ffdae73e1042430ae3c10e224a4904d23271394`

**Review date:** 2026-08-24

**Controlled language:** English

**Localized drafts checked for factual and link parity:** `es-419`, `pt-BR`

## Executive conclusion

Manual 02 is suitable to remain in draft source review after the source-control corrections documented here. No confirmed material misstatement of a published source, broken external link, direct-equivalence crosswalk, certification guarantee, or substantial reproduction of ISO text was found in the reviewable repository content. The review did identify three Annex A statements whose unconditional wording may overstate applicability, several implementation statements using normative terms, and certification-stage descriptions that require comparison with licensed standards or the selected certification scheme.

The controlled source registry now includes every ISO publication explicitly used in the manual's official-reference set or material integration/certification discussion. Three moved open-source project links were replaced with their current canonical locations. ISO/IEC 42007's status was updated from a generic work-in-progress description to draft international standard status while retaining the critical boundary that it is not a published requirement.

This is a source and citation review, not a conformity assessment, legal opinion, certification decision, or substitute for authorized ISO publications.

## Method and evidence boundary

- Reviewed the complete 32-chapter English Markdown master, both four-part localized source sets, Manual 02 entry documents, the authoritative-source registry, the Manual 02 QA baseline, and repository QA logic.
- Tested all 34 unique HTTPS destinations in the English master for existence, provenance, and current canonical location.
- Checked 21 authoritative source/status records and 18 official tool or project destinations against first-party pages.
- Classified one principal claim bundle per chapter, then separately inventoried normative terms and exact clause/Annex references.
- Used public official metadata and summaries only. The licensed full text of ISO/IEC 42001 and related standards was not available for line-by-line comparison.
- Any conclusion dependent on exact ISO wording, control count, clause strength, Annex applicability, or certification-scheme detail is therefore marked **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION**.

## A. Source registry

### A.1 Controlling and directly cited ISO sources

| Source ID | Official publication/status verified | Manual relevance | Result |
|---|---|---|---|
| `iso-iec-42001-2023` | [ISO/IEC 42001:2023](https://www.iso.org/standard/42001), edition 1, published December 2023 | AIMS requirements | Current; exact official title recorded |
| `iso-iec-42005-2025` | [ISO/IEC 42005:2025](https://www.iso.org/standard/42005), edition 1, published May 2025 | AI system impact assessment | Current; exact official title recorded |
| `iso-iec-42006-2025` | [ISO/IEC 42006:2025](https://www.iso.org/standard/42006), edition 1, published July 2025 | Additional requirements for AIMS audit and certification bodies | Current; exact official title recorded |
| `iso-iec-23894-2023` | [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html), edition 1, published February 2023 | AI risk-management guidance | Current; exact official title recorded |
| `iso-iec-22989-2022` | [ISO/IEC 22989:2022](https://www.iso.org/standard/74296.html), edition 1, published July 2022 | AI concepts and terminology | Current base publication; amendments are under development |
| `iso-iec-23053-2022` | [ISO/IEC 23053:2022](https://www.iso.org/standard/74438.html), edition 1, published 2022 | ML-system framework | Current base publication; amendments are under development |
| `iso-iec-38507-2022` | [ISO/IEC 38507:2022](https://www.iso.org/standard/56641.html), edition 1, published April 2022 | Governance implications of organizational AI use | Current |
| `iso-iec-27001-2022` | [ISO/IEC 27001:2022](https://www.iso.org/standard/27001), edition 3, published October 2022 | Management-system integration reference | Current; generic `ISO 27001` label corrected |
| `iso-iec-27001-2022-amd1-2024` | [ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/standard/88435.html), published February 2024 | Current-edition source control | Current published amendment recorded separately |
| `iso-19011-2026` | [ISO 19011:2026](https://www.iso.org/standard/19011), edition 4, published May 2026 | Management-system audit guidance | Current; exact title capitalization recorded |
| `iso-iec-17021-1-2015` | [ISO/IEC 17021-1:2015](https://www.iso.org/standard/61651.html), edition 1, published June 2015 | General certification-body requirements and Stage 1/Stage 2 context | Published and current, but under systematic review; tracked as supporting, not a final-status QA prerequisite |

### A.2 Developing publications and change watch

The [ISO/IEC JTC 1/SC 42 catalogue](https://committee.iso.org/committee/6794475/x/catalogue/) shows:

- ISO/IEC 42003 remains an approved work item at stage 20.
- ISO/IEC 42007 has advanced to draft international standard status.
- Neither is treated as a published Manual 02 requirement.

ISO/IEC 22989 and ISO/IEC 23053 have amendment work in development. The published base editions remain the sources used by the manual. ISO/IEC 17021-1:2015 is under systematic review, so its metadata has a 30-day review interval.

### A.3 Other official contextual sources

- [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) remains a voluntary framework and is being revised. The manual uses it only as an integration/context reference.
- The [European Commission AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) remains an appropriate official overview. The manual correctly avoids treating ISO/IEC 42001 certification as proof of legal compliance.
- [IAF CertSearch](https://www.iafcertsearch.org/) remains an appropriate certificate-status verification destination. Search results must still be evaluated for entity, scope, certification body, accreditation, dates, and status.

## B. Normative claim review

### B.1 Chapter-level claim classification

The following mutually exclusive classification applies to the principal explanatory claim bundle in each chapter. It is a content-review aid, not a clause-by-clause conformity mapping.

| Classification | Chapters | Count | Assessment |
|---|---:|---:|---|
| Directly supported by public official source descriptions | 1, 9, 24, 29, 30 | 5 | The high-level source purpose or assurance boundary is explicit in an official source |
| Supported with implementation interpretation | 2, 4–8, 10–22, 25, 28 | 21 | Consistent with public source purpose and management-system practice, but detailed strength depends on licensed text |
| Implementation recommendation | 3, 31, 32 | 3 | Practical guidance, laboratory design, templates, and analyst workflow; not represented as verbatim ISO requirements |
| Possibly mischaracterized | 23, 26, 27 | 3 | Lead wording says an Annex A group “requires” an outcome without stating that Annex A control applicability is risk-treatment/SoA-dependent |
| Unsupported | — | 0 | None found at the chapter-lead bundle level |
| Source outdated | — | 0 | No superseded principal requirement source found after correction |

### B.2 Normative-language inventory

The English master contains 39 normative tokens on 38 lines: `must` 15, `required` 6, `requires` 4, `should` 3, `may` 5, and `can` 6. Many are appropriate boundaries or plain-language implementation rules, but the following merit licensed human review because a reader could interpret them as direct ISO obligations:

| Location / wording cue | Review issue | Disposition |
|---|---|---|
| Chapter 23, “Annex A.4 requires visibility…” | Annex A applicability may be conditional through risk treatment and the SoA | **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION** |
| Chapter 26, “Annex A.7 requires governed data…” | Same applicability issue | **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION** |
| Chapter 27, “Annex A.8 requires useful information…” | Same applicability issue | **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION** |
| Chapter 26 graphic alternative text, “Lineage must connect…” | Strong implementation recommendation may read as normative text | Human editor should label as recommended evidence design or verify source strength |
| Chapter 28 supplier graphic alternative text, “Supplier assurance must match…” | Strong implementation recommendation | Human editor should label as risk-based practice or verify source strength |
| Chapter 7 risk/impact comparison, “Must stay connected” / “both must exchange…” | Operational integration recommendation | Human editor should distinguish recommended method from direct requirement |
| Chapter 31 audit-finding explanation, “finding must identify…” | Audit-practice rule; source strength may derive from audit guidance, not ISO/IEC 42001 alone | Verify against authorized ISO 19011 and applicable audit criteria |
| Chapter 31 tool-evidence explanation, “must be scoped…” | Sound evidence practice, but not established here as verbatim normative language | Retain as guidance or relabel explicitly |

No text should be changed solely to weaken an accurate requirement. The accountable human reviewer should compare these passages with the authorized source and decide whether to retain, qualify, or relabel them.

## C. Clause/reference review

The manual references Clauses 4–10; subclauses 6.1.2, 6.1.3, 6.1.4, 6.2, 6.3, 7.1–7.5, 8.1–8.4, 9.1–9.3; Annexes A–D; and Annex A groups A.2–A.10. Public ISO descriptions support the overall AIMS scope, risk/impact, audit, and improvement framing. They do not expose enough licensed text to certify every clause label, obligation verb, control count, or detailed interpretation.

Specific human checks:

1. Verify every chapter-heading clause number and scope against an authorized copy of ISO/IEC 42001:2023.
2. Verify Chapter 20's statement that Annex A contains 38 controls in nine groups.
3. Verify the relationship among Annex A selection, the risk-treatment process, additional controls, exclusions, and the Statement of Applicability.
4. Verify that Annex B–D descriptions preserve their informative/normative status and do not imply equivalence.
5. Verify whether the three “Annex A.x requires” lead statements should instead say the organization evaluates and applies relevant controls through risk treatment and the SoA.

**CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION.**

## D. Certification/conformity review

### D.1 Boundaries found to be appropriately stated

- Certification is described as scoped third-party assessment of the AIMS, not certification of every output or individual AI product.
- The manual states that certification does not guarantee accuracy, fairness, security, legality, safety, or explainability.
- Tools and repository QA are described as evidence support, not automatic conformity.
- Internal audit is not represented as certification.
- ISO/IEC 42006 is correctly framed as applying to bodies auditing and certifying AIMS, rather than as a direct requirement imposed on every organization seeking certification.
- ISO/IEC 42001 certification is not represented as proof of EU AI Act compliance.

### D.2 Items requiring scheme-specific or licensed verification

- Chapter 29 and the glossary describe Stage 1 and Stage 2. The broad distinction is consistent with management-system certification practice, but exact activities, sequencing, sampling, readiness conclusions, and scheme rules must be confirmed against ISO/IEC 17021-1, ISO/IEC 42006, accreditation requirements, and the selected certification body's process.
- Certificate and accreditation verification must use the precise legal entity, AIMS scope, standard/edition, certification body, accreditation, certificate dates, status, and any suspension or withdrawal information.

**CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION.**

## E. Crosswalk review

| Relationship checked | Classification | Finding |
|---|---|---|
| ISO/IEC 42001 ↔ ISO/IEC 27001:2022 | Contextual/structural integration | The manual recommends reuse and mapping of compatible management-system processes; it does not claim control equivalence or dual conformity |
| ISO/IEC 42001 ↔ NIST AI RMF | Contextual | NIST AI RMF is mentioned as an external mapping target; no one-to-one crosswalk is asserted |
| ISO/IEC 42001 ↔ EU AI Act | Contextual/legal boundary | The manual expressly rejects certification-alone proof of legal compliance |
| ISO/IEC 27002:2022 | Not applicable to a current crosswalk | No substantive control mapping or equivalence claim appears in Manual 02 |
| ISO/IEC 27701:2025 | Not applicable to a current crosswalk | No substantive privacy-management mapping appears in Manual 02 |
| ISO/IEC 27005:2022 | Not applicable to a current crosswalk | No substantive risk-method mapping appears in Manual 02 |

No direct-equivalence crosswalk requiring correction was found. Any future crosswalk should classify relationships as direct, partial, contextual, or not applicable; identify edition and scope; and avoid inferring conformity across frameworks.

## F. Citation/link review

### F.1 Results

| Metric | Before correction | After correction |
|---|---:|---:|
| Unique HTTPS destinations in English master | 34 | 34 |
| Current/canonical | 31 | 34 |
| Moved or superseded project destinations | 3 | 0 |
| Confirmed broken destinations | 0 | 0 |

### F.2 Canonical-link corrections

| Project | Previous destination | Current official destination |
|---|---|---|
| Giskard | `github.com/Giskard-AI/giskard` | [Giskard OSS](https://github.com/Giskard-AI/giskard-oss) |
| PyRIT | archived `github.com/Azure/PyRIT` | [microsoft/PyRIT](https://github.com/microsoft/PyRIT) |
| Presidio | moved documentation site | [Presidio documentation](https://presidio.dataprivacystack.org/) |

The same destinations were corrected in the English, `es-419`, and `pt-BR` chapter 30 source material. Remaining tool/project destinations resolved to their current official organization, project, or documentation pages during review.

## G. Copyright review

The repository consistently describes the manual as original educational implementation guidance, instructs readers to obtain authorized standards, and avoids presenting itself as an ISO-authorized translation. No obvious long clause reproduction or confirmed substantial copying was identified in the available material.

Because the licensed full text was unavailable, this is not an exhaustive similarity determination. Before publication, the accountable human reviewer should compare all italicized chapter-lead claims, definitions, table entries that closely track standard terminology, and clause/Annex summaries against authorized copies. Short necessary identifiers and standard titles should remain accurate; extended protected expression should remain paraphrased.

**Licensed-text similarity review remains a human release item.**

## H. Impact assessment

| Area | Impact | Required action/status |
|---|---|---|
| English Markdown master | Source metadata, one integration label, three URLs, and reference list changed | Corrected in this change set |
| `es-419` source | Current-information note, ISO/IEC 27001 label, three URLs, and reference list changed | Fact/link parity corrected; human semantic review remains open |
| `pt-BR` source | Current-information note, ISO/IEC 27001 label, three URLs, and reference list changed | Fact/link parity corrected; human semantic review remains open |
| Source registry and QA baseline | Five cited/integration sources added as required; ISO/IEC 17021-1 added as supporting under review | Corrected in this change set |
| Graphics | No factual or link content required a graphic change | No change |
| English DOCX | Now stale relative to controlled Markdown | Regenerate and complete page/accessibility QA before release |
| Localized DOCX/PDF | Not yet produced | Existing roadmap item; no new artifact created by this review |
| Release readiness | Source/citation corrections are editorial and source-control changes | Not an independent blocker after QA; licensed clause review and localization review remain blockers |

## HUMAN REVIEW QUEUE

1. Compare all Clause 4–10 and Annex A–D descriptions with an authorized ISO/IEC 42001:2023 copy. **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION.**
2. Decide whether Chapters 23, 26, and 27 should qualify “Annex A.x requires” to reflect risk-treatment and Statement-of-Applicability decisions. **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION.**
3. Verify the stated count of 38 Annex A controls in nine groups. **CLAUSE REFERENCE REQUIRES HUMAN VERIFICATION.**
4. Verify Stage 1/Stage 2 and certification-cycle descriptions against authorized ISO/IEC 17021-1:2015, ISO/IEC 42006:2025, the applicable accreditation framework, and the chosen certification scheme.
5. Review the eight normative-language cues listed in B.2 and distinguish direct requirements from implementation recommendations.
6. Complete licensed-text similarity/copyright-boundary review.
7. Complete the existing human semantic and terminology review for `es-419` and `pt-BR`, including the newly localized current-information wording.
8. Regenerate the English DOCX from the corrected Markdown, then rerun page-by-page visual and accessibility QA.

## CODEX HANDOFF TO CHATGPT

- Preserve PR #89 as a draft on `build/iso-iec-42001-manual-02-2026` with base `maintenance/eu-ai-act-manual-01-2026`.
- Do not merge, retarget, or mark the pull request ready as part of this source-review task.
- Treat the three Annex A lead statements, control count, detailed clause interpretations, and Stage 1/Stage 2 wording as human verification items—not as confirmed defects without the licensed sources.
- Next content action: accountable human completes the queue above, then the repository owner regenerates release artifacts and reruns full visual/accessibility QA.
- Next source-watch action: recheck ISO/IEC 42003, ISO/IEC 42007, ISO/IEC 22989 amendments, ISO/IEC 23053 amendments, NIST AI RMF revision status, and ISO/IEC 17021-1 review status on the registry intervals.

RESEARCH QA STATUS: PASS WITH HUMAN VERIFICATION ITEMS REMAINING
