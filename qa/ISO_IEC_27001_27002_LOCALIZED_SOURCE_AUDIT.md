# ISO/IEC 27001 and 27002 Localized Source Audit

## Result

**FAIL-CLOSED**

This deterministic audit identifies structural and known localization defects. It does not replace native-language, standards, legal, accessibility, or page-level review.

## es-419

- Source: `02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`
- Status: **FAIL**
- Missing major sections: [2, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19, 22, 25, 27]
- Duplicate major sections: none
- Missing image references: [2, 5, 6, 8]
- Table signals: `{'pipe_rows': 239, 'separator_rows': 15, 'collapsed_rule_rows': 0}`

### Findings

#### malformed_html_or_image_markup
- Line 187: `لimg src="media/image1.png" style="width:6.15in;height:3.39605in" alt="Context and risk drive planning, implementation, evaluation, and improvement." /`
- Line 236: `El estilo "png"="width:6.15in;height:3.39605in" alt="Los dueños de Risk evalúan escenarios, tratamiento y riesgo residual utilizando criterios definidos".`

#### placeholder_or_injected_text
- Line 192: `|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ La vida eterna... |`
- Line 378: `|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------`
- Line 590: `La vida eterna---------------------------------------------------------------------- La vida--`
- Line 196: `| ISO/IEC 27005:2022 Silencioso Guía para la gestión del riesgo de seguridad de la información | Orientación de apoyo, no el estándar de certificación 27001`
- Line 224: `Silencioso ** Prueba de la encuesta**`
- Line 274: `| **Control** Silencioso ** Aplicable** |`
- Line 292: `Silencioso | Establece dirección y compromisos`
- Line 349: `tención 6.3 Silencioso Plan ISMS cambia para que se tengan en cuenta sus propósitos, consecuencias, recursos, responsabilidades e integridad del sistema. tención Confirme la propiedad, alcance, método, aprobación, pruebas de funcionamiento,`
- Line 633: `Silencioso Conformidad | La evidencia es compatible con los criterios`
- Line 705: `tención SimpleRisk Community Silencioso www.simplerisk.com`
- Line 707: `Silencioso osquery | www.osquery.io | Inventario y consultas`
- Line 708: `| OpenSCAP Silencioso www.open-scap.org Evaluación de la configuración de Linux |`
- Line 863: `Silencioso Certificación | ¿Son las reclamaciones alcances, actuales y compatibles? Verde / Amarillo / Rojo`
- Line 948: `Silencioso Declaración de aplicabilidad Silencioso`
- Line 966: `| 23–25 | Noconformidad, causa raíz, acción correctiva, mejora Silencioso Dos registros de hallazgo y acción correctiva`
- Line 1062: `Silencioso Conformity | Fulfillment of a requirement.`
- Line 1068: `| Noconformidad Silencioso para cumplir con un requisito. |`
- Line 1070: `Silencioso propietario | Persona o entidad responsable y autorizado para gestionar un riesgo.`
- Line 1071: `| SoA Silencioso Declaración de Aplicabilidad. |`
- Line 1079: `Silencioso en la auditoría`
- Line 1080: `Silencioso Certificación | 21 |`
- Line 1085: `Silencioso analista junior`
- Line 1086: `Silencioso examen de la gestión`
- Line 1089: `Silencioso evaluación y tratamiento de los riesgos`
- Line 1090: `Silencioso en la vida útil 2, 6`
- Line 1091: `Silencioso Declaración de aplicabilidad`
- Line 16: `|. |`
- Line 53: `|. |`
- Line 225: `|. |`
- Line 275: `|. |`
- Line 307: `|. |`
- Line 412: `|. |`
- Line 470: `|. |`
- Line 492: `|. |`
- Line 516: `|. |`
- Line 560: `|. |`
- Line 583: `|. |`
- Line 643: `|. |`
- Line 720: `|. |`
- Line 922: `|. |`
- Line 1044: `|. |`
- Line 1109: `|. |`

#### malformed_markdown_links
- Line 59: `[Uso electrónico y autorizado [2] (#ethical-and-authorized-use)](#ethical-and-authorized-use)`
- Line 61: `[Prefacio [3] (#preface)](#preface)`
- Line 81: `[8. Cláusula 6 — Planificación [14] (#clause-6-planning)] (#clause-6-planning)`
- Line 85: `[10. Cláusula 8 — Operación [16] (#clause-8-operation)] (#clause-8-operation)`
- Line 149: `[26. Plan de aprendizaje de 30 días [39] (#thirty-day-learning-plan)](#thirty-day-learning-plan)`
- Line 57: `[Notificación de publicación y uso [2](#publication-and-use-notice)](#publication-and-use-notice)`
- Line 59: `[Uso electrónico y autorizado [2] (#ethical-and-authorized-use)](#ethical-and-authorized-use)`
- Line 61: `[Prefacio [3] (#preface)](#preface)`
- Line 63: `[Cómo utilizar este manual [4](#how-to-use-this-manual)](#how-to-use-this-manual)`
- Line 65: `[Tabla de contenidos [4](#table-of-contents)](#table-of-contents)`
- Line 67: `[1. ISO/IEC 27001 y 27002 Foundations [7](#isoiec-27001-and-27002-foundations)](#isoiec-27001-and-27002-foundations)`
- Line 69: `[2. ISMS Scope and Interested Parties [8](#isms-scope-and-interested-parties)](#isms-scope-and-interested-parties)`
- Line 71: `[3. Evaluación del riesgo y tratamiento del riesgo [9](#risk-assessment-and-risk-treatment)](#risk-assessment-and-risk-treatment)`
- Line 73: `[4. Declaración de aplicabilidad [10](#statement-of-applicability)](#statement-of-applicability)`
- Line 75: `[5. Documentación y pruebas [11](#documentation-and-evidence)](#documentation-and-evidence)`
- Line 77: `[6. Cláusula 4 — Contexto de la organización [12](#clause-4-context-of-the-organization)](#clause-4-context-of-the-organization)`
- Line 79: `[7. Cláusula 5 — Liderazgo [13](#clause-5-leadership)](#clause-5-leadership)`
- Line 83: `[9. Cláusula 7 - Apoyo [15](#clause-7-support)](#clause-7-support)`
- Line 87: `[11. Cláusula 9 — Evaluación del desempeño [17](#clause-9-performance-evaluation)](#clause-9-performance-evaluation)`
- Line 89: `[12. Cláusula 10 — Mejora [18](#clause-10-improvement)](#clause-10-improvement)`
- Line 91: `[13. Anexo A 5 Controles de organización [19](#annex-a-5-organizational-controls)](#annex-a-5-organizational-controls)`
- Line 93: `[14. Anexo A 6 Controles de personas [22](#annex-a-6-people-controls)](#annex-a-6-people-controls)`
- Line 95: `[15. Anexo A 7 Controles físicos [23](#annex-a-7-physical-controls)](#annex-a-7-physical-controls)`
- Line 97: `[16. Anexo A 8 Controles tecnológicos [24](#annex-a-8-technological-controls)](#annex-a-8-technological-controls)`
- Line 99: `[17. Implementing Controls with ISO/IEC 27002 [26](#implementing-controls-with-isoiec-27002)](#implementing-controls-with-isoiec-27002)`
- Line 101: `[18. Pruebas de medición y control [27](#metrics-and-control-testing)](#metrics-and-control-testing)`
- Line 103: `[19. Auditoría interna [28](#internal-audit)](#internal-audit)`
- Line 105: `[20. Management Review and Corrective Action [29](#management-review-and-corrective-action)](#management-review-and-corrective-action)`
- Line 107: `[21. Lectura de certificación [30](#certification-readiness)](#certification-readiness)`
- Line 109: `[22. Herramientas de código abierto [31](#open-source-tools)](#open-source-tools)`
- Line 111: `[22.1 Auxiliar de CISO [31](#ciso-assistant)](#ciso-assistant)`
- Line 113: `[22.2 Comunidad SimpleRisk [31](#simplerisk-community)](#simplerisk-community)`
- Line 115: `[22.3 Wazuh [31](#wazuh)](#wazuh)`
- Line 117: `[22.4 osquery [32](#osquery)](#osquery)`
- Line 119: `[22.5 OpenSCAP [32](#openscap)](#openscap)`
- Line 121: `[22.6 Greenbone Community Edition [32](#greenbone-community-edition)](#greenbone-community-edition)`
- Line 123: `[22.7 Nmap [32](#nmap)](#nmap)`
- Line 125: `[22.8 Trivy [32](#trivy)](#trivy)`
- Line 127: `[22.9 OWASP ZAP [33](#owasp-zap)](#owasp-zap)`
- Line 129: `[22.10 Keycloak [33](#keycloak)](#keycloak)`
- Line 131: `[22.11 DefectDojo [33](#defectdojo)](#defectdojo)`
- Line 133: `[22.12 AIDE [33](#aide)](#aide)`
- Line 135: `[22.13 Lynis [33](#lynis)](#lynis)`
- Line 137: `[22.14 Agente de política abierta [33](#open-policy-agent)](#open-policy-agent)`
- Line 139: `[23. Manual del SGSI para gerentes [35](#managers-isms-playbook)](#managers-isms-playbook)`
- Line 141: `[24. Guía de la carrera de analista junior [36](#junior-analyst-career-guide)](#junior-analyst-career-guide)`
- Line 143: `[24.1 Trabajo junior típico [36](#typical-junior-work)](#typical-junior-work)`
- Line 145: `[24.2 Valor de los empleadores de habilidades [37](#skills-employers-value)](#skills-employers-value)`
- Line 147: `[25. Laboratorio de Ficción y Cartera [38](#fictional-laboratory-and-portfolio)](#fictional-laboratory-and-portfolio)`
- Line 149: `[26. Plan de aprendizaje de 30 días [39] (#thirty-day-learning-plan)](#thirty-day-learning-plan)`
- Line 151: `[27. Preparación de entrevistas [40](#interview-preparation)](#interview-preparation)`
- Line 153: `[27.1 ¿Qué es un ISMS? [40](#what-is-an-isms)](#what-is-an-isms)`
- Line 155: `[27.2 ISO 27001 versus 27002? [40](#iso-27001-versus-27002)](#iso-27001-versus-27002)`
- Line 157: `[27.3 ¿Cuál es el SoA? [40](#what-is-the-soa)](#what-is-the-soa)`
- Line 159: `[27.4 ¿Todos los controles del anexo A son obligatorios? [40](#are-all-annex-a-controls-mandatory)](#are-all-annex-a-controls-mandatory)`
- Line 161: `[27.5 ¿Cómo se prueba un control? [40](#how-do-you-test-a-control)](#how-do-you-test-a-control)`
- Line 163: `[27.6 ¿Qué es una no conformidad? [40](#what-is-a-nonconformity)](#what-is-a-nonconformity)`
- Line 165: `[27.7 ¿Qué cambió en 2024? [40](#what-changed-in-2024)](#what-changed-in-2024)`
- Line 167: `[27.8 ¿Qué puede concluir un analista junior con seguridad? [40](#what-can-a-junior-analyst-safely-conclude)](#what-can-a-junior-analyst-safely-conclude)`
- Line 169: `[27.9 Preguntas para hacer al empleador [40](#questions-to-ask-the-employer)](#questions-to-ask-the-employer)`
- Line 171: `[28. Plantillas, Glosario, Índice y Referencias [42](#templates-glossary-index-and-references)](#templates-glossary-index-and-references)`
- Line 173: `[28.1 Registro mínimo de riesgo [42](#minimal-risk-record)](#minimal-risk-record)`
- Line 175: `[28.2 Documentos de prueba de control [42](#control-test-workpaper)](#control-test-workpaper)`
- Line 177: `[28.3 Glosario [42](#glossary)](#glossary)`
- Line 179: `[28.4 Índice de asunto [43](#subject-index)](#subject-index)`
- Line 181: `[28.5 Referencias oficiales [43](#official-references)](#official-references)`

#### untranslated_english_headings
- Line 18: `# Publication and Use Notice`

#### known_mistranslations
- Line 107: `[21. Lectura de certificación [30](#certification-readiness)](#certification-readiness)`
- Line 147: `[25. Laboratorio de Ficción y Cartera [38](#fictional-laboratory-and-portfolio)](#fictional-laboratory-and-portfolio)`
- Line 145: `[24.2 Valor de los empleadores de habilidades [37](#skills-employers-value)](#skills-employers-value)`
- Line 905: `## 24.2 Valor de los empleadores de habilidades`
- Line 59: `[Uso electrónico y autorizado [2] (#ethical-and-authorized-use)](#ethical-and-authorized-use)`
- Line 52: `Contenido de la palabra:** Este documento contiene un campo de mesa de contenido de Word nativo y una guía de capítulo verificada. Después de editar, haga clic con el botón derecho en el contenido y elija el campo de actualización, luego ac`
- Line 218: `- Considerar si el cambio climático es relevante para la eficacia del SIV y si las partes interesadas tienen requisitos relacionados con el clima; documentar el razonamiento.`
- Line 318: `TEN **2024 enmienda:** Determinar explícitamente si el cambio climático es relevante para el contexto del SIV y reconocer que las partes interesadas pertinentes pueden tener requisitos relacionados con el clima. Mantenga la evidencia del ra`
- Line 200: `- En el anexo A se enumeran 93 controles de referencia en cuatro temas: 37 orgánicos, 8 personas, 14 físicos y 34 tecnológicos.`

## pt-BR

- Source: `02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`
- Status: **FAIL**
- Missing major sections: [2, 16]
- Duplicate major sections: none
- Missing image references: none
- Table signals: `{'pipe_rows': 0, 'separator_rows': 36, 'collapsed_rule_rows': 35}`

### Findings

#### malformed_markdown_links
- Line 157: `[27.3 O que é o SoA? [40] (#what-is-the-soa)] (#what-is-the-soa)`
- Line 165: `[27.7 O que mudou em 2024? [40] (#what-changed-in-2024)] (#what-changed-in-2024)`
- Line 57: `[Comunicação de publicação e utilização [2](#publication-and-use-notice)](#publication-and-use-notice)`
- Line 59: `[Utilização ética e autorizada [2](#ethical-and-authorized-use)](#ethical-and-authorized-use)`
- Line 61: `[Prefácio [3](#preface)](#preface)`
- Line 63: `[Como usar este manual [4](#how-to-use-this-manual)](#how-to-use-this-manual)`
- Line 65: `[Quadro de conteúdos [4](#table-of-contents)](#table-of-contents)`
- Line 67: `[1. ISO/IEC 27001 e 27002 Fundações [7](#isoiec-27001-and-27002-foundations)](#isoiec-27001-and-27002-foundations)`
- Line 69: `[2. Âmbito de aplicação do ISMS e partes interessadas [8](#isms-scope-and-interested-parties)](#isms-scope-and-interested-parties)`
- Line 71: `[3. Avaliação dos riscos e tratamento dos riscos [9](#risk-assessment-and-risk-treatment)](#risk-assessment-and-risk-treatment)`
- Line 73: `[4. Declaração de aplicabilidade [10](#statement-of-applicability)](#statement-of-applicability)`
- Line 75: `[5. Documentação e provas [11](#documentation-and-evidence)](#documentation-and-evidence)`
- Line 77: `[6. Cláusula 4 — Contexto da organização [12](#clause-4-context-of-the-organization)](#clause-4-context-of-the-organization)`
- Line 79: `[7. Cláusula 5 — Liderança [13](#clause-5-leadership)](#clause-5-leadership)`
- Line 81: `[8. Cláusula 6 — Planeamento [14](#clause-6-planning)](#clause-6-planning)`
- Line 83: `[9. Cláusula 7 — Apoio [15](#clause-7-support)](#clause-7-support)`
- Line 85: `[10. Cláusula 8 — Operação [16](#clause-8-operation)](#clause-8-operation)`
- Line 87: `[11. Cláusula 9 — Avaliação do desempenho [17](#clause-9-performance-evaluation)](#clause-9-performance-evaluation)`
- Line 89: `[12. Cláusula 10 — Melhoria [18](#clause-10-improvement)](#clause-10-improvement)`
- Line 91: `[13. Anexo A 5 Controlos organizacionais [19](#annex-a-5-organizational-controls)](#annex-a-5-organizational-controls)`
- Line 93: `[14) Anexo A 6 Pessoas que controlam [22](#annex-a-6-people-controls)](#annex-a-6-people-controls)`
- Line 95: `[15. Anexo A 7 Controlos físicos [23](#annex-a-7-physical-controls)](#annex-a-7-physical-controls)`
- Line 97: `[16. Anexo A 8 Controlos tecnológicos [24](#annex-a-8-technological-controls)](#annex-a-8-technological-controls)`
- Line 99: `[17. Controlos de execução com ISO/IEC 27002 [26](#implementing-controls-with-isoiec-27002)](#implementing-controls-with-isoiec-27002)`
- Line 101: `[18. Testes Métricos e de Controlo [27](#metrics-and-control-testing)](#metrics-and-control-testing)`
- Line 103: `[19. Auditoria Interna [28](#internal-audit)](#internal-audit)`
- Line 105: `[20. Revisão de gestão e ação corretiva [29](#management-review-and-corrective-action)](#management-review-and-corrective-action)`
- Line 107: `[21. Preparação da certificação [30](#certification-readiness)](#certification-readiness)`
- Line 109: `[22. Ferramentas de Código Aberto [31](#open-source-tools)](#open-source-tools)`
- Line 111: `[22.1 Assistente CISO [31](#ciso-assistant)](#ciso-assistant)`
- Line 113: `[22.2 Comunidade SimpleRisk [31](#simplerisk-community)](#simplerisk-community)`
- Line 115: `[22.3 Wazuh [31](#wazuh)](#wazuh)`
- Line 117: `[22,4 osquery [32](#osquery)](#osquery)`
- Line 119: `[22.5 OpenSCAP [32](#openscap)](#openscap)`
- Line 121: `[22.6 Greenbone Community Edition [32](#greenbone-community-edition)](#greenbone-community-edition)`
- Line 123: `[22,7 Nmap [32](#nmap)](#nmap)`
- Line 125: `[22.8 Trivy [32](#trivy)](#trivy)`
- Line 127: `[22,9 OWASP ZAP [33](#owasp-zap)](#owasp-zap)`
- Line 129: `[22.10 Keycloak [33](#keycloak)](#keycloak)`
- Line 131: `[22.11 DefectDojo [33](#defectdojo)](#defectdojo)`
- Line 133: `[22,12 AIDE [33](#aide)](#aide)`
- Line 135: `[22.13 Lynis [33](#lynis)](#lynis)`
- Line 137: `[22.14 Agente de política aberta [33](#open-policy-agent)](#open-policy-agent)`
- Line 139: `[23. Manual do SGSI para gerentes [35](#managers-isms-playbook)](#managers-isms-playbook)`
- Line 141: `[24. Guia de carreira do analista júnior [36](#junior-analyst-career-guide)](#junior-analyst-career-guide)`
- Line 143: `[24,1 Trabalho júnior típico [36](#typical-junior-work)](#typical-junior-work)`
- Line 145: `[24,2 Valor dos empregadores de competências [37](#skills-employers-value)](#skills-employers-value)`
- Line 147: `[25. Laboratório Fictício e Portfólio [38](#fictional-laboratory-and-portfolio)](#fictional-laboratory-and-portfolio)`
- Line 149: `[26. Plano de aprendizagem de trinta dias [39](#thirty-day-learning-plan)](#thirty-day-learning-plan)`
- Line 151: `[27. Preparação da entrevista [40](#interview-preparation)](#interview-preparation)`
- Line 153: `[27.1 O que é um ISMS? [40](#what-is-an-isms)](#what-is-an-isms)`
- Line 155: `[27,2 ISO 27001 versus 27002? [40](#iso-27001-versus-27002)](#iso-27001-versus-27002)`
- Line 159: `[27.4 Todos os controlos do anexo A são obrigatórios? [40](#are-all-annex-a-controls-mandatory)](#are-all-annex-a-controls-mandatory)`
- Line 161: `[27.5 Como se testa um controlo? [40](#how-do-you-test-a-control)](#how-do-you-test-a-control)`
- Line 163: `[27.6 O que é uma não conformidade? [40](#what-is-a-nonconformity)](#what-is-a-nonconformity)`
- Line 167: `[27.8 O que pode um analista júnior concluir com segurança? [40](#what-can-a-junior-analyst-safely-conclude)](#what-can-a-junior-analyst-safely-conclude)`
- Line 169: `[27.9 Perguntas ao empregador [40](#questions-to-ask-the-employer)](#questions-to-ask-the-employer)`
- Line 171: `[28. Modelos, Glossário, Índice e Referências [42](#templates-glossary-index-and-references)](#templates-glossary-index-and-references)`
- Line 173: `[28.1 Registo mínimo de risco [42](#minimal-risk-record)](#minimal-risk-record)`
- Line 175: `[28.2 Papel de ensaio de controlo [42](#control-test-workpaper)](#control-test-workpaper)`
- Line 177: `[28.3 Glossário [42](#glossary)](#glossary)`
- Line 179: `[28,4 Índice de assunto [43](#subject-index)](#subject-index)`
- Line 181: `[28.5 Referências oficiais [43](#official-references)](#official-references)`

#### malformed_emphasis
- Line 3: `** SÉRIES PRÁTICAS DE CIBERSegurança, PRIVACIDADE E CONFORMIDADE`

#### untranslated_english_text
- Line 258: `![The SoA registra seleção de controle fundamentada e status de implementação.](media/image3.png)`

#### non_brazilian_or_mixed_locale_forms
- Line 15: `• todos os 93 controlos do Anexo A • risco • declaração de aplicabilidade • auditoria • certificação • provas • ferramentas • laboratórios • preparação para a carreira`
- Line 91: `[13. Anexo A 5 Controlos organizacionais [19](#annex-a-5-organizational-controls)](#annex-a-5-organizational-controls)`
- Line 95: `[15. Anexo A 7 Controlos físicos [23](#annex-a-7-physical-controls)](#annex-a-7-physical-controls)`
- Line 97: `[16. Anexo A 8 Controlos tecnológicos [24](#annex-a-8-technological-controls)](#annex-a-8-technological-controls)`
- Line 99: `[17. Controlos de execução com ISO/IEC 27002 [26](#implementing-controls-with-isoiec-27002)](#implementing-controls-with-isoiec-27002)`
- Line 159: `[27.4 Todos os controlos do anexo A são obrigatórios? [40](#are-all-annex-a-controls-mandatory)](#are-all-annex-a-controls-mandatory)`
- Line 193: `ISO/IEC 27001:2022 □ Requisitos de ISMS Normativos, incluindo os controlos de referência do anexo A`
- Line 195: `ISO/IEC 27002:2022 □ Orientações de implementação para os controlos de segurança da informação`
- Line 200: `- O Anexo A enumera 93 controlos de referência em quatro temas: 37 organizativos, 8 pessoas, 14 físicos e 34 tecnológicos.`
- Line 202: `- A selecção dos controlos segue o tratamento de risco e as obrigações aplicáveis; o anexo A não é uma lista de verificação universal onde cada controlo deve ser sempre aplicado.`
- Line 204: `- A declaração de aplicabilidade regista os controlos necessários, a justificação, o estado de execução e as exclusões justificadas do anexo A.`
- Line 256: `* A ponte entre o tratamento de risco, o anexo A, outros controlos e provas de auditoria.*`
- Line 262: `- Listar os controlos necessários para tratar os riscos identificados de segurança da informação e cumprir os requisitos legais, regulamentares, contratuais e comerciais.`
- Line 264: `- Compare os controlos seleccionados com o anexo A, pelo que os controlos de referência necessários não são ignorados.`
- Line 270: `- Inclua controlos específicos da organização quando o anexo A não abordar totalmente um risco.`
- Line 295: `□ Declaração de Aplicabilidade • Explica a selecção e o estado de controlo • Todos os controlos do anexo A abordados; justificações suportadas`
- Line 425: `# 13. Anexo A 5 Controlos organizacionais`
- Line 427: `* Resumos originais dos controlos de referência, foco de verificação e exemplos de provas.*`
- Line 469: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 478: `* Resumos originais dos controlos de referência, foco de verificação e exemplos de provas.*`
- Line 491: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 494: `# 15. Anexo A 7 Controlos físicos`
- Line 496: `* Resumos originais dos controlos de referência, foco de verificação e exemplos de provas.*`
- Line 515: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 518: `16. Anexo A 8 Controlos tecnológicos`
- Line 520: `* Resumos originais dos controlos de referência, foco de verificação e exemplos de provas.*`
- Line 559: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 704: `□ Ciso Assistant; intuitem.github.io; ISMS, riscos, controlos, provas`
- Line 984: `Um registo controlado dos controlos necessários, a justificação da inclusão ou exclusão no anexo A e o estado de execução, ligados ao tratamento e às provas.`
- Line 1014: `- Que sistemas gerem riscos, controlos, fornecedores, resultados e medidas correctivas?`
- Line 1034: `Controlos existentes`
- Line 1060: `• Anexo A • Conjunto de referência de 93 controlos de segurança da informação em ISO/IEC 27001:2022.`
- Line 1078: `□ Controlos do anexo A`
- Line 202: `- A selecção dos controlos segue o tratamento de risco e as obrigações aplicáveis; o anexo A não é uma lista de verificação universal onde cada controlo deve ser sempre aplicado.`
- Line 295: `□ Declaração de Aplicabilidade • Explica a selecção e o estado de controlo • Todos os controlos do anexo A abordados; justificações suportadas`
- Line 469: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 491: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 515: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 559: `Regra da selecção:** O anexo A é um conjunto de referência utilizado para verificar se os controlos necessários não foram ignorados. A organização pode precisar de outros controles. Qualquer inclusão ou exclusão deve ser justificada através`
- Line 244: `□ Activo ou objectivo □ Portal do cliente e disponibilidade contratualmente exigida`
- Line 764: `Objectivo: Gestão da vulnerabilidade. Projeto oficial: [<u>Greenbone Community Edition</u>](https://greenbone.github.io/docs/latest/)`
- Line 812: `Objectivo: Monitorização da integridade dos ficheiros. Projecto oficial: [<u>AIDE</u>](https://aide.github.io/)`
- Line 1031: `Objectivo / activo`
- Line 244: `□ Activo ou objectivo □ Portal do cliente e disponibilidade contratualmente exigida`
- Line 710: `O Nmap nmap.org O Activo e a descoberta do serviço`
- Line 1031: `Objectivo / activo`
- Line 173: `[28.1 Registo mínimo de risco [42](#minimal-risk-record)](#minimal-risk-record)`
- Line 289: `**Documento ou registo** **Purpose** **Controle**`
- Line 293: `O método de risco e o registo mostram a avaliação e as decisões repetiveis . Critérios aplicados de forma consistente; os proprietários aprovam o risco residual .`
- Line 690: `Método utilizado de forma consistente; registo completo; os proprietários aceitam risco residual`
- Line 910: `• Risco • Criar um plano de registo e tratamento consistente`
- Line 947: `• Método de risco, registo, tratamento`
- Line 952: `• Registo de acção correctiva`
- Line 984: `Um registo controlado dos controlos necessários, a justificação da inclusão ou exclusão no anexo A e o estado de execução, ligados ao tratamento e às provas.`
- Line 81: `[8. Cláusula 6 — Planeamento [14](#clause-6-planning)](#clause-6-planning)`
- Line 340: `□ ** Finalidade da clausa: ** Planeamento`
- Line 57: `[Comunicação de publicação e utilização [2](#publication-and-use-notice)](#publication-and-use-notice)`
- Line 59: `[Utilização ética e autorizada [2](#ethical-and-authorized-use)](#ethical-and-authorized-use)`

#### known_mistranslations
- Line 9: `* Um manual de trabalho para gerentes, analistas júnior, estudantes, mudadores de carreira, auditores internos e equipes de segurança*`
- Line 194: `ISO/IEC 27001:2022/Amd 1:2024 □ Alterações da ação climática que afetam o contexto e a consideração de partes interessadas`
- Line 229: `Alteração O que desencadeia uma revisão do escopo? Mudar registros, aquisição e portas do produto`
- Line 175: `[28.2 Papel de ensaio de controlo [42](#control-test-workpaper)](#control-test-workpaper)`
- Line 65: `[Quadro de conteúdos [4](#table-of-contents)](#table-of-contents)`

## Release implication

Any FAIL blocks localized DOCX/PDF rebuild and publication-readiness claims until the source defects are repaired and this audit passes at the exact candidate SHA.
