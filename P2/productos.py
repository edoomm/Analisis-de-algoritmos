# INSTITUTO POLITÉCNICO NACIONAL
# ESCUELA SUPERIOR DE CÓMPUTO
# ANÁLISIS DE ALGORITMOS
# GRUPO: 3CV2
# ALUMNOS:
#   MENDOZA MARTÍNEZ EDUARDO
#   AGUILAR GONZALES DANIEL
#
# PROFESOR: BENJAMÍN LUNA BENOSO
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# PRÁCTICA NÚMERO: 2
# TÍTULO: FUNCIONES RECURSIVAS VS ITERATIVAS
# DESARROLLO: ANALIZAR ALGORITMOS RECURSIVOS E ITERATIVOS CON EL FIN DE OBSERVAR CUAL ES EL MÁS EFICIENTE
# FECHA: 12/02/19

import random as rand # Libreria para numeros aleatorios
import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math

def prod1(m, n):
    r=0;
    while n>0:
        r=r+m
        n=n-1

    return r

def prod2(m, n):
    r = 0
    while n>0:
        if (n%2)==1:
            r=r+m
        m=2*m
        n=n/2

    return r

def prod3(a,b):
    if b == 1:
        return a
    else:
        return a+prod3(a,b-1)

i = 2
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
while i <= 900:
    tiempoIniciado = time.time()
    prod3(1, i)
    tiempoFinal = time.time() - tiempoIniciado
    print(i, "* 1, calculado en: ", tiempoFinal, "segundos --")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    i += 10

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica de productos de dos enteros positivos")
plt.show()
