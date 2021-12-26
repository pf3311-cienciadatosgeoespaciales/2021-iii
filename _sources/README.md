## Creación y configuración del Jupyter Book de PF-3311 Ciencia de datos geoespaciales

1. Creación de un ambiente Conda.
2. Creación del Jupyter Book principal: pf3311-cienciadatosgeoespaciales.github.io
3. Creación de un Jupyter Book para cada curso, por ejemplo: 2021-iii, accesible en https://pf3311-cienciadatosgeoespaciales.github.io/2021-iii/
4. Publicación de modificaciones.

### 1. Creación de un ambiente Conda

```shell
# Actualización de Conda
$ conda update conda

# Borrado del ambiente (si es que existe)
$ # conda remove -n pf3311 --all

# Creación del ambiente
$ conda create -n pf3311

# Activación del ambiente
$ conda activate pf3311

# Configuración del ambiente
$ conda config --env --add channels conda-forge
$ conda config --env --set channel_priority strict

# Instalación de módulos requeridos (Python 3.9 es la versión más avanzada que funcionó)
$ conda install git python=3 jupyter numpy pandas matplotlib plotly dash gdal fiona shapely geopandas rasterio folium

# Instalación de módulos opcionales
# Si se desea usar QGIS en conda:
$ conda install qgis
# Si se desea desarrollar con streamlit:
$ conda install streamlit
# Si se desea desarrollar con jupyter-book:
$ conda install jupyter-book ghp-import

# Desactivación del ambiente
$ conda deactivate
```

### 2. Creación del Jupyter Book principal y publicación inicial del sitio web en GitHub Pages

```shell
$ conda activate pf3311

# Creación del Jupyter Book con una plantilla inicial
$ jupyter-book create pf3311-cienciadatosgeoespaciales.github.io

# Generación de archivos HTML (en el subdirectorio _build/html)
$ jupyter-book build pf3311-cienciadatosgeoespaciales.github.io

# En este punto, se crea en GitHub el repositorio pf3311-cienciadatosgeoespaciales.github.io

# Configuración del repositorio local y su branch main (para manejar los archivos fuente)
$ cd pf3311-cienciadatosgeoespaciales.github.io
$ git init
$ git add .
$ git commit -m "Commit inicial"
$ git branch -M main
$ git remote add origin https://github.com/pf3311-cienciadatosgeoespaciales/pf3311-cienciadatosgeoespaciales.github.io.git
$ git push -u origin main

# Creación del branch gh-pages (para manejar los archivos HTML publicados)
$ ghp-import -n -p -f _build/html

# En este punto, se configura el repositorio para buscar los archivos de GH Pages en la rama gh-pages
# El sitio debe estar disponible en https://pf3311-cienciadatosgeoespaciales.github.io/

$ conda deactivate
```

### 3. Creación de un Jupyter Book para cada curso y publicación inicial del sitio web en GitHub Pages

```shell
$ conda activate pf3311

# Creación del Jupyter Book con una plantilla inicial
$ jupyter-book create 2021-iii

# Generación de archivos HTML (en el subdirectorio _build/html)
$ jupyter-book build 2021-iii

# En este punto, se crea en GitHub el repositorio 2021-iii

# Configuración del repositorio local y su branch main (para manejar los archivos fuente)
$ cd 2021-iii
$ git init
$ git add .
$ git commit -m "Commit inicial"
$ git branch -M main
$ git remote add origin https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii.git
$ git push -u origin main

# Creación del branch gh-pages (para manejar los archivos HTML publicados)
$ ghp-import -n -p -f _build/html

# En este punto, se configura el repositorio para buscar los archivos de GH Pages en la rama gh-pages
# El sitio debe estar disponible en https://pf3311-cienciadatosgeoespaciales.github.io/2021-iii/
```

### 4. Publicación de modificaciones

```shell
# Generación de archivos HTML (debe hacerse desde el directorio padre del Jupyter Book)
$ jupyter-book build 2021-iii

$ cd 2021-iii

# Aplicación de cambios en el branch main
$ git status
$ git add .
$ git commit -m "###Comentario###"
$ git push

# Aplicación de cambios en el branch gh-pages
$ ghp-import -n -p -f _build/html
```
