# Software para manejo de datos geoespaciales


## Trabajo previo

### Lecturas
Pebesma, E., Wagner, W., Verbesselt, J., Goor, E., Briese, C., & Neteler, M. (2016). OpenEO: a GDAL for Earth Observation Analytics. https://r-spatial.org/2016/11/29/openeo.html


## Resumen
Se introducen las bibliotecas GDAL, GEOS y PROJ.


## Bibliotecas
Las bibliotecas de sftware GDAL, GEOS y PROJ son utilizadas desde una gran cantidad de aplicaciones geoespaciales (ej. sistemas de información geográfica de escritorio, motores de bases de datos, servidores de mapas).

* **GDAL**: [Geospatial Data Abstraction Library (GDAL](https://gdal.org/) es una biblioteca para leer y escribir datos geoespaciales en varios formatos [raster](https://gdal.org/drivers/raster/) y [vectoriales](https://gdal.org/drivers/vector/). Implementa un único [modelo abstracto de datos raster](https://gdal.org/user/raster_data_model.html) y un único [modelo abstracto de datos vectoriales](https://gdal.org/user/vector_data_model.html), lo que permite programar aplicaciones geoespaciales sin tener que ocuparse de las particularidades de cada formato que se utilice (GeoTIFF, NetCDF, ESRI Shapefile, GeoJSON, etc.). A pesar de que GDAL está programada en C/C++, cuenta con una interfaz de programación de aplicaciones (API) para varios lenguajes de programación, incluyendo [C](https://gdal.org/api/index.html#c-api), [C++](https://gdal.org/api/index.html#id3), [Python](https://gdal.org/python/index.html) y [Java](https://gdal.org/java/overview-summary.html). Además, ofrece un conjunto de [utilitarios de línea de comandos](https://gdal.org/programs/) cuyas [distribuciones binarias](https://gdal.org/download.html#binaries) están disponibles para varios sistemas operativos, incluyendo Windows, macOS y Linux.

* **GEOS**: [Geometry Engine, Open Source (GEOS)](https://libgeos.org/) es una implementación en C++ de la biblioteca [JTS Topology Suite](http://www.tsusiatsoftware.net/jts/main.html) (desarrollada en Java) y que implementa un conjunto de operaciones y predicados geoespaciales (ej. unión, intersección, distancia, área).

* **PROJ**: [PROJ](https://proj.org/) es una biblioteca que transforma coordenadas entre diferentes CRS, incluyendo tanto proyecciones cartográficas como transformaciones geodésicas.

## Otros tipos de software
Las bibliotecas mencionadas en la sección anterior pueden utilizarse para desarrollar una gran variedad de software, incluyendo otras bibliotecas, sistemas administradores de bases de datos, servidores de mapas, sistemas de información geográfica de escritorio y sistemas de gestión de contenidos, entre otros.

La [Open Source Geospatial Foundation (OSGeo)](https://www.osgeo.org/) mantiene una lista de proyectos de software geoespacial, muchos de los cuales utilizan estas bibliotecas.