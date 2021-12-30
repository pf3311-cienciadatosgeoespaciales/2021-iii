# Datos geoespaciales

Una gran parte de los datos disponibles contiene algún tipo de componente geográfico o espacial[^footnote-geografico-espacial]. Este componente puede expresarse de varias formas. Por ejemplo:

- **Con nombres de lugares**: *El [sapo dorado (*Incilius periglenes*)](https://es.wikipedia.org/wiki/Incilius_periglenes) era una especie de anfibio, endémica de los bosques nubosos de altitud de Monteverde, Costa Rica.*
- **Con direcciones**: *La [sede de la Organización de las Naciones Unidas (ONU)](https://es.wikipedia.org/wiki/Sede_de_la_Organizaci%C3%B3n_de_las_Naciones_Unidas) está ubicada en la ciudad de Nueva York, Estados Unidos, en la Primera Avenida, 750.*
- **Con coordenadas**: *La cima del [Monte Everest](https://es.wikipedia.org/wiki/Monte_Everest) se localiza en las coordenadas geográficas 86°55′31″ E y 27°59′17″ N, como se muestra en la {numref}`figure-mapa-nepal-everest`.*

```{figure} img/nepal-map.jpg
:name: figure-mapa-nepal-everest

Mapa de Nepal que muestra la ubicación del Monte Everest en el sistema de coordenadas geográficas. Fuente: [https://www.mapsofworld.com/](https://www.mapsofworld.com/).
```

Las coordenadas correspondientes a lugares y direcciones pueden obtenerse a través de un proceso denominado [*georreferenciación*](https://es.wikipedia.org/wiki/Georreferenciaci%C3%B3n), mediante el cual, en general, se determina la posición espacial de alguna entidad en un sistema de coordenadas. La georreferenciación puede emplearse también para obtener las coordenadas de, por ejemplo, fotografías aéreas o mapas antiguos. Es un proceso que puede resultar complejo y costoso y para el que se han desarrollado metodologías y plataformas especializadas (ej. [Chapman AD & Wieczorek JR (2020) Georeferencing Best Practices](https://doi.org/10.15468/doc-gg7h-s853), [GEOLocate](https://www.geo-locate.org/)).

En la actualidad, hay una gran cantidad de fuentes que generan datos georreferenciados. Entre estas pueden mencionarse las tecnologías de [observación de la Tierra (*Earth Observation*)](https://ec.europa.eu/jrc/en/research-topic/earth-observation) (ej. [imágenes satelitales](https://es.wikipedia.org/wiki/Imagen_satelital)), los dispositivos móviles y los sensores remotos, entre muchas otras.




[^footnote-geografico-espacial]: El adjetivo *geográfico* se refiere a la superficie de la Tierra. Así, por ejemplo, las *coordenadas geográficas* se utilizan para ubicar cualquier punto en la superficie terrestre. El término *espacial* se emplea para referirse a cualquier espacio, no siempre localizable en el planeta Tierra. En muchas ocasiones, ambas palabras son intercambiables. Por ejemplo, muchos de los métodos utilizados para analizar datos geográficos pueden aplicarse también en espacios no geográficos como, por ejemplo, otros planetas, el cosmos, el cuerpo humano (ej. con radiografías) o secuencias genómicas. En los últimos años, se ha incrementado el uso del término *geoespacial*, el cual se eligió para el nombre de este curso, como una forma de referirse al subconjunto del espacio correspondiente a la superficie de la Tierra {cite}`longley_geographic_2005`.