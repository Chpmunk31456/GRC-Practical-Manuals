# Capítulo 97 — Riesgo de ciberseguridad

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 97.

## Requisito

Las organizaciones deben identificar, evaluar, mitigar, probar y monitorear los riesgos de ciberseguridad que afectan a los sistemas, modelos, datos, interfaces, infraestructura, usuarios y servicios dependientes de IA durante todo el ciclo de vida.

## Explicación en lenguaje sencillo

Los atacantes pueden manipular avisos, datos tóxicos, evadir la detección, extraer modelos, robar credenciales, explotar APIs, comprometer dependencias o inducir acciones de herramientas inseguras. Por lo tanto, la seguridad requiere controles coordinados entre software, modelos, datos, identidad, infraestructura, proveedores y operaciones.

## Necesidades de evaluación

Evaluar como mínimo:

1. activos, límites de confianza, usuarios, privilegios y flujos de datos;
2. inyección rápida, inyección rápida indirecta, fugas y uso inseguro de herramientas;
3. envenenamiento de datos de formación, manipulación de fuentes de recuperación y uso indebido de bucles de retroalimentación;
4. ejemplos contradictorios, evasión, extracción de modelos, inversión e inferencia de miembros;
5. secretos, credenciales, APIs, plugins, agentes e integraciones privilegiadas;
6. confidencialidad, integridad, disponibilidad, autenticidad y resiliencia;
7. vulnerabilidades de modelo, biblioteca, contenedor, nube y proveedor;
8. registro, detección, respuesta a incidentes, retroceso y preservación de pruebas;
9. denegación del servicio, agotamiento de la capacidad y fallo de la dependencia;
10. desarrollo seguro, control de cambios, parches y revelación de vulnerabilidad;
11. fuga de datos, memorización de modelos, filtrado de salidas y control de acceso;
12. el cambio de material y los desencadenantes de la reevaluación posterior al incidente.

## Ejemplo de GlobalWay

GlobalWay modela un agente de asistencia para viajes que puede leer itinerarios e iniciar cambios en la reserva. Identifica la inyección rápida indirecta a través de contenido externo, cuentas de servicio sobreprivilegiadas, fugas de datos sensibles, plugins maliciosos y interrupciones del proveedor de modelos. La liberación se bloquea hasta que se validen la reducción de privilegios, el aislamiento de contenido, la confirmación de transacciones, el monitoreo y los controles de reserva.

## Actividad de control

Los sistemas de IA de materiales deben pasar la revisión de la arquitectura de seguridad basada en el riesgo, la modelización de amenazas, el desarrollo seguro, los ensayos contradictorios, la gestión de la vulnerabilidad y la verificación de la preparación para incidentes antes de la producción y después de cambios significativos.

## Pruebas

- modelo de amenaza e inventario de la superficie de ataque;
- arquitectura de seguridad y diagramas de flujo de datos;
- los registros de desarrollo seguro y de revisión de códigos;
- análisis de vulnerabilidad e inventarios de dependencia;
- resultados contradictorios y pruebas de penetración;
- identidad, acceso y pruebas de gestión de secretos;
- procedimientos de seguimiento y respuesta a incidentes;
- rehabilitación, reprueba, y registros de cierre.

## Prueba de auditoría

Seleccione los sistemas de IA de material y verifique que los modelos de amenaza cubren ataques específicos de IA y convencionales, los controles coinciden con la arquitectura y privilegios reales, los hallazgos críticos fueron remediados y probados, el monitoreo detecta eventos relevantes y los cambios materiales desencadenaron una reevaluación.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: disposiciones aplicables en materia de gestión de riesgos, gobernanza de los datos, exactitud, robustez, seguridad cibernética, vigilancia, incidentes y GPAI.
- Seguridad cibernética aplicable en la Unión y en los Estados miembros y requisitos sectoriales.
- Los textos oficiales consolidados actuales controlan los resúmenes antiguos.
