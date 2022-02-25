# Tarea 03 - Análisis de datos geoespaciales mediante pandas, plotly, geopandas y folium

## Fecha de entrega
La fecha y hora límite para la entrega de esta tarea es **sábado 05 de marzo de 2022 a las 23:59**.

## Desarrollo
Debe programar un [Jupyter Notebook](https://jupyter.org/) con salidas tabulares, gráficas y geoespaciales sobre la red vial de Costa Rica, generadas con los paquetes [pandas](https://pandas.pydata.org/), [plotly](https://plotly.com/python/), [geopandas](https://geopandas.org/en/stable/) y [folium](https://python-visualization.github.io/folium/) de [Python](https://www.python.org/). El código fuente debe compartirse en [GitHub](https://github.com/) y los resultados (tablas, gráficos, mapas, etc.) deben visualizarse en [NBViewer](https://nbviewer.org/).

El *notebook* debe contener:

1. Una **tabla** que muestre para cada uno de los 82 cantones de Costa Rica:
- El nombre del cantón.
- La longitud de las autopistas.
- La longitud de las carreteras de pavimento de dos vías o más.
- La longitud de las carreteras de pavimento de una vía.
- La longitud de las carreteras sin pavimento de dos vías.
- La longitud de los caminos de tierra.
- La longitud total (i.e. todos los tipos de red vial) de la red vial del cantón.
- La densidad total (i.e. todos los tipos de red vial) de la red vial del cantón.

2. Un **gráfico plotly de barras apiladas** que muestre la longitud de los cinco tipos de red vial (autopistas, carreteras sin pavimento, caminos de tierra, etc.) en los 15 cantones de mayor longitud total de red vial.

3. Un **gráfico plotly de pastel** que muestre el porcentaje de red vial de los 15 cantones de mayor longitud total de la red vial, con respecto a la longitud de la red vial en todo el país. Además, debe incluirse una porción (*slice*) adicional en el gráfico de pastel llamada "Otros cantones", correspondiente al porcentaje de la suma de la red vial en los 67 cantones restantes.

4. Un  **mapa folium** con las siguientes capas:
- Capa base (OpenStreetMap, Stamen, etc.).
- Capa de [coropletas](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico) correspondiente a la densidad de la red vial en los cantones.
- Líneas de la red vial.

Y los siguientes controles:
- Control para activar y desactivar capas.
- Escala.


Tenga en consideración que:

- La densidad de la red vial para un polígono se define como:  
**km de longitud de red vial / km2 de área**  
Por ejemplo, si un cantón tiene 500 km de longitud de red vial y un área de 1000 km2, la densidad de su red vial es 0.5.

- Debe utilizar las siguientes capas Web Feature Service (WFS) publicadas por el Instituto Geográfico Nacional (IGN) en el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/):
- Límite cantonal 1:5000
- Red vial 1:200000

- Las longitudes y áreas deben presentarse expresadas en kilómetros y kilómetros cuadrados.

## Entregables
Un enlace correspondiente a la visualización del *notebook* en NBViewer. En el **notebook**, incluya un enlace al código fuente en GitHub.

La entrega debe realizarse a través de la plataforma [Mediación Virtual](https://mediacionvirtual.ucr.ac.cr/).

## Calificación
- 15% - Tabla.
- 25% - Gráfico de barras.
- 30% - Gráfico de pastel.
- 30% - Mapa.

**La tarea puede realizarse en grupos de uno, dos o tres estudiantes. En el encabezado del programa, indique los nombres de los integrantes del grupo**.