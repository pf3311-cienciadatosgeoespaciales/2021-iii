# QGIS: sistema de información geográfica de escritorio


## Trabajo previo

### Tutoriales
Gandhi, U. (2020b, febrero 1). Spatial Data Visualization and Analytics. Spatial Thoughts. https://spatialthoughts.com/courses/spatial-data-viz/


## Resumen
Se propone la elaboración de diferentes mapas con el sistema de información geográfica de escritorio QGIS.


## Mapa de registros de presencia de tolomucos (*Eira barbara*) en Costa Rica
Elabore con QGIS un mapa de registros de presencia de la especie de mamíferos [*Eira barbara*](https://es.wikipedia.org/wiki/Eira_barbara) como el que se presenta en la {numref}`figure-mapa-registros-tolomucos`.

```{figure} img/mapa-registros-tolomucos.png
:name: figure-mapa-registros-tolomucos

Mapa de registros de presencia de tolomucos (*Eira barbara*) en Costa Rica.
```

Utilice las siguientes fuentes:

Datos de presencia de tolomucos:  
https://doi.org/10.15468/dl.nfurnv  
Archivo CSV consultado a la [Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://www.gbif.org/), con datos de diferentes publicadores.

Capa geoespacial de provincias de Costa Rica:  
https://geos.snitcr.go.cr/be/IGN_5/wfs? (Límite Provincial 1:5mil - IGN_5:limiteprovincial_5k)
Capa WFS publicada por el Instituto Geográfico Nacional (IGN) en el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/).

Capas geoespaciales de territorios de Nicaragua y Panamá:  
https://gadm.org/download_country.html  
Archivos SHP o GPKG compartidos por [GADM](https://gadm.org/).


## Mapas de expediciones históricas a la Antárdida
Siga el tutorial [QGIS Map Design – Free Christmas DLC](https://blog.locatepress.com/qgis-map-design-free-christmas-dlc/) de [Anita Graser](https://anitagraser.com/), sobre elaboración de mapas de la [edad heroica de la exploración de la Antártida](https://es.wikipedia.org/wiki/Edad_heroica_de_la_exploraci%C3%B3n_de_la_Ant%C3%A1rtida). El tutorial utiliza el paquete de datos [Quantarctica](https://www.npolar.no/quantarctica/) {cite}`matsuoka_quantarctica_2021`.

Se recomienda descargar los datos de [QGIS Freestyle - 17 Dec 2021 #2](https://github.com/timlinux/QGIS-Freestyle/issues/2).

Puede comparar sus mapas con el [proyecto QGIS con el resultado final del tutorial](https://locatepress.com/files/qmd2/QMD2021DLC.zip).

Se sugieren las siguientes propiedades para las capas geoespaciales:

| Capa | Color | Opacidad | Etiquetas
| :- | :- | :- | :- |
| ADD Simple basemap | Campo **category**:<br>*Ice shelf*: rgb(170,204,204)<br>*Ice tongue*: rgb(170,204,204)<br>*Land*: rgb(235,255,255)<br>*Ocean*: rgb(197,199,199)<br>*Rumple*: rgb(235,255, 255)<br>*Sub-antarctic_G*: rgb(174,174,174)<br>*Sub-antarctic_L*: rgb(174,174,174)|||
| Quantarctica Antarctic Circle | rgb(0,0,0 ) |||
| Overview place names |  | 0 | **Reglas**<br>Descripción: Region, Filtro: "labelclass"  =  'Region', Valor: place_name, Tamaño: 19, Color: rgb(133,174,174)<br><br>Descripción: Sea, Filtro: "labelclass"  =  'Sea', Valor: place_name, Tamaño: 21, Color: rgb(164,164,164)  |
| South Pole | rgb(255,0,0) |||


## Mapas de la situación de la covid-19 en Costa Rica
Elabore con QGIS un [mapa de coropletas](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico) que muestre la cantidad de casos activos de covid-19 en los cantones de Costa Rica, como el que se muestra en la {numref}`figure-mapa-covid-casos-activos`.

```{figure} img/mapa-covid-casos-activos.png
:name: figure-mapa-covid-casos-activos

Mapa de casos activos de covid-19 en cantones de Costa Rica al 2022-01-11.
```

Elabore mapas similares para casos positivos, fallecidos y recuperados por cantón.

Utilice las siguientes fuentes:

Datos de covid-19 en Costa Rica:  
https://geovision.uned.ac.cr/oges/  
Archivos CSV compartidos por el [Ministerio de Salud de Costa Rica](http://www.ministeriodesalud.go.cr/).

Capa geoespacial de cantones de Costa Rica:  
https://geos.snitcr.go.cr/be/IGN_5/wfs? (Límite Cantonal 1:5mil - IGN_5:limitecantonal_5k)
Capa WFS publicada por el Instituto Geográfico Nacional (IGN) en el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/).

Capas geoespaciales de territorios de Nicaragua y Panamá:  
https://gadm.org/download_country.html  
Archivos SHP o GPKG compartidos por [GADM](https://gadm.org/).


## Mapas de distribución de especies de murciélagos (orden *Chiroptera*) en Costa Rica
Elabore con QGIS un [mapa de coropletas](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico) que muestre la cantidad de especies de [murciélagos](https://es.wikipedia.org/wiki/Chiroptera) en los cantones de Costa Rica, como el que se presenta en la {numref}`figure-mapa-especies-murcielagos-cantones`.

```{figure} img/mapa-especies-murcielagos-cantones.png
:name: figure-mapa-especies-murcielagos-cantones

Mapa de cantidad de especies de murciélagos (orden *Chiroptera*) en cantones de Costa Rica.
```

Utilice las siguientes fuentes:

Datos de presencia de murciélagos:  
https://doi.org/10.15468/dl.r4n8p2  
Archivo CSV consultado a la [Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://www.gbif.org/), con datos de diferentes publicadores.

Capa geoespacial de cantones de Costa Rica:  
https://geos.snitcr.go.cr/be/IGN_5/wfs? (Límite Cantonal 1:5mil - IGN_5:limitecantonal_5k)
Capa WFS publicada por el Instituto Geográfico Nacional (IGN) en el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/).

Capas geoespaciales de territorios de Nicaragua y Panamá:  
https://gadm.org/download_country.html  
Archivos SHP o GPKG compartidos por [GADM](https://gadm.org/).


## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```