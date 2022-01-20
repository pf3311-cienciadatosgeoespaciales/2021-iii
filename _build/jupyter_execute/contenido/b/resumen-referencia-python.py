#!/usr/bin/env python
# coding: utf-8

# # Resumen de referencia de Python

# Este capítulo contiene un resumen de la sintaxis y la semántica base de Python. También puede consultar:
# 
# - [Documentación oficial de Python](https://docs.python.org/)
#     - [Referencia del lenguaje Python](https://docs.python.org/3/reference/i)
#     - [La biblioteca estándar de Python](https://docs.python.org/3/library/index.html#library-index)
#     - [El tutorial de Python](https://docs.python.org/3/tutorial/index.html#tutorial-index)

# ## Comentarios

# Python permite varios tipos de comentarios en el código fuente. Las convenciones generales para su uso se detallan en [PEP 8 -- Style Guide for Python Code - Comments](https://www.python.org/dev/peps/pep-0008/#comments).

# ### De una línea

# Se definen con el símbolo `#` (*hash*). Por ejemplo:

# In[1]:


# Cálculo del índice de masa corporal (IMC)

peso = 73 # peso en kilogramos
estatura = 1.70 # estatura en metros

imc = peso/estatura**2

print("El IMC es {imc:.2f}".format(imc=imc))


# ### De múltiples líneas

# Python no tiene soporte explícito para comentarios de varias líneas. Sin embargo, se pueden implementar de dos formas:

# 1. Con varias líneas iniciadas con `#`:

# In[2]:


# Línea 1
# Línea 2
# Línea 3


# 2. Con bloques de líneas delimitados con `"""` (tres comillas dobles) al inicio y al final:

# In[3]:


"""
Línea 1
Línea 2
Línea 3
"""


# ### docstrings

# Las *docstrings* son una forma de documentar módulos, funciones, clases y métodos de Python. Se agregan debajo del encabezado y están delimitados con `"""` (tres comillas dobles) al inicio y al final.
# 
# Pueden contener una o varias líneas. En este último caso, la primera línea es una descripción corta y es seguida de una línea en blanco, previa a las líneas restantes. Deben iniciar con mayúscula y finalizar con punto.

# *docstring* de una línea:

# In[4]:


def imc(peso, estatura):
    """Cálculo del índice de masa corporal (IMC)."""
    return peso/estatura**2

print(imc.__doc__)


# *docstring* de varias líneas:

# In[5]:


def imc2(peso, estatura):
    """Cálculo del índice de masa corporal (IMC)
    
    El IMC es una razón matemática que asocia el peso y la estatura de un individuo, 
    ideada por el estadístico belga Adolphe Quetelet, 
    por lo que también se conoce como índice de Quetelet. 
    """
    
    return peso/estatura**2

print(imc2.__doc__)


# Varias herramientas pueden generar documentación a partir de *docstrings*. Entre estas, pueden mencionarse [Doxygen](http://www.doxygen.nl/), [pydoc](https://docs.python.org/3/library/pydoc.html) y [Sphinx](https://www.sphinx-doc.org/).
# 
# Las convenciones para el uso de *docstrings* se detallan en [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).

# ## Tipos de datos
# Python puede trabajar con una gran variedad de tipos de datos, entre los que están los siguientes:
# 
# <table>
# 
# <tr><th>Nombre</th><th>Palabra reservada</th><th>Descripción</th></tr>
# 
# <tr><td>Enteros</td><td>int</td><td>Números enteros: 0, 20, -34</td></tr>
# <tr><td>Punto flotante</td><td>float</td><td>Números con punto decimal: 0.1, 35.0, -100.5</td></tr>
# <tr><td>Booleanos</td><td>bool</td><td>Valores lógicos de <strong>True</strong> (verdadero) o <strong>False</strong> (falso)</td></tr>
# <tr><td>Hileras</td><td>str</td><td>Secuencias ordenadas de caracteres: "Python", "Hola mundo"</td></tr>
# <tr><td>Listas</td><td>list</td><td>Secuencias ordenadas de objetos: [1, 2, 3, "cuatro", True, [5, 6, 7]]</td></tr>
# <tr><td>Tuplas</td><td>tuple</td><td>Secuencias ordenadas inmutables de objetos: ("tres", [23, 34], -89, False)</td></tr>
# <tr><td>Conjuntos</td><td>set</td><td>Colecciones no ordenadas de objetos: {1, 2, "a", "b"}</td></tr>
# <tr><td>Diccionarios</td><td>dict</td><td>Pares ordenados atributo:valor: {"nombre":"Juan", "apellido":"Pérez"}</td></tr>
# 
# </table>
# 
# Existen otros tipos de datos más especializados (ej. fechas, horas, enumerados) que pueden consultarse en la [documentación oficial de Python sobre tipos de datos](https://docs.python.org/3/library/datatypes.html).

# ### La función type()
# La función [type()](https://docs.python.org/3/library/functions.html#type) retorna el tipo del objeto que recibe como argumento.

# In[6]:


type(25)


# In[7]:


type("Costa Rica")


# In[8]:


type([1, 2, 3])


# In[9]:


type(2 > 5)


# ## Variables
# Una variable es un nombre que se asigna a un espacio en la memoria del computador que contiene un valor. El valor se asigna mediante el operador **=**

# In[10]:


# A la variable x se le asigna el valor 10
x = 10
print(x)
print(type(x))


# In[11]:


# A la variable nombre se le asigna el valor "Patricia"
nombre = "Patricia"
print(nombre)
print(type(nombre))


# In[12]:


# A la variable lista_primos se le asigna una lista de números primos
lista_primos = [2, 3, 5, 7, 11, 13, 17]
print(lista_primos)
print(type(lista_primos))


# In[13]:


# Una variable puede cambiar de valor durante la ejecución del programa
i = 1
print(i)
i = i + 1
print(i)


# In[14]:


# El valor de una variable pueden asignarse con base en los de otras variable
x = 20
y = 10
z = x + y
print(z)


# ### Reglas para los nombres de variables
# - No pueden empezar con un número (sí pueden usarse números en el resto del nombre).
# - No pueden contener espacios (se sugiere usar el guión bajo: _).
# - No pueden contener ninguno de los siguientes símbolos: '",<>:/?|\!@#%^&*~-+
# - No deben utilizarse [palabras reservadas de Python](https://docs.python.org/3/reference/lexical_analysis.html#keywords).
# - Se considera una [buena práctica utilizar nombres en minúscula y con guiones bajos](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names), para así mejorar la legibilidad.
# - Es importante utilizar nombres significativos para las variables, que reflejen su propósito.

# Las variables mejoran la legibilidad de los procesos:

# In[15]:


# Cálculo del impuesto de ventas, sin variables
100000 * 0.13


# In[16]:


# Cálculo del impuesto de ventas, con variables

# Entrada
precio_articulo = 100000
tasa_impuesto = 0.13

# Proceso
monto_impuesto = precio_articulo * tasa_impuesto

# Salida
print(monto_impuesto)


# ## Ejercicios

# ### Ejercicio 1
# Utilice variables en un programa que covierta grados Celsius a Fahrenheit. Puede consultar la fórmula en https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html

# In[17]:


# Entrada

# Proceso

# Salida


# ### Ejercicio 2
# Utilice variables en un programa que calcule el índice de masa corporal. Pueden consultar la fórmula en [https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator](https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator)

# In[18]:


# Entrada

# Proceso

# Salida


# ### Ejercicio 3
# Copie en archivos el código fuente de los ejercicios 1 y 2 y ejecútelos desde la línea de comandos de Anaconda.
