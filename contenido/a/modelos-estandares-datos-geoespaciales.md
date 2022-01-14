# Modelos y estándares de datos geoespaciales

## Trabajo previo

### Lecturas
Lovelace, R., Nowosad, J., & Münchow, J. (2019). Geocomputation with R. CRC Press, Taylor and Francis Group, CRC Press is an imprint of theTaylor and Francis Group, an informa Buisness, A Chapman & Hall Book. https://geocompr.robinlovelace.net/

Olaya, V. (2020). Sistemas de Información Geográfica. https://volaya.github.io/libro-sig/

## Resumen
Se introducen los modelos vectorial y raster, así como el estándar Simple Features. También se presentan las principales bibliotecas de software geoespacial.

## Modelos de datos
Se utilizan dos modelos para la representación de datos geoespaciales: el vectorial y el raster.

### El modelo vectorial
El modelo vectorial de datos está basado en puntos localizados en un sistema de referencia de coordenadas (CRS; en inglés, *Coordinate Reference System*). Los puntos individuales pueden representar objetos independientes (ej. un poste eléctrico, una cabina telefónica) o pueden también agruparse para formar geometrías más complejas como líneas o polígonos. Por lo general, los puntos tienen solo dos dimensiones (x, y), a las que se les puede agregar una tercera dimensión _z_, usualmente correspondiente a la altitud sobre el nivel del mar.

#### El estándar Simple Features
[_Simple Features_](https://www.ogc.org/standards/sfa) (o _Simple Feature Access_) es un estándar abierto de la [Organización Internacional de Estandarización (ISO)](https://iso.org/) y del [_Open Geospatial Consortium_ (OGC)](https://www.ogc.org/) que especifica un modelo común de almacenamiento y acceso para geometrías de dos dimensiones (líneas, polígonos, multilíneas, multipolígonos, etc.). El estándar es implementado por muchas bibliotecas y bases de datos geoespaciales como [GDAL](https://gdal.org/), [Fiona (Python)](http://github.com/Toblerity/Fiona), [Shapely (Python)](http://github.com/Toblerity/Shapely), [sf (R)](https://cran.r-project.org/web/packages/sf/index.html), [PostgreSQL/PostGIS](https://en.wikipedia.org/wiki/PostGIS), [SQLite/SpatiaLite](https://www.gaia-gis.it/fossil/libspatialite/), [Oracle Spatial](https://www.oracle.com/database/technologies/spatialandgraph.html) y [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/), entre muchas otras.

La especificación define 17 tipos de geometrías, de las cuales siete son las más comúnmente utilizadas. Estas últimas se muestran en la {numref}`figure-tipos-geometrias-sf`.

```{figure} img/tipos-geometrias-sf.png
:name: figure-tipos-geometrias-sf

Tipos de geometrías de Simple Features más usadas. Imagen de [Robin Lovelace et al.](https://geocompr.robinlovelace.net/spatial-class.html#vector-data).
```


