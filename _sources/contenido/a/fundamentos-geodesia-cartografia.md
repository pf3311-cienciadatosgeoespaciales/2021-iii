# Fundamentos de cartografía y geodesia

## Trabajo previo

### Lecturas

Olaya, V. (2020). Sistemas de Información Geográfica. https://volaya.github.io/libro-sig/

## Resumen
La cartografía es ...

## Conceptos geodésicos básicos
La [geodesia](https://oceanservice.noaa.gov/facts/geodesy.html) es la ciencia que trata de la medición de la forma de la Tierra, su orientación en el espacio y su campo gravitacional. Entre las tareas típicas de un geodesta están, por ejemplo, la delineación de costas, el establecimiento de límites de entidades territoriales administrativas (ej. países, provincias) y la medición de áreas de territorios.

El planeta Tierra tiene forma esférica, sin embargo, no es una esfera perfecta: es achatada en los polos y abultada en el Ecuador. Además, su superficie es irregular debido a accidentes geográficos como valles, montañas o depresiones tectónicas, entre muchos otros.

Para realizar sus cálculos y mediciones, los geodestas deben utilizar varios modelos matemáticos, los cuales aproximan la forma real de la Tierra. Entre estos modelos están el elipsoide de referencia y el geoide. Las características de estos modelos pueden variar para satisfacer requerimientos particulares de navegación, agrimensura, catastro, uso del suelo y otras cuestiones de interés.

### Elipsoide de referencia
El [elipsoide de referencia](https://es.wikipedia.org/wiki/Elipsoide_de_referencia) es el modelo más sencillo de la forma de la Tierra. Se define por dos parámetros: el radio ecuatorial (semieje mayor) y el radio polar (semieje menor), los cuales se ejemplifican en la {numref}`figure-elipsoide-wgs84`.

```{figure} img/elipsoide-wgs84.png
:name: figure-elipsoide-wgs84

Radio ecuatorial y radio polar del elipsoide de referencia del sistema geodésico [WGS84](https://es.wikipedia.org/wiki/WGS84). Imagen de [Cmglee](https://commons.wikimedia.org/wiki/User:Cmglee) compartida a través de <a href="https://commons.wikimedia.org/wiki/File:WGS84_mean_Earth_radius.svg">Wikimedia Commons</a>.
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

Geoide. Imagen de [ICGEM](http://icgem.gfz-potsdam.de/home) compartida a través de <a href="https://commons.wikimedia.org/wiki/File:Geoid_undulation_10k_scale.jpg">Wikimedia Commons</a>.
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
- [CR05](https://epsg.io/1065-datum) (Costa Rica 2005): para Costa Rica, declarado como datum oficial mediante [Decreto Ejecutivo No. 33797-MJ-MOPT - PGR](http://www.pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?param1=NRTC&nValor1=1&nValor2=60238&nValor3=67698&strTipM=TC).

## Sistemas de coordenadas
Una vez que se dispone de modelos precisos para representar la forma de la Tierra, es posible establecer un sistema para codificar cada una de las posiciones sobre su superficie y asignar a estas las coordenadas correspondientes. Así, podemos definir un sistema de coordenadas esféricas para un elipsoide. A este tipo de coordenadas se les llama **coordenadas geográficas**.

Por otra parte, muchas veces es útil situar los elementos de la superficie del elipsoide sobre una superficie plana, dando lugar a las **proyecciones cartográficas**, las cuales utilizan coordenadas cartesianas, también llamadas coordenadas planas, debido a que resultan de proyectar la superficie del elipsoide sobre un plano.

### Coordenadas geográficas
El sistema de [coordenadas geográficas](https://es.wikipedia.org/wiki/Coordenadas_geogr%C3%A1ficas) es un sistema de coordenadas esféricas mediante el cual un punto se localiza con dos valores angulares denominados latitud y longitud, los cuales se muestran en la {numref}`figure-latitud-longitud`.

```{figure} img/latitud-longitud.png
:name: figure-latitud-longitud

Latitud y longitud en una esfera con una gratícula con intervalos de 10°. Imagen de [Peter Mercator](https://commons.wikimedia.org/wiki/User:Peter_Mercator) compartida a través de <a href="https://commons.wikimedia.org/wiki/File:Latitude_and_longitude_graticule_on_a_sphere.svg">Wikimedia Commons</a>.
```

- La **latitud** (φ, o *phi*) de un punto en la superficie de la Tierra es el ángulo entre el plano ecuatorial y la línea que pasa por este punto y el centro de la Tierra. Todos los puntos con la misma latitud forman un plano paralelo al plano del ecuador. El [ecuador](https://es.wikipedia.org/wiki/Ecuador_terrestre) es el paralelo 0° y divide el globo en hemisferios norte y sur; así el polo norte es 90° N y el polo sur es 90° S. A medida que la latitud aumenta, hacia el Norte o hacia el Sur, disminuyen los kilómetros por grado. Para el paralelo del Ecuador, sabiendo que la circunferencia que corresponde al Ecuador mide 40 075,017 km, 1° equivale a 111,319 km (resultado de dividir el perímetro del ecuador entre los 360° de longitud).

- La **longitud** (λ, o *lambda*) de un punto en la superficie de la Tierra es el ángulo entre el meridiano de referencia y el meridiano que pasa por este punto. El meridiano de referencia mayormente aceptado es el meridiano que pasa por el Real Observatorio de Greenwich, situado al sureste de Londres, Inglaterra. Este primer meridiano determina los hemisferios este y oeste. Las líneas de longitud forman semicírculos máximos que pasan por los polos y se llaman meridianos. La distancia en km a la que equivale un grado de longitud depende de la latitud.

Las líneas de los paralelos y meridianos se ilustran en la {numref}`figure-paralelos-meridianos`.

```{figure} img/paralelos-meridianos.png
:name: figure-paralelos-meridianos

Paralelos y meridianos. Imagen de Djexplo compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Latitud_y_Longitud_en_la_Tierra.svg).
```

Las coordenadas geográficas resultan de gran utilidad, especialmente cuando se trabaja con grandes regiones o con sitios distribuidos por todo el planeta. Sin embargo, no se trata de un sistema cartesiano, y tareas como la medición de áreas o distancias es mucho más complicadas. Si bien la distancia entre dos paralelos es prácticamente constante (es decir, un grado de latitud equivale más o menos a una misma distancia en todos los puntos), la distancia entre dos meridianos no lo es, y varía entre unos 11,3 kilómetros en el Ecuador hasta los cero kilómetros en los polos, donde los meridianos convergen {cite}`olaya_sistemas_2020`.

### Proyecciones cartográficas
En muchas situaciones, los sistemas cartesianos resultan más convenientes que los esféricos. En un sistema cartesiano, la posición de un punto se define mediante un par de medidas de distancia: x e y. Además, las representaciones visuales de la información cartográfica son más cómodas de manejar en una superficie plana (ej. una lámina de papel o la pantalla de una computadora) que en una esférica (ej. un globo terráqueo).

El resultado de asignar una coordenada plana a cada punto de la superficie de la Tierra (que no es plana) se conoce como [proyección cartográfica](https://es.wikipedia.org/wiki/Proyecci%C3%B3n_cartogr%C3%A1fica). Matemáticamente, se trata de asignar a cada par de coordenadas geográficas (longitud, latitud) un par de coordenadas cartesianas (x, y). 

#### Tipos de proyecciones
Las proyecciones pueden clasificarse, según la superficie sobre la que se proyectan los objetos, en cilíndricas, cónicas y azimutales.

- **Cilíndricas**: El globo terrestre se proyecta en una superficie cilíndrica. Son muy utilizadas, pero con frecuencia se modifican debido a las grandes distorsiones que muestran en las zonas de latitud elevada, lo que impide apreciar a las regiones polares en su verdadera proporción. Son muy útiles para apreciar la superficie de la Tierra completa, por lo que se utiliza en [mapamundis](https://es.wikipedia.org/wiki/Mapamundi). La {numref}`figure-proyeccion-cilindrica` muestra un esquema de una proyección cilíndrica.

```{figure} img/proyeccion-cilindrica.jpg
:name: figure-proyeccion-cilindrica

Esquema de proyección cilíndrica. Imagen de [Traroth](https://commons.wikimedia.org/wiki/User:Traroth) compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Projection_cylindrique.jpg).
```

- **Cónicas**: El globo terrestre se proyecta en una superficie cónica tangente, situando el vértice en el eje que une los dos polos. Aunque las formas presentadas son de los polos, los cartógrafos utilizan este tipo de proyección para ver los países y continentes. La {numref}`figure-proyeccion-conica` muestra un esquema de una proyección cilíndrica.

```{figure} img/proyeccion-conica.jpg
:name: figure-proyeccion-conica

Esquema de proyección cónica. Imagen de [Traroth](https://commons.wikimedia.org/wiki/User:Traroth) compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Projection_conique.jpg).
```

- **Azimutales**: También son llamadas proyecciones polares. Se proyecta una porción de la Tierra sobre un plano tangente al globo en un punto seleccionado, obteniéndose una imagen similar a la visión de la Tierra desde un punto interior o exterior. Se utilizan principalmente para los polos y los hemisferios. La {numref}`figure-proyeccion-azimutal` muestra un esquema de una proyección azimutal.

```{figure} img/proyeccion-azimutal.jpg
:name: figure-proyeccion-azimutal

Esquema de proyección azimutal. Imagen de [Traroth](https://commons.wikimedia.org/wiki/User:Traroth) compartida a través de [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Projection_azimutale_gnomonique.jpg).
```


## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```