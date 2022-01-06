# Fundamentos de geodesia y cartografía

## Trabajo previo

### Lecturas

Olaya, V. (2020). Sistemas de Información Geográfica. https://volaya.github.io/libro-sig/

## Resumen


## Conceptos geodésicos básicos
La [geodesia](https://oceanservice.noaa.gov/facts/geodesy.html) es la ciencia que trata de la medición de la forma de la Tierra, su orientación en el espacio y su campo gravitacional. Entre las tareas típicas de un geodesta están, por ejemplo, la delineación de costas, el establecimiento de límites de entidades territoriales administrativas (ej. países, provincias) y la medición de áreas de territorios.

El planeta Tierra tiene forma esférica, sin embargo, no es una esfera perfecta: es achatada en los polos y abultada en el Ecuador. Además, su superficie es irregular debido a accidentes geográficos como valles, montañas o depresiones tectónicas, entre muchos otros.

Para realizar sus cálculos y mediciones, los geodestas deben utilizar varios modelos matemáticos, los cuales aproximan la forma real de la Tierra. Entre estos modelos están el elipsoide de referencia y el geoide. Las características de estos modelos pueden variar para satisfacer requerimientos particulares de navegación, agrimensura, catastro, uso del suelo y otras cuestiones de interés.

### Elipsoide de referencia
El [elipsoide de referencia](https://es.wikipedia.org/wiki/Elipsoide_de_referencia) es el modelo más sencillo de la forma de la Tierra. Se define por dos parámetros: el radio ecuatorial (semieje mayor) y el radio polar (semieje menor), los cuales se ejemplifican en la {numref}`figure-elipsoide-wgs84`.

```{figure} img/elipsoide-wgs84.png
:name: figure-elipsoide-wgs84

Radio ecuatorial y radio polar del elipsoide de referencia del sistema geodésico [WGS84](https://es.wikipedia.org/wiki/WGS84). Imagen de <a href="https://commons.wikimedia.org/wiki/File:WGS84_mean_Earth_radius.svg">Wikimedia Commons</a>.
```

A través de la historia, se han utilizado diferentes elipsoides cuyas medidas varían de acuerdo con los instrumentos y conocimientos disponibles en cada época y lugar. La lista de la {numref}`figure-tabla-elipsoides` muestra algunos de estos elipsoides de referencia y sus parámetros.

```{figure} img/tabla-elipsoides.png
:name: figure-tabla-elipsoides

Lista de elipsoides de referencia. Fuente <a href="https://en.wikipedia.org/wiki/Earth_ellipsoid#Historical_Earth_ellipsoids">Wikipedia</a>.
```

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```