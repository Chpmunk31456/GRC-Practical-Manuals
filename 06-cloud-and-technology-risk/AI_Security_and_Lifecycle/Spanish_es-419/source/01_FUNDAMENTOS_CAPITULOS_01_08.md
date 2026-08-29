# Manual 07 — Seguridad de IA y Controles del Ciclo de Vida
## Fuente controlada en español latinoamericano — Capítulos 01–08

> Traducción de trabajo para revisión semántica humana. Esta guía original de implementación de seguridad operacionaliza la línea base controlada sin reproducir texto de estándares. No garantiza seguridad, seguridad operacional, cumplimiento ni ausencia de vulnerabilidades explotables.

## Capítulo 01 — Objetivo de seguridad y límite del ciclo de vida

La seguridad de IA debe cubrir el ciclo de vida completo del sistema y no únicamente el endpoint del modelo. El límite controlado incluye definición del caso de uso, adquisición de datos y modelos, diseño, desarrollo, evaluación, despliegue, operación, monitoreo, respuesta a incidentes, cambios y retiro.

Cada sistema debe contar con un objetivo de seguridad documentado vinculado con sus datos, acciones, usuarios, autonomía, conectividad externa y consecuencias de falla.

## Capítulo 02 — Inventario de activos de IA

El inventario debe identificar modelos, conjuntos de datos, prompts, fuentes de recuperación, almacenes vectoriales, herramientas, agentes, APIs, cuentas de servicio, secretos, guardrails, componentes de monitoreo, entornos de alojamiento, proveedores y sistemas críticos aguas abajo.

Los registros de inventario deben incluir responsable, versión, ubicación, clasificación de datos, límite de autenticación, proveedor, exposición, autoridad de cambio y estado de retiro. Los componentes desconocidos crean superficie de ataque no administrada.

## Capítulo 03 — Modelado de amenazas

El modelado de amenazas debe identificar activos, límites de confianza, actores, puntos de entrada, privilegios, dependencias y rutas plausibles de abuso. Las amenazas específicas de IA deben evaluarse junto con amenazas convencionales de aplicaciones, nube, identidad, datos y cadena de suministro.

Los escenarios deben incluir usuarios maliciosos, contenido de recuperación comprometido, agentes con privilegios excesivos, secretos expuestos, APIs inseguras, ejecución insegura de herramientas, datos envenenados, divulgación de modelos o prompts, compromiso de proveedores y comportamiento autónomo no previsto cuando corresponda.

## Capítulo 04 — Desarrollo seguro y control de cambios

Los componentes de IA deben desarrollarse y modificarse mediante repositorios controlados, revisión, pruebas, gestión de dependencias, control de acceso y procesos de liberación. Los cambios en prompts, políticas, recuperación, herramientas y guardrails pueden ser significativos para la seguridad y no deben eludir el control de cambios por no ser código tradicional.

Los cambios materiales requieren reevaluar la evidencia de seguridad previa y pueden reabrir la aprobación de liberación.

## Capítulo 05 — Procedencia de datos y modelos

Los equipos de seguridad deben poder identificar el origen de modelos, conjuntos de datos, pesos, adaptadores, paquetes, prompts y componentes externos, así como quién aprobó su uso.

Los registros de procedencia deben incluir origen, versión, evidencia de integridad cuando exista, límites de licencia o uso, proveedor, aprobación, historial de transformación y limitaciones conocidas. La procedencia apoya decisiones de confianza, pero no prueba que un componente sea seguro.

## Capítulo 06 — Identidad, mínimo privilegio y autorización de herramientas

Los sistemas de IA que invoquen herramientas o acciones externas deben utilizar identidades explícitas y permisos de mínimo privilegio. El modelo no debe recibir credenciales amplias únicamente porque la aplicación requiera acceso a múltiples funciones.

Siempre que sea posible, la autorización debe imponerse fuera del modelo. Las acciones de alto impacto deben utilizar verificaciones de política, credenciales acotadas, límites transaccionales, aprobación humana u otros controles deterministas apropiados al riesgo.

## Capítulo 07 — Inyección de prompts y contenido no confiable

La inyección directa e indirecta de prompts debe tratarse como amenaza de seguridad cuando una entrada no confiable pueda influir en comportamiento privilegiado, exponer información sensible, alterar instrucciones del sistema o provocar uso inseguro de herramientas.

Los controles pueden incluir aislamiento de contenido, límites de permisos, filtrado de recuperación, validación de salidas, listas permitidas de herramientas, separación de contexto, privilegios reducidos, pasos de confirmación y monitoreo. Ningún prompt o clasificador individual debe considerarse una defensa completa.

## Capítulo 08 — Puerta de liberación de seguridad fail-closed

La liberación debe fallar de forma cerrada cuando falte evidencia crítica de seguridad, existan hallazgos materiales no resueltos sin tratamiento aprobado, no se hayan completado las pruebas adversariales requeridas, se requiera rollback o contención sin haberlos probado, o falte una revisión humana obligatoria.

Un workflow automatizado en verde respalda la decisión de liberación, pero no garantiza que el sistema sea seguro. La aprobación final continúa siendo una puerta controlada por humanos y los cambios materiales posteriores a la revisión reabren los controles de seguridad afectados.
