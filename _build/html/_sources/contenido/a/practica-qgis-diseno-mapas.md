# Práctica: Diseño de mapas con QGIS

## Trabajo previo

### Lecturas

Gandhi, U. (2020b, febrero 1). Spatial Data Visualization and Analytics. Spatial Thoughts. https://spatialthoughts.com/courses/spatial-data-viz/

Gandhi, U. (2021). QGIS Tutorials and Tips. https://www.qgistutorials.com/
GDAL/OGR contributors. (2021). GDAL/OGR Geospatial Data Abstraction software Library. Open Source Geospatial Foundation. https://gdal.org/

Graser, A. (2021, diciembre 20). QGIS Map Design – Free Christmas DLC. Locate Press Blog. https://blog.locatepress.com/qgis-map-design-free-christmas-dlc/

## Resumen

## Mapas de expediciones históricas a la Antárdida
Siga el tutorial [QGIS Map Design – Free Christmas DLC](https://blog.locatepress.com/qgis-map-design-free-christmas-dlc/) de [Anita Graser](https://anitagraser.com/), basado en el paquete de datos [Quantarctica](https://www.npolar.no/quantarctica/) {cite}`matsuoka_quantarctica_2021`, para la elaboración de mapas de expediciones históricas a la Antártida.

Se sugieren las siguientes propiedades para las capas geoespaciales:

| Capa | Color |
| :- | :- |
| ADD Simple basemap | Campo **category**:<br>*Ice shelf*: rgb( 170, 204, 204 )<br>*Ice tongue*: rgb( 170, 204, 204 )<br>*Land*: rgb( 235, 255, 255 )<br>*Ocean*: rgb( 197, 199, 199 )<br>*Rumple*: rgb( 235, 255, 255 )<br>*Sub-antarctic_G*: rgb( 174, 174, 174 )<br>*Sub-antarctic_L*: rgb( 174, 174, 174 )|

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```