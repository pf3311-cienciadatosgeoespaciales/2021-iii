#!/usr/bin/env python
# coding: utf-8

# # geopandas: paquete para agregar capacidades geoespaciales a pandas

# [GeoPandas](http://geopandas.org/) es un proyecto de software libre que extiende los tipos de datos de [pandas](http://pandas.pydata.org/) para incorporar objetos geométricos (puntos, líneas, polígonos, etc). GeoPandas se apoya en las bibliotecas [Shapely](https://github.com/Toblerity/Shapely/) para realizar las operaciones geométricas, [Fiona](https://github.com/Toblerity/Fiona/) para acceder a los datos (ej. en archivos) y [Matplotlib](https://matplotlib.org/) para graficación.
# 
# El objetivo de GeoPandas es facilitar el trabajo con datos geoespaciales en el lenguaje Python, lo que se logra a través de la implementación de nuevas estructuras. Las dos estructuras principales de GeoPandas son:
# 
# - [GeoSeries](http://geopandas.org/data_structures.html#geoseries): es un vector en el que cada elemento es un conjunto de una o varias geometrías correspondientes a una observación. Por ejemplo, el polígono (o multipolígono) que representa una provincia.
# - [GeoDataFrame](http://geopandas.org/data_structures.html#geodataframe): es una estructura tabular (i.e. con filas y columnas) de datos geométricos y no geométricos (ej. textos, números). El conjunto de geometrías se implementa a través de GeoSeries.

# ## Instalación

# ### En una estación de trabajo

# geopandas puede instalarse tanto mediante [Conda](https://conda.io/) como mediante [pip](https://pypi.org/project/pip/).
# 
# ```shell
# # Instalación mediante Conda
# conda install geopandas
# 
# # Instalación mediante pip
# pip install geopandas
# ```

# ### En Google Colab

# ```shell
# # Instalación de bibliotecas de GDAL para Python
# !apt install gdal-bin python-gdal python3-gdal
# 
# # Instalación de r-tree
# !apt install python3-rtree
# 
# # Instalación de GeoPandas
# !pip install git+git://github.com/geopandas/geopandas.git
# 
# # Instalación de Descartes
# !pip install descartes
# ```

# ## Carga

# Para instalar [contextily](https://contextily.readthedocs.io/en/latest/):
# 
# ```shell
# !conda install -c conda-forge contextily -y
# ```

# In[1]:


import os
import requests
import zipfile

import pandas as pd

import geopandas as gpd
import contextily as cx
from geojson import dump
from owslib.wfs import WebFeatureService

import matplotlib
import matplotlib.pyplot as plt


# In[2]:


# Versión de geopandas
gpd.__version__


# ## Operaciones básicas

# ### read_file() - carga de datos

# In[3]:


# Lectura de datos de países de Natural Earth

paises = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

paises


# ### info() - información general sobre un conjunto de datos

# In[4]:


paises.info()


# ### head(), tail(), sample() - despliegue de filas de un conjunto de datos

# In[5]:


# Muestra de 10 filas
paises.head(10)


# ### Selección de columnas

# In[6]:


paises[["name", "pop_est"]]


# ### Selección de filas

# In[7]:


# Países con población estimada mayor o igual a mil millones
paises[paises["pop_est"] >= 1000000000]


# ### Selección de filas y columnas en la misma expresión

# In[8]:


paises.loc[paises["pop_est"] >= 1000000000, ["name", "pop_est"]]


# ### plot() - mapeo

# In[9]:


# Mapa de coropletas

paises.plot(column = "pop_est", 
            cmap='OrRd', 
            scheme='quantiles',
            figsize=(20, 20)
            )


# In[10]:


# Mapa de coropletas con leyenda

from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, ax = plt.subplots(1, 1, figsize=(20, 20))

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

paises.plot(column='pop_est', ax=ax, legend=True, cax=cax)


# In[11]:


# Mapa con múltiples capas

ciudades = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

base = paises.plot(color='white', edgecolor='black', figsize=(20, 20))
ciudades.plot(ax=base, marker='o', color='red', markersize=8)


# ## Ejemplos de uso

# ### Análisis de distribución de especies de murciélagos en Costa Rica

# #### 1. Obtención de datos

# ##### Registros de presencia de murciélagos

# In[12]:


# Descarga de archivo CSV comprimido en ZIP mediante solicitud tipo GET
response = requests.get('https://api.gbif.org/v1/occurrence/download/request/0105729-210914110416597.zip', 
                        allow_redirects=True)
open('datos/murcielagos.zip', 'wb').write(response.content)

# Descompresión
with zipfile.ZipFile("datos/murcielagos.zip") as zipfile:
    zipfile.extractall("datos/")
    
# Cambio de nombre del archivo CSV
os.rename("datos/0105729-210914110416597.csv", "datos/murcielagos.csv")


# In[13]:


# Carga de registros de presencia de murciélagos en un dataframe

murcielagos = pd.read_csv("datos/murcielagos.csv", sep="\t")
murcielagos


# In[14]:


murcielagos = gpd.GeoDataFrame(murcielagos, geometry=gpd.points_from_xy(murcielagos.decimalLongitude, murcielagos.decimalLatitude))
murcielagos.plot(figsize=(20, 20))


# ##### Capas geoespaciales de Costa Rica

# ###### Áreas silvestres protegidas (ASP)

# In[15]:


wfs = WebFeatureService(url='http://geos1pne.sirefor.go.cr/wfs', version='1.1.0')

# Parámetros de la solicitud
params = dict(service='WFS',
              version='1.1.0', 
              request='GetFeature', 
              typeName='PNE:areas_silvestres_protegidas',
              srsName='urn:ogc:def:crs:EPSG::4326',
              outputFormat='json')

# Solicitud
response = requests.Request("GET", "http://geos1pne.sirefor.go.cr/wfs", params=params).prepare().url
response


# In[16]:


# Leer datos del URL
asp = gpd.read_file(response)

asp.plot(figsize=(20, 20))


# ### 2. Visualización de todas las capas

# In[17]:


# Mapa con todas las capas

base = asp.plot(color='white', edgecolor='green', figsize=(20, 20))
ax = murcielagos.plot(ax=base, marker='o', color='black', markersize=8)

cx.add_basemap(ax, crs=asp.crs)


# ### 3. Conteo de especies en cada polígono

# In[18]:


# Join espacial de las capas de ASP y registros de presencia de murciélagos

asp_contains_murcielagos = asp.sjoin(murcielagos, how="inner", op="contains")


# In[19]:


asp_contains_murcielagos.info()


# In[20]:


asp_contains_murcielagos


# In[21]:


asp_contains_murcielagos.plot(figsize=(20, 20))


# In[22]:


# Conteo de especies en cada ASP
asp_count_especies = asp_contains_murcielagos.groupby("id").species.nunique()
asp_count_especies = asp_count_especies.reset_index() # para convertir la serie a dataframe

asp_count_especies.rename(columns = {'species': 'especies_murcielagos'}, inplace = True)

asp_count_especies.head(10)


# In[23]:


# Join para agregar la columna con el conteo a la capa de ASP
asp_especies = asp.join(asp_count_especies.set_index('id'), on='id', rsuffix='_b')
asp_especies


# In[24]:


# Mapeo

fig, ax = plt.subplots(1, 1, figsize=(20, 20))

divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)

asp_especies.plot(column='especies_murcielagos', ax=ax, legend=True, cax=cax)

cx.add_basemap(ax, crs=asp_especies.crs, source=cx.providers.Stamen.TonerLite)


# In[ ]:




