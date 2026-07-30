# Capítulo 88 — Extracción y hurto de modelos

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 88 en conflicto.

## Requisito

Las organizaciones deben implementar salvaguardias proporcionadas contra la copia no autorizada de modelos, extracción, inversión, robo de peso, divulgación de sistemas confidenciales y consultas abusivas que puedan comprometer la propiedad intelectual, la seguridad, la privacidad, la seguridad o el cumplimiento normativo.

## Explicación en lenguaje sencillo

Los atacantes pueden recrear el comportamiento del modelo a través de consultas repetidas, robar pesas o artefactos, inferir información de entrenamiento sensible o aprovechar el acceso privilegiado.La protección requiere controles técnicos, contractuales, de monitoreo y de incidentes adaptados al valor y riesgo del modelo.

## Requisitos de control

Aplicar, según proceda:

1. acceso de los menos privilegiados a pesas, puestos de control, código, avisos y configuración;
2. autenticación fuerte, gestión de secretos, encriptación y aislamiento ambiental;
3. controles de tasa de consulta, volumen, patrón y abuso de cuentas;
4. detección de anomalías para el comportamiento de extracción e inversión;
5. la minimización de la producción y los controles de confianza e información cuando estén justificados;
6. marcas de agua, huellas dactilares, canarios o técnicas de procedencia cuando sean eficaces;
7. controles seguros de la distribución y el acceso de los proveedores;
8. el control de los empleados y contratistas de conformidad con la legislación aplicable;
9. la preservación de pruebas, la contención, la rotación de credenciales y la respuesta a las infracciones;
10. escalada legal, contractual y regulatoria.

## Ejemplo de GlobalWay

GlobalWay opera un modelo propietario de precios de viaje a través de una API. Monitoring identifica una cuenta de nueva creación que hace consultas sistemáticas de límites a un alto volumen. La cuenta está limitada y suspendida, se conservan registros, se revisan credenciales y rutas de acceso, y el incidente se evalúa para el robo de modelos, la exposición a la privacidad y la notificación del proveedor.

## Actividad de control

Los propietarios de seguridad deben monitorear los indicadores de extracción, probar los controles de acceso privilegiado y mantener un libro de jugadas sobre incidentes que cubra artefactos robados, puntos finales expuestos y consultas sospechosas.

## Pruebas

- modelo de clasificación de activos;
- registros de acceso-control y privilegios;
- API y configuración del límite de velocidad;
- normas y alertas de detección de anomalías;
- los resultados de los ensayos de extracción;
- los registros forenses y de incidentes;
- pruebas de rotación y contención de credenciales;
- registros de respuesta contractual y jurídica.

## Prueba de auditoría

Seleccione modelos de alto valor y verifique que los pesos y artefactos están controlados por acceso, los puntos finales se monitorean para el comportamiento de extracción, se investiga la actividad anormal, se prueban los procedimientos de incidentes y se documenta el riesgo residual.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, modificado: disposiciones aplicables en materia de seguridad cibernética, robustez, confidencialidad, gestión de riesgos, seguimiento, incidentes y riesgo sistémico.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
