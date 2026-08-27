# Manual 07 — Seguridad de IA y Controles del Ciclo de Vida
## Fuente controlada en español latinoamericano — Capítulos 25–32

> Traducción de trabajo para revisión semántica humana. Esta guía defensiva original no garantiza seguridad ni reemplaza la revisión específica de la organización.

## Capítulo 25 — Cambio de proveedores y dependencias

Los cambios de proveedor o dependencia deben evaluarse por su efecto en seguridad antes de adoptarse. Los cambios relevantes incluyen alojamiento, versión del modelo, arquitectura del servicio, procesamiento de datos, subprocesadores, métodos de acceso, logging, controles de seguridad y compromisos contractuales de notificación.

## Capítulo 26 — Resiliencia y operación degradada

La planificación de seguridad debe considerar cómo se comporta el sistema cuando modelos, APIs, recuperación, monitoreo o servicios externos se degradan o no están disponibles. Los modos alternos no deben eludir silenciosamente controles de seguridad, aprobación o protección de datos.

## Capítulo 27 — Consideraciones de respaldo y recuperación

La planificación de recuperación debe identificar qué configuraciones, prompts, políticas, índices, credenciales, evidencia y dependencias son necesarias para restaurar un estado controlado conocido. Los procedimientos de recuperación deben validarse en proporción a la criticidad.

## Capítulo 28 — Retiro y desmantelamiento

El retiro debe revocar identidades, credenciales e integraciones; deshabilitar endpoints; eliminar o archivar datos conforme a requisitos; preservar evidencia obligatoria; cerrar acceso de proveedores; y documentar obligaciones no resueltas.

## Capítulo 29 — Métricas de seguridad e informes de gestión

Las métricas deben estar vinculadas con decisiones. Los informes útiles pueden incluir hallazgos materiales, excepciones, estado de reevaluación, tendencias de incidentes, cambios de dependencias, cobertura de validación, remediación vencida e indicadores de salud de controles.

## Capítulo 30 — Limitaciones del aseguramiento de seguridad

Ninguna suite automatizada de pruebas, checklist de controles, revisión de seguridad o workflow del repositorio puede establecer que un sistema de IA esté libre de debilidades. Las declaraciones de aseguramiento deben identificar alcance, período, evidencia y limitaciones que las respaldan.

## Capítulo 31 — Mejora continua

Las lecciones de incidentes, casi incidentes, pruebas, cambios de proveedores, retroalimentación de usuarios y fallas de controles deben retroalimentar modelos de amenazas, planes de validación, controles operativos y capacitación.

## Capítulo 32 — Límite de liberación del manual

Antes de publicar este manual deben completarse la verificación de fuentes, el maestro controlado completo en inglés, la revisión técnica/de seguridad, la revisión semántica de `es-419` y `pt-BR`, la revisión de gráficos/accesibilidad, QA documental y por página, procedencia, auditoría de seguridad del repositorio y la Aprobación Humana Final de Liberación.

Los cambios materiales de contenido posteriores a la aprobación humana reabren los controles afectados.
