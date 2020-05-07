"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 5 "DIVIDE Y VENCERAS Y ALGORITMOS VORACES"
"""

import random
import time                     # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math
# from maxSubarreglo import * # Importando funciones de Maximo Subarreglo DC
from mochila import * # Importando funciones de la mochila fraccionaria

def crearLista(n, a, b):
    return [random.randint(a, b) for i in range (0, n)]

i = 1
x = []  # Puntos en x de la grafica
y = []  # Puntos en y de la grafica
fc = [] # Funcion que cota

x.insert(0, 0)
y.insert(0, 0)
fc.insert(0, 0)

while i <= 1000:
    tiempoInicial = time.time()
    # maxSubArrayDC(crearLista(i, -100, 100), 0, int((i - 1)/2), i - 1) # Cruzado
    # maxSubArrayDC(crearLista(i, -100, 100), 0, i - 1) # MaxSubarrayDc
    mochilaFraccionaria(crearLista(i, 1, 100), crearLista(i, 1, 100), random.randint(50, 100), 3)
    tiempoFinal = time.time() - tiempoInicial
    # print("Maximo subarreglo cruzado de arreglo de tamaño", i, "\n---Encontrado en", tiempoFinal, "segundos") # Cruzado
    # print("Maximo subarreglo DC de arreglo de tamaño", i, "\n---Encontrado en", tiempoFinal, "segundos") # MaxSubarrayDc
    print("Mochila fraccionaria con arreglos de tamaño", i, "\n---Encontrado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    # # f.insert(i,(1/390000) * i) # Cruzado
    # # f.insert(i,(1/1000000) * i * (math.log(i)/math.log(2))) # MaxSubarrayDc
    fc.insert(i,(1/1150000) * i * (math.log(i)/math.log(2)))

    i += 1

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
# fig.suptitle("Grafica del maximo subarreglo cruzado") # Cruzado
# fig.suptitle("Grafica del maximo subarreglo DC") # MaxSubarrayDc
fig.suptitle("Grafica de la mochila fraccionaria")
plt.show()
