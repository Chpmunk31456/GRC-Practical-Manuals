# NIST CSF 2.0 — Spanish and Brazilian Portuguese Rewrite Standard

**Status:** Active editorial control for the full human-quality rewrite of the NIST CSF 2.0 manual.

## Purpose

This standard governs the replacement of the defective machine-assisted Spanish and Brazilian Portuguese editions. It preserves NIST identifiers, framework meaning, links, document structure, evidence language, and audience accessibility.

## Non-negotiable rules

1. Keep all NIST identifiers unchanged: `GV.OC`, `GV.RM`, `GV.RR`, `GV.PO`, `GV.OV`, `GV.SC`, `ID.AM`, `ID.RA`, `ID.IM`, `PR.AA`, `PR.AT`, `PR.DS`, `PR.PS`, `PR.IR`, `DE.CM`, `DE.AE`, `RS.MA`, `RS.AN`, `RS.CO`, `RS.MI`, `RC.RP`, and `RC.CO`.
2. Keep product names, commands, URLs, code, filenames, and tool names unchanged unless an official localized name exists.
3. Preserve the six official Function names in uppercase English when used as NIST labels: `GOVERN`, `IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND`, `RECOVER`. A localized explanation may follow in parentheses.
4. Preserve `Core`, `Profile`, `Current Profile`, `Target Profile`, `Community Profile`, `Tier`, `Category`, `Subcategory`, `Implementation Example`, `Informative Reference`, and `Quick Start Guide` as defined NIST concepts; translate consistently without changing meaning.
5. Do not translate `Policy` as police/polícia. Use **política**.
6. Do not translate `Tier` as tiro. Use **Nivel de implementación** in Spanish explanatory prose and **Nível de implementação** in Brazilian Portuguese explanatory prose; retain **Tier** when referring to the official NIST label.
7. Do not introduce European Portuguese into the Brazilian Portuguese edition. Use Brazilian spelling and usage: `controle`, `equipe`, `gerenciamento`, `usuário`, `planejamento`, `conformidade`, `cadeia de suprimentos`.
8. Remove all extraction artifacts such as `Silencio`, `TEN`, `TENIDO`, stray squares, malformed table fragments, translated CSS properties, and damaged image markup.
9. Preserve Markdown heading levels, anchors, lists, tables, image paths, alt text, and link destinations.
10. Every rewritten section must be checked against the English source for omissions, additions, altered claims, and terminology drift.

## Spanish terminology

| English source term | Approved Latin American Spanish |
|---|---|
| Cybersecurity Framework | Marco de Ciberseguridad |
| Core | Núcleo |
| Core outcome | resultado del Núcleo |
| Function | Función |
| Category | Categoría |
| Subcategory | Subcategoría |
| Organizational Profile | Perfil Organizacional |
| Current Profile | Perfil Actual |
| Target Profile | Perfil Objetivo |
| Community Profile | Perfil Comunitario |
| Tier | Tier / Nivel de implementación |
| risk appetite | apetito de riesgo |
| risk tolerance | tolerancia al riesgo |
| governance | gobernanza |
| oversight | supervisión |
| policy | política |
| accountability | rendición de cuentas |
| supply chain | cadena de suministro |
| cybersecurity supply chain risk management | gestión del riesgo de ciberseguridad en la cadena de suministro |
| evidence | evidencia |
| finding | hallazgo |
| control testing | pruebas de controles |
| operating effectiveness | eficacia operativa |
| design effectiveness | eficacia del diseño |
| gap | brecha |
| corrective action | acción correctiva |
| retest | volver a probar / nueva prueba |
| stakeholder | parte interesada |
| board | junta directiva |
| executive sponsor | patrocinador ejecutivo |
| open-source tools | herramientas de código abierto |
| junior analyst | analista junior |
| career changer | persona en transición profesional |

## Brazilian Portuguese terminology

| English source term | Approved Brazilian Portuguese |
|---|---|
| Cybersecurity Framework | Framework de Cibersegurança / Marco de Cibersegurança |
| Core | Núcleo |
| Core outcome | resultado do Núcleo |
| Function | Função |
| Category | Categoria |
| Subcategory | Subcategoria |
| Organizational Profile | Perfil Organizacional |
| Current Profile | Perfil Atual |
| Target Profile | Perfil-Alvo |
| Community Profile | Perfil da Comunidade |
| Tier | Tier / Nível de implementação |
| risk appetite | apetite a risco |
| risk tolerance | tolerância a risco |
| governance | governança |
| oversight | supervisão |
| policy | política |
| accountability | responsabilização / prestação de contas |
| supply chain | cadeia de suprimentos |
| cybersecurity supply chain risk management | gerenciamento de riscos de cibersegurança na cadeia de suprimentos |
| evidence | evidência |
| finding | achado |
| control testing | teste de controles |
| operating effectiveness | eficácia operacional |
| design effectiveness | eficácia do desenho |
| gap | lacuna |
| corrective action | ação corretiva |
| retest | novo teste / reteste |
| stakeholder | parte interessada |
| board | conselho de administração |
| executive sponsor | patrocinador executivo |
| open-source tools | ferramentas de código aberto |
| junior analyst | analista júnior |
| career changer | profissional em transição de carreira |

## Required editorial checks per chapter

- Meaning matches the English source.
- No English prose remains except official labels, names, commands, or quotations intentionally retained.
- No mixed Spanish/Portuguese language.
- No European Portuguese in the Brazilian edition.
- NIST concepts and identifiers are preserved.
- Markdown structure and internal links remain valid.
- Tables remain readable and semantically correct.
- Image markup and alt text remain valid.
- Educational, ethical-use, and limitation notices retain their original scope.
- Claims involving dates, versions, quantities, or official NIST positions are verified against the English source and current authoritative references before publication.

## Publication gate

The rewritten Markdown files must be reviewed and approved before DOCX/PDF regeneration. The regenerated DOCX and PDF files must then pass integrity, searchable-text, page-by-page visual, accessibility, link, and metadata checks before pull request #3 can leave draft status.