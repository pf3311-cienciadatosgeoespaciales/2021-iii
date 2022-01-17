# GDAL: biblioteca para lectura y escritura de datos geoespaciales

## Trabajo previo

### Tutoriales
Gandhi, U. (2020a, febrero 1). Mastering GDAL Tools. Spatial Thoughts. https://spatialthoughts.com/courses/mastering-gdal-tools/


## Resumen
Se introduce la biblioteca GDAL para lectura y escritura de datos geoespaciales y se muestran varios ejemplos de su uso a través de los programas para la línea de comandos del sistema operativo.


## Características generales de GDAL
[Geospatial Data Abstraction Library (GDAL)](https://gdal.org/) es una biblioteca para leer y escribir datos geoespaciales en varios formatos [raster](https://gdal.org/drivers/raster/) y [vectoriales](https://gdal.org/drivers/vector/). En ocasiones, también es denominada GDAL/OGR, en donde GDAL se refiere a la funcionalidad para datos raster y OGR (sigla antes usada para "OpenGIS Simple Features Reference Implementation") a la correspondiente a datos vectoriales. En este documento, se utilizará la sigla GDAL para referirse a la funcionalidad para ambos modelos de datos. GDAL es distribuida por la [Open Source Geospatial Foundation (OSGeo)](https://www.osgeo.org/) con una [licencia X/MIT](https://gdal.org/license.html#license).

GDAL cuenta con un único [modelo abstracto de datos raster](https://gdal.org/user/raster_data_model.html) y un único [modelo abstracto de datos vectoriales](https://gdal.org/user/vector_data_model.html), lo que permite programar aplicaciones geoespaciales sin tener que ocuparse de las particularidades de cada formato que se utilice (GeoTIFF, NetCDF, ESRI Shapefile, GeoJSON, etc.).

A pesar de que GDAL está programada en C/C++, cuenta con una interfaz de programación de aplicaciones (API) para varios lenguajes de programación, incluyendo [C](https://gdal.org/api/index.html#c-api), [C++](https://gdal.org/api/index.html#id3), [Python](https://gdal.org/python/index.html) y [Java](https://gdal.org/java/overview-summary.html). Además, ofrece un conjunto de [programas para la línea de comandos del sistema operativo](https://gdal.org/programs/) cuyas [distribuciones binarias](https://gdal.org/download.html#binaries) están disponibles para varios sistemas operativos, incluyendo Windows, macOS y Linux. Estas API y los programas también están incluídos en la plataforma de ciencia de datos llamada [Anaconda](https://www.anaconda.com/), la cual cuenta con versiones para todos los sistemas operativos mencionados.

### Programas para la línea de comandos del sistema operativo
Los [programas de GDAL para la línea de comandos del sistema operativo](https://gdal.org/programs/) permiten ejecutar tareas de geoprocesamiento y de conversión entre formatos geoespaciales sin utilizar una interfaz gráfica o un lenguaje de programación.

#### Instalación
En el sitio web de GDAL se describen varias opciones para su [descarga e instalación](https://gdal.org/download.html), incluyendo [archivos binarios ejecutables para varias plataformas](https://gdal.org/download.html#binaries).

Seguidamente, se detalla el procedimiento de [instalación mediante Conda](https://gdal.org/download.html#conda), el cual puede ejecutarse desde Linux, macOS o Windows. [Conda](https://conda.io/) es un administrador de paquetes que puede instalarse como parte de [Anaconda](https://anaconda.org/) o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (se recomienda esta última opción, por requerir menos recursos). Entre otras ventajas, conda permite el manejo de [ambientes (*environments*)](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), cada uno con sus propias versiones de los paquetes instalados.

Para instalar los programas de GDAL, luego de instalar Anaconda o Miniconda, ejecute los siguientes comandos desde una terminal:

```shell
# Actualización de conda
conda update conda

# Creación de un ambiente conda llamado gdal (puede usarse cualquier otro nombre)
conda create --name gdal

# Activación del ambiente
conda activate gdal

# Instalación de la biblioteca gdal a través del canal conda-forge
conda install -c conda-forge gdal

# Prueba de la instalación
gdalinfo --version
ogrinfo --version

# Desactivación del ambiente (luego de finalizado el trabajo con GDAL)
conda deactivate
```

Una vez instalado el ambiente, puede activarse y desactivarse con `conda activate gdal` y `conda deactivate` respectivamente.

#### Consideraciones generales
Los programas de GDAL comparten una serie de [opciones comunes para datos raster](https://gdal.org/programs/raster_common_options.html#raster-common-options) y de [opciones comunes para datos vectoriales](https://gdal.org/programs/vector_common_options.html) que pueden visualizarse con la opción `-- help-general`. Por ejemplo:

```shell
ogrinfo --help-general
```
```shell
Generic GDAL utility command options:
  --version: report version of GDAL in use.
  --license: report GDAL license info.
  --formats: report all configured format drivers.
  --format [format]: details of one format.
  --optfile filename: expand an option file into the argument list.
  --config key value: set system configuration option.
  --debug [on/off/value]: set debug level.
  --pause: wait for user input, time to attach debugger
  --locale [locale]: install locale for debugging (i.e. en_US.UTF-8)
  --help-general: report detailed help on general options.
```
  
Para obtener ayuda acerca de un comando particular, puede usarse la opción `-- help`. Por ejemplo:

```shell
ogrinfo --help
```
```shell
Usage: ogrinfo [--help-general] [-ro] [-q] [-where restricted_where|@filename]
               [-spat xmin ymin xmax ymax] [-geomfield field] [-fid fid]
               [-sql statement|@filename] [-dialect sql_dialect] [-al] [-rl] [-so] [-fields={YES/NO}]
               [-geom={YES/NO/SUMMARY}] [[-oo NAME=VALUE] ...]
               [-nomd] [-listmdd] [-mdd domain|`all`]*
               [-nocount] [-noextent] [-nogeomtype] [-wkt_format WKT1|WKT2|...]
               [-fielddomain name]
               datasource_name [layer [layer ...]]
```

#### Ejemplos de uso de programas

##### Vectoriales

###### ogrinfo
El programa [ogrinfo](https://gdal.org/programs/ogrinfo.html) despliega información acerca de una fuente de datos vectoriales.

Los siguientes comandos despliegan información sobre la [capa de países](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/) de [Natural Earth](https://www.naturalearthdata.com/), tanto para el formato comprimido como para el formato shapefile. En el caso comprimido, note el uso de [/vsizip/](https://gdal.org/user/virtual_file_systems.html), para sistemas de archivos virtuales.

```shell
# Descarga del archivo ZIP (en Windows, puede instalar wget o descargar el archivo con un navegador)
wget https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip

# Información sobre la capa comprimida en formato ZIP
ogrinfo -al -so /vsizip/ne_110m_admin_0_countries.zip

# Descompresión del archivo ZIP
unzip ne_110m_admin_0_countries.zip

# Información sobre la capa descomprimida en formato SHP
ogrinfo -al -so ne_110m_admin_0_countries.shp
```

Puede utilizarse SQL para consultar los datos:

```shell
# Consulta SQL (en Windows, sustituya los "\" por "^" para los cambios de línea)
ogrinfo \
  -sql "SELECT name, continent FROM ne_110m_admin_0_countries WHERE continent = 'Oceania' ORDER BY name" \
  -geom=NO \
  ne_110m_admin_0_countries.shp
```

###### ogr2ogr
El comando [ogr2ogr](https://gdal.org/programs/ogr2ogr.html) realiza conversiones entre formatos de fuentes de datos geoespaciales. A la vez, puede ejecutar otras operaciones como selección de atributos y geometrías, filtrado por criterios espaciales y no espaciales, reproyección y validación de geometrías, entre otras.

Conversión entre formatos:

```shell
# Despliegue de la lista de formatos vectoriales soportados por GDAL/OGR
ogr2ogr --formats

# Conversión de SHP a GeoJSON
ogr2ogr ne_110m_admin_0_countries.geojson ne_110m_admin_0_countries.shp

# Conversión de SHP a GeoPackage
ogr2ogr ne_110m_admin_0_countries.gpkg ne_110m_admin_0_countries.shp
```

###### Ejemplo de análisis: distribución de especies de murciélagos
Se crea el archivo distribucion-murcielagos.gpkg para contener las capas necesarias para el análisis de distribución de murciélagos en Costa Rica.

Descarga de capas desde un servicio WFS, reproyección y validación de geometrías:

```shell
# Lista de capas en servicio WFS del Sinac
ogrinfo WFS:"http://geos1pne.sirefor.go.cr/wfs"

# Descarga a GPKG de la capa WFS de áreas silvestres protegidas (ASP) con reproyección a WGS84 y validación de geometrías
ogr2ogr -nln asp \
  -s_srs EPSG:5367 -t_srs EPSG:4326 \
  -makevalid \
  distribucion-murcielagos.gpkg WFS:"http://geos1pne.sirefor.go.cr/wfs" "PNE:areas_silvestres_protegidas"

# Información sobre la capa descargada
ogrinfo -al -so distribucion-murcielagos.gpkg asp


# Lista de capas en servicio WFS del IGN
ogrinfo WFS:"https://geos.snitcr.go.cr/be/IGN_5/wfs"

# Descarga a GPKG de la capa WFS de cantones con reproyección a WGS84 y validación de geometrías
ogr2ogr -update -nln cantones \
  -s_srs EPSG:5367 -t_srs EPSG:4326 \
  -makevalid \
  distribucion-murcielagos.gpkg WFS:"https://geos.snitcr.go.cr/be/IGN_5/wfs" "IGN_5:limitecantonal_5k"

# Información sobre la capa descargada
ogrinfo -al -so distribucion-murcielagos.gpkg cantones
```

Descarga de datos desde un archivo CSV y conversión a un formato geoespacial:

```shell
# Descarga de registros de presencia de murciélagos
wget https://api.gbif.org/v1/occurrence/download/request/0105729-210914110416597.zip

# Descompresión
unzip 0105729-210914110416597.zip

# Cambio de nombre del archivo (en Windows, puede usar el comando ren)
mv 0105729-210914110416597.csv murcielagos.csv

# Información sobre el conjunto de datos, sin interpretación de columnas de coordenadas
ogrinfo -al -so murcielagos.csv

# Información sobre el conjunto de datos, con interpretación de columnas de coordenadas
ogrinfo -al -so \
  -oo X_POSSIBLE_NAMES=decimalLongitude -oo Y_POSSIBLE_NAMES=decimalLatitude \
  murcielagos.csv

# Adición al GPKG de análisis de distribución de murciélagos
ogr2ogr -update -nln registros-murcielagos \
  -s_srs EPSG:4326 -t_srs EPSG:4326 \
  -oo X_POSSIBLE_NAMES=decimalLongitude -oo Y_POSSIBLE_NAMES=decimalLatitude \
  distribucion-murcielagos.gpkg murcielagos.csv
```

Generación de capa con cantidad de especies de murciélagos en polígonos

```shell
# Revisión de índices y nombres de columnas geométricas
ogrinfo \
  -sql "SELECT table_name, column_name, HasSpatialIndex(table_name, column_name) FROM gpkg_geometry_columns" \
  distribucion-murcielagos.gpkg

# Creación de capa con cantidad de especies por ASP
ogr2ogr \
  -update -nln asp-especies \
  -dialect sqlite -sql "SELECT ST_Union(p.SHAPE), p.nombre_asp, Count(DISTINCT species) AS especies_murcielagos FROM asp p LEFT JOIN 'registros-murcielagos' r ON ST_Contains(p.SHAPE, r.geom) GROUP BY p.nombre_asp" \
  distribucion-murcielagos.gpkg distribucion-murcielagos.gpkg

# Creación de capa con cantidad de especies por cantón
ogr2ogr \
  -update -nln cantones-especies \
  -dialect sqlite -sql "SELECT p.SHAPE, p.canton, Count(DISTINCT species) AS especies_murcielagos FROM cantones p LEFT JOIN 'registros-murcielagos' r ON ST_Contains(p.SHAPE, r.geom) GROUP BY p.canton" \
  distribucion-murcielagos.gpkg distribucion-murcielagos.gpkg
```

**Preguntas de análisis**

¿Cuáles son las 10 ASP con mayor cantidad de especies de murciélagos?

```shell
# 10 ASP con mayor cantidad de especies de murciélagos
ogrinfo \
  -sql "SELECT nombre_asp, especies_murcielagos FROM 'asp-especies' ORDER BY especies_murcielagos DESC LIMIT 10" \
  distribucion-murcielagos.gpkg
```

¿Cuál es el promedio de especies de murciélagos en los cantones de la provincia de Heredia?

```shell
# Cantidad de especies de murciélagos en los cantones de la provincia de Heredia
ogrinfo \
  -sql "SELECT c.canton, especies_murcielagos FROM cantones c, 'cantones-especies' ce WHERE c.provincia = 'Heredia' AND c.canton=ce.canton ORDER BY especies_murcielagos DESC" \
  distribucion-murcielagos.gpkg

# Promedio de especies de murciélagos en los cantones de la provincia de Heredia
ogrinfo \
  -sql "SELECT Avg(especies_murcielagos) promedio FROM cantones c, 'cantones-especies' ce WHERE c.provincia = 'Heredia' AND c.canton=ce.canton" \
  distribucion-murcielagos.gpkg
```

¿Cuáles son las 5 especies de murciélagos con mayor cantidad de registros?