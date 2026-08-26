# Manual 04 — Implementación del Perfil de IA Generativa NIST AI 600-1
## Fuente controlada en español latinoamericano — Capítulos 01–08

> Traducción asistida por máquina para revisión controlada. Guía de implementación original basada en la línea base controlada de NIST AI 600-1 / AI RMF. Este texto no reproduce el texto de la publicación de NIST ni crea certificación, cumplimiento legal ni una opinión de auditoría. La aprobación semántica humana sigue siendo obligatoria antes de la publicación.

## Capítulo 01 — Propósito, alcance y aplicabilidad

Este manual operacionaliza la gestión de riesgos de IA generativa para organizaciones que diseñan, adquieren, integran, despliegan, operan o retiran capacidades de IA generativa. El límite de implementación es deliberadamente basado en riesgo: no todos los controles, pruebas, elementos de evidencia o prácticas operativas aplican a todos los casos de uso.

Cada implementación comienza con una decisión documentada de aplicabilidad que cubra el caso de uso, las partes afectadas, el contexto de despliegue, los datos tratados, el nivel de autonomía, las dependencias externas y las consecuencias de error o uso indebido. El registro de aplicabilidad se convierte en evidencia controlada y debe revisarse cuando cambien de manera material el sistema, modelo, datos, herramientas, proveedor o contexto operativo.

Evidencia mínima:
- descripción del caso de uso y responsable de negocio;
- referencia al inventario del sistema/modelo/componente;
- identificación de partes afectadas y grupos de interés;
- nivel de riesgo o clasificación equivalente;
- fundamento de aplicabilidad;
- revisor y fecha de aprobación.

## Capítulo 02 — Relación con AI RMF 1.0

NIST AI 600-1 se trata como un perfil de IA generativa y recurso complementario de AI RMF, no como una lista de verificación universal independiente. Por ello, el modelo operativo conserva GOVERN, MAP, MEASURE y MANAGE como ciclo de gestión, incorporando familias de riesgo específicas de IA generativa, expectativas de pruebas, consideraciones de procedencia y señales de incidentes.

Las organizaciones deberían mapear cada decisión de implementación de IA generativa con la función correspondiente de AI RMF y conservar trazabilidad desde la declaración de riesgo hasta la evidencia, decisión, acción y riesgo residual.

Comportamiento de control requerido:
- GOVERN establece política, responsabilidad, autoridad y escalamiento;
- MAP define contexto, uso, actores, dependencias y daños plausibles;
- MEASURE evalúa desempeño, seguridad, ciberseguridad, privacidad, integridad e incertidumbre;
- MANAGE selecciona tratamientos, acepta riesgo residual, supervisa la operación y activa detener/revertir cuando se superan los umbrales.

## Capítulo 03 — Rutas de implementación

Se admiten tres rutas proporcionales.

### Esencial
Para usos de menor complejidad o impacto. Requiere inventario, responsables, evaluación básica de riesgo, pruebas mínimas, supervisión humana, gestión de incidentes y aprobación documentada.

### Estructurada
Para usos materiales de negocio, clientes, fuerza laboral, seguridad, privacidad, finanzas u operaciones. Requiere registros formales de riesgos, matrices de evidencia, planes de prueba, revisión de proveedores, controles de cambio, umbrales de monitoreo, guías de respuesta a incidentes y reevaluación periódica.

### Reforzada
Para usos de alto impacto, alta autonomía, sensibles a la seguridad, regulados, expuestos externamente o de otra forma consecuenciales. Requiere desafío independiente, pruebas adversariales más profundas, criterios formales de liberación, mayor procedencia, autoridad explícita para detener/revertir, monitoreo reforzado y aceptación documentada del riesgo residual por la dirección responsable.

La selección de la ruta debe justificarse y solo puede reducirse mediante aprobación documentada.

## Capítulo 04 — Gobernanza y responsabilidad

Todo sistema de IA generativa debe tener responsables de negocio, técnicos, de seguridad, privacidad/datos y riesgo adecuados a su alcance. La responsabilidad no puede delegarse únicamente al proveedor del modelo o al proveedor de implementación.

La gobernanza debería definir:
- quién puede aprobar un nuevo caso de uso;
- quién puede aprobar cambios de modelo, prompt, recuperación, herramientas o datos;
- quién es responsable de las pruebas y la evidencia;
- quién puede suspender o revertir el despliegue;
- quién acepta el riesgo residual;
- quién recibe notificaciones de incidentes;
- quién realiza la revisión periódica.

Deben identificarse conflictos de interés cuando la misma persona diseña, prueba y aprueba un sistema de alto impacto. Las implementaciones reforzadas deberían añadir revisión o desafío independiente.

## Capítulo 05 — Inventario y descomposición del sistema

Trate la capacidad de IA generativa como un sistema, no solo como un modelo. El inventario debería identificar modelo, entorno de alojamiento, capa de recuperación, almacén vectorial, prompts/instrucciones del sistema, herramientas, API, fuentes de datos, artefactos de ajuste, guardrails, componentes de monitoreo, servicios externos y puntos de decisión humana.

El inventario debería capturar versión, responsable, proveedor, ubicación de despliegue, clasificación de datos, límite de autenticación, autoridad de cambio y estado de retiro. Las dependencias que puedan alterar materialmente la salida o el comportamiento deben ser trazables por separado.

Un cambio del sistema es material cuando puede alterar riesgo, capacidad, exposición, calidad de salida, seguridad, ciberseguridad, privacidad, postura de cumplimiento o impacto sobre partes afectadas.

## Capítulo 06 — Modelo de familias de riesgo de IA generativa

La línea base controlada de Manual 04 conserva doce familias de riesgo de IA generativa:

1. Información o capacidades CBRN
2. Confabulación
3. Contenido peligroso, violento o de odio
4. Privacidad de datos
5. Impactos ambientales
6. Sesgo perjudicial y homogeneización
7. Configuración humano-IA
8. Integridad de la información
9. Seguridad de la información
10. Propiedad intelectual
11. Contenido obsceno, degradante y/o abusivo
12. Integración de cadena de valor y componentes

Estas familias son categorías de evaluación, no hallazgos automáticos. Cada caso de uso debe determinar qué familias aplican, los escenarios creíbles, los controles existentes, la evidencia, el riesgo residual y los indicadores de monitoreo.

## Capítulo 07 — Declaraciones de riesgo y rutas de impacto

Los registros de riesgo deberían basarse en escenarios y no ser genéricos. Una estructura útil es:

**Condición o amenaza → comportamiento del sistema → activo/persona/proceso afectado → consecuencia → control/evidencia → riesgo residual.**

Por ejemplo, un asistente con recuperación puede ingerir contenido no confiable, seguir instrucciones maliciosas incrustadas, invocar una herramienta externa y exponer información restringida. La declaración de riesgo debería describir la ruta completa y no limitarse a etiquetar el problema como “prompt injection”.

El análisis de impacto debería considerar efectos directos, indirectos, acumulativos y de uso indebido previsible. Cuando los impactos sean inciertos, la incertidumbre debe registrarse en lugar de convertirse silenciosamente en una conclusión de bajo riesgo.

## Capítulo 08 — Autoridad de liberación y compuertas fail-closed

Ningún caso de uso de IA generativa debería pasar a producción únicamente porque las pruebas automatizadas fueron aprobadas. La liberación requiere evidencia documentada suficiente para la ruta seleccionada, excepciones no resueltas dentro de tolerancias aprobadas, aprobación de responsables y toda revisión humana requerida.

Una compuerta de liberación debe fallar en cerrado cuando:
- falte evidencia requerida o esté desactualizada;
- las pruebas obligatorias estén incompletas o hayan fallado;
- existan hallazgos críticos abiertos sin tratamiento aprobado;
- falte una revisión humana obligatoria, haya sido rechazada o invalidada por cambio material;
- la aplicabilidad legal, de seguridad, privacidad, protección u operación esté sin resolver;
- se requiera capacidad de detener/revertir y no esté validada.

Un cambio material posterior a la aprobación reabre las revisiones y compuertas de liberación afectadas.
