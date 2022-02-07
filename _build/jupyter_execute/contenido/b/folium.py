#!/usr/bin/env python
# coding: utf-8

# # folium: paquete para desarrollo de mapas web

# ## Descripción general

# [folium](https://python-visualization.github.io/folium/) es una biblioteca de Python para el desarrollo de mapas web, basada en la biblioteca [Leaflet](https://leafletjs.com/) de JavaScript. Así, es posible manipular los datos con bibliotecas de Python (ej. pandas, GeoPandas) y presentarlos en mapas Leaflet a través de folium.

# ## Instalación

# folium puede instalarse tanto mediante [Conda](https://conda.io/) como mediante [pip](https://pypi.org/project/pip/).
# 
# ```shell
# # Instalación mediante Conda
# conda install -c conda-forge folium
# 
# # Instalación mediante pip
# pip install folium
# ```

# ## Carga

# In[1]:


import folium

# Versión
folium.__version__


# ## Opciones básicas de configuración

# Las siguientes son algunas de las opciones de configuración que provee la clase [Map](https://python-visualization.github.io/folium/modules.html#folium.folium.Map).

# In[2]:


# Creación de un mapa con un centro (x, y)
m = folium.Map(location=[10, -84])

# Despliegue del mapa en el notebook
m


# In[3]:


# Especificación del ancho y del largo (en pixeles) del mapa
m = folium.Map(
    location=[10, -84], 
    width=650, height=400)

m


# In[4]:


# Especificación del nivel inicial de acercamiento (zoom)
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7)

m


# ## Manejo de capas base

# Por defecto, Folium utiliza OpenStreetMap como mapa base. Pueden elegirse otros mapas base mediante el parámetro tiles, el cual tiene un conjunto de valores predeterminados:
# 
# - “OpenStreetMap”
# - “Mapbox Bright”
# - “Mapbox Control Room”
# - “Stamen” ("Terrain", "Toner" y "Watercolor")
# - “Cloudmade” (Requiere una llave del API)
# - “Mapbox” (Requiere una llave del API)
# - “CartoDB” ("positron" y "dark_matter")

# In[5]:


# Mapa de Stamen Terrain
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=5, 
    tiles='Stamen Terrain')
m


# In[6]:


# Mapa de Stamen Toner
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='Stamen Toner')

m


# In[7]:


# Mapa de Stamen Watercolor
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='Stamen Watercolor')

m


# In[8]:


# Mapa de CartoDB positron
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='CartoDB positron')

m


# In[9]:


# Mapa de CartoDB dark_matter
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='CartoDB dark_matter')

m


# El siguiente es un ejemplo que utiliza la opción como mapa base el mapa “World Imagery” de ESRI. Pueden verse más ejemplos de mapas de ESRI en [https://ocefpaf.github.io/python4oceanographers/blog/2015/03/23/wms_layers/](https://ocefpaf.github.io/python4oceanographers/blog/2015/03/23/wms_layers/).

# In[10]:


# Mapa "World Imagery "de ESRI
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    tiles='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/MapServer/tile/{z}/{y}/{x}', 
    attr='ESRI World Imagery')

m


# Registros de presencia de especies en la Infraestructura Mundial de Información en Biodiversidad (GBIF). Pueden verse más ejemplos de uso de este tipo de información en la documentación del API de mapas de GBIF.

# In[11]:


# Registros de presencia de especies en GBIF
m = folium.Map(
    location=[0, 0],
    width=650, height=400,
    zoom_start=1,
    tiles='https://api.gbif.org/v2/map/occurrence/density/{z}/{x}/{y}@1x.png?style=purpleYellow.point',
    attr='GBIF')

m


# ## Controles

# In[12]:


# Control de escala
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    control_scale=True)

m


# In[13]:


# Mapa con múltiples capas base

# Creación de un mapa
m = folium.Map(
    location=[10, -84], 
    width=650, height=400, 
    zoom_start=7, 
    control_scale=True)

# Se añaden capas base adicionales
folium.TileLayer(
    tiles='CartoDB positron', 
    name='CartoDB positron').add_to(m)

folium.TileLayer(
    tiles='Stamen Terrain', 
    name='Stamen Terrain').add_to(m)


# ESRI NatGeo World Map
folium.TileLayer(
    tiles='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/MapServer/tile/{z}/{y}/{x}',
    name='NatGeo World Map',
    attr='ESRI NatGeo World Map').add_to(m)

# Densidad de registros de presencia de especies
folium.TileLayer(
    tiles='https://api.gbif.org/v2/map/occurrence/density/{z}/{x}/{y}@1x.png?&bin=hex&hexPerTile=28&style=classic.poly',
    name='Densidad de registros de presencia de especies',
    attr='GBIF').add_to(m)

# Se añade un control de capas
folium.LayerControl().add_to(m)

m


# In[14]:


# Grabación del mapa en el disco
m.save("/home/mfvargas/mapa-folium.html")


# ## Mapas con múltiples capas

# In[15]:


# Mapa con capa base y capa vectorial

# Creación del mapa
m = folium.Map(location=[10, -84], tiles='CartoDB positron', zoom_start=7)

# Se añaden al mapa las capas GeoJson
folium.GeoJson(data="https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/raw/main/contenido/b/datos/redvial.geojson", name='Red vial').add_to(m)

# Control de capas
folium.LayerControl().add_to(m)

# Despliegue del mapa
m


# ## Mapeo de puntos de un archivo CSV

# In[16]:


import pandas as pd

# Lectura del archivo
felinos = pd.read_csv("https://raw.githubusercontent.com/pf3311-cienciadatosgeoespaciales/2021-iii/main/contenido/b/datos/felinos.csv", sep="\t")

felinos.head()


# In[17]:


from folium import Marker

# Creación del mapa
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Adición de marcadores
for idx, row in felinos.iterrows():
    Marker([row['decimalLatitude'], row['decimalLongitude']], popup=row['species']).add_to(m)

# Despliegue del mapa
m


# **Ejercicio**: incluya en la ventana emergente (“popup”) de los puntos, la información relacionda con la localidad y la fecha.

# ## Mapas de puntos agrupados (“cluster maps”)

# In[18]:


import math
from folium.plugins import MarkerCluster

# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Adición de puntos agrupados
mc = MarkerCluster()
for idx, row in felinos.iterrows():
    if not math.isnan(row['decimalLongitude']) and not math.isnan(row['decimalLatitude']):
        mc.add_child(Marker([row['decimalLatitude'], row['decimalLongitude']], popup=row['species']))
m.add_child(mc)

# Despliegue del mapa
m


# ## Mapas de burbuja (“bubble maps”)

# In[19]:


from folium import Circle

# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Adición de las "burbujas"
for i in range(0,len(felinos)):
    Circle(
        location=[felinos.iloc[i]['decimalLatitude'], felinos.iloc[i]['decimalLongitude']],
        radius=1000,
        color="black", 
        popup=row['species']).add_to(m)

# Despliegue del mapa
m


# El tamaño y el color de los puntos puede utilizarse para diferenciar algún atributo de los datos.

# In[20]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

def color_especie(especie):
    if especie == "Panthera onca":
        return 'orange'
    else:
        return 'black'

# Adición de las "burbujas"
for i in range(0,len(felinos)):
    Circle(
        location=[felinos.iloc[i]['decimalLatitude'], felinos.iloc[i]['decimalLongitude']],
        radius=1000,
        color=color_especie(felinos.iloc[i]['species']),
        popup=felinos.iloc[i]['species']).add_to(m)

# Despliegue del mapa
m


# **Ejercicio**: Modifique la función color_especie() para que retorne un color diferente por cada especie de felino.

# ## Mapas de calor (“heatmaps”)

# In[21]:


from folium.plugins import HeatMap


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)

# Mapa de color
HeatMap(data=felinos[['decimalLatitude', 'decimalLongitude']], radius=10).add_to(m)

# Despliegue del mapa
m


# In[ ]:




