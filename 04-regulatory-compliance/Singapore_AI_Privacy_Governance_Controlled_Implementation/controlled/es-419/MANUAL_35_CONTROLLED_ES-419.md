# Manual 35 — Implementación controlada de Gobernanza de IA y Privacidad de Singapur

**Idioma:** Español de América Latina (es-419)  
**Línea base controlada:** PDPA/PDPC de Singapur más los recursos vigentes de gobernanza para IA tradicional, IA generativa, AI Verify e IA agéntica, verificados el 31 de agosto de 2026.  
**Límite:** La ley/regulación vinculante, la guía y enforcement del regulador, los marcos voluntarios de IA, los overlays sectoriales y la práctica de la organización permanecen separados. Esta es una traducción de proyecto no oficial y no constituye asesoría legal, aprobación regulatoria ni certificación.

## Chapter 01 — Propósito, alcance y jerarquía controlada de fuentes
Use la PDPA y las regulaciones aplicables como capa vinculante de privacidad. Clasifique materiales de PDPC, IMDA, AI Verify, reguladores sectoriales, contratos y procedimientos internos según su verdadero estatus jurídico. Mantenga un registro fechado de fuentes, propietarios y cambios materiales.

## Chapter 02 — Ecosistema regulatorio y de gobernanza de Singapur
Mapee PDPC, IMDA, reguladores sectoriales, contrapartes contractuales y órganos internos. Identifique de forma explícita qué obligación proviene de ley, regulación, guía, contrato o marco voluntario.

## Chapter 03 — Aplicabilidad de la PDPA, exclusiones y roles organizacionales
Documente si la PDPA aplica a la organización, actividad, datos y relación evaluada. Preserve distinciones sobre individuos en capacidad personal, agencias públicas, datos de empleados, información de contacto comercial, data intermediaries y otras excepciones aplicables.

## Chapter 04 — Accountability y gobierno del Data Protection Officer
Establezca gobernanza de privacidad con DPO designado, supervisión ejecutiva, responsabilidades claras, recursos, escalamiento y revisión de management. Conserve nombramientos, charters, políticas, reportes, issues y corrective actions.

## Chapter 05 — Notification, consentimiento y retiro de consentimiento
Diseñe procesos de colección, uso y disclosure para informar propósitos y obtener consentimiento cuando corresponda. Permita retiro con aviso razonable y documente excepciones o bases alternativas válidas.

## Chapter 06 — Purpose Limitation y razonamiento de propósito apropiado
Evalúe si cada colección, uso o disclosure responde a un propósito que una persona razonable consideraría apropiado. Nuevos usos habilitados por IA no deben heredar automáticamente permiso del propósito original.

## Chapter 07 — Accuracy y controles de impacto de decisiones
Aplique controles proporcionales de exactitud e integridad cuando los datos personales puedan afectar decisiones o ser divulgados. Para decisiones apoyadas por IA, pruebe calidad, actualidad, representatividad y vías de error material.

## Chapter 08 — Protection Obligation y arreglos razonables de seguridad
Implemente salvaguardas administrativas, técnicas y físicas razonables según sensibilidad, volumen, uso y amenazas. Incluya sistemas de IA en IAM, configuración segura, logging, vulnerability management, protección de datos, resiliencia e incident response.

## Chapter 09 — Retention Limitation y disposición defendible
Deje de retener datos personales cuando ya no sean necesarios para fines legales o de negocio. Incluya training data, evaluaciones, prompts, logs, embeddings, backups, memorias de agentes y datos derivados en las reglas de retención.

## Chapter 10 — Transfer Limitation y transferencias internacionales
Antes de transferir datos fuera de Singapur, determine el mecanismo aplicable y la protección comparable requerida por la PDPA. Mantenga assessments, contratos, due diligence, data flows, excepciones y reassessment periódico.

## Chapter 11 — Operaciones de acceso y corrección
Implemente intake, identity verification, búsqueda, review, respuesta, corrección, excepciones y escalamiento. Incluya copias y datos derivados usados por IA cuando corresponda.

## Chapter 12 — Evaluación y notificación obligatoria de data breaches
Evalúe breaches bajo los criterios vigentes de significant harm y/o significant scale. Una vez determinado que el breach es notificable, notifique a la PDPC tan pronto como sea practicable y no más tarde de tres días calendario después de esa determinación, además de manejar notificación a individuos cuando sea requerida.

## Chapter 13 — Data intermediaries y responsabilidades contractuales
Identifique roles de data intermediary y distribuya responsabilidades contractuales y operacionales. Cubra instrucciones, seguridad, breach escalation, subprocessors, retención, transferencias, audit evidence y termination.

## Chapter 14 — Data Portability: change-watch y activación
Trate Data Portability como no operativa hasta que entren en vigor las regulaciones necesarias. Mantenga monitoreo formal, readiness assessment y un punto de decisión para activación futura.

## Chapter 15 — Inventario de datos, clasificación, lineage y processing records
Mantenga inventario de datos personales, sistemas, repositorios, modelos, agentes, flujos, propósitos, owners, retención, recipients y ubicaciones de transferencia. La lineage debe mostrar cómo los datos alimentan y salen de sistemas de IA.

## Chapter 16 — Privacy by Design y Data-Protection Impact Assessment
Integre privacidad en product, system, AI, procurement y change lifecycle. Use impact assessment proporcional para high-risk processing, nuevas tecnologías, datos sensibles, decisiones automatizadas o cambios materiales.

## Chapter 17 — Intake de casos de uso de IA y clasificación de riesgo
Registre cada caso material de IA antes de producción. Documente propósito, usuarios, personas afectadas, datos, modelo o agente, terceros, autonomía, impacto de decisión, privacidad, seguridad y overlays regulatorios.

## Chapter 18 — Implementación del marco de IA tradicional
Use el Model AI Governance Framework tradicional como guía voluntaria para governance interno, human involvement, operations management y stakeholder communication. No lo presente como certificación legal o regulatoria.

## Chapter 19 — Implementación del marco de IA generativa
Aplique el framework de GenAI a accountability, data, trusted development/deployment, incident reporting, testing/assurance, security, provenance, safety/alignment y ecosystem considerations según el caso de uso.

## Chapter 20 — Implementación del marco de IA agéntica
Evalúe y limite autonomía, acceso a tools/data, transaction authority, persistence y delegation. Defina human approval checkpoints, lifecycle controls, monitoring, transparency, training, third-party agents, multi-agent risk y safeguards contra automation bias.

## Chapter 21 — Accountability humana, checkpoints y meaningful oversight
Asigne humanos u órganos responsables de resultados de IA. El oversight debe contar con información, autoridad, competencia, tiempo y capacidad real de intervención; una revisión nominal no es control significativo.

## Chapter 22 — AI data governance, provenance, quality y minimisation
Gobierne training, retrieval, evaluation, prompts, fine-tuning, telemetry y agent memory con provenance, permitted use, quality, minimisation, access, retention y transfer controls documentados.

## Chapter 23 — Fairness, bias, explainability, transparency y contestability
Identifique riesgos de fairness y bias según contexto, defina necesidades de explicación, comunique el uso de IA y proporcione revisión o contestability cuando lo requieran el riesgo, la ley, el contrato o compromisos internos.

## Chapter 24 — AI security, robustness, testing y lifecycle controls
Integre IA con secure development, change management, model/dependency governance, access control, secrets, logging, evaluation, robustness testing, incident response y retirement. Mayor autonomía requiere controles más fuertes.

## Chapter 25 — AI Verify y límites de assurance/testing
Use AI Verify como mecanismo voluntario de testing y evidencia donde sea útil. Los resultados deben quedar vinculados al sistema, versión, datos, configuración, benchmark y fecha; no son prueba universal de seguridad, legalidad o aprobación regulatoria.

## Chapter 26 — Third-party models, agents, processors y supply chain
Realice due diligence basada en riesgo para providers, hosted AI, processors, agent platforms, plugins, tools y dependencies críticas. Cubra data handling, confidentiality, security, subprocessors, changes, incidents, retention, transfers, evidence y exit.

## Chapter 27 — Multi-agent systems, tool access y bounded authority
Documente interacciones permitidas, authority limits, handoffs, shared context, external services y approval boundaries. Cada agente debe recibir solo los datos, tools, credentials y actions necesarios para el propósito aprobado.

## Chapter 28 — Comunicaciones, notices, feedback y responsible use
Comunique participación material de IA, propósito, limitaciones, responsabilidades y opciones de escalamiento. Capacite sobre over-reliance, confidentiality, data entry, approval duties y mandatory human review.

## Chapter 29 — Integración de incidentes, privacy breaches y AI harm
Integre incidentes de IA con cybersecurity, privacy, operational risk, legal, communications y executives. Distinga security event, personal-data breach, model defect, harmful output, control failure y regulatory trigger.

## Chapter 30 — Monitoring, métricas, enforcement learnings y mejora continua
Use métricas que demuestren efectividad. Revise enforcement de PDPC y actualizaciones de IMDA para identificar implicaciones de control sin convertir hechos específicos en reglas universales.

## Chapter 31 — Arquitectura de evidencia, auditability y crosswalk governance
Permita trazabilidad desde requirement o commitment hasta owner, control, operation, test, exception y remediation. Crosswalks pueden mostrar relaciones, pero no equivalencia legal o de controles sin análisis sustentado.

## Chapter 32 — Change control legal/framework y roadmap de implementación
Antes de release, reverifique PDPA/PDPC, Data Portability, breach notification, marcos Traditional/GenAI/Agentic AI, AI Verify y overlays sectoriales. Cambios materiales posteriores al candidate freeze requieren impact assessment y, cuando corresponda, candidate superseding con nueva provenance.
