# Manual 05 — Auditoría y Aseguramiento de IA
## Fuente localizada es-419 — Capítulos 01–08

> Borrador de localización para revisión semántica humana. Guía original de implementación de auditoría. Este material utiliza la línea base controlada de normas y la referencia de práctica profesional AAIA sin reproducir contenido propietario de normas, capacitación o exámenes. Por sí mismo no constituye una opinión de auditoría ni una certificación.

## Capítulo 01 — Mandato y objetivo de auditoría

Toda auditoría de IA comienza con un mandato documentado. El mandato identifica quién solicitó el trabajo, por qué se realiza la auditoría, qué decisión apoyarán los resultados, la autoridad del equipo auditor y cualquier restricción de acceso o reporte.

El objetivo de auditoría debe redactarse como una declaración comprobable. “Revisar la gobernanza de IA” es demasiado amplio; “determinar si los sistemas de IA en producción por encima del umbral de alto riesgo de la organización cuentan con responsables aprobados, evaluaciones de riesgo vigentes, evidencia de liberación, monitoreo y aceptación documentada del riesgo residual” es auditable.

## Capítulo 02 — Criterios y límite del aseguramiento

Los criterios de auditoría deben identificarse antes del trabajo de campo. Pueden provenir de leyes, regulaciones, contratos, políticas internas, normas aprobadas, compromisos de la dirección, marcos de control o requisitos operativos definidos.

El registro de auditoría debe distinguir los criterios obligatorios de la orientación y las referencias de práctica profesional. ISACA AAIA se utiliza aquí como referencia de práctica profesional para capacidad y cobertura de dominios de auditoría; no es una ley, regulación, norma ISO, certificación organizacional ni una opinión de auditoría.

## Capítulo 03 — Alcance y límite del sistema

El alcance debe identificar los sistemas de IA, procesos de negocio, entidades legales, ubicaciones, entornos, período, proveedores, conjuntos de datos, modelos, interfaces y etapas del ciclo de vida incluidos. Las exclusiones requieren justificación.

Las auditorías de IA deben descomponer los sistemas en componentes pertinentes: datos, modelo, prompts, recuperación, herramientas, identidades, infraestructura, monitoreo, revisión humana, proveedores y procesos de cambio. Un alcance limitado al modelo puede omitir riesgos materiales en la orquestación o en acciones posteriores.

## Capítulo 04 — Independencia, competencia y conflictos

El líder de auditoría debe evaluar si el equipo posee independencia y competencia suficientes para el objetivo. Las pruebas técnicas de alto impacto pueden requerir especialistas en seguridad, privacidad, ciencia de datos, riesgo de modelos, asuntos legales, accesibilidad, seguridad operacional o el dominio correspondiente.

Los conflictos deben revelarse cuando los auditores hayan diseñado, implementado, aprobado u operado materialmente el control evaluado. Cuando no sea posible una independencia organizacional plena, deben documentarse la limitación y la revisión compensatoria.

## Capítulo 05 — Planificación de auditoría y priorización por riesgo

La planificación debe priorizar áreas donde una falla de control pueda causar daño material o donde la calidad de la evidencia sea incierta. Las entradas pueden incluir hallazgos anteriores, incidentes, registros de riesgo, obligaciones regulatorias, criticidad del modelo, sensibilidad de los datos, autonomía, dependencia de proveedores y cambios recientes.

El plan de auditoría debe indicar procedimientos, fuentes de evidencia, enfoque de muestreo, pruebas técnicas, entrevistas, auditores responsables, calendario y entregables esperados.

## Capítulo 06 — Estrategia y suficiencia de la evidencia

La evidencia debe ser pertinente al criterio de auditoría y suficientemente confiable para sustentar la conclusión. Las políticas demuestran intención de diseño; no prueban la operación. Las capturas de pantalla muestran un momento específico; pueden no demostrar operación sostenida. Las afirmaciones de proveedores pueden apoyar una conclusión, pero deben corroborarse cuando el riesgo del proveedor sea material.

La evidencia debe evaluarse por pertinencia, confiabilidad, integridad, oportunidad, reproducibilidad cuando corresponda e independencia respecto del propietario del control.

## Capítulo 07 — Muestreo y definición de la población

El muestreo comienza definiendo la población. Algunos ejemplos son todos los sistemas de IA en producción, todos los casos de uso de alto riesgo, todas las liberaciones de modelos de un período, todos los proveedores críticos o todos los incidentes que alcancen un umbral de severidad.

El método de muestreo debe reflejar el objetivo y el riesgo de auditoría. El muestreo por juicio puede enfocarse en elementos de alto riesgo; las técnicas estadísticas pueden ser apropiadas para poblaciones homogéneas. Deben revelarse las limitaciones de la muestra y las partes no examinadas de la población.

## Capítulo 08 — Ciclo de vida de auditoría y controles de calidad fail-closed

El ciclo de vida controlado de auditoría es:
1. mandato y alcance;
2. criterios y plan de evidencia;
3. trabajo de campo y pruebas;
4. hallazgos y severidad;
5. respuesta de la dirección;
6. validación de remediación;
7. cierre y seguimiento.

Los controles de calidad fallan de manera cerrada cuando la evidencia requerida no está disponible, existen preocupaciones de independencia sin resolver, las pruebas están incompletas, quedan comentarios abiertos del revisor, cambios materiales de alcance invalidan procedimientos o falta una aprobación humana obligatoria.

El QA automatizado del repositorio respalda la consistencia del paquete del manual; no reemplaza el juicio del auditor ni la aprobación humana de publicación.