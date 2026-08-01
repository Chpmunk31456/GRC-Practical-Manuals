# ISO/IEC 27001 and 27002 Localized Source Audit

## Result

**FAIL-CLOSED**

This deterministic audit identifies structural and known localization defects. It does not replace native-language, standards, legal, accessibility, or page-level review.

## es-419

- Source: `02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`
- Status: **FAIL**
- Missing major sections: [6]
- Duplicate major sections: none
- Missing image references: none
- Table signals: `{'pipe_rows': 304, 'separator_rows': 36, 'collapsed_rule_rows': 0, 'malformed_separator_rows': 0}`
- Table blockers: none

### Findings

#### untranslated_english_control_text
- Line 1050: ` Conformity | Fulfillment of a requirement.`
- Line 1050: ` Conformity | Fulfillment of a requirement.`

#### known_mistranslations
- Line 50: `Contenido de la palabra:** Este documento contiene un campo de mesa de contenido de Word nativo y una guía de capítulo verificada. Después de editar, haga clic con el botón derecho en el contenido y elija el campo de actualización, luego ac`

## pt-BR

- Source: `02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`
- Status: **FAIL**
- Missing major sections: none
- Duplicate major sections: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- Missing image references: none
- Table signals: `{'pipe_rows': 0, 'separator_rows': 36, 'collapsed_rule_rows': 35, 'malformed_separator_rows': 0}`
- Table blockers: ['collapsed_rule_rows=35', 'pipe_rows=0']

### Findings

#### malformed_emphasis
- Line 3: `** SÉRIES PRÁTICAS DE CIBERSegurança, PRIVACIDADE E CONFORMIDADE`

#### untranslated_english_text
- Line 258: `![The SoA registra seleção de controle fundamentada e status de implementação.](media/image3.png)`
- Line 289: `**Documento ou registro** **Purpose** **Controle**`
- Line 702: `. **Ferramenta** . **Purpose** . **Possível suporte** .`

#### known_mistranslations
- Line 9: `* Um manual de trabalho para gerentes, analistas júnior, estudantes, mudadores de carreira, auditores internos e equipes de segurança*`

## Release implication

Any FAIL blocks localized DOCX/PDF rebuild and publication-readiness claims until the source defects are repaired and this audit passes at the exact candidate SHA.
