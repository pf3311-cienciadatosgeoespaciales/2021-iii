#!/usr/bin/env python
# coding: utf-8

# # Ejemplo de análisis con pandas, geopandas y folium

# Se presenta un ejemplo de análisis [reproducible](https://es.wikipedia.org/wiki/Reproducibilidad_y_repetibilidad) de datos geoespaciales: la distribución en áreas silvestres protegidas (ASP) de especies de murciélagos.

# ## Entradas

# ### Registros de presencia de murciélagos

# Provienen de una [consulta](https://doi.org/10.15468/dl.kj2qnn) al portal de la [Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://www.gbif.org/).
# 
# Para efectos de este análisis, están disponibles en [https://raw.githubusercontent.com/pf3311-cienciadatosgeoespaciales/2021-iii/main/contenido/b/datos/murcielagos.csv](https://raw.githubusercontent.com/pf3311-cienciadatosgeoespaciales/2021-iii/main/contenido/b/datos/murcielagos.csv).

# ### Polígonos de áreas silvestres protegidas (ASP)

# Fueron publicados por el [Sistema Nacional de Áreas de Conservación (Sinac)](http://www.sinac.go.cr/) a través del [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/), en [http://geos1pne.sirefor.go.cr/wfs?](http://geos1pne.sirefor.go.cr/wfs?).
# 
# Para efectos de este análisis, están disponibles en [https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/blob/main/contenido/b/datos/asp.geojson](https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/blob/main/contenido/b/datos/asp.geojson).

# ## Procesamiento

# In[1]:


import math

import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import geopandas as gpd

import folium
from folium import Marker
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap


# ### Lectura de datos

# **Registros de presencia de murciélagos**

# In[2]:


# Carga de registros de presencia de murciélagos en un dataframe de pandas

murcielagos = pd.read_csv("https://raw.githubusercontent.com/pf3311-cienciadatosgeoespaciales/2021-iii/main/contenido/b/datos/murcielagos.csv", 
                          sep="\t")

murcielagos


# **Polígonos de ASP**

# In[3]:


# Carga de registros de presencia de murciélagos en un dataframe de pandas

asp = gpd.read_file("https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/raw/main/contenido/b/datos/asp.geojson")

asp


# ### Visualización preliminar

# **Mapa interactivo de puntos agrupados (*clusters*)**

# In[4]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8)


# Capa de ASP
folium.GeoJson(data="https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/raw/main/contenido/b/datos/asp.geojson", 
               name="ASP").add_to(m)


# Capa de registros de presencia de murciélagos agrupados
mc = MarkerCluster()
for idx, row in murcielagos.iterrows():
    if not math.isnan(row['decimalLongitude']) and not math.isnan(row['decimalLatitude']):
        mc.add_child(Marker([row['decimalLatitude'], row['decimalLongitude']], popup=row['species']))
m.add_child(mc)

# Control de capas
folium.LayerControl().add_to(m)

# Despliegue del mapa
m


# **Mapa interactivo de calor (*heatmap*)**

# In[5]:


# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB dark_matter', zoom_start=8)


# Capa de ASP
folium.GeoJson(data="https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/raw/main/contenido/b/datos/asp.geojson", 
               name="ASP").add_to(m)


# Capa de calor de registros de presencia de murciélagos
HeatMap(data=murcielagos[['decimalLatitude', 'decimalLongitude']], radius=10).add_to(m)

# Control de capas
folium.LayerControl().add_to(m)

# Despliegue del mapa
m


# ### Cálculo de la cantidad de especies por ASP

# **Conversión del dataframe de murciélagos a geodataframe**

# In[6]:


murcielagos = gpd.GeoDataFrame(murcielagos, 
                               geometry=gpd.points_from_xy(murcielagos.decimalLongitude, murcielagos.decimalLatitude))


# In[7]:


# Join espacial de las capas de ASP y registros de presencia de murciélagos

asp_contienen_murcielagos = asp.sjoin(murcielagos, how="left", op="contains")

# Conteo de especies en cada ASP
asp_especies = asp_contienen_murcielagos.groupby("id").species.nunique()
asp_especies = asp_especies.reset_index() # para convertir la serie a dataframe

asp_especies.rename(columns = {'species': 'cantidad_especies_murcielagos'}, inplace = True)

asp_especies


# ## Salidas

# ### Tabular

# In[8]:


# Join para agregar la columna con el conteo a la capa de ASP
asp_especies = asp_especies.join(asp.set_index('id'), on='id', rsuffix='_b')

asp_especies[["nombre_asp", "cantidad_especies_murcielagos"]].sort_values("cantidad_especies_murcielagos", ascending=[False])


# ### Gráfica

# In[9]:


asp_especies_grafico = asp_especies[["nombre_asp", "cantidad_especies_murcielagos"]].sort_values("cantidad_especies_murcielagos", ascending=[False]).head(15)


# Graficación
asp_especies_grafico.plot(x='nombre_asp', 
                          y='cantidad_especies_murcielagos', 
                          kind='bar', 
                          figsize=(20,10), 
                          color='red')

# Título y leyendas en los ejes
plt.title('Cantidad de especies de murciélagos por ASP', fontsize=20)
plt.xlabel('ASP', fontsize=16)
plt.ylabel('Cantidad de especies', fontsize=16)


# ### Geoespacial

# In[10]:


# Creación del mapa base
m = folium.Map(location=[9.8, -84], tiles='CartoDB positron', zoom_start=8)

folium.Choropleth(
    name="Cantidad de especies en ASP",
    geo_data=asp,
    data=asp_especies,
    columns=['id', 'cantidad_especies_murcielagos'],
    bins=8,
    key_on='feature.properties.id',
    fill_color='Reds', 
    fill_opacity=0.5, 
    line_opacity=1,
    legend_name='Cantidad de especies de murciélagos',
    smooth_factor=0).add_to(m)

# Control de capas
folium.LayerControl().add_to(m)

# Despliegue del mapa
m


# In[ ]:




