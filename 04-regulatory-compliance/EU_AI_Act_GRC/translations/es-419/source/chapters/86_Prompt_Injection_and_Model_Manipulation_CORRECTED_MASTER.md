# Capítulo 86 — Pronta inyección y manipulación de modelos

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador del Capítulo 86 anterior.

## Requisito

Los sistemas de IA que procesan instrucciones, contenido recuperado, salidas de herramientas, archivos, contenido web o datos suministrados por el usuario deben implementar controles proporcionados contra la inyección rápida, secuestro de instrucciones, fugas de jailbreaks, manipulación del contexto, ejecución de herramientas inseguras y ataques de manipulación de modelos relacionados.

## Explicación en lenguaje sencillo

Un sistema de IA puede tratar el contenido hostil como instrucciones de confianza. Los controles deben evitar que la entrada no confiable cambie el propósito previsto del sistema, las salvaguardias superiores, la exposición de información confidencial, o causar acciones no autorizadas.

## Requisitos de control

Aplicar, según proceda:

1. separación de los contenidos generados por el sistema, el desarrollador, el usuario y la herramienta;
2. la herramienta y el acceso a los datos de los menos privilegiados;
3. listas de permisos, aplicación de políticas y confirmación de acciones;
4. procedencia del contenido y etiquetado de confianza;
5. filtrado de entrada y salida con limitaciones conocidas documentadas;
6. aislamiento o sandboxing del contenido no de confianza;
7. aprobación humana de acciones consecuentes o irreversibles;
8. detección de anomalías, registro, límites de velocidad y controles de sesión;
9. pruebas contradictorias de inyección directa e indirecta;
10. Fallo seguro, retroceso, respuesta a incidentes y escalada de proveedores.

## Ejemplo de GlobalWay

El asistente de viajes de GlobalWay lee descripciones de hoteles y correos electrónicos externos. Una página maliciosa contiene instrucciones ocultas pidiendo al agente que revele los datos del viajero y cambie una reserva. El sistema trata el contenido externo como no confiable, bloquea el acceso a datos no relacionados, requiere confirmación del usuario para los cambios de reserva, y registra el intento de manipulación.

## Actividad de control

Los sistemas habilitados para ello deben pasar pruebas documentadas de inyección y manipulación antes de la liberación y después del modelo de material, cambios rápidos, de herramienta, recuperación o integración.

## Pruebas

- arquitectura rápida y de herramientas;
- diseño de fideicomisos y privilegios;
- los casos de ensayo y los resultados contradictorios;
- configuración de política y filtrado;
- los registros de confirmación de la acción;
- registros de ataques y registros de incidentes;
- rehabilitación y reprueba las pruebas.

## Prueba de auditoría

Seleccione sistemas habilitados rápidamente y verifique que los escenarios de inyección directa e indirecta fueron probados, los privilegios están limitados, las acciones consiguientes requieren la autorización apropiada, los intentos de ataque son detectables y la rehabilitación fue validada.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: disposiciones aplicables en materia de gestión de riesgos, supervisión humana, precisión, robustez, seguridad cibernética, tala, vigilancia e incidentes.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
