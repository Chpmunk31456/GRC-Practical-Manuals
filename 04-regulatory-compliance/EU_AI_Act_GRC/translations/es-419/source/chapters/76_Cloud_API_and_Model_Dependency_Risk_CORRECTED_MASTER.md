# Capítulo 76 — Riesgo de dependencia en la nube, la API y el modelo

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 76 en conflicto.

## Requisito

Las organizaciones deben identificar y gestionar la nube de materiales, API, modelo, datos, componentes de software y dependencias de subprocesadores que afectan a sus sistemas de IA. La Ley de IA de la UE no crea un programa independiente de riesgo de dependencia para cada operador, sino que el proveedor, el implementador, el importador, el distribuidor, el fabricante de productos, la gestión de la calidad, la gestión de riesgos, la ciberseguridad, el monitoreo, los incidentes, la documentación y las obligaciones de cooperación requieren suficiente visibilidad y control sobre las dependencias pertinentes.

## Explicación en lenguaje sencillo

Un servicio de IA puede depender de varios componentes externos incluso cuando parece a los usuarios como un sistema único. Un cambio de proveedor, corte, sustitución de modelos, deprecación de API, cambio de ruta regional, subprocesador indocumentado, o pérdida de registros puede alterar la clasificación legal, seguridad, accesibilidad, privacidad, seguridad, supervisión humana o continuidad. Contratar un componente no elimina los deberes legales de la organización.

## Necesidades en materia de gobernanza de las dependencias

Para cada dependencia material, documentar y evaluar:

1. componente, proveedor, subprocesador, propósito, propietario y criticidad;
2. modelos, API, software, datos y versiones de configuración;
3. los lugares de tratamiento y apoyo, los flujos de datos, la retención y los acuerdos de transferencia;
4. disponibilidad, niveles de servicio, capacidad de recuperación, cuotas y límites de tarifas;
5. los procesos de cambio-notificación, liberación, depredación y cambio de emergencia;
6. seguridad, acceso privilegiado, secretos, separación de inquilinos y gestión de la vulnerabilidad;
7. la capacidad de tala, vigilancia, acceso a pruebas y notificación de incidentes;
8. concentración, bloqueo, sustitución y riesgo de fallo en un solo punto;
9. sistemas de retroactividad ensayados, modo seguro, solo para personas o suspensión controlada;
10. desencadenantes de reevaluación, revalidación, revisión de la transparencia o análisis de modificaciones sustanciales.

## Ejemplo de GlobalWay

El servicio de asistencia al viajero de GlobalWay se basa en un modelo alojado, plataforma en la nube, API de traducción, proveedor de identidad, base de datos de recuperación y servicio de monitoreo. Después de una actualización de modelo sin previo aviso reduce la precisión multilingüe y omite las limitaciones de accesibilidad, GlobalWay restringe las funciones afectadas, dirige los casos a consultores capacitados, preserva la versión y la evidencia de salida, requiere investigación del proveedor y revalida el servicio antes de la restauración.

## Actividad de control

Las dependencias materiales deben ser registradas en el inventario de IA y la documentación de arquitectura. Las dependencias altas o críticas deben ser monitoreadas para cambios y cortes, probadas antes de cambios en la producción de materiales, y apoyadas por arreglos aprobados de continuidad y escalada.

## Pruebas

- la dependencia y el inventario de arquitectura;
- registros de proveedores y subprocesadores;
- la versión y el historial de configuración;
- contratos, niveles de servicio y avisos de cambio;
- evaluaciones de la localización y transferencia de datos;
- las revisiones de la seguridad y el acceso;
- resultados de ensayo, regresión y revalidación;
- el seguimiento, el corte y los registros de incidentes;
- ejercicios de recuperación y continuidad;
- la aceptación del riesgo y las decisiones de los propietarios responsables.

## Prueba de auditoría

Seleccionar sistemas de IA altos y críticos. Confirmar que las dependencias materiales son completas y actuales; se conocen versiones, regiones, subprocesadores y propietarios; los cambios materiales desencadenaron revisiones y pruebas apropiadas; se llevaron a cabo arreglos de continuidad; las pruebas siguieron siendo accesibles; y los riesgos de dependencia no resueltos se intensificaron para los encargados de adoptar decisiones autorizados.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: artículos 9 a 17, 20 a 26, 72 a 74, 78 a 82 aplicables, y anexos conexos, en función de la función y la clasificación del sistema.
- Reglamento (UE) 2016/679 y otros requisitos aplicables en materia de privacidad, ciberseguridad, seguridad de los productos, protección de los consumidores y sector.
- Las prácticas de gestión de la dependencia en este capítulo son métodos de gobernanza y garantía utilizados para apoyar las obligaciones jurídicas aplicables; no son un catálogo de control legal independiente.
- Los textos oficiales consolidados actuales controlan los resúmenes antiguos.
