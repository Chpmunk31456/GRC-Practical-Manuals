# Manual 39 — Implementación Controlada de COPPA

**Línea base controlada:** Children's Online Privacy Protection Act, 15 U.S.C. §§ 6501–6506, y 16 CFR Part 312 vigente, incluidas las enmiendas finales de la FTC de 2025.  
**Límite:** guidance, policy statements, materiales de safe harbor de la FTC, leyes estatales de privacidad infantil, obligaciones educativas, contratos y prácticas internas permanecen como capas separadas.  
**Regla de release:** reverificar 16 CFR Part 312, estado de enmiendas y fechas de vigencia al congelar el candidato.

## Chapter 01 — Propósito, alcance y jerarquía controlada de fuentes
Defina alcance COPPA, jerarquía de fuentes, ownership y control de cambios. Mantenga registro de aplicabilidad, fuentes, responsables, evidencia y change watch.

## Chapter 02 — Aplicabilidad del operador y del servicio
Determine si la organización actúa como operator o está dentro del alcance COPPA. Documente propiedad del sitio/app, relaciones de servicio, flujos de recolección y supuestos jurisdiccionales.

## Chapter 03 — Análisis de servicios dirigidos a niños
Use factores documentados para evaluar si sitio, app, función o audiencia es child-directed. Conserve evidencia de audiencia, contenido, diseño, marketing, analytics y uso previsto.

## Chapter 04 — Conocimiento real y audiencias mixtas
Defina cómo se identifica, escala y trata el actual knowledge respecto de menores de 13 años. Para mixed audiences, documente age-screening, consecuencias y controles contra evasión.

## Chapter 05 — Inventario de información personal
Inventarie identificadores, contactos, persistent identifiers, medios, geolocalización, conducta, dispositivo, contenido generado por usuarios y demás información relevante. Mapee recolección, uso, disclosure, storage y deletion.

## Chapter 06 — Gobernanza y accountability
Asigne roles legal/privacy, producto, security, engineering, marketing, data, procurement, support y executive. Mantenga RACI, approvals, exceptions y management-review evidence.

## Chapter 07 — Aviso directo a padres
Defina cuándo y cómo se entrega direct notice antes de la recolección o de cambios materiales cuando corresponda. Mantenga versiones, evidencia de entrega, timing, aprobación y accessibility records.

## Chapter 08 — Aviso de privacidad en línea
Mantenga un privacy notice claro, completo y vigente sobre operadores cubiertos, prácticas de información, derechos parentales, disclosures, retention y contactos aplicables.

## Chapter 09 — Marco de consentimiento parental verificable
Establezca proceso controlado para seleccionar y operar métodos de verifiable parental consent adecuados al uso y riesgo. Conserve consentimiento, rationale, validación de identidad/autoridad y revocación.

## Chapter 10 — Excepciones al consentimiento
Exija análisis documentado antes de depender de una recolección o uso que pueda proceder sin consentimiento previo. Registre base, alcance, propósito, datos, duración y controles contra expansión indebida.

## Chapter 11 — Minimización de datos
Limite la recolección a información razonablemente necesaria para la participación del menor en la actividad o servicio, conforme a los requisitos aplicables. Mantenga necessity assessments y evidencia de diseño.

## Chapter 12 — Limitación de propósito y uso secundario
Defina usos permitidos para datos de menores e impida secondary uses incompatibles, profiling, advertising o reutilización sin el análisis y consentimiento requeridos.

## Chapter 13 — Controles de publicidad y uso comercial
Gobierne targeted advertising, behavioral advertising, contextual advertising, measurement, attribution y monetización relacionados con child data. Separe requisitos regulatorios de políticas internas de riesgo.

## Chapter 14 — Persistent identifiers, cookies y SDKs
Inventarie cookies, pixels, SDKs, device identifiers, analytics, ad-tech y código embebido. Documente propósito, proveedor, flujos, configuración, efectos de consentimiento y controles de desactivación.

## Chapter 15 — Gobernanza de disclosures a terceros
Controle disclosures a service providers, platforms, ad-tech, analytics, processors y otros recipients. Mantenga inventario, propósito, necesidad, contratos, restricciones downstream y monitoring.

## Chapter 16 — Ciclo de vida de vendors y service providers
Aplique due diligence de child data antes del onboarding. Evalúe collection, use, disclosure, security, retention, subprocessors, incident support, deletion, audit rights y termination.

## Chapter 17 — Casos de uso escolares y EdTech
Evalúe usos autorizados por escuelas sin asumir una excepción COPPA universal. Documente rol del operator, autoridad escolar, comunicaciones parentales, uso de datos, restricciones comerciales y overlays FERPA/estatales por separado.

## Chapter 18 — Acceso, revisión, eliminación y negativa parental
Implemente workflows para derechos aplicables de padres a revisar información, pedir deletion y rechazar collection/use futura. Mantenga validación, timing, search, response y closure evidence.

## Chapter 19 — Age-screening y diseño neutral
Diseñe age screens y audience controls sin inducir una respuesta específica. Mantenga pruebas, bypass monitoring, exception handling y product-change reviews.

## Chapter 20 — Salvaguardas de seguridad
Implemente safeguards administrativos, técnicos y físicos razonables. Mantenga access controls, encryption decisions, secure configuration, logging, vulnerability management, monitoring y corrective actions.

## Chapter 21 — Retención y eliminación
Conserve child personal information solo durante el tiempo razonablemente necesario para el propósito y elimínela de forma segura cuando deje de ser requerida, salvo excepciones documentadas.

## Chapter 22 — Incident response y breach analysis
Integre incidentes de child data con incident response, revisión legal/privacy, evidence preservation, contratos, análisis de leyes estatales y obligaciones FTC/orders aplicables.

## Chapter 23 — Desarrollo de producto y privacy engineering
Integre COPPA en requirements, design, architecture, testing, release, experimentation y change management. Requiera privacy review para nuevos datos, features, integrations y monetization changes.

## Chapter 24 — AI, personalización y funciones automatizadas
Evalúe assistants, recommendations, moderation, profiling, inference, biometrics y generative features por collection, secondary use, model training, disclosure, retention y transparency risks.

## Chapter 25 — Gobernanza de safe harbor
Si se depende de un FTC-approved COPPA safe harbor, documente membership, requisitos, monitoring, assessments, corrective actions y límite entre obligaciones del programa y la regla base.

## Chapter 26 — Overlays estatales de privacidad infantil y sectoriales
Mantenga análisis separado para leyes child/teen privacy, consumer privacy, education, biometrics, health, gaming y otros overlays. No presente deberes del overlay como requisitos COPPA.

## Chapter 27 — Gestión de registros y evidencia
Conserve notices, consent records, age-screening decisions, vendor records, data inventories, disclosures, rights requests, retention/deletion evidence, incidents, training, testing y approvals bajo retención controlada.

## Chapter 28 — Capacitación y competencia por rol
Proporcione training por rol para product, engineering, design, marketing, data, privacy, legal, security, procurement, support y leadership. Registre completion, competency checks, remediation y refresh triggers.

## Chapter 29 — Assurance y testing
Pruebe notices, consent flows, age screens, SDK inventories, vendor controls, rights handling, retention/deletion, security controls y decisiones child-directed. Mantenga samples, findings, remediation y retest evidence.

## Chapter 30 — Métricas y management review
Controle consent failures, bypass rates, unauthorized SDKs, vendor findings, rights-request timing, retention exceptions, incidents, training completion y remediation aging.

## Chapter 31 — Localización exact-hash, provenance y evidencia de release
Congele candidatos EN/es-419/pt-BR antes del review final. Vincule DOCX/PDF a SHA-256 y conserve evidencia de localization, accessibility, rendered-page, workflow-security y release QA.

## Chapter 32 — Roadmap de implementación y reverificación al release
Implemente por fases: applicability; data inventory; notices/consent; product/vendor controls; rights; security; retention; assurance; metrics; continual improvement. Antes de publicar, reverifique texto FTC vigente, enmiendas, effective dates y overlays expresamente reclamados. La publicación permanece secuencial después del Manual 38.
