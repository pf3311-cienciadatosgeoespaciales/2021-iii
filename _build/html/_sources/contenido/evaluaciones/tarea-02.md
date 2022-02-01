# Tarea 02 - Análisis de datos geoespaciales mediante Fiona y Shapely

## Fecha de entrega
La fecha y hora límite para la entrega de esta tarea es **martes 15 de febrero de 2022 a las 16:59**.

## Desarrollo
Debe elaborar un [mapa de coropletas](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico) que muestre la densidad de la red vial en los cantones de Costa Rica. Los datos deben procesarse mediante un programa en Python que utilice los paquetes [Fiona](https://github.com/Toblerity/Fiona) y [Shapely](https://github.com/shapely/shapely) para generar un archivo GeoPackage (GPKG) con el resultado. El archivo gráfico del mapa debe generase con [QGIS](https://qgis.org/).

La densidad de la red vial para un polígono se define como:  
**km de longitud de red vial / km2 de área**  
Por ejemplo, si un cantón tiene 500 km de longitud de red vial y un área de 1000 km2, la densidad de su red vial es 0.5.

Utilice las siguientes capas Web Feature Service (WFS) publicadas por el Instituto Geográfico Nacional (IGN) en el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/):

- Límite cantonal 1:5000
- Red vial 1:200000

## Entregables
Un archivo comprimido (ej. ZIP) que incluya tres archivos:

- El código fuente del programa en un archivo `.py`, `.pynb` (*notebook*) o un enlace a un *notebook* en [Google Colab](https://colab.research.google.com/) (en este último caso, debe compartirlo con `mfvargas@gmail.com`). El código debe estar debidamente documentado, de manera que explique el procedimiento seguido.
- Un archivo GPKG con la capa de cantones y el campo correspondiente a la densidad de la red vial para cada cantón.
- Un archivo gráfico (ej. PNG, JPG) con el mapa de coropletas correspondiente a la densidad de la red vial en los cantones de Costa Rica. Debe generarlo con [QGIS](https://qgis.org/), a partir del archivo GPKG generado por el programa en Python.


La entrega debe realizarse a través de la plataforma [Mediación Virtual](https://mediacionvirtual.ucr.ac.cr/).

## Calificación
- 70% - Programa en Python que genera el archivo GPKG con la capa de cantones y el campo correspondiente a la densidad de la red vial para cada cantón.
- 15% - Archivo GeoPackage (GPKG) mencionado en el punto anterior. **Se verificará que el programa genere este archivo**.
- 15% - Archivo gráfico con el mapa.

**La tarea puede realizarse en grupos de uno, dos o tres estudiantes. En el encabezado del programa, indique los nombres de los integrantes del grupo**.