# Capítulo 85 — Modelización de amenazas

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador del Capítulo 85 anterior.

## Requisito

Las organizaciones deben realizar modelos proporcionados de amenazas para los sistemas de IA y los componentes de IA de uso general cuando la seguridad, la seguridad, la resiliencia, la privacidad, los derechos fundamentales o los riesgos operacionales puedan verse afectados materialmente por un uso indebido malintencionado o accidental.

## Explicación en lenguaje sencillo

El modelado de amenazas de IA identifica cómo los atacantes, internautas, usuarios, dependencias, tuberías de datos, avisos, modelos, herramientas e interfaces pueden causar resultados dañinos. Debe cubrir todo el ciclo de vida y actualizarse cuando el sistema, modelo, propósito previsto, datos, entorno de implementación o situación de amenaza cambie.

## Alcance de la modelización de amenazas

Evaluar como mínimo:

1. activos, límites de confianza, actores y superficies de ataque;
2. formación, ajuste, recuperación, conducción rápida e inferencia;
3. envenenamiento de datos, inyección rápida, manipulación de modelos, extracción y robo;
4. uso no autorizado de herramientas, escalada de privilegios y abuso de agentes;
5. cadena de suministro, API, plugin, código abierto y dependencias en la nube;
6. fugas de privacidad, memorización, exposición a información confidencial e inversión de modelos;
7. derivación de seguridad, generación de contenidos nocivos, evasión y uso indebido;
8. registro, monitoreo, detección, contención, retroceso y recuperación;
9. las consecuencias para las personas afectadas, operativas y reglamentarias;
10. riesgos residuales, suposiciones y controles necesarios.

## Ejemplo de GlobalWay

Antes de liberar un agente de asistencia para viajes de IA que puede acceder a los sistemas de reserva, GlobalWay mapea los permisos de la herramienta del agente, los canales rápidos, API externas, entradas de usuario, almacenes de datos y rutas de escalada.La revisión identifica la inyección rápida, los cambios de itinerario no autorizados, las fugas de datos y la sustitución de modelos de proveedores como escenarios prioritarios.

## Actividad de control

Los propietarios de sistemas y de seguridad deben completar un modelo de amenaza vinculado a versiones antes de la liberación de la producción y después del cambio de material. Los resultados de alto riesgo deben asignarse controles, propietarios, plazos, pruebas de validación y criterios de bloqueo de liberaciones.

## Pruebas

- modelo de amenaza aprobado;
- arquitectura y diagramas de flujo de datos;
- inventario de activos y fideicomisos;
- los casos de abuso y los árboles de ataque;
- controlar la cartografía y las decisiones sobre riesgos residuales;
- validación y resultados del equipo rojo;
- registros de reevaluación activados por el cambio.

## Prueba de auditoría

Seleccione una muestra de sistemas de IA de material y verifique que los modelos de amenaza reflejen la arquitectura implementada, las dependencias actuales, los escenarios de uso indebido realistas, las medidas de mitigación asignadas, la eficacia de control probada y la aceptación documentada del riesgo residual.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: disposiciones aplicables sobre gestión del riesgo, exactitud, solidez, seguridad cibernética, post-comercialización, incidencia y riesgo sistémico.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
- Los marcos y directrices de seguridad reconocidos no son vinculantes a menos que se incorporen mediante otro requisito vinculante.
