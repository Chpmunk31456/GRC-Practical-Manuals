# Manual 07 — Seguridad de IA y Controles del Ciclo de Vida
## Fuente controlada en español latinoamericano — Capítulos 09–16

> Traducción de trabajo para revisión semántica humana. Esta guía defensiva original no reproduce texto de estándares ni garantiza seguridad.

## Capítulo 09 — Seguridad de recuperación y fuentes de conocimiento

Las fuentes de recuperación deben tratarse como entradas influenciadas externamente. Los controles deben abordar admisión de fuentes, autoridad de escritura, validación de contenido, control de acceso, separación entre tenants, contenido obsoleto, exposición de datos sensibles y eliminación.

Los almacenes vectoriales e índices deben heredar controles apropiados de clasificación de datos, acceso, retención, logging y respaldo.

## Capítulo 10 — Manejo de secretos y datos sensibles

Los secretos no deben incorporarse en prompts, código fuente, notebooks o contexto del modelo cuando existan alternativas más seguras. Las credenciales de servicio deben estar acotadas, rotarse, monitorearse y almacenarse mediante mecanismos aprobados de gestión de secretos.

Los logs, trazas, evaluaciones y artefactos de soporte también deben revisarse para detectar exposición no prevista de datos sensibles.

## Capítulo 11 — Cadena de suministro de modelos y componentes

La revisión de seguridad debe incluir origen del modelo, paquetes, contenedores, adaptadores, conjuntos de datos, APIs, plugins, servicios de seguridad y dependencias de alojamiento. Los componentes deben versionarse y ser trazables para que los equipos de seguridad puedan evaluar el impacto de cambios de proveedor o componente.

Los cambios materiales de proveedores deben activar una reevaluación en lugar de heredarse silenciosamente.

## Capítulo 12 — Evaluación y validación de seguridad

La evaluación de seguridad debe utilizar objetivos y resultados esperados basados en riesgo. La validación debe cubrir si los controles de acceso, límites de datos, permisos de herramientas, controles de recuperación, manejo de salidas, comportamiento de dependencias y restricciones operativas funcionan como se espera bajo condiciones representativas y de frontera.

La evidencia de pruebas debe registrar configuración, alcance, resultado, limitación y remediación.

## Capítulo 13 — Desafío independiente

El desafío independiente debe probar si las suposiciones y límites de control siguen siendo válidos fuera de condiciones normales de operación. La revisión debe estar autorizada, acotada y basada en evidencia.

La actividad de desafío sin responsable de remediación ni validación de seguimiento no debe representarse como aseguramiento.

## Capítulo 14 — Guardrails y controles deterministas

Los guardrails pueden reducir riesgo, pero deben combinarse con controles de seguridad deterministas cuando las consecuencias sean significativas. La autorización, validación de entradas, validación de salidas, listas permitidas, límites transaccionales, controles de red y aprobación humana pueden ofrecer una aplicación más fuerte que el comportamiento del modelo por sí solo.

## Capítulo 15 — Supervisión humana para acciones sensibles a seguridad

Debe requerirse aprobación humana cuando las acciones automatizadas puedan generar impacto material de seguridad o negocio y el sistema no pueda limitar el riesgo de forma confiable mediante controles deterministas.

Los revisores necesitan suficiente contexto, tiempo, competencia y autoridad para rechazar o detener la acción. Un paso nominal de aprobación sin información significativa no constituye supervisión eficaz.

## Capítulo 16 — Paquete de seguridad previo al despliegue

Antes de liberar, reúna el modelo de amenazas vigente, arquitectura, inventario de activos, resultados de validación, hallazgos abiertos, evidencia de proveedores, revisión de identidad/permisos, umbrales de monitoreo, plan de incidentes, plan de rollback/detención, excepciones y aprobaciones.

El paquete debe corresponder al candidato exacto de liberación y los cambios materiales deben reabrir la evidencia afectada.
