# Práctica: Diseño de mapas con QGIS

## Trabajo previo

### Lecturas

Gandhi, U. (2020b, febrero 1). Spatial Data Visualization and Analytics. Spatial Thoughts. https://spatialthoughts.com/courses/spatial-data-viz/

Gandhi, U. (2021). QGIS Tutorials and Tips. https://www.qgistutorials.com/
GDAL/OGR contributors. (2021). GDAL/OGR Geospatial Data Abstraction software Library. Open Source Geospatial Foundation. https://gdal.org/

Graser, A. (2021, diciembre 20). QGIS Map Design – Free Christmas DLC. Locate Press Blog. https://blog.locatepress.com/qgis-map-design-free-christmas-dlc/

## Resumen

## Mapas de expediciones históricas a la Antárdida
Siga el tutorial [QGIS Map Design – Free Christmas DLC](https://blog.locatepress.com/qgis-map-design-free-christmas-dlc/) de [Anita Graser](https://anitagraser.com/), sobre elaboración de mapas de la [edad heroica de la exploración de la Antártida](https://es.wikipedia.org/wiki/Edad_heroica_de_la_exploraci%C3%B3n_de_la_Ant%C3%A1rtida). El tutoria utiliza el paquete de datos [Quantarctica](https://www.npolar.no/quantarctica/) {cite}`matsuoka_quantarctica_2021`.

Se recomienda descargar los datos de [QGIS Freestyle - 17 Dec 2021 #2](https://github.com/timlinux/QGIS-Freestyle/issues/2).

Puede comparar sus mapas con el [proyecto QGIS con el resultado final del tutorial](https://locatepress.com/files/qmd2/QMD2021DLC.zip).

Se sugieren las siguientes propiedades para las capas geoespaciales:

| Capa | Color | Opacidad | Etiquetas
| :- | :- | :- | :- |
| ADD Simple basemap | Campo **category**:<br>*Ice shelf*: rgb(170,204,204)<br>*Ice tongue*: rgb(170,204,204)<br>*Land*: rgb(235,255,255)<br>*Ocean*: rgb(197,199,199)<br>*Rumple*: rgb(235,255, 255)<br>*Sub-antarctic_G*: rgb(174,174,174)<br>*Sub-antarctic_L*: rgb(174,174,174)|||
| Quantarctica Antarctic Circle | rgb(0,0,0 ) |||
| Overview place names |  | 0 | **Reglas**<br>Descripción: Region, Filtro: "labelclass"  =  'Region', Valor: place_name, Tamaño: 19, Color: rgb(133,174,174)<br><br>Descripción: Sea, Filtro: "labelclass"  =  'Sea', Valor: place_name, Tamaño: 21, Color: rgb(164,164,164)  |
| South Pole | rgb(255,0,0) |||

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```