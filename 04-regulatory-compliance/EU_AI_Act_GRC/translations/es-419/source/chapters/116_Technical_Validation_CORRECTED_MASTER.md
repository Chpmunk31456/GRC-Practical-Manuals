# Capítulo 116 — Validación técnica

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador del Capítulo 116 anterior en conflicto.

## Requisito

Los proveedores de sistemas de IA de alto riesgo deben establecer y documentar la validación y las pruebas adecuadas al propósito y los riesgos previstos del sistema, incluida la información requerida por el artículo 11 y el anexo IV y los requisitos de rendimiento, robustez, seguridad cibernética y supervisión humana aplicables al sistema. Otras organizaciones que desarrollen, adquieran, integren o desplieguen sistemas de IA de materiales deben aplicar una validación técnica proporcionada antes de la liberación y después del cambio de material para que puedan demostrar que la configuración de producción opera dentro de los límites aprobados y que pueden cumplir sus propias obligaciones legales y operativas.

## Explicación en lenguaje sencillo

La Ley de IA de la UE no impone un procedimiento de validación universal a todos los sistemas y actores de IA. El deber exacto depende de la clasificación y el papel. Para los sistemas de IA de alto riesgo, los proveedores deben mantener la gestión de riesgos, documentación técnica, pruebas, precisión, robustez, seguridad cibernética y pruebas de gestión de calidad. Los empleados y otros agentes de la cadena de valor necesitan pruebas de validación suficientes para utilizar el sistema de acuerdo con las instrucciones, ejercer supervisión, supervisar el funcionamiento y reevaluar los cambios.

## Requisitos de validación

El plan de validación debe abordar, según proceda:

1. el agente regulado, la clasificación, la finalidad prevista y la activación legal;
2. sistema, modelo, datos, prompt, herramienta, software, firmware y versión de configuración;
3. uso indebido previsible y condiciones de funcionamiento razonablemente previsibles;
4. precisión, robustez, fiabilidad, consistencia y límites de error;
5. datos de ensayo representativos y adecuados al contexto y métricas de rendimiento;
6. subgrupo, accesibilidad y rendimiento específico para cada contexto, cuando proceda;
7. control de la supervisón humana, anulación, parada, escalada y seguridad;
8. seguridad cibernética, abuso, fugas, manipulación y resistencia a la dependencia;
9. registro, trazabilidad, seguimiento, captura de pruebas y vinculación de versiones;
10. integración, latencia, disponibilidad, failover y comportamiento en modo degradado;
11. criterios de aceptación, limitaciones no resueltas, medidas correctivas y riesgo residual;
12. revisión independiente y decisión de liberación autorizada.

## Ejemplo de GlobalWay

GlobalWay valida un sistema de recomendaciones de interrupción de viajes utilizando datos equivalentes a la producción, condiciones de red degradadas, itinerarios inusuales, entradas multilingües, escenarios de sobrecarga humana y simulaciones de falla del proveedor. Registra los roles del proveedor y el implementador, la versión de producción probada, instrucciones aplicables, limitaciones, criterios de aceptación, desviaciones sin resolver y la base para la liberación.

## Actividad de control

Un sistema de IA de alto riesgo no debe ser liberado por su proveedor hasta que se cumplan los requisitos aplicables de gestión de riesgos, documentación, pruebas, conformidad y gestión de calidad. GlobalWay no debe poner en producción ningún sistema de IA de material hasta que haya obtenido y evaluado pruebas de validación suficientes para su papel real, uso previsto, responsabilidades de supervisión y riesgo.

## Pruebas

- evaluación de las funciones jurídicas y de clasificación;
- plan de validación aprobado;
- versión y registro de configuración;
- datos de ensayo, justificación de la representatividad y descripción del entorno;
- métricas, resultados de las pruebas, registros y registros de defectos;
- criterios de aceptación, limitaciones y excepciones;
- el examen y la aprobación independientes;
- las pruebas de conformidad y liberación, cuando proceda;
- registros de seguimiento y revalidación posteriores a la liberación.

## Prueba de auditoría

Confirme que la validación abarcó la versión de producción real, coincidió con el actor y la clasificación, utilizó datos y métricas apropiados, probó los riesgos legales y operativos pertinentes, las limitaciones y desviaciones documentadas, y vinculó los resultados a las decisiones de conformidad, liberación, monitoreo y reevaluación, según proceda.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado, incluidos los artículos 9 a 15, 16 a 18, 26, 43, 72 y el anexo IV, según proceda.
- Reglamento (UE) 2026/1744, cuando sus modificaciones afecten a los requisitos, fechas de aplicación o procedimientos pertinentes.
- Normas armonizadas aplicables y especificaciones comunes, cuando estén legalmente disponibles y sean pertinentes; de lo contrario, no deben describirse como leyes vinculantes simplemente porque son referencias de validación útiles.
- Los actuales controles consolidados de texto EUR-Lex sobre resúmenes y borradores antiguos.
