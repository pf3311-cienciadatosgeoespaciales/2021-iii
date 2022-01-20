#!/usr/bin/env python
# coding: utf-8

# # Resumen de referencia de Python

# Este capítulo contiene un resumen de la sintaxis y la semántica base de Python. También puede consultar:
# 
# - [Documentación del lenguaje Python](https://docs.python.org/)
# - [Referencia del lenguaje Python](https://docs.python.org/3/reference/i)

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

# In[1]:


type(25)


# In[2]:


type("Costa Rica")


# In[3]:


type([1, 2, 3])


# In[4]:


type(2 > 5)


# ## Variables
# Una variable es un nombre que se asigna a un espacio en la memoria del computador que contiene un valor. El valor se asigna mediante el operador **=**

# In[5]:


# A la variable x se le asigna el valor 10
x = 10
print(x)
print(type(x))


# In[6]:


# A la variable nombre se le asigna el valor "Patricia"
nombre = "Patricia"
print(nombre)
print(type(nombre))


# In[7]:


# A la variable lista_primos se le asigna una lista de números primos
lista_primos = [2, 3, 5, 7, 11, 13, 17]
print(lista_primos)
print(type(lista_primos))


# In[8]:


# Una variable puede cambiar de valor durante la ejecución del programa
i = 1
print(i)
i = i + 1
print(i)


# In[9]:


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

# In[10]:


# Cálculo del impuesto de ventas, sin variables
100000 * 0.13


# In[11]:


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

# In[12]:


# Entrada

# Proceso

# Salida


# ### Ejercicio 2
# Utilice variables en un programa que calcule el índice de masa corporal. Pueden consultar la fórmula en [https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator](https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator)

# In[13]:


# Entrada

# Proceso

# Salida


# ### Ejercicio 3
# Copie en archivos el código fuente de los ejercicios 1 y 2 y ejecútelos desde la línea de comandos de Anaconda.
