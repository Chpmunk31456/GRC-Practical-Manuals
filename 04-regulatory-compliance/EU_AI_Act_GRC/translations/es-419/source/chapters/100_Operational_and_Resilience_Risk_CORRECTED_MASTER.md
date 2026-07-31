# Capítulo 100 — Riesgo operativo y de resiliencia

> **Estatus legal:** Corregido Maestro de inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 100.

## Requisito

Las organizaciones deben identificar y gestionar los riesgos operacionales y de resiliencia que podrían causar que un sistema de IA o un proceso dependiente fracase, degrade, produzca resultados poco fiables o no esté disponible.

## Explicación en lenguaje sencillo

Un sistema de IA puede fallar incluso sin un ciberataque. Los límites de capacidad, las fuentes de datos incorrectas, los cortes del proveedor de modelos, la deriva de configuración, latencia, fallos de dependencia o control de cambios débil pueden interrumpir las operaciones o producir decisiones perjudiciales.

## Necesidades de evaluación

Evaluar como mínimo:

1. procesos críticos, niveles de servicio y tolerancias de impacto;
2. modelo, API, nube, datos, red, identidad y dependencias del proveedor;
3. capacidad, latencia, rendimiento, tiempo de espera y riesgos de límite de tarifas;
4. fallo de la tubería de datos, datos rancios, cambio de esquema y degradación de la integridad;
5. configuración, versión, rapidez y deriva de la fuente de recuperación;
6. el seguimiento de la cobertura y los umbrales de alerta;
7. soluciones manuales, canales alternativos y modos degradados seguros;
8. objetivos de respaldo, restauración, reversión, failover y recuperación;
9. la preparación del operador, las comunicaciones y la autoridad de decisión;
10. retención de pruebas, coordinación de incidentes y validación posterior a la recuperación.

## Ejemplo de GlobalWay

El servicio de asistencia de viajes para IA de GlobalWay depende de un modelo de terceros, API de reserva, servicios de identidad y datos de perfil del cliente. GlobalWay define un modo seguro de solo lectura, bloquea los cambios de reserva automatizados durante el fallo de la dependencia, dirige solicitudes urgentes a agentes humanos y prueba la recuperación antes de restaurar el servicio normal.

## Actividad de control

Los servicios de IA de materiales deben tener planes de continuidad y recuperación documentados alineados con el impacto del negocio. Los planes deben incluir cierre seguro, retroceso, monitoreo de dependencia, validación de recuperación y ejercicios periódicos que cubran escenarios realistas de fracaso específicos de IA.

## Pruebas

- evaluación de impacto empresarial y dependencia;
- las definiciones de nivel de servicio y tolerancia al impacto;
- los planes de continuidad, recuperación y recuperación;
- los resultados de las pruebas de respaldo, retroceso y fallo;
- el seguimiento y los registros de capacidad;
- informes de ejercicio y medidas correctoras;
- comunicaciones de interrupción del servicio y aprobaciones de recuperación;
- pruebas de validación posterior a la recuperación.

## Prueba de auditoría

Seleccione servicios de IA de material y revise incidentes o ejercicios recientes. Confirme que las dependencias críticas son conocidas, los procesos de recuperación son utilizables, los objetivos de recuperación son probados, versiones restauradas y los datos son validados, y las brechas de resiliencia no resueltas se incrementan.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: disposiciones aplicables sobre gestión de riesgos, exactitud, robustez, seguridad cibernética, supervisión humana, vigilancia, incidentes y medidas correctoras.
- Requerimientos aplicables de resiliencia operativa, ciberseguridad, seguridad de productos y sector.
- Los textos oficiales consolidados actuales controlan los resúmenes antiguos.
