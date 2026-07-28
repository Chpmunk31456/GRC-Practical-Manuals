# Multilingual Editorial Style Sheet

**Scope:** Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) editions.

**Status:** Editorial control for human review. It does not make any edition publication-ready.

## Editorial principles

1. Preserve technical meaning, framework identifiers, control identifiers, version numbers, commands, code, URLs, filenames, link destinations, and Markdown structure.
2. Prefer clear professional language used across Latin America and Brazil. Avoid country-specific slang, European Portuguese usage, and unnecessary literal calques.
3. Preserve every machine-assisted draft notice until all publication gates are complete.
4. Do not silently add facts, legal interpretations, requirements, or promises that are absent from the English source.
5. Do not invent, rename, or replace missing legacy images. Record unresolved image references as review gates.
6. Keep official product and framework names in their authoritative form unless an official localized name is established.

## Capitalization and framework names

| Source concept | Latin American Spanish | Brazilian Portuguese |
|---|---|---|
| NIST Cybersecurity Framework 2.0 | Marco de Ciberseguridad de NIST 2.0; retain `NIST CSF 2.0` | Framework de Cibersegurança do NIST 2.0; retain `NIST CSF 2.0` |
| NIST Risk Management Framework | Marco de Gestión de Riesgos de NIST; retain `NIST RMF` | Framework de Gerenciamento de Riscos do NIST; retain `NIST RMF` |
| CIS Critical Security Controls | Controles Críticos de Seguridad de CIS; retain the official product name where cited | Controles Críticos de Segurança do CIS; retain the official product name where cited |
| ISO/IEC 27001 and ISO/IEC 27002 | retain standard numbers and `ISO/IEC` | retain standard numbers and `ISO/IEC` |
| PCI DSS | retain `PCI DSS` and requirement numbers | retain `PCI DSS` and requirement numbers |
| GDPR | retain `GDPR`; use `RGPD` only when explaining a recognized localized abbreviation | retain `GDPR`; use `RGPD` only when explaining a recognized localized abbreviation |
| HIPAA | retain `HIPAA` | retain `HIPAA` |
| SOC 2 | retain `SOC 2` and Trust Services Criteria | retain `SOC 2` and Trust Services Criteria |

- Capitalize defined framework concepts consistently when the source uses them as formal labels.
- Preserve official NIST Function labels in uppercase English: `GOVERN`, `IDENTIFY`, `PROTECT`, `DETECT`, `RESPOND`, `RECOVER`.
- Use sentence case for ordinary headings, table cells, captions, and explanatory prose unless the source intentionally uses title case or uppercase.

## Core terminology

| English | Latin American Spanish | Brazilian Portuguese |
|---|---|---|
| risk | riesgo | risco |
| risk assessment | evaluación de riesgos | avaliação de riscos |
| risk appetite | apetito de riesgo | apetite a risco |
| risk tolerance | tolerancia al riesgo | tolerância a risco |
| risk treatment | tratamiento del riesgo | tratamento de riscos |
| residual risk | riesgo residual | risco residual |
| inherent risk | riesgo inherente | risco inerente |
| control | control | controle |
| safeguard | salvaguarda | salvaguarda |
| control owner | responsable del control | responsável pelo controle |
| control objective | objetivo de control | objetivo de controle |
| control design | diseño del control | desenho do controle |
| design effectiveness | eficacia del diseño | eficácia do desenho |
| operating effectiveness | eficacia operativa | eficácia operacional |
| control testing | pruebas de controles | teste de controles |
| test procedure | procedimiento de prueba | procedimento de teste |
| sample | muestra | amostra |
| evidence | evidencia | evidência |
| finding | hallazgo | achado |
| observation | observación | observação |
| exception | excepción | exceção |
| gap | brecha | lacuna |
| remediation | remediación | remediação |
| corrective action | acción correctiva | ação corretiva |
| retest | nueva prueba / volver a probar | reteste / novo teste |
| issue owner | responsable del hallazgo | responsável pelo achado |
| due date | fecha límite | prazo |
| governance | gobernanza | governança |
| oversight | supervisión | supervisão |
| accountability | rendición de cuentas | responsabilização / prestação de contas |
| stakeholder | parte interesada | parte interessada |
| supply chain | cadena de suministro | cadeia de suprimentos |
| third party | tercero | terceiro |
| service provider | proveedor de servicios | prestador de serviços |
| business continuity | continuidad del negocio | continuidade de negócios |
| disaster recovery | recuperación ante desastres | recuperação de desastres |
| incident response | respuesta a incidentes | resposta a incidentes |

## Preferred action language

- Translate `review` according to meaning:
  - assessment or inspection: `revisión` / `revisão`;
  - formal audit review: use the established audit term in context;
  - approval: `aprobación` / `aprovação`.
- Translate `monitor` as `monitorear` or `supervisar` in Spanish according to context, and `monitorar` in Brazilian Portuguese.
- Translate `perform testing` as `realizar pruebas` / `realizar testes`, not literal constructions based on “execute.”
- Use `documentar`, `validar`, `verificar`, and `confirmar` only when the source supports the corresponding level of assurance.
- Do not translate `must`, `should`, or `may` interchangeably. Preserve obligation strength.

## Tables, figures, and captions

| English label | Latin American Spanish | Brazilian Portuguese |
|---|---|---|
| Purpose | Propósito | Objetivo |
| Plain meaning | Significado en lenguaje claro | Significado em linguagem simples |
| Manager or analyst verification | Verificación del gerente o analista | Verificação do gerente ou analista |
| Example evidence | Ejemplo de evidencia | Exemplo de evidência |
| Owner | Responsable | Responsável |
| Frequency | Frecuencia | Frequência |
| Status | Estado | Status |
| Result | Resultado | Resultado |
| Pass | Aprobado / Cumple, according to context | Aprovado / Atende, according to context |
| Fail | No aprobado / No cumple, according to context | Reprovado / Não atende, according to context |
| Figure | Figura | Figura |
| Table | Tabla | Tabela |
| Source | Fuente | Fonte |
| Note | Nota | Observação |

- Keep table headers short, parallel, and consistent within a manual.
- Captions use sentence case and end without a period unless they are complete sentences or the source uses punctuation consistently.
- Alt text describes the figure’s purpose or relationship, not only its appearance.
- Accessibility text must not claim compliance merely because alt text exists.

## Accessibility language

Preferred:

- Spanish: `texto alternativo`, `orden de lectura`, `encabezados descriptivos`, `propósito del enlace`, `contraste de color`, `tecnologías de asistencia`.
- Brazilian Portuguese: `texto alternativo`, `ordem de leitura`, `cabeçalhos descritivos`, `finalidade do link`, `contraste de cores`, `tecnologias assistivas`.

Avoid:

- absolute claims such as “fully accessible” without documented testing;
- using color alone to communicate status;
- vague link text when a descriptive destination can be used;
- treating automated checks as human accessibility approval.

## Manual-level review checklist

- [ ] Draft notice is present and unchanged in meaning.
- [ ] Framework and control identifiers match the English source.
- [ ] Obligation strength and technical claims are unchanged.
- [ ] Approved terminology is used consistently.
- [ ] Headings, tables, captions, and alt text follow this sheet.
- [ ] URLs, Markdown links, code, commands, filenames, and code fences are preserved.
- [ ] No missing image is invented, renamed, or replaced.
- [ ] Corrections are limited to language issues that are clear from the English source.
- [ ] Uncertain terminology is recorded for human review instead of guessed.
- [ ] DOCX/PDF regeneration occurs only after the manual’s Markdown correction set is accepted.
