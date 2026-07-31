# Capítulo 40 — Registros y registros

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador del Capítulo 40 anterior en conflicto.

## Requisito

Los sistemas de IA de alto riesgo deben estar diseñados para permitir el registro automático de los acontecimientos a lo largo de la vida útil del sistema en la medida apropiada para el propósito previsto. Los proveedores y los implementadores deben conservar registros y registros conexos durante los períodos exigidos por el Reglamento (UE) 2024/1689, en su versión modificada, y otras leyes aplicables.

## Explicación en lenguaje sencillo

Los registros son la pista de evidencia operativa de cómo se comporta un sistema de IA de alto riesgo. Apoyan el monitoreo, la investigación de incidentes, la supervisión humana, la evaluación de la conformidad, las medidas correctivas y la revisión regulatoria.

La Ley de IA no crea un período de retención universal para cada registro. La retención debe ser determinada por el papel del actor, el tipo de registro, el artículo aplicable, la ley sectorial, los requisitos de protección de datos, las obligaciones contractuales, los plazos de prescripción, y los litigios o las retenciones reglamentarias.

## Requisitos de registro

El diseño de registro deberá tener en cuenta, según proceda:

1. versión de sistema y modelo;
2. fecha y hora de la operación;
3. fuente de entrada y contexto de procesamiento pertinente;
4. producción, puntuación, recomendación o decisión;
5. la confianza o la información relativa a los umbrales, cuando proceda;
6. revisión humana, intervención, anulación o escalada;
7. errores, anomalías, controles fallidos y eventos de seguridad;
8. cambios de configuración, rapidez, recuperación y dependencia;
9. identidad o función de los operadores autorizados cuando sea lícito y necesario;
10. vínculos con quejas, incidentes, medidas correctivas y registros de seguimiento.

## Controles de seguridad y protección de datos

El registro no debe convertirse en vigilancia incontrolada ni en una recopilación excesiva de datos personales. La organización debe definir el propósito legítimo, la minimización de datos, las restricciones de acceso, la protección de la integridad, la retención, la eliminación y los procedimientos de exportación seguros.

## Ejemplo de GlobalWay

El sistema de reclutamiento de alto riesgo de GlobalWay registra la versión del modelo de producción, la marca de tiempo de procesamiento de candidatos, el resultado de puntuación relevante, el umbral aplicado, la identidad del revisor, la decisión del revisor, la razón de anulación y cualquier error del sistema.

## Actividad de control

El proveedor debe definir las capacidades de registro durante el diseño, y el implementador debe asegurarse de que los registros estén habilitados, protegidos, revisados y retenidos de acuerdo con un calendario aprobado. Cualquier brecha de registro que impida el monitoreo, supervisión, investigación o respuesta regulatoria efectiva debe bloquear el despliegue o desencadenar acciones correctivas.

## Pruebas

- especificación de registro;
- diccionario de datos;
- la muestra de registros de eventos;
- configuración de control de acceso;
- el calendario de retención;
- los procedimientos de supresión y retención legal;
- controles de integridad y pruebas de manipulación;
- los registros de seguimiento y revisión;
- los vínculos entre incidentes y medidas correctivas;
- evaluación de la privacidad.

## Prueba de auditoría

Seleccione una muestra de eventos del sistema de alto riesgo y confirme que los registros son generados, completos, vinculados a versiones, protegidos contra cambios no autorizados, accesibles a revisores autorizados, retenidos bajo un cronograma aprobado, y usados en monitoreo e investigación de incidentes.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: artículo 12 y obligaciones de los agentes aplicables en materia de conservación y acceso de troncos.
- RGPD y normas de conservación específicas del sector cuando se trate de datos personales o registros regulados.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
