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

Los primeros elipsoides de referencia fueron diseñados para usos locales (ej. Europa, India, América del Norte). Más recientemente, se identificó la necesidad de contar con modelos para todo el planeta, como el del elipsoide WGS84, uno de los más utilizados en la actualidad, por ser el empleado por el [Sistema de Posicionamiento Global (GPS; en inglés, Global Positioning System)](https://es.wikipedia.org/wiki/GPS). El WGS84 (*World Geodetic System 1984*) es la revisión más reciente del [World Geodetic System (WGS)](https://en.wikipedia.org/wiki/World_Geodetic_System), un estándar mundial usado en geodesia, cartografía y navegación.

### Geoide
El elipsoide tiene una superficie lisa y no puede representar las protuberancias y depresiones de la Tierra. El [geoide](https://es.wikipedia.org/wiki/Geoide) es un modelo mucho más acertado de la superficie del planeta que sí contempla estas características. La {numref}`figure-geoide` muestra una imagen de un geoide.

```{figure} img/geoide.jpg
:name: figure-geoide

Geoide. Imagen de ICGEM compartida a través de <a href="https://commons.wikimedia.org/wiki/File:Geoid_undulation_10k_scale.jpg">Wikimedia Commons</a>.
```

De manera similar al caso de los elipsoides, existen varios geoides de referencia que han sido desarrollados a través del tiempo y han evolucionado para adaptarse a las modificaciones de la superficie terrestre.

### Datum geodésico
Cuando se trabaja con un elipsoide global (ej. WGS84), se sitúa de tal modo que tanto la posición de su centro de gravedad como su plano ecuatorial coincidan con los terrestres. Por el contrario, cuando el elipsoide es local, estas propiedades no se cumplen necesariamente, y el elipsoide resulta insuficiente, ya que no se cuenta con información sobre su posicionamiento con respecto a la superficie terrestre {cite}`olaya_sistemas_2020`.

Surge así el concepto de [datum](https://es.wikipedia.org/wiki/Datum), que es el conjunto formado por una superficie de referencia (el elipsoide) y un punto en el que este se une al geoide. Este punto se denomina punto astronómico fundamental (para su cálculo se emplean métodos astronómicos), o simplemente punto fundamental, y en él el elipsoide es tangente al geoide {cite}`olaya_sistemas_2020`.

Para un mismo elipsoide pueden utilizarse distintos puntos fundamentales, que darán lugar a distintos datum y a distintas coordenadas para un mismo punto {cite}`olaya_sistemas_2020`. Además de los datum globales o continentales, varios países han creado sus propios datum para hacer su cartografía lo más precisa posible. Algunos de los datum usados en la actualidad son:

- WGS84: para todo el mundo.
- NAD27 (*North American Datum* 1927) y NAD83 (*North American Datum* 1983): para América del Norte.
- ETRS89 (*European Terrestrial Reference System* 1989): para Europa.
- ED50 (*European Datum* 1950) y ED79 (*European Datum* 1979): para España.
- SAD69 (*South American Datum* 1969): para Brasil.
- [CR05](https://epsg.io/1065-datum) (Costa Rica 2005): para Costa Rica, establecido mediante [Decreto Ejecutivo No. 33797-MJ-MOPT - PGR](http://www.pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=60238&nValor3=67698&strTipM=TC).

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```