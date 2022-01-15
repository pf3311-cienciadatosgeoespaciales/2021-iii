# Sistemas de información geográfica


## Trabajo previo

### Lecturas
Olaya, V. (2020). Sistemas de Información Geográfica. https://volaya.github.io/libro-sig/ (Parte 1, capítulo “¿Qué es un SIG?”)


## Resumen
En general, un sistema de información geográfica (SIG) maneja datos georreferenciados (i.e. ubicados en un sistema de coordenadas) y los asocia con datos convencionales (ej. números, textos).


## Sistemas de información geográfica
A principios de la década de 1960, el geógrafo inglés [Roger Tomlinson](https://es.wikipedia.org/wiki/Roger_Tomlinson) desarrolló en Canadá el que se considera el primer sistema de información geográfica. Se trataba del [Canada Geographic Information System (CGIS)](https://en.wikipedia.org/wiki/Canada_Geographic_Information_System) y su objetivo fue manejar los datos del inventario geográfico canadiense y su análisis para la gestión del territorio rural. De manera casi simultánea al trabajo de Tomlinson, surgieron desarrollos similares en Estados Unidos y en el Reino Unido. El surgimiento de los sistemas de información geográfica no implicó solo el surgimiento de nuevas herramientas de software, sino también el desarrollo de técnicas que hasta entonces no habían sido necesarias {cite}`olaya_sistemas_2020` como, por ejemplo, la manipulación de nuevos tipos de datos geométricos (ej. puntos, líneas, polígonos).

En general, un sistema de información geográfica (SIG) maneja datos georreferenciados (i.e. ubicados en un sistema de coordenadas) y los asocia con datos convencionales (ej. números, textos), como se muestra en la {numref}`figure-mapa-qgis`.

```{figure} img/mapa-qgis.png
:name: figure-mapa-qgis

Mapa elaborado en QGIS que muestra la ubicación de los aeródromos de Costa Rica.
```

En la actualidad, los SIG presentan los datos en capas (*layers*). Por ejemplo, el mapa de la {numref}`figure-mapa-qgis` contiene una capa base raster (la que muestra el mar y el continente), una capa de polígonos correspondiente a las provincias de Costa Rica y una capa de puntos correspondiente a los aeródromos. A la izquierda puede apreciarse la lista de esas capas y a la derecha un cuadro con información detallada sobre uno de los aeródromos.

Los SIG de escritorio (ej. [ArcGIS Desktop](https://www.esri.com/en-us/arcgis/products/arcgis-desktop/overview), [QGIS](https://www.qgis.org/)) son herramientas con interfaces de usuario muy gráficas e intuitivas, que no requieren de conocimientos de programación de computadoras y que permiten generar cartografía de alta calidad. Sin embargo, son poco flexibles y los resultados que producen son difícilmente [reproducibles](https://es.wikipedia.org/wiki/Reproducibilidad_y_repetibilidad).