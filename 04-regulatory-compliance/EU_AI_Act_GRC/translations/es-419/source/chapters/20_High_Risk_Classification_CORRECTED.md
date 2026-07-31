# Capítulo 20 — Clasificación de alto riesgo

## Estado de la publicación

**Texto original en inglés corregido legalmente.** Este capítulo reemplaza el lenguaje de clasificación de alto riesgo en borradores anteriores hasta que todos los archivos fuente sean reconciliados.

## Finalidad

Este capítulo explica cómo determinar si un sistema de IA es de alto riesgo con arreglo al artículo 6 del Reglamento (UE) 2024/1689, modificado por el Reglamento (UE) 2026/1744.

## Requisito

Las organizaciones deben realizar y documentar una clasificación actual de alto riesgo para cada sistema de IA de material antes del despliegue y después de los cambios pertinentes.

La clasificación debe distinguir:

- el artículo 6, apartado 1, sistemas conectados a los productos cubiertos por la legislación de armonización de la Unión del anexo I;
- los sistemas del artículo 6, apartado 2, utilizados a efectos del anexo III;
- los sistemas que figuran en el anexo III pero que pueden acogerse a la excepción del apartado 3 del artículo 6, cuando proceda;
- sistemas fuera del artículo 6 que puedan tener aún transparencia, GPAI, privacidad, empleo, consumo, seguridad, ciberseguridad o obligaciones sectoriales.

## Explicación en lenguaje sencillo

"Alto riesgo" es una clasificación jurídica, no una descripción general de un sistema que parece importante o peligroso. El análisis debe seguir la vía del artículo 6 y el anexo correspondiente.

Un sistema puede ser operacionalmente crítico sin ser de alto riesgo en virtud del artículo 6. Por el contrario, un sistema puede ser legalmente de alto riesgo incluso cuando la organización considera que su puntuación de riesgo interno es moderada.

## Vía de clasificación

### Paso 1 — Confirmar el sistema y la finalidad prevista

Documento:

- el sistema de IA y los componentes del modelo;
- la finalidad prevista;
- usuarios y personas afectadas;
- las decisiones o los productos apoyados;
- países y sectores de despliegue;
- las funciones de proveedor e implementador;
- integración de productos;
- dependencias de los proveedores de materiales.

### Fase 2 — Artículo 6, apartado 1, y anexo I

Evaluar si el sistema de IA:

- esté destinado a utilizarse como componente de seguridad de un producto contemplado en el anexo I, o
- sea en sí mismo un producto contemplado en el anexo I;
- y está obligado a someterse a una evaluación de conformidad de terceros con arreglo a la legislación aplicable sobre el producto.

La fecha de aplicación modificada para los requisitos de las secciones 1 a 3 del capítulo III que rigen los sistemas del artículo 6, apartado 1, del anexo I es **2 de agosto de 2028**. Esta fecha de retraso no debe utilizarse para aplazar las obligaciones aplicables de forma independiente.

### Etapa 3 — Artículo 6, apartado 2, y anexo III

Evaluar si la finalidad prevista corresponde a una categoría del anexo III, incluidas las actuales categorías y condiciones modificadas.

La fecha de aplicación modificada para los requisitos de las secciones 1 a 3 del capítulo III que rigen los sistemas del apartado 2 del artículo 6/anexo III es **2 de diciembre de 2027**.

### Etapa 4 — Evaluar cualquier excepción del apartado 3 del artículo 6

Cuando esté legalmente disponible, determinar si el sistema no plantea un riesgo significativo de daño a la salud, la seguridad o los derechos fundamentales porque no influye materialmente en el resultado de la toma de decisiones y cumple las condiciones legales.

No aplicar esta excepción cuando el sistema realice la elaboración de perfiles de personas físicas cuando la ley excluya la utilización de la excepción.

La organización debe mantener una evaluación razonada y estar preparada para transmitirla a una autoridad competente.

### Paso 5 — Registrar el resultado

Use uno de estos resultados controlados:

- Artículo 6, apartado 1/Anexo I de alto riesgo;
- Artículo 6, apartado 2, del anexo III, de alto riesgo;
- uso del anexo III con excepción documentada del artículo 6, apartado 3;
- no es de alto riesgo en virtud del artículo 6, pero está sujeto a otras obligaciones de la Ley de IA;
- clasificación diferida en espera de pruebas jurídicas o técnicas;
- Se prohíbe o suspende el despliegue.

## Regla de la fecha efectiva

Las fechas posteriores de alto riesgo se aplican estrictamente a los requisitos correspondientes de las secciones 1 a 3 del capítulo III. No retrasan automáticamente:

- - Las tareas de alfabetización de la IA;
- restricciones de prácticas prohibidas;
- Obligaciones de la GPAI;
- las obligaciones de transparencia;
- disposiciones de gobernanza y autoridad;
- RGPD, empleo, igualdad, consumidores, seguridad, seguridad cibernética o obligaciones de derecho sectorial;
- compromisos contractuales;
- controles internos de riesgos necesarios para prevenir daños.

## Ejemplo de servicios de viajes de GlobalWay

GlobalWay evalúa un sistema de selección de la contratación destinado a clasificar a los solicitantes de decisiones de empleo. El propósito previsto se inscribe en una categoría de empleo del anexo III. GlobalWay clasifica el sistema como el artículo 6, apartado 2, de alto riesgo y asigna la fecha modificada del 2 de diciembre de 2027 a los requisitos aplicables del capítulo III.

GlobalWay no considera la fecha como un permiso para aplazar la privacidad, la discriminación, la legislación laboral, la alfabetización en materia de IA, el proveedor, la seguridad o los controles de revisión humana.

## Actividades de control

- Exigir una clasificación documentada con arreglo al artículo 6 antes de la aprobación.
- Vincular la evaluación al texto actual de los anexos I y III.
- Exigir la aprobación legal de las excepciones del apartado 3 del artículo 6.
- Grabar el propósito previsto y evitar la repurposición no aprobada.
- Reevaluar después de los cambios de modelo, datos, flujo de trabajo, proveedor, jurisdicción, producto o usuario.
- Mapa de los resultados de la clasificación a la fecha de implementación correcta.
- Mantener pruebas que apoyen determinaciones no de alto riesgo.

## Pruebas

- declaración de finalidad prevista;
- Hoja de trabajo del artículo 6;
- la cartografía de los anexos I y III;
- análisis de la legislación sobre productos;
- la evaluación del artículo 6, apartado 3, si procede;
- aprobación legal;
- restricciones de despliegue;
- cambios y antecedentes de reevaluación;
- mapeo de artículo a control.

## Pruebas de auditoría

1. Trazar sistemas seleccionados a través de cada etapa de clasificación del artículo 6.
2. Verifique las referencias de los anexos I y III utilizando el texto modificado.
3. Revisar las pruebas de excepción del apartado 3 del artículo 6 y la aprobación legal.
4. Confirmar que los sistemas de perfiles no están excluidos incorrectamente.
5. Verificar que las fechas 2027 y 2028 se aplican únicamente a los requisitos pertinentes.
6. Confirmar que los sistemas no de alto riesgo siguen siendo evaluados para otras obligaciones.
7. Comprobar si los cambios desencadenan la reclasificación.

## Lista de verificación de gestión

- ¿Se documenta con exactitud el propósito previsto?
- ¿Se han sometido a prueba el artículo 6, apartado 1, y el artículo 6, apartado 2?
- ¿Se apoya plenamente alguna excepción del apartado 3 del artículo 6?
- ¿Las fechas 2027 y 2028 se usan por poco?
- ¿Se hace un seguimiento independiente de otras obligaciones jurídicas?

## Especificación de la figura — Ruta de clasificación de alto riesgo

Crear un árbol de decisiones que comience con la finalidad prevista, y luego separar el artículo 6, apartado 1, el anexo I y el artículo 6, apartado 2, el anexo III, seguidos del análisis de las excepciones del artículo 6, apartado 3, los resultados de la clasificación controlada y los desencadenantes de la reevaluación.

**Texto Alt:** Ensayo de árbol de decisión de clasificación de IA de alto riesgo Artículo 6, apartado 1, y anexo I, sistemas de productos, artículo 6, apartado 2, y casos de uso del anexo III, la excepción del artículo 6, apartado 3, los resultados finales de la clasificación, las fechas de aplicación y los desencadenantes de la reevaluación.
