# Manual 08 — Ciclo de vida de riesgo de proveedores y terceros
## Borrador controlado es-419 — Capítulos 01–08

> Borrador de localización para revisión semántica humana. Esta guía original operacionaliza la línea base controlada sin reproducir texto de normas y no certifica a ningún proveedor ni elimina el riesgo de terceros.

## Capítulo 01 — Objetivo y ciclo de vida de TPRM

La gestión de riesgos de terceros debe gobernar todo el ciclo de la relación: ingreso, clasificación, debida diligencia, decisión de riesgo, contratación, incorporación, monitoreo, gestión de incidentes y cambios, reevaluación y salida.

El proceso debe aplicarse de forma proporcional según aquello a lo que el proveedor puede acceder, influir, procesar, alojar, operar o interrumpir.

## Capítulo 02 — Inventario de proveedores y responsables

Mantenga un inventario controlado de proveedores, prestadores de servicios, subencargados, proveedores de IA/modelos, proveedores de datos, API, servicios de alojamiento y otras dependencias externas relevantes.

Cada registro debe identificar responsable de negocio, servicio, datos tratados, dependencias de sistemas, contrato, criticidad, geografía cuando corresponda, exposición a cuartas partes, fecha de renovación, nivel de monitoreo y requisitos de salida.

## Capítulo 03 — Criticidad y riesgo inherente

La criticidad pregunta qué ocurre si el proveedor falla; el riesgo inherente pregunta qué exposición existe antes de considerar controles. Están relacionados, pero no son lo mismo.

Los factores pueden incluir acceso a datos sensibles, conectividad privilegiada, acceso a producción, dependencia operativa, concentración, posibilidad de sustitución, impacto financiero, exposición regulatoria, autonomía de IA, dependencia de modelos o datos y consecuencias para la continuidad del negocio.

## Capítulo 04 — Planificación de la debida diligencia

La debida diligencia debe basarse en evidencia y ser proporcional. El plan de revisión debe identificar las preguntas que deben resolverse, la evidencia necesaria, los revisores y los umbrales de aceptación.

La evidencia posible incluye políticas, informes independientes, certificaciones, información de arquitectura, resultados de pruebas, historial de incidentes, evidencia de resiliencia, documentación de privacidad, compromisos contractuales, información financiera y entrevistas dirigidas.

Un cuestionario por sí solo no constituye aseguramiento para un proveedor material.

## Capítulo 05 — Revisión de seguridad, privacidad y resiliencia

La revisión debe determinar si los controles del proveedor son apropiados para el servicio y la exposición. Seguridad, privacidad y resiliencia deben evaluarse como disciplinas conectadas y no como cuestionarios aislados.

La revisión debe abordar identidad, acceso, protección de datos, registros, gestión de vulnerabilidades, respuesta a incidentes, capacidad de recuperación, subcontratación, ubicación, retención, eliminación y continuidad del servicio cuando corresponda.

## Capítulo 06 — Proveedores de IA y dependencias de modelos/componentes

La revisión de proveedores de IA debe identificar proveedores de modelos, inferencia alojada, servicios de ajuste fino, proveedores de datos, servicios de seguridad, fuentes de recuperación, proveedores de agentes/herramientas y otros componentes de IA.

Las preguntas clave incluyen uso de datos, comportamiento de entrenamiento o retención, notificación de cambios de modelo/versión, límites de seguridad, controles de contenido y abuso, disponibilidad del servicio, términos de propiedad intelectual, evidencia de auditoría, notificación de incidentes y opciones de salida.

## Capítulo 07 — Decisión de riesgo y excepciones

Todo resultado material de debida diligencia debe producir una decisión: aprobar, aprobar condicionalmente, exigir remediación, restringir alcance, aplazar o rechazar.

Las excepciones deben registrar el requisito incumplido, justificación de negocio, control compensatorio, responsable, riesgo residual, aprobador, fecha de vencimiento y requisito de monitoreo. Deben evitarse las excepciones permanentes sin revisión periódica.

## Capítulo 08 — Puerta de incorporación con cierre por defecto

La incorporación debe bloquearse cuando la debida diligencia requerida esté incompleta, falte evidencia crítica, los hallazgos de alto riesgo carezcan de tratamiento aprobado, los términos contractuales obligatorios estén sin resolver o falte una aprobación humana obligatoria.

Un proveedor no debe representarse como “aprobado” solo porque terminó el proceso de compras. Un cambio material posterior —por ejemplo, un nuevo subencargado, modelo de servicio, uso de datos, componente de IA, ubicación de alojamiento o arquitectura de seguridad— puede reabrir la revisión afectada.