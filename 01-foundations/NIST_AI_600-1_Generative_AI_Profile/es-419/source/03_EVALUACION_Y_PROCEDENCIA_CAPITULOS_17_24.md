# Manual 04 — Implementación del Perfil de IA Generativa NIST AI 600-1
## Fuente controlada en español latinoamericano — Capítulos 17–24

> Traducción asistida por máquina para revisión controlada. Este conjunto apoya gobernanza basada en evidencia y no reproduce el texto de NIST. La aprobación semántica humana sigue siendo obligatoria antes de la publicación.

## Capítulo 17 — Estrategia de evaluación

La evaluación comienza con una pregunta documentada: qué debe poder hacer el sistema, qué debe evitar, bajo qué condiciones y con qué nivel de confianza. La estrategia debería definir objetivos, escenarios, conjuntos de datos, evaluadores, métodos, umbrales, muestreo, limitaciones y reglas de decisión.

La evaluación debería incluir uso normal representativo y uso indebido plausible. Los sistemas de alto impacto deberían incorporar desafío independiente o separación entre quienes construyen y quienes toman la decisión final de liberación.

## Capítulo 18 — Gobernanza de datos de prueba y escenarios

Los datos de prueba deberían ser trazables a su propósito. Los equipos deberían registrar origen, cobertura, sensibilidad, transformación, representatividad, limitaciones conocidas y si los datos pueden retenerse o compartirse.

Los datos sintéticos pueden mejorar cobertura, pero no deben asumirse representativos de poblaciones reales o comportamiento adversarial. Cuando se usen, el registro de evaluación debería indicar por qué son apropiados y qué puntos ciegos permanecen.

## Capítulo 19 — Umbrales de aceptación y criterios de decisión

Los umbrales deberían establecerse antes de las pruebas finales cuando sea práctico y reflejar consecuencias, no conveniencia. Un asistente de redacción de bajo impacto puede tolerar tasas de falla distintas a un sistema que influya en decisiones de seguridad, finanzas, salud, empleo o protección.

La decisión de liberación debería registrar si cada umbral aprobó, falló, fue aceptado condicionalmente o fue eximido. Las exenciones requieren fundamento, responsable, control compensatorio, fecha de vencimiento o revisión y aprobación del riesgo residual.

## Capítulo 20 — Red teaming y evaluación adversarial

La evaluación adversarial debería probar si los controles siguen siendo efectivos cuando usuarios o contenido externo intentan evadirlos deliberadamente. Los casos deberían abordar manipulación directa de prompts, instrucciones indirectas, envenenamiento de recuperación, abuso de herramientas, fallas de identidad o permisos, extracción de datos, revelación del prompt del sistema y encadenamiento inseguro de acciones cuando aplique.

Los resultados de red team deben tratarse como evidencia, no como exhibición. Pruebas repetidas sin responsable de remediación ni re-pruebas no deben representarse como aseguramiento.

## Capítulo 21 — Controles de procedencia de contenido

La procedencia debería responder preguntas prácticas: qué modelo y configuración produjo la salida, qué datos o fuentes influyeron materialmente, qué transformaciones ocurrieron y quién o qué aprobó el uso posterior.

La organización debería seleccionar mecanismos proporcionales al riesgo, como enlaces a fuentes, hashes de artefactos, identificadores de modelo/versión, versiones de prompts o políticas, registros de transformación, aprobaciones humanas o metadatos firmados. La procedencia mejora trazabilidad, pero no prueba por sí sola exactitud factual u origen lícito.

## Capítulo 22 — Paquete de pruebas previo al despliegue

Un paquete de evidencia previo al despliegue debería reunir lo necesario para una decisión responsable. Como mínimo debería incluir inventario del sistema/caso de uso, registro de riesgos e impactos, plan y resultados de evaluación, pruebas de seguridad/adversariales, revisión de privacidad/datos cuando aplique, evidencia de proveedores/componentes, hallazgos y excepciones abiertos, umbrales de monitoreo, plan de detener/revertir y registro de aprobación.

El paquete debe versionarse y vincularse con el candidato exacto de liberación.

## Capítulo 23 — Preparación para divulgación y escalamiento de incidentes

Antes del despliegue, la organización debería definir qué eventos califican como incidentes de IA generativa, quién debe ser informado, qué evidencia debe preservarse y cuándo puede requerirse notificación o divulgación externa.

Las categorías pueden incluir salida dañina, exposición de datos, acción no autorizada, evasión de controles, falla de proveedor, desinformación material, autonomía inesperada, incumplimiento regulatorio o contractual o violación repetida de umbrales. Los criterios de escalamiento deberían ser suficientemente explícitos para evitar improvisación durante un evento.

## Capítulo 24 — Suficiencia de evidencia y calidad de revisión

La evidencia debería demostrar que un control operó para el sistema y periodo pertinentes. Políticas, capturas de pantalla, afirmaciones de proveedores o cuestionarios pueden apoyar la evidencia, pero no deben tratarse automáticamente como prueba de efectividad.

Los revisores deberían considerar relevancia, confiabilidad, integridad, oportunidad e independencia. Cuando la evidencia sea débil o no esté disponible, el registro debe declarar esa limitación y su efecto sobre el riesgo residual o la confianza en la liberación.
