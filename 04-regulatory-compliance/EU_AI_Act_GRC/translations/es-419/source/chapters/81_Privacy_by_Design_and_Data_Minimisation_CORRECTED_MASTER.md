# Capítulo 81 — Privacidad por diseño y minimización de datos

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 81 en conflicto.

## Requisito

Los sistemas de IA que procesan datos personales deben incorporar principios de privacidad y protección de datos en el diseño, desarrollo, configuración, despliegue, supervisión y jubilación. Los datos personales deben ser adecuados, pertinentes y limitados a lo que sea necesario para el propósito documentado, mientras que se cumplen los requisitos de gobernanza, exactitud, gestión de riesgos y evidencia de los datos de la Ley de IA.

## Explicación en lenguaje sencillo

Más datos no es automáticamente mejor o legal. Los equipos deben justificar por qué cada elemento de datos, función, campo rápido, registro, anotación y período de retención es necesario. Diseño que mejora la privacidad debe ser considerado antes de la recopilación y antes de cambios de modelo o flujo de trabajo, no añadido sólo después de la implementación.

## Controles de diseño

La organización debería aplicar:

1. pruebas documentadas de finalidad y necesidad para cada elemento de datos personales;
2. revisión de características y variables indirectas;
3. límites de recogida y retención;
4. acceso basado en funciones y menor privilegio;
5. seudonimización, agregación, enmascaramiento o datos sintéticos, cuando proceda;
6. separación de los datos de formación, validación, ensayo y producción;
7. la conservación de la privacidad en el registro y el seguimiento;
8. controles contra la memorización, divulgación o reidentificación no deseadas;
9. supresión, corrección, restricción y flujos de trabajo de portabilidad, cuando proceda;
10. reevaluación después de nuevas fuentes de datos, características, actualizaciones de modelos, integraciones o propósitos.

## Ejemplo de GlobalWay

El sistema de asistencia para viajes de GlobalWay no retiene números de pasaporte, datos de tarjetas de pago o información de salud en avisos simplemente porque esos campos existen en sistemas anteriores. La revisión del diseño confirma qué atributos son necesarios, enmascara valores sensibles, limita el contenido de los registros y establece períodos de retención alineados con las necesidades legales y operacionales.

## Actividad de control

Privacy Engineering y AI Governance deben aprobar una revisión de privacidad por diseño antes de la liberación de la producción y después de cambios materiales. La revisión debe documentar la necesidad, proporcionalidad, decisiones de minimización, salvaguardias técnicas, riesgos residuales y compensaciones no resueltas.

## Pruebas

- inventario de datos y mapa de flujo;
- evaluación de la finalidad y la necesidad;
- justificación de la selección de características;
- el calendario de retención;
- diseño de control de acceso;
- pruebas de seudonimización o enmascaramiento;
- los resultados de las pruebas de privacidad;
- procedimientos de supresión y gestión de derechos;
- aprobación de diseño-revisión y cambiar la historia.

## Prueba de auditoría

Seleccione una muestra de elementos de datos de IA, características, indicaciones y registros. Confirme que se documentaron las necesidades, se eliminaron los datos excesivos o rancios, las salvaguardias funcionan como están diseñadas y los cambios materiales desencadenaron una revisión renovada.

## Referencias jurídicas primarias

- Reglamento (UE) 2016/679: artículo 5, apartado 1, letra c), artículo 25 y artículo 32, con otras disposiciones aplicables.
- Reglamento (UE) 2024/1689, modificado: artículos 9, 10, 12, 15, 26 y anexo IV, según proceda.
- El actual control consolidado de los textos EUR-Lex sobre resúmenes y borradores anteriores.
