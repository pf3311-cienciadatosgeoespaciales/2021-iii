#!/usr/bin/env python
# coding: utf-8

# # Fiona y Shapely: paquetes para lectura, escritura y análisis de datos vectoriales

# ## Descripción general

# ### Fiona

# [Fiona](https://github.com/Toblerity/Fiona) es una biblioteca en Python para la lectura y escritura de datos geoespaciales. Su código está enlazado con [GDAL](https://gdal.org/), desarrollada en C/C++.
# 
# A diferencia de otras bibliotecas basadas en GDAL (ej. [osgeo.gdal/osgeo.ogr](https://gdal.org/python/), con ejemplos en [Python GDAL/OGR Cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/)), Fiona está diseñada para seguir el estilo estándar de entrada-salida (IO) de Python, mediante protocolos y tipos de datos típicos de Python, tales como archivos, diccionarios, mapeos e iteradores, en lugar de clases específicas de la implementación C/C++ de GDAL.
# 
# Fiona está hecha para ser "simple y confiable". Está integrada con otras bibliotecas geoespaciales de Python como [pyproj](https://github.com/pyproj4/pyproj), [Rtree](https://github.com/Toblerity/rtree) y [Shapely](https://github.com/shapely/shapely).

# ### Shapely

# [Shapely](https://github.com/shapely/shapely) es una biblioteca en Python para la manipulación y análisis de objetos geométricos planos. Está basada en la biblioteca [GEOS](https://libgeos.org/), programada en C/C++.
# 
# Shapely no se ocupa de formatos de datos o sistemas de coordenadas, pero puede integrarse con bibliotecas que lo hacen (ej. [Fiona](https://github.com/Toblerity/Fiona), [pyproj](https://github.com/pyproj4/pyproj)).

# Tanto Fiona como Shapely son utilizadas por la biblioteca [geopandas](https://geopandas.org/), para el análisis avanzado de datos geoespaciales.

# ## Ejemplos de uso

# ### Análisis de distribución de especies de murciélagos en Costa Rica

# Se analiza la distribución de especies de [murciélagos](https://es.wikipedia.org/wiki/Chiroptera) en Costa Rica con base en varias divisiones del territorio. Se utilizan las siguientes fuentes de datos:
# 
# - Registros de presencia de murciélagos, agrupados por la [Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://api.gbif.org/v1/occurrence/download/request/0105729-210914110416597.zip).
# - Capas geoespaciales de Costa Rica agrupadas por el [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/).
# 
# Los pasos del procedimiento a seguir son:
# 
# 1. Obtención de datos.
# 2. Creación de un archivo GeoPackage con todas las capas.
# 3. Conteo de especies en cada polígono de las capas.

# #### Bibliotecas

# In[1]:


import os
import requests
import zipfile

import csv

import fiona
import fiona.crs
from shapely.geometry import Point, mapping, shape

from owslib.wfs import WebFeatureService
from geojson import dump


# #### 1. Obtención de datos

# ##### Registros de presencia de murciélagos

# Se descargan en un archivo CSV desde una consulta al portal de GBIF.

# In[2]:


# Descarga de archivo CSV comprimido en ZIP mediante solicitud tipo GET

response = requests.get('https://api.gbif.org/v1/occurrence/download/request/0105729-210914110416597.zip', 
                        allow_redirects=True)
open('datos/murcielagos.zip', 'wb').write(response.content)


# In[3]:


# Descompresión

with zipfile.ZipFile("datos/murcielagos.zip") as zipfile:
    zipfile.extractall("datos/")


# In[4]:


# Cambio de nombre del archivo CSV

os.rename("datos/0105729-210914110416597.csv", "datos/murcielagos.csv")


# ##### Capas geoespaciales de Costa Rica

# Se descargan como archivos GeoJON desde servicios WFS.

# ###### Áreas silvestres protegidas (ASP)

# Lista de capas del servidor WFS del Sinac:

# In[5]:


# Clase WebFeatureService de owslib.wfs

wfs = WebFeatureService(url='http://geos1pne.sirefor.go.cr/wfs', version='1.1.0')
list(wfs.contents)


# Otras propiedades del objeto WebFeatureService:

# In[6]:


# Título
wfs.identification.title


# In[7]:


# Operaciones
[operation.name for operation in wfs.operations]


# Las operaciones y sus parámetros están documentados en [http://opengeospatial.github.io/e-learning/wfs/text/operations.html](http://opengeospatial.github.io/e-learning/wfs/text/operations.html).

# Operación [GetCapabilities](http://opengeospatial.github.io/e-learning/wfs/text/operations.html#getcapabilities):

# In[8]:


# Solicitud de metadatos del servicio

# Parámetros de la solicitud
params = dict(service='WFS', version='1.1.0', request='GetCapabilities')

# Solicitud
response = requests.get("http://geos1pne.sirefor.go.cr/wfs", params=params)

# Despliegue del contenido de la respuesta
response.content


# Puede ver el XML de manera estructurada en [https://jsonformatter.org/xml-parser](https://jsonformatter.org/xml-parser)

# Operación [GetFeature](http://opengeospatial.github.io/e-learning/wfs/text/operations.html#getfeature):

# In[9]:


# Solicitud de capa WFS de ASP mediante GET, para retornarse como JSON

# Parámetros de la solicitud
params = dict(service='WFS',
              version='1.1.0', 
              request='GetFeature', 
              typeName='PNE:areas_silvestres_protegidas',
              srsName='urn:ogc:def:crs:EPSG::4326',
              outputFormat='json')

# Solicitud
response = requests.get("http://geos1pne.sirefor.go.cr/wfs", params=params)


# In[10]:


# Descarga de la respuesta en un archivo GeoJSON

with open('datos/asp.geojson', 'w') as file:
   dump(response.json(), file)


# #### 2. Creación de un archivo GeoPackage con todas las capas

# El archivo Geopackage se crea con el objetivo de mantener todas las capas en una misma estructura y así facilitar la manipulación de los datos.

# ##### Registros de presencia de murciélagos

# In[11]:


# Esquema de la nueva capa de registros de presencia de murciélagos
# Se incluyen solo los campos más importantes para el análisis
schema = {'geometry':'Point',
          'properties':{'gbifID':'str',
                        'species':'str',
                        'decimalLatitude':'float',
                        'decimalLongitude':'float'
                       }}

# Inserción de registros en el archivo GeoPackage
with fiona.collection('datos/distribucion-murcielagos.gpkg', 
                mode='w',
                schema=schema,
                driver='GPKG',
                crs=fiona.crs.from_epsg(4326),
                layer='registros-murcielagos') as collection:
    with open('datos/murcielagos.csv') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            point = Point(float(row['decimalLongitude']), float(row['decimalLatitude']))
            collection.write({
                'properties': {
                    'gbifID':row['gbifID'],
                    'species':row['species'],
                    'decimalLatitude':row['decimalLatitude'],
                    'decimalLongitude':row['decimalLongitude']
                },
                'geometry':mapping(point)
            })                        


# ##### Áreas Silvestres Protegidas (ASP)

# In[ ]:


# Se agrega el archivo GeoJSON de ASP al GPKG

with fiona.open('datos/asp.geojson') as source:
    with fiona.open('datos/distribucion-murcielagos.gpkg', 'w', 'GPKG', source.schema, source.crs, layer='asp') as sink:
        for record in source:
            sink.write(record)


# #### 3. Conteo de especies en cada polígono de las capas

# ##### En ÁSP

# In[ ]:


# Conteo de especies en ASP

# Esquema de la capa con el total y la lista de especies por ASP
schema = {'geometry':'Unknown',
          'properties':{'id':'str',
                        'nombre_asp':'str',
                        'cantidad_especies':'int',
                        'lista_especies':'str'
                       }}

with fiona.collection('datos/distribucion-murcielagos.gpkg', 'r', layer='asp') as asp:
    
    i = 1 # contador de ASP, para imprimir el progreso del procedimiento
    
    with fiona.open('datos/asp-especies.geojson','w','GeoJSON', schema, asp.crs) as sink:
    
        for record_asp in asp:
            print(i, record_asp['properties']['siglas_cat'], record_asp['properties']['nombre_asp'])

            species_set = set() # conjunto de especies en el ASP

            with fiona.collection('datos/distribucion-murcielagos.gpkg', 'r', layer='registros-murcielagos') as registros:
                for registro in registros:
                    if (registro['properties']['species'] == ''):
                        continue
                    
                    if shape(record_asp['geometry']).contains(shape(registro['geometry'])):
                        species_set.add(registro['properties']['species'])

            print(len(species_set))
            print(', '.join(species_set))
            print('\n')

            i += 1
                
            sink.write({
                'properties': {
                    'id':record_asp['properties']['id'],
                    'nombre_asp':record_asp['properties']['nombre_asp'],
                    'cantidad_especies':len(species_set),
                    'lista_especies':', '.join(species_set)
                },
                'geometry':record_asp['geometry']
            }) 


# In[ ]:


# Se agrega el archivo GeoJSON de asp-especies al GPKG

with fiona.open('datos/asp-especies.geojson') as source:
    with fiona.open('datos/distribucion-murcielagos.gpkg', 'w', 'GPKG', source.schema, source.crs, layer='asp-especies') as sink:
        for record in source:
            sink.write(record)


# In[ ]:




