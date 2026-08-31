# Manual 28 — Implementación Controlada de Privacidad de IA y Gobernanza de Decisiones Automatizadas

Traducción no oficial del proyecto al español latinoamericano. La fuente controladora del proyecto es la edición inglesa. Este manual operacionaliza controles de gobernanza y evidencia; no constituye asesoría legal ni convierte orientación voluntaria en obligación jurídica. Las obligaciones específicas de cada jurisdicción deben validarse para cada despliegue y caso de uso.

## 01. Propósito, alcance y límite de uso controlado
**Capa de fuente:** NIST Privacy Framework 1.0, NIST AI RMF 1.0, gobernanza interna y capas legales aplicables.
**Aplicabilidad:** Sistemas asistidos por IA, algorítmicos, de perfilamiento y de decisión automatizada que procesan datos personales o vinculables a personas, o que afectan materialmente a individuos.
**Responsable:** Líder de gobernanza de IA con privacidad/legal, seguridad, producto y responsables de negocio.
**Procedimiento:** Definir alcance, poblaciones afectadas, rol de la decisión, uso de datos personales, jurisdicciones, usos excluidos y objetivos de implementación antes del despliegue.
**Evidencia:** Registro de alcance aprobado, identificador del sistema, responsables, mapa jurisdiccional y límite de liberación.
**Revisión/prueba:** Confirmar que el alcance coincide con el comportamiento y los flujos de datos en producción.
**Remediación/revaluación:** Corregir brechas y revaluar tras cambios materiales de uso, jurisdicción, modelo o datos.

## 02. Jerarquía de fuentes, jurisdicción y vigilancia de cambios
**Capa de fuente:** Ley/regulación aplicable; orientación de reguladores; contratos; NIST PF/AI RMF; políticas y estándares internos.
**Aplicabilidad:** Todo sistema gobernado por este manual.
**Responsable:** Legal/privacidad con gobernanza de IA y cumplimiento.
**Procedimiento:** Mantener un registro que distinga obligaciones vinculantes de orientación voluntaria y separe material borrador o en desarrollo.
**Evidencia:** Registro de fuentes, versión/fecha, autoridad, justificación de aplicabilidad y bitácora de vigilancia.
**Revisión/prueba:** Verificar el estado de las fuentes inmediatamente antes de congelar el candidato y tras cambios regulatorios materiales.
**Remediación/revaluación:** Actualizar mapeos y controles sin tratar retroactivamente borradores como obligatorios.

## 03. Inventario de sistemas de IA/decisión automatizada y propiedad
**Capa de fuente:** Conceptos de inventario y rendición de cuentas de NIST y gobernanza interna de activos.
**Aplicabilidad:** Usos productivos, pilotos, integrados, comprados, basados en API y no registrados.
**Responsable:** Propietario de negocio del sistema y gobernanza de IA.
**Procedimiento:** Mantener inventario autoritativo de propósito, modelo/proveedor, dominios de datos, rol de decisión, ambientes, usuarios, personas afectadas y responsables.
**Evidencia:** Registro de inventario, estado del ciclo de vida, propietario de negocio, técnico y de privacidad, y fecha de revisión.
**Revisión/prueba:** Conciliar contra compras, APIs, cuentas cloud, registros de modelos y plataformas de datos.
**Remediación/revaluación:** Registrar sistemas no controlados y escalar usos no autorizados.

## 04. Taxonomía de decisiones y clasificación de consecuencias
**Capa de fuente:** Taxonomía interna informada por NIST y definiciones legales aplicables.
**Aplicabilidad:** Todo sistema que influya una decisión sobre una persona.
**Responsable:** Propietario de producto/negocio con privacidad/legal y riesgo de IA.
**Procedimiento:** Clasificar como asistivo, recomendatorio, automatizado o consecuencial y documentar si una persona puede alterar materialmente el resultado.
**Evidencia:** Registro de taxonomía, nivel de consecuencia, descripción del rol humano y cruce con definiciones legales cuando aplique.
**Revisión/prueba:** Probar el flujo real contra la clasificación declarada.
**Remediación/revaluación:** Reclasificar cuando cambien automatización, dependencia o consecuencia.

## 05. Linaje de datos y flujo del modelo
**Capa de fuente:** Orientación de ingeniería de privacidad/gobernanza de datos de NIST y controles internos de arquitectura.
**Aplicabilidad:** Flujos de entrenamiento, evaluación, inferencia, enriquecimiento, retroalimentación y decisión.
**Responsable:** Arquitecto/ingeniero de datos con privacidad y propietario del modelo.
**Procedimiento:** Mapear fuentes, transformaciones, características, llamadas al modelo, salidas, destinatarios, almacenes, transferencias y bucles de retroalimentación.
**Evidencia:** Diagramas de flujo, registros de linaje, inventario de interfaces y mapa de transferencias.
**Revisión/prueba:** Rastrear registros representativos de extremo a extremo.
**Remediación/revaluación:** Corregir flujos no documentados y revaluar tras cambios de canalización.

## 06. Especificación de propósito y limitación de uso
**Capa de fuente:** Principios de gobernanza de privacidad, contratos, requisitos legales aplicables y política interna.
**Aplicabilidad:** Recolección, reutilización, inferencia y procesamiento para decisiones.
**Responsable:** Propietario de negocio con privacidad/legal.
**Procedimiento:** Registrar propósitos aprobados, usos compatibles, usos prohibidos, disparadores de revisión de uso secundario y límites de decisión.
**Evidencia:** Registro de propósito, casos aprobados, lista de usos prohibidos y excepciones.
**Revisión/prueba:** Comparar características, prompts, análisis y usos posteriores reales con los propósitos aprobados.
**Remediación/revaluación:** Detener o corregir usos incompatibles y revaluar antes de expandirlos.

## 07. Gobernanza de datos de entrenamiento y evaluación
**Capa de fuente:** NIST AI RMF, controles de privacidad/datos, contratos y ley aplicable.
**Aplicabilidad:** Datos usados para entrenar, ajustar, evaluar, calibrar o comparar modelos.
**Responsable:** Propietario del modelo/datos con privacidad, seguridad y legal.
**Procedimiento:** Documentar procedencia, autorización, representatividad, sensibilidad, retención, calidad, exclusiones y usos permitidos.
**Evidencia:** Fichas de datasets, procedencia, licencias/contratos, pruebas de calidad, aprobaciones y obligaciones de eliminación.
**Revisión/prueba:** Muestrear registros de origen y verificar permisos y usos declarados.
**Remediación/revaluación:** Retirar o reemplazar datos no conformes y reentrenar/reprobar cuando el impacto sea material.

## 08. Gobernanza de datos sensibles e inferidos
**Capa de fuente:** Ley de privacidad/sector aplicable, orientación regulatoria y clasificación interna.
**Aplicabilidad:** Identificadores sensibles, salud, finanzas, biometría, ubicación precisa, datos de menores, rasgos protegidos donde estén regulados e inferencias sensibles.
**Responsable:** Privacidad/legal con propietario de datos y gobernanza de IA.
**Procedimiento:** Identificar entradas e inferencias sensibles, aplicar controles reforzados de acceso/minimización y documentar restricciones jurisdiccionales.
**Evidencia:** Registro de datos sensibles, inventario de inferencias, reglas de acceso, controles de enmascaramiento y análisis de aplicabilidad.
**Revisión/prueba:** Revisar características y salidas por inferencias sensibles no declaradas.
**Remediación/revaluación:** Suprimir, restringir o rediseñar el procesamiento y revaluar base legal y riesgo.

## 09. Evaluación de riesgo y daños de privacidad
**Capa de fuente:** NIST Privacy Framework/ingeniería de privacidad y deberes de evaluación aplicables.
**Aplicabilidad:** Sistemas con riesgo material de privacidad, autonomía, economía, reputación, seguridad o vigilancia.
**Responsable:** Propietario del riesgo de privacidad con gobernanza de IA y negocio.
**Procedimiento:** Identificar personas afectadas, acciones de datos dañinas, probabilidad, severidad, escala, reversibilidad, mitigaciones y riesgo residual.
**Evidencia:** Evaluación de riesgo, escenarios de daño, plan de tratamiento, aceptación residual y fecha de revisión.
**Revisión/prueba:** Desafiar supuestos con escenarios representativos y perspectivas de poblaciones afectadas cuando sea viable.
**Remediación/revaluación:** Implementar controles adicionales o detener el uso si el riesgo residual excede tolerancia.

## 10. Interfaces de DPIA y evaluación de impacto de IA
**Capa de fuente:** Requisitos jurisdiccionales aplicables y métodos internos de riesgo IA/privacidad.
**Aplicabilidad:** Usos que alcancen umbrales legales o internos para evaluación formal.
**Responsable:** Privacidad/legal y gobernanza de IA.
**Procedimiento:** Determinar si se requiere DPIA, evaluación de impacto de IA, algorítmica o equivalente, sin asumir que una evaluación satisface automáticamente otra jurisdicción.
**Evidencia:** Análisis de umbral, evaluaciones completas, aprobaciones, consultas y decisiones de riesgo residual.
**Revisión/prueba:** Confirmar que la evaluación cubre sistema, datos, personas y contexto reales.
**Remediación/revaluación:** Reabrir evaluaciones tras cambios materiales de modelo, propósito, población, datos o despliegue.

## 11. Análisis de aplicabilidad de decisiones automatizadas
**Capa de fuente:** Ley y orientación específica por jurisdicción sobre decisiones automatizadas/perfilamiento.
**Aplicabilidad:** Decisiones realizadas o materialmente influenciadas por procesamiento automatizado.
**Responsable:** Legal/privacidad con propietario del proceso de negocio.
**Procedimiento:** Determinar definiciones, exclusiones, umbrales, avisos, derechos, revisión humana, pruebas y documentación aplicables por jurisdicción/caso.
**Evidencia:** Matriz de aplicabilidad, revisión legal, clasificación del sistema y mapeo de controles.
**Revisión/prueba:** Comparar automatización y discreción humana reales con el análisis.
**Remediación/revaluación:** Actualizar controles cuando cambie la automatización o el alcance legal.

## 12. Gobernanza de perfilamiento y personalización
**Capa de fuente:** Reglas aplicables de privacidad/protección al consumidor y gobernanza interna de analítica.
**Aplicabilidad:** Predicción conductual, segmentación, ranking, recomendación, targeting y personalización de individuos.
**Responsable:** Propietario de producto/negocio con privacidad y gobernanza de datos.
**Procedimiento:** Documentar propósito, entradas, atributos inferidos, destinatarios, nivel de consecuencia, interfaces de derechos/opt-out cuando aplique y perfiles prohibidos.
**Evidencia:** Registro de perfilamiento, lista de características, definiciones de audiencia, mapeo de derechos y aprobaciones.
**Revisión/prueba:** Probar perfilamiento no declarado y reutilización incompatible.
**Remediación/revaluación:** Restringir o rediseñar y revaluar avisos y derechos.

## 13. Arquitectura de transparencia y avisos
**Capa de fuente:** Deberes aplicables de transparencia/aviso, conceptos NIST y estándares internos de comunicación.
**Aplicabilidad:** Personas que interactúan materialmente con o son afectadas por IA/ADM.
**Responsable:** Producto/negocio con privacidad/legal y comunicaciones.
**Procedimiento:** Proporcionar avisos por capas que describan correctamente rol del sistema, uso de datos, contexto de decisión, limitaciones materiales, derechos/opciones cuando apliquen y canales de escalamiento.
**Evidencia:** Avisos aprobados, historial de versión, evidencia de entrega, controles de idioma/accesibilidad y bitácora de cambios.
**Revisión/prueba:** Comparar afirmaciones con comportamiento real.
**Remediación/revaluación:** Corregir avisos engañosos, obsoletos o incompletos.

## 14. Gobernanza de explicabilidad y códigos de razón
**Capa de fuente:** Deberes aplicables de explicación/razón, conceptos NIST AI RMF y estándares internos de riesgo de modelos.
**Aplicabilidad:** Decisiones que requieren una razón comprensible para usuarios, revisores, auditores o personas afectadas.
**Responsable:** Propietario del modelo con negocio, legal/privacidad y riesgo de modelos.
**Procedimiento:** Definir audiencia, método, lógica de códigos de razón, requisitos de fidelidad, limitaciones y escalamiento para resultados no explicables.
**Evidencia:** Especificación de explicación, catálogo de razones, validaciones y muestras de explicaciones.
**Revisión/prueba:** Probar fidelidad y consistencia contra los verdaderos factores de decisión.
**Remediación/revaluación:** Corregir explicaciones engañosas o restringir el uso.

## 15. Mecanismos de impugnación y apelación
**Capa de fuente:** Derechos aplicables y deberes de consumidor/empleo/sector, más política interna.
**Aplicabilidad:** Resultados consecuenciales o apelables.
**Responsable:** Propietario del proceso con legal/privacidad y operaciones.
**Procedimiento:** Proporcionar ruta documentada para cuestionar, impugnar, corregir datos, aportar contexto y obtener revisión calificada cuando se requiera o adopte por política.
**Evidencia:** Procedimiento, expedientes, resultados, niveles de servicio y cualificación de revisores.
**Revisión/prueba:** Muestrear apelaciones por independencia, oportunidad y reconsideración significativa.
**Remediación/revaluación:** Corregir fallas y alimentar problemas sistémicos a mejora de modelo/proceso.

## 16. Diseño de supervisión e intervención humana
**Capa de fuente:** NIST AI RMF, deberes aplicables de IA/ADM y diseño interno de controles.
**Aplicabilidad:** Sistemas donde personas supervisan, aprueban, anulan o revisan resultados.
**Responsable:** Propietario del proceso y gobernanza de IA.
**Procedimiento:** Definir autoridad, competencia, información disponible, capacidad de anulación, límites de carga, escalamiento y protección contra aprobación mecánica.
**Evidencia:** RACI, instrucciones, capacitación, registros de anulación, escalamiento y métricas de carga.
**Revisión/prueba:** Observar decisiones representativas y medir comportamiento real de revisión/anulación.
**Remediación/revaluación:** Rediseñar supervisión nominal o inefectiva.

## 17. Interfaces de consentimiento, preferencias y base legal
**Capa de fuente:** Ley de privacidad aplicable y controles internos de preferencias.
**Aplicabilidad:** Procesamiento basado en consentimiento, opt-in/opt-out u otras bases jurídicas específicas.
**Responsable:** Privacidad/legal con producto y datos.
**Procedimiento:** Registrar base o permiso aplicable, propagar elecciones, soportar retiro cuando proceda y separar consentimiento de usos basados válidamente en otra base.
**Evidencia:** Registro de base legal, estado de consentimiento/preferencia, versión de aviso, logs de propagación y excepciones.
**Revisión/prueba:** Rastrear cambios de preferencias a través de sistemas posteriores.
**Remediación/revaluación:** Corregir estados obsoletos/conflictivos y cesar procesamiento no autorizado.

## 18. Minimización de datos y gobernanza de características
**Capa de fuente:** Principios de minimización, ley aplicable y gobernanza de modelos.
**Aplicabilidad:** Características, prompts, embeddings, almacenes de contexto, logs y atributos de decisión.
**Responsable:** Propietario de modelo/datos con privacidad y producto.
**Procedimiento:** Exigir necesidad documentada para cada característica material y retirar datos redundantes, excesivamente granulares o injustificados.
**Evidencia:** Registro de características, justificación, pruebas de ablación cuando proceda y excepciones aprobadas.
**Revisión/prueba:** Desafiar periódicamente necesidad y sensibilidad.
**Remediación/revaluación:** Retirar/transformar datos y reprobar desempeño/riesgo.

## 19. Retención, eliminación y memoria del modelo
**Capa de fuente:** Deberes aplicables de retención/eliminación, política de registros y arquitectura.
**Aplicabilidad:** Datos de entrenamiento, prompts, historiales, embeddings, bases vectoriales, logs, caché, salidas y retroalimentación.
**Responsable:** Propietario de datos con privacidad, registros y plataforma.
**Procedimiento:** Definir calendarios, hold legal, propagación de eliminación, límites de memoria, backups y excepciones.
**Evidencia:** Calendario, trabajos de eliminación, verificación, holds y excepciones.
**Revisión/prueba:** Probar eliminación extremo a extremo en almacenes primarios y derivados cuando sea técnicamente viable.
**Remediación/revaluación:** Reparar rutas fallidas y revaluar arquitectura si la eliminación no es fiable.

## 20. Desidentificación, seudonimización y PETs
**Capa de fuente:** Ingeniería de privacidad, ley aplicable y estándares internos de seguridad.
**Aplicabilidad:** Usos basados en menor identificabilidad o tecnologías de mejora de privacidad.
**Responsable:** Ingeniería de privacidad/seguridad de datos.
**Procedimiento:** Seleccionar técnicas proporcionales, documentar modelo de amenaza y supuestos de reidentificación, y restringir claves de enlace/reversión.
**Evidencia:** Especificación técnica, controles de claves, pruebas de reidentificación, parámetros de privacidad y restricciones.
**Revisión/prueba:** Revaluar frente a nuevos datos auxiliares y ataques.
**Remediación/revaluación:** Reforzar transformación o dejar de afirmar desidentificación.

## 21. Interfaces de equidad y sesgo sin equivalencia legal falsa
**Capa de fuente:** NIST AI RMF, ley antidiscriminación/sector aplicable y política de IA responsable.
**Aplicabilidad:** Sistemas con posibles diferencias materiales entre grupos o proxies relevantes.
**Responsable:** Riesgo de IA/modelos con legal y negocio.
**Procedimiento:** Definir preguntas de equidad según contexto, categorías protegidas cuando apliquen, riesgo de proxies, cortes de desempeño, umbrales y criterios de escalamiento.
**Evidencia:** Plan de pruebas, métricas por subgrupo, análisis de proxies, revisión de aplicabilidad y decisiones.
**Revisión/prueba:** Probar disparidades adversas materiales y limitaciones de medición.
**Remediación/revaluación:** Ajustar datos, características, umbrales, proceso o caso y reprobar.

## 22. Acceso, identidad y administración privilegiada
**Capa de fuente:** Estándares de seguridad/IAM y requisitos de confidencialidad.
**Aplicabilidad:** Consolas, datasets, prompts, logs, feature stores, bases vectoriales, herramientas de etiquetado y sistemas de decisión.
**Responsable:** Seguridad/IAM y propietario de plataforma.
**Procedimiento:** Aplicar mínimo privilegio, autenticación fuerte, PAM, segregación, revisión periódica y revocación rápida.
**Evidencia:** Matriz de acceso, aprobaciones, MFA/PAM, revisiones y bajas.
**Revisión/prueba:** Muestrear accesos privilegiados y a datos sensibles.
**Remediación/revaluación:** Revocar excesos e investigar uso no autorizado.

## 23. Modelos, APIs y proveedores de datos terceros
**Capa de fuente:** Contratos, riesgo de terceros, privacidad, NIST AI RMF y cadena de suministro.
**Aplicabilidad:** Modelos externos, APIs alojadas, brokers, enriquecimiento, evaluadores y subprocesadores.
**Responsable:** Compras/riesgo de terceros con gobernanza IA, privacidad, seguridad y negocio.
**Procedimiento:** Evaluar uso y reutilización de datos, retención, subprocesadores, seguridad, privacidad, cambios de modelo, incidentes, auditoría, terminación y salida.
**Evidencia:** Due diligence, cláusulas, términos de procesamiento, model cards, evidencia y plan de salida.
**Revisión/prueba:** Revalidar proveedores de alto riesgo y cambios materiales.
**Remediación/revaluación:** Restringir datos, exigir cambios o salir del proveedor.

## 24. Procesamiento y despliegue transfronterizo
**Capa de fuente:** Reglas aplicables de transferencia/localización, contratos y gobernanza de privacidad.
**Aplicabilidad:** Datos, hosting de modelos, soporte, telemetría o decisiones que crucen jurisdicciones relevantes.
**Responsable:** Privacidad/legal con propietario cloud/plataforma.
**Procedimiento:** Mapear rutas, mecanismos/restricciones, acceso de soporte, subprocesadores y requisitos regionales sin asumir un mecanismo global único.
**Evidencia:** Mapa de transferencias, análisis legal, mecanismo contractual, arquitectura regional y lista de subprocesadores.
**Revisión/prueba:** Comparar hosting/soporte/telemetría reales con regiones aprobadas.
**Remediación/revaluación:** Reconfigurar routing/hosting o actualizar mecanismos legales.

## 25. Registro, trazabilidad y expedientes de decisión
**Capa de fuente:** Conceptos de trazabilidad NIST AI RMF, rendición de cuentas de privacidad y estándares de logging.
**Aplicabilidad:** Decisiones materiales y acciones de soporte.
**Responsable:** Propietario de plataforma/modelo con seguridad y negocio.
**Procedimiento:** Registrar versión, referencias de entradas pertinentes, decisión/salida, razones cuando corresponda, acciones humanas, anulaciones y estado de política, minimizando datos personales innecesarios.
**Evidencia:** Logs, esquema de expediente, retención, controles de integridad y accesos.
**Revisión/prueba:** Reconstruir decisiones muestreadas.
**Remediación/revaluación:** Reparar brechas y ajustar balance entre retención y minimización.

## 26. Monitoreo de deriva, daño de privacidad y abuso
**Capa de fuente:** Conceptos de monitoreo NIST AI RMF y controles internos de riesgo.
**Aplicabilidad:** Sistemas en producción durante su operación.
**Responsable:** Propietario del modelo, riesgo IA, privacidad y operaciones.
**Procedimiento:** Monitorear deriva, calidad, quejas, inferencias sensibles, violaciones de política, abuso, desempeño por grupo y uso inesperado.
**Evidencia:** Dashboards, alertas, umbrales, investigaciones y tendencias.
**Revisión/prueba:** Validar cobertura de alertas y muestrear resoluciones.
**Remediación/revaluación:** Ajustar, suspender, revertir o rediseñar al superar umbrales.

## 27. Coordinación de incidentes, quejas y solicitudes de derechos
**Capa de fuente:** Deberes aplicables de privacidad/incidentes/derechos y respuesta interna.
**Aplicabilidad:** Eventos de seguridad/privacidad, salidas dañinas, quejas, solicitudes y desafíos.
**Responsable:** Operaciones de incidentes/privacidad con gobernanza IA y negocio.
**Procedimiento:** Enrutar al proceso correcto, preservar evidencia y cumplir plazos aplicables.
**Evidencia:** Expedientes, triage, notificaciones, respuestas, contención y lecciones aprendidas.
**Revisión/prueba:** Ejercitar escenarios representativos de incidentes IA/privacidad.
**Remediación/revaluación:** Corregir fallas de enrutamiento, control o modelo y revaluar riesgo.

## 28. Gestión de cambios y actualizaciones materiales del modelo
**Capa de fuente:** Cambio interno, ciclo de vida NIST AI RMF, terceros y deberes regulatorios aplicables.
**Aplicabilidad:** Cambios de modelo/versión, prompt, recuperación, características, datos, umbral, proveedor, propósito o despliegue.
**Responsable:** Producto/modelo con gobernanza IA, privacidad y seguridad.
**Procedimiento:** Clasificar materialidad, identificar evaluaciones/avisos/contratos/pruebas afectados, aprobar y mantener rollback.
**Evidencia:** Ticket, análisis de impacto, resultados, aprobaciones, release notes y plan de reversión.
**Revisión/prueba:** Confirmar que producción coincide con versión aprobada.
**Remediación/revaluación:** Revertir cambios no autorizados o insuficientemente evaluados.

## 29. Métricas, KRI/KPI y reporte gerencial
**Capa de fuente:** Gobernanza interna y conceptos de medición NIST.
**Aplicabilidad:** Gobernanza de cartera y sistema.
**Responsable:** Liderazgo de gobernanza IA/privacidad.
**Procedimiento:** Medir cobertura de inventario, evaluaciones, derechos/apelaciones, incidentes, deriva, terceros, excepciones, remediación vencida y señales materiales de disparidad/riesgo.
**Evidencia:** Definiciones, dashboards, tendencias, umbrales y acciones gerenciales.
**Revisión/prueba:** Verificar linaje de métricas y evitar agregación engañosa.
**Remediación/revaluación:** Corregir indicadores débiles y escalar brechas sostenidas.

## 30. Aseguramiento, pruebas e inspección de evidencia
**Capa de fuente:** Auditoría/aseguramiento interno, evaluación NIST AI RMF y requisitos aplicables.
**Aplicabilidad:** Sistemas de alto riesgo y muestras de cartera.
**Responsable:** Auditoría/aseguramiento independiente con apoyo experto.
**Procedimiento:** Probar diseño y efectividad operativa mediante evidencia, muestreo, pruebas técnicas, entrevistas, solicitudes/apelaciones y reconstrucción de decisiones.
**Evidencia:** Plan, papeles de trabajo, hallazgos, respuestas, remediación y cierre.
**Revisión/prueba:** Mantener independencia proporcional al riesgo y no depender solo de autoatestación.
**Remediación/revaluación:** Llevar hallazgos a cierre verificado y volver a probar correcciones materiales.

## 31. Localización, accesibilidad y gestión de fuente controlada
**Capa de fuente:** Controles de liberación del proyecto y obligaciones aplicables de accesibilidad/comunicación.
**Aplicabilidad:** Ediciones controladas en inglés, es-419 y pt-BR y sus artefactos.
**Responsable:** Documentación/release con revisión terminológica de privacidad/legal cuando corresponda.
**Procedimiento:** Preservar distinciones de fuentes, paridad de capítulos, terminología, calificadores legales, estructura accesible, metadatos de idioma y aviso de traducción no oficial.
**Evidencia:** Fuentes, resultados de paridad, controles de accesibilidad, notas terminológicas e historial.
**Revisión/prueba:** Comparar capítulos, encabezados, calificadores clave y renderizado entre idiomas.
**Remediación/revaluación:** Corregir defectos antes de congelar candidato.

## 32. Liberación, procedencia y hoja de ruta de implementación
**Capa de fuente:** Política de liberación del repositorio y procedimiento controlled-build.
**Aplicabilidad:** Liberación final del Manual 28 y futuras revisiones.
**Responsable:** Propietario de liberación con gobernanza IA/privacidad.
**Procedimiento:** Revalidar fuentes; congelar fuentes; construir reproduciblemente DOCX/PDF EN/es-419/pt-BR; vincular SHA-256; ejecutar QA de paquete/accesibilidad/render; staged exacto; verificar Manual 27 publicado; reconciliar catálogo y registro.
**Evidencia:** Registro de fuentes, workflow/artifact, manifiesto, seis hashes, QA, commit de staging, checks exact-head y merge.
**Revisión/prueba:** Fallar cerrado ante predecesor faltante, binario cambiado, gate fallido, defecto material o supuesto de fuente obsoleto.
**Remediación/revaluación:** Regenerar solo cuando un defecto determinista o cambio material de fuente/control lo requiera; de lo contrario preservar bytes revisados.