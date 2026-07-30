# Capítulo 87 — Riesgo de envenenamiento y formación de datos

> **Estatus legal:** Corregido Maestro Inglés para la consolidación. Este archivo controla el lenguaje de borrador anterior del Capítulo 87.

## Requisito

Las organizaciones deben proteger los datos de capacitación, validación, pruebas, ajuste, recuperación y retroalimentación contra alteraciones no autorizadas, contaminación maliciosa, fallos en la procedencia, degradación de la calidad y sesgos ocultos que puedan socavar el cumplimiento, la seguridad o el desempeño.

## Explicación en lenguaje sencillo

El envenenamiento de datos puede ser deliberado o accidental. Una pequeña cantidad de datos manipulados puede crear comportamientos ocultos, resultados sesgados, precisión degradada o debilidades de seguridad. Los controles deben cubrir fuentes de datos, transformaciones, etiquetas, acceso, linaje, aprobaciones y bucles de retroalimentación después del despliegue.

## Requisitos de control

Aplicar, según proceda:

1. controles de origen y origen aprobados;
2. el control de acceso, la separación de funciones y el cambio de la tala;
3. controles de integridad, hashes, versiones y tuberías reproducibles;
4. anomalía, duplicación, atípico y pruebas de calidad de etiqueta;
5. análisis de subgrupos y representatividad;
6. la diligencia debida en el conjunto de datos del proveedor y del código abierto;
7. cuarentena y revisión de la información de los usuarios o de los datos de producción antes de su reutilización;
8. pruebas de contrapuerta, de activación y de envenenamiento selectivo;
9. retroceso, readiestramiento e identificación de la versión afectada;
10. retención de conjuntos de datos, decisiones, transformaciones y pruebas de validación.

## Ejemplo de GlobalWay

GlobalWay afina un modelo de reclutamiento utilizando datos históricos de aplicaciones. Antes de su uso, el equipo valida la procedencia, detecta registros duplicados y manipulados, revisa la representación de grupos protegidos, separa la retroalimentación de la producción de los datos de readiestramiento aprobados y bloquea la entrada de datos no revisados en la tubería.

## Actividad de control

Ningún conjunto de datos puede entrar en un material de entrenamiento de IA o tuberías de ajuste sin propiedad documentada, procedencia, integridad, calidad, uso legal y aprobación de riesgos.

## Pruebas

- el inventario de datos y los registros de procedencia;
- acceso y cambio de registros;
- los resultados de los ensayos de integridad y calidad;
- análisis de subgrupos y representatividad;
- garantía del conjunto de datos del proveedor;
- los resultados de las pruebas de envenenamiento y backdoor;
- los registros de readiestramiento y reversión;
- aprobación y liberación de pruebas.

## Prueba de auditoría

Seleccione una muestra de conjuntos de datos utilizados en los modelos de producción. Verifique la procedencia aprobada, el acceso controlado, las transformaciones reproducibles, las pruebas de integridad y envenenamiento, las limitaciones de calidad documentadas y la vinculación entre la versión del conjunto de datos, la versión del modelo y la decisión de liberación.

## Referencias jurídicas primarias

- Reglamento (UE) 2024/1689, en su versión modificada: normas aplicables en materia de gobernanza de datos, gestión de riesgos, exactitud, robustez, ciberseguridad, documentación técnica y posteriores a la comercialización.
- Los actuales controles consolidados de texto EUR-Lex sobre los resúmenes antiguos.
