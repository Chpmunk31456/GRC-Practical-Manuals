# NIST CSF 2.0 Multilingual QA Findings

**Review scope:** Latin American Spanish and Brazilian Portuguese Markdown source editions

**Review status:** Publication-blocking defects identified

**Disposition:** Do not mark these editions final. Do not merge Pull Request #3 until the defects are corrected and the regenerated DOCX/PDF files are revalidated.

## Spanish edition

File reviewed:

`01-foundations/NIST_CSF_2/Espanol/NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Espanol_v1.0.md`

### Publication-blocking findings

- Major portions of the cover, notices, navigation, function names, and category labels remain in English.
- Machine mistranslations materially alter meaning, including:
  - `Tiros` for CSF Tiers.
  - `Policía (GV.PO)` for Policy.
  - `Función del PROTECTO` for the PROTECT function.
  - `Priorización de la computación` for gap prioritization.
  - `Uso electrónico y autorizado` for ethical and authorized use.
- Stray generated text such as `Silencio.` appears in the document.
- The phrase describing the Word table of contents is malformed (`Contenido de la palabra`).
- Mixed-language sentences remain, including the legal/privacy/safety review sentence.
- Several table-of-contents labels remain untranslated, producing inconsistent terminology and poor usability.
- Markdown/anchor formatting contains malformed spacing and duplicated nested links.

### Required remediation

- Perform a full professional Latin American Spanish rewrite from the authoritative English source.
- Apply a controlled terminology glossary for NIST CSF 2.0 functions, categories, profiles, tiers, evidence, governance, risk, and incident response.
- Remove all stray machine-output text.
- Rebuild the table of contents and validate every internal link.
- Regenerate DOCX and PDF files only after the corrected Markdown passes language review.

## Brazilian Portuguese edition

File reviewed:

`01-foundations/NIST_CSF_2/Portugues_BR/NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`

### Publication-blocking findings

- The cover contains malformed capitalization, spacing, and mixed languages, including `CIBERSegurança`, `COMPLIANÇA`, `Framework`, and `Práctica`.
- Multiple phrases are unnatural or incorrect Brazilian Portuguese, including:
  - `mudadores de carreira`.
  - `qualificadas legais`.
  - `metodologia-primeira abordagem`.
  - `Conteúdo verdadeiro da palavra`.
  - `Função do Governo` for the NIST GOVERN function.
  - `Análise Incidental` for incident analysis.
  - `Língua de conclusão` for conclusion language.
- European Portuguese terminology appears throughout (`cadeia de abastecimento`, `controlo`, `monitorização`, `âmbito`, `elementos de prova`), conflicting with the required Brazilian Portuguese edition.
- Some headings remain in English, including `Oversight`, `IDENTIFY`, `DETECT`, `CSF Tiers`, and `CSF Work`.
- One table-of-contents item is missing its title and displays only `[27]`.
- Stray horizontal rules and malformed Markdown headings are present.
- Internal links and duplicated nested anchors require validation.

### Required remediation

- Perform a full Brazilian Portuguese rewrite from the authoritative English source.
- Standardize terminology to Brazilian usage, including `cadeia de suprimentos`, `controle`, `monitoramento`, `escopo`, and `evidências` where contextually appropriate.
- Preserve official NIST function names consistently, preferably with a controlled bilingual convention where needed.
- Repair headings, Markdown, table of contents, and internal links.
- Regenerate DOCX and PDF files only after the corrected Markdown passes language review.

## QA conclusion

Automated file generation and package-integrity checks succeeded, but the NIST CSF 2.0 Spanish and Brazilian Portuguese editions fail human language and terminology QA. This confirms that automated generation success is not sufficient for publication approval.

The next corrective step is to replace both machine-generated translations with reviewed language editions, then regenerate and perform page-by-page DOCX/PDF inspection, accessibility checks, and factual verification.
