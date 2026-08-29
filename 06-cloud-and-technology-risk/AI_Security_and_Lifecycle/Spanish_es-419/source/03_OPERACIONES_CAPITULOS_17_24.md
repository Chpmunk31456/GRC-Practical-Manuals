# Manual 07 — Seguridad de IA y Controles del Ciclo de Vida
## Fuente controlada en español latinoamericano — Capítulos 17–24

> Traducción de trabajo para revisión semántica humana. Esta guía defensiva original no garantiza seguridad ni reemplaza decisiones de riesgo específicas de la organización.

## Capítulo 17 — Endurecimiento del despliegue

El despliegue debe utilizar configuraciones aprobadas, identidades de mínimo privilegio, secretos protegidos, rutas de red controladas, logging, monitoreo y capacidad de rollback apropiados al riesgo.

El sistema desplegado debe compararse con el candidato de liberación validado para evitar introducir deriva relevante para la seguridad durante la promoción.

## Capítulo 18 — Monitoreo y alertas

El monitoreo debe concentrarse en indicadores vinculados con riesgos conocidos: accesos inusuales, cambios de permisos, fallas repetidas de controles, actividad inesperada de herramientas, manejo de datos sensibles, cambios de dependencias, degradación de disponibilidad y excepciones de política.

Las alertas deben tener responsables, reglas de severidad, rutas de escalamiento y expectativas documentadas de respuesta.

## Capítulo 19 — Logging y preservación de evidencia

Los logs relevantes para seguridad deben conservar contexto suficiente para apoyar investigaciones respetando al mismo tiempo privacidad y minimización de datos. Los registros útiles pueden incluir identidades, marcas de tiempo, referencias de modelo/configuración, invocaciones de herramientas, decisiones de política, referencias de recuperación y eventos de cambio.

La retención debe estar definida y el acceso a los logs controlado.

## Capítulo 20 — Respuesta a incidentes

Los eventos de seguridad relacionados con IA deben integrarse al proceso de incidentes de la organización. Los planes de respuesta deben identificar opciones de contención, evidencia a preservar, contactos de proveedores, rutas de notificación, pasos de recuperación y criterios para suspender o restringir el servicio.

## Capítulo 21 — Mecanismos de rollback y detención

Los sistemas con impacto material operativo o de seguridad deben contar con mecanismos de rollback o detención probados. La autoridad para invocarlos debe ser explícita.

Un control que exista únicamente en papel no debe acreditarse hasta que haya sido validado técnica y operacionalmente.

## Capítulo 22 — Gestión de cambios y configuración

Los cambios en modelos, recuperación, prompts, instrucciones del sistema, herramientas, permisos, fuentes de datos, alojamiento, guardrails o proveedores pueden modificar la postura de seguridad. Los registros de cambio deben clasificar la materialidad e identificar qué validación previa continúa siendo válida.

## Capítulo 23 — Gobierno de excepciones

Las excepciones de seguridad deben registrar el requisito no satisfecho, justificación de negocio, controles compensatorios, responsable, riesgo residual, aprobador, fecha de expiración y requisito de monitoreo.

Las excepciones de alto riesgo no deben convertirse en permanentes mediante extensiones administrativas repetidas sin reevaluación.

## Capítulo 24 — Reevaluación periódica de seguridad

La reevaluación periódica debe examinar si amenazas, dependencias, accesos, uso de datos, estado de proveedores, comportamiento operativo y suposiciones previas continúan siendo válidos.

La evidencia debe mostrar qué se revisó, qué cambió, qué continúa siendo aceptable y qué acción adicional se requiere.
