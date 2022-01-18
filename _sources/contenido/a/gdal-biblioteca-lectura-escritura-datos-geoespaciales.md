# GDAL: biblioteca para lectura y escritura de datos geoespaciales

## Trabajo previo

### Tutoriales
Gandhi, U. (2020a, febrero 1). Mastering GDAL Tools. Spatial Thoughts. https://spatialthoughts.com/courses/mastering-gdal-tools/


## Resumen
Se introduce la biblioteca GDAL para lectura y escritura de datos geoespaciales y se muestran varios ejemplos de su uso a través de los programas para la línea de comandos del sistema operativo.


## Características generales de GDAL
[Geospatial Data Abstraction Library (GDAL)](https://gdal.org/) es una biblioteca para leer y escribir datos geoespaciales en varios formatos [raster](https://gdal.org/drivers/raster/) y [vectoriales](https://gdal.org/drivers/vector/). En ocasiones, también es denominada GDAL/OGR, en donde GDAL se refiere a la funcionalidad para datos raster y OGR (sigla antes usada para "OpenGIS Simple Features Reference Implementation") a la correspondiente a datos vectoriales. En este documento, se utilizará la sigla GDAL para referirse a la funcionalidad para ambos modelos de datos. GDAL es distribuida por la [Open Source Geospatial Foundation (OSGeo)](https://www.osgeo.org/) con una [licencia X/MIT](https://gdal.org/license.html#license).

GDAL cuenta con un único [modelo abstracto de datos raster](https://gdal.org/user/raster_data_model.html) y un único [modelo abstracto de datos vectoriales](https://gdal.org/user/vector_data_model.html), lo que permite programar aplicaciones geoespaciales sin tener que ocuparse de las particularidades de cada formato que se utilice (GeoTIFF, NetCDF, ESRI Shapefile, GeoPackage, GeoJSON, etc.).

A pesar de que GDAL está programada en C/C++, cuenta con una interfaz de programación de aplicaciones (API; en inglés, *Application Programming Interface*) para varios lenguajes de programación, incluyendo [C](https://gdal.org/api/index.html#c-api), [C++](https://gdal.org/api/index.html#id3), [Python](https://gdal.org/python/index.html) y [Java](https://gdal.org/java/overview-summary.html). Además, ofrece un conjunto de [programas para la línea de comandos del sistema operativo](https://gdal.org/programs/) cuyas [distribuciones binarias](https://gdal.org/download.html#binaries) están disponibles para varios sistemas operativos, incluyendo Windows, macOS y Linux. Estas API y los programas también están incluídos en la plataforma de ciencia de datos [Anaconda](https://www.anaconda.com/), la cual puede instalarse en todos los sistemas operativos mencionados.

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
```
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
```
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
En esta sección, se presentan ejemplos de uso de los programas, tanto para datos vectoriales como para datos raster.


##### Programas para datos vectoriales

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
```
INFO: Open of `ne_110m_admin_0_countries.shp'
      using driver `ESRI Shapefile' successful.

Layer name: ne_110m_admin_0_countries
Metadata:
  DBF_DATE_LAST_UPDATE=2021-12-07
Geometry: Polygon
Feature Count: 177
Extent: (-180.000000, -90.000000) - (180.000000, 83.645130)
Layer SRS WKT:
GEOGCRS["WGS 84",
    DATUM["World Geodetic System 1984",
        ELLIPSOID["WGS 84",6378137,298.257223563,
            LENGTHUNIT["metre",1]]],
    PRIMEM["Greenwich",0,
        ANGLEUNIT["degree",0.0174532925199433]],
    CS[ellipsoidal,2],
        AXIS["latitude",north,
            ORDER[1],
            ANGLEUNIT["degree",0.0174532925199433]],
        AXIS["longitude",east,
            ORDER[2],
            ANGLEUNIT["degree",0.0174532925199433]],
    ID["EPSG",4326]]
Data axis to CRS axis mapping: 2,1
featurecla: String (15.0)
scalerank: Integer (1.0)
LABELRANK: Integer (1.0)
SOVEREIGNT: String (32.0)
...
```

Para consultar los datos, puede utilizarse el lenguaje [Structured Query Language (SQL)](https://es.wikipedia.org/wiki/SQL) junto con el dialecto [sqlite](https://www.sqlite.org/) y sus [funciones espaciales](http://www.gaia-gis.it/gaia-sins/spatialite-sql-5.0.1.html). Estas funcionalidades espaciales son parte de los proyectos de [Gaia-SINS](http://www.gaia-gis.it/gaia-sins/).

```shell
# Consulta SQL (en Windows, sustituya los "\" por "^" para los cambios de línea)
ogrinfo \
  -sql "SELECT name, continent FROM ne_110m_admin_0_countries WHERE continent = 'Oceania' ORDER BY name" \
  -geom=NO \
  ne_110m_admin_0_countries.shp
```
```
...
OGRFeature(ne_110m_admin_0_countries):137
  name (String) = Australia
  continent (String) = Oceania

OGRFeature(ne_110m_admin_0_countries):0
  name (String) = Fiji
  continent (String) = Oceania

OGRFeature(ne_110m_admin_0_countries):134
  name (String) = New Caledonia
  continent (String) = Oceania

OGRFeature(ne_110m_admin_0_countries):136
  name (String) = New Zealand
  continent (String) = Oceania

OGRFeature(ne_110m_admin_0_countries):7
  name (String) = Papua New Guinea
  continent (String) = Oceania

OGRFeature(ne_110m_admin_0_countries):135
  name (String) = Solomon Is.
  continent (String) = Oceania

OGRFeature(ne_110m_admin_0_countries):89
  name (String) = Vanuatu
  continent (String) = Oceania
```

###### ogr2ogr
El comando [ogr2ogr](https://gdal.org/programs/ogr2ogr.html) realiza conversiones entre formatos de fuentes de datos vectoriales. A la vez, puede ejecutar otras operaciones como selección de atributos y geometrías, filtrado por criterios espaciales y no espaciales, reproyección y validación de geometrías, entre otras.

Visualización de la lista de formatos vectoriales:

```shell
# Despliegue de la lista de formatos vectoriales soportados por GDAL/OGR
ogr2ogr --formats
```
```
Supported Formats:
  FITS -raster,vector- (rw+): Flexible Image Transport System
  PCIDSK -raster,vector- (rw+v): PCIDSK Database File
  netCDF -raster,multidimensional raster,vector- (rw+vs): Network Common Data Format
  PDS4 -raster,vector- (rw+vs): NASA Planetary Data System 4
  VICAR -raster,vector- (rw+v): MIPL VICAR file
  JP2OpenJPEG -raster,vector- (rwv): JPEG-2000 driver based on OpenJPEG library
  PDF -raster,vector- (rw+vs): Geospatial PDF
  MBTiles -raster,vector- (rw+v): MBTiles
  BAG -raster,multidimensional raster,vector- (rw+v): Bathymetry Attributed Grid
  EEDA -vector- (ro): Earth Engine Data API
  OGCAPI -raster,vector- (rov): OGCAPI
  ESRI Shapefile -vector- (rw+v): ESRI Shapefile
...
```

Conversión entre formatos:

```shell
# Conversión de SHP a GeoJSON
ogr2ogr ne_110m_admin_0_countries.geojson ne_110m_admin_0_countries.shp

# Conversión de SHP a GeoPackage
ogr2ogr ne_110m_admin_0_countries.gpkg ne_110m_admin_0_countries.shp
```

###### **Ejemplo de análisis: distribución de especies de murciélagos**
Se analiza la distribución de especies de [murciélagos](https://es.wikipedia.org/wiki/Chiroptera) en Costa Rica con base en varias divisiones del territorio.

Se utilizan las siguientes fuentes de datos:

- Registros de presencia de murciélagos, agrupados por la [Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://api.gbif.org/v1/occurrence/download/request/0105729-210914110416597.zip).
- Capas geoespaciales de Costa Rica agrupadas por el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/).

Se crea el archivo `distribucion-murcielagos.gpkg` para contener las capas necesarias para el análisis.

Descarga de capas desde servicios Web Feature Service (WFS) agrupados en el SNIT, reproyección y validación de geometrías:

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

Descarga de datos de presencia de murciélagos desde un archivo CSV y conversión a un formato geoespacial:

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

Generación de capa con cantidad de especies de murciélagos en polígonos:

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

La {numref}`figure-mapa-especies-murcielagos-asp` muestra un [mapa de coropletas](https://es.wikipedia.org/wiki/Mapa_coropl%C3%A9tico) elaborado con [QGIS](https://qgis.org/), con la distribución de especies de murciélagos por ASP:

```{figure} img/mapa-especies-murcielagos-asp.png
:name: figure-mapa-especies-murcielagos-asp

Mapa de cantidad de especies de murciélagos por cantón.
```

**Preguntas**

¿Cuáles son las 5 ASP con mayor cantidad de especies de murciélagos?

```shell
# 5 ASP con mayor cantidad de especies de murciélagos
ogrinfo \
  -sql "SELECT nombre_asp, especies_murcielagos FROM 'asp-especies' ORDER BY especies_murcielagos DESC LIMIT 5" \
  distribucion-murcielagos.gpkg
```
```
OGRFeature(SELECT):0
  nombre_asp (String) = Golfo Dulce
  especies_murcielagos (Integer) = 55

OGRFeature(SELECT):1
  nombre_asp (String) = Arenal Monteverde
  especies_murcielagos (Integer) = 32

OGRFeature(SELECT):2
  nombre_asp (String) = Palo Verde
  especies_murcielagos (Integer) = 30

OGRFeature(SELECT):3
  nombre_asp (String) = Corcovado
  especies_murcielagos (Integer) = 29

OGRFeature(SELECT):4
  nombre_asp (String) = Barra del Colorado
  especies_murcielagos (Integer) = 28
```

¿Cuál es el promedio de especies de murciélagos en los cantones de la provincia de Heredia?

```shell
# Cantidad de especies de murciélagos en los cantones de la provincia de Heredia
ogrinfo \
  -sql "SELECT c.canton, especies_murcielagos FROM cantones c, 'cantones-especies' ce WHERE c.provincia = 'Heredia' AND c.canton=ce.canton ORDER BY especies_murcielagos DESC" \
  distribucion-murcielagos.gpkg
```
```
...
OGRFeature(SELECT):0
  canton (String) = Sarapiquí
  especies_murcielagos (Integer) = 76

OGRFeature(SELECT):1
  canton (String) = Heredia
  especies_murcielagos (Integer) = 22

OGRFeature(SELECT):2
  canton (String) = Barva
  especies_murcielagos (Integer) = 7

OGRFeature(SELECT):3
  canton (String) = Santo Domingo
  especies_murcielagos (Integer) = 5

OGRFeature(SELECT):4
  canton (String) = San Rafael
  especies_murcielagos (Integer) = 5

OGRFeature(SELECT):5
  canton (String) = Belén
  especies_murcielagos (Integer) = 0

OGRFeature(SELECT):6
  canton (String) = San Pablo
  especies_murcielagos (Integer) = 0

OGRFeature(SELECT):7
  canton (String) = Flores
  especies_murcielagos (Integer) = 0

OGRFeature(SELECT):8
  canton (String) = San Isidro
  especies_murcielagos (Integer) = 0

OGRFeature(SELECT):9
  canton (String) = Santa Bárbara
  especies_murcielagos (Integer) = 0
```

```shell
# Promedio de especies de murciélagos en los cantones de la provincia de Heredia
ogrinfo \
  -sql "SELECT Avg(especies_murcielagos) promedio FROM cantones c, 'cantones-especies' ce WHERE c.provincia = 'Heredia' AND c.canton=ce.canton" \
  distribucion-murcielagos.gpkg
```
```
...
promedio: Real (0.0)
OGRFeature(SELECT):0
  promedio (Real) = 11.5
```

¿Cuáles son las 5 especies de murciélagos con mayor cantidad de registros?

```shell
```

##### Programas para datos raster

###### gdalinfo
El programa [gdalinfo](https://gdal.org/programs/gdalinfo.html) despliega información acerca de una fuente de datos raster.

Los siguientes comandos trabajan con la capa global de altitud de la base de datos de tiempo y clima [WorldClim](https://www.worldclim.org/).

Descarga y descompresión de la capa de altitud global:

```shell
# Descarga de la capa de altitud global
wget https://biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_30s_elev.zip

# Descompresión
unzip wc2.1_30s_elev.zip
```

Información sobre la capa:

```shell
# Información sobre la capa
gdalinfo -stats wc2.1_30s_elev.tif
```
```
Driver: GTiff/GeoTIFF
Files: wc2.1_30s_elev.tif
Size is 43200, 21600
Coordinate System is:
GEOGCRS["WGS 84",
    DATUM["World Geodetic System 1984",
        ELLIPSOID["WGS 84",6378137,298.257223563,
            LENGTHUNIT["metre",1]]],
    PRIMEM["Greenwich",0,
        ANGLEUNIT["degree",0.0174532925199433]],
    CS[ellipsoidal,2],
        AXIS["geodetic latitude (Lat)",north,
            ORDER[1],
            ANGLEUNIT["degree",0.0174532925199433]],
        AXIS["geodetic longitude (Lon)",east,
            ORDER[2],
            ANGLEUNIT["degree",0.0174532925199433]],
    ID["EPSG",4326]]
Data axis to CRS axis mapping: 2,1
Origin = (-180.000000000000000,90.000000000000000)
Pixel Size = (0.008333333333333,-0.008333333333333)
Metadata:
  AREA_OR_POINT=Area
Image Structure Metadata:
  COMPRESSION=DEFLATE
  INTERLEAVE=BAND
Corner Coordinates:
Upper Left  (-180.0000000,  90.0000000) (180d 0' 0.00"W, 90d 0' 0.00"N)
Lower Left  (-180.0000000, -90.0000000) (180d 0' 0.00"W, 90d 0' 0.00"S)
Upper Right ( 180.0000000,  90.0000000) (180d 0' 0.00"E, 90d 0' 0.00"N)
Lower Right ( 180.0000000, -90.0000000) (180d 0' 0.00"E, 90d 0' 0.00"S)
Center      (   0.0000000,   0.0000000) (  0d 0' 0.01"E,  0d 0' 0.01"N)
Band 1 Block=43200x1 Type=Int16, ColorInterp=Gray
  Min=-415.000 Max=8424.000 
  Minimum=-415.000, Maximum=8424.000, Mean=nan, StdDev=nan
  NoData Value=-32768
  Metadata:
    STATISTICS_MAXIMUM=8424
    STATISTICS_MEAN=1.#SNAN
    STATISTICS_MINIMUM=-415
    STATISTICS_STDDEV=1.#SNAN
```

###### gdalwarp
El programa [gdalwarp](https://gdal.org/programs/gdalwarp.html) se utiliza para reproyectar y transformar datos raster.

Recorte de la capa raster de altitud global con el contorno de la capa de cantones de Costa Rica:

```shell
# Recorte de la capa raster de altitud global con el contorno de la capa de cantones de Costa Rica
gdalwarp \
  -dstnodata -9999 \
  -tr 0.00833333 0.00833333 -q \
  -cutline 'distribucion-murcielagos.gpkg' -cl cantones -crop_to_cutline wc2.1_30s_elev.tif altitud-cr.tif

# Información sobre la capa de altitud de Costa Rica
gdalinfo -stats altitud-cr.tif
```

###### gdaldem
El programa [gdaldem](https://gdal.org/programs/gdaldem.html) proporciona un conjunto de herramientas para analizar y visualizar [modelos digitales de elevaciones (DEM; en inglés, *Digital Elevation Model*)](https://es.wikipedia.org/wiki/Modelo_digital_del_terreno).

Generación de *hillshade* (efecto de relieve):

```shell
# Generación de efecto "hillshade"
gdaldem hillshade 'altitud-cr.tif' 'relieve-cr.tif' -s 111120

# Generación de efecto "hillshade" multidireccional
gdaldem hillshade 'altitud-cr.tif' 'relieve-multi-cr.tif' -s 111120 -multidirectional
```

El *hillshade* multidireccional se muestra en la {numref}`figure-relieve-multi-cr`.

```{figure} img/relieve-multi-cr.png
:name: figure-relieve-multi-cr

Mapa de Costa Rica con *hillshade* (efecto relieve) multidireccional.
```

Generación de efecto relieve de color:

Se requiere un archivo con la codificación de los colores para cada banda de altitud, como el siguiente:

```shell
# Contenido de colores.txt
# altitud, rojo, verde, azul

0,101,146,82
500,190,202,130
1000,241,225,145
1500,244,200,126
2000,197,147,117
2500,204,169,170
3000,251,238,253
3500,255,255,255
nv 0 0 0 0
```

```shell
# Generación de efecto relieve de color
gdaldem color-relief 'altitud-cr.tif' colores.txt relieve-color-cr.tif
```

El efecto relieve de color se muestra en la {numref}`figure-relieve-color-cr`.

```{figure} img/relieve-color-cr.png
:name: figure-relieve-color-cr

Mapa de Costa Rica con efecto relieve de color.
```