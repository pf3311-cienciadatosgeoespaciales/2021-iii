# Proyecto - Desarrollo de tablero de datos en Streamlit

## Fecha de entrega
La fecha y hora límite para la entrega del proyecto es **sábado 05 de marzo de 2022 a las 23:59**.

## Desarrollo
Debe programar un tablero de datos (*dashboard*) interactivo en [Streamlit](https://streamlit.io/) con salidas tabulares, gráficas y geoespaciales sobre la red vial de Costa Rica, generadas con los paquetes [pandas](https://pandas.pydata.org/), [plotly](https://plotly.com/python/), [geopandas](https://geopandas.org/en/stable/) y [folium](https://python-visualization.github.io/folium/) de [Python](https://www.python.org/). El código fuente debe compartirse en [GitHub](https://github.com/) y el tablero deben publicarse en [Streamlit Cloud](https://streamlit.io/cloud).

El tablero de datos debe contener:

1. Una barra lateral (*sidebar*) con un filtro por categoría de vía (autopista, carretera de pavimento de dos vías o más, carreteras de pavimento de una vía, etc.). Este filtro operará en las salidas que se describen seguidamente.

2. Una **tabla** que muestre para cada uno de los 82 cantones de Costa Rica:
    - El nombre del cantón.
    - La longitud de las vías de la categoría seleccionada en la barra lateral.
    - La densidad de la red vial del cantón para esa categoría.

2. Un **gráfico plotly de barras** que muestre la longitud de las vías de la categoría seleccionada en los 15 cantones de mayor longitud de red vial para esa categoría.

3. Un **gráfico plotly de pastel** que muestre el porcentaje de red vial, para la categoría seleccionada, de los 15 cantones de mayor longitud de red vial para esa categoría, con respecto a la longitud de la red vial en todo el país, para esa categoría. Además, debe incluirse una porción (*slice*) adicional en el gráfico de pastel llamada "Otros cantones", correspondiente al porcentaje de la suma de la red vial, para la categoría seleccionada, en los 67 cantones restantes.

4. Un  **mapa folium** con las siguientes capas:
- Capa base (OpenStreetMap, Stamen, etc.).
- Capa de [coropletas](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico) correspondiente a la densidad de la red vial en los cantones, para la categoría seleccionada.
- Líneas de la red vial de la categoría seleccionada.

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

- Organice los componentes del tablero de manera que sean fáciles de usar y visualizar.

## Entregables
Un enlace al tablero de datos en Streamlit Cloud. En el tablero, incluya un enlace al código fuente en GitHub.

La entrega debe realizarse a través de la plataforma [Mediación Virtual](https://mediacionvirtual.ucr.ac.cr/).

## Calificación
- 15% - Barra lateral con filtro de categoría de vía.
- 15% - Tabla.
- 20% - Gráfico de barras.
- 25% - Gráfico de pastel.
- 25% - Mapa.

**El proyecto puede realizarse en grupos de uno, dos o tres estudiantes. En el encabezado del programa, indique los nombres de los integrantes del grupo**.