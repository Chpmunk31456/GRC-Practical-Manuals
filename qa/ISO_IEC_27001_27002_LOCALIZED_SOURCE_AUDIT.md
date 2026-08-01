# ISO/IEC 27001 and 27002 Localized Source Audit

## Result

**FAIL-CLOSED**

This deterministic audit identifies structural and known localization defects. It does not replace native-language, standards, legal, accessibility, or page-level review.

## es-419

- Source: `02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`
- Status: **FAIL**
- Missing major sections: [11, 12]
- Duplicate major sections: [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Missing image references: [5, 6, 8]
- Table signals: `{'pipe_rows': 224, 'separator_rows': 16, 'collapsed_rule_rows': 0}`

### Findings

#### known_mistranslations
- Line 105: `[21. Lectura de certificación [30]](#certification-readiness)`
- Line 145: `[25. Laboratorio de Ficción y Cartera [38]](#fictional-laboratory-and-portfolio)`
- Line 143: `[24.2 Valor de los empleadores de habilidades [37]](#skills-employers-value)`
- Line 895: `## 24.2 Valor de los empleadores de habilidades`
- Line 57: `[Uso electrónico y autorizado [2]](#ethical-and-authorized-use)`
- Line 315: `TEN **2024 enmienda:** Determinar explícitamente si el cambio climático es relevante para el contexto del SIV y reconocer que las partes interesadas pertinentes pueden tener requisitos relacionados con el clima. Mantenga la evidencia del ra`

## pt-BR

- Source: `02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`
- Status: **FAIL**
- Missing major sections: none
- Duplicate major sections: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Missing image references: none
- Table signals: `{'pipe_rows': 0, 'separator_rows': 36, 'collapsed_rule_rows': 35}`

### Findings

#### malformed_emphasis
- Line 3: `** SÉRIES PRÁTICAS DE CIBERSegurança, PRIVACIDADE E CONFORMIDADE`

#### untranslated_english_text
- Line 258: `![The SoA registra seleção de controle fundamentada e status de implementação.](media/image3.png)`

#### known_mistranslations
- Line 9: `* Um manual de trabalho para gerentes, analistas júnior, estudantes, mudadores de carreira, auditores internos e equipes de segurança*`

## Release implication

Any FAIL blocks localized DOCX/PDF rebuild and publication-readiness claims until the source defects are repaired and this audit passes at the exact candidate SHA.
