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
# PRÁCTICA NÚMERO: 3
# TÍTULO: COMPLEJIDADES TEMPORALES POLINOMIALES Y NO POLINOMIALES
# DESARROLLO: IMPLEMENTAR FUNCIONES RECURSIVAS E ITERATIVAS PARA PODER CALCULAR SU COMPLEJIDAD A TRAVES DE GRAFICAS POR ANALISIS A POSTERIORI
# FECHA: 19/02/19

import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math

def fibo1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)

def fibo2(n):
    i = 0
    while i <= n:
        if i == 0:
            res = 0
            aux0 = 0
        elif i == 1:
            res = 1
            aux1 = 1
        else:
            res = aux0 + aux1
            aux = aux0
            aux0 = aux1
            aux1 = aux1 + aux

        i += 1

    return res

i = 0
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
fc = [] # Funcion que cota
while i <= 30:
    tiempoInicial = time.time()
    nf = fibo1(i)
    tiempoFinal = time.time() - tiempoInicial
    print(i, "numero de la sucesion de fibonacci:", nf, "\n---Calculado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    fc.insert(i,(1/20000000)*math.pow(2,i))

    i += 1


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica del algoritmo de FIbonacci recursivo")
plt.show()
