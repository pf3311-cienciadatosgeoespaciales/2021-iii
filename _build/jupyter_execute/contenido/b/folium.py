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


# In[ ]:




