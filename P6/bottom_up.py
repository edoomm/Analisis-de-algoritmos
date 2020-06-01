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
# PRÁCTICA NÚMERO: 6
# TÍTULO: PROGRAMACIÓN DINÁMICA
# DESARROLLO: IMPLEMENTAR ALGORITMOS MEDIANTE EL METODO DE RESOLUCION PROGRAMACIÓN DINÁMICA
# FECHA: 01/06/2020
#Bottom-Up

import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math

fibo = [0]*5000000
def fibonacci_asc(n): #Funcion que contiene el algoritmo de Fibonacci bottom upompañame
    if n <= 1 :
        return 1
    else:
        fibo[0] = 0
        fibo[1] = 1
        for i in range(2,n+1):
            fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]



i = 1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
fc = [] # Funcion que cota
while i <= 1300:
    tiempoInicial = time.time()
    nf = fibonacci_asc(i)
    tiempoFinal = time.time() - tiempoInicial
    print(i, "Número de la sucesion de fibonacci:", nf, "\n---Calculado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    fc.insert(i,(1/60000)*i)

    i += 1


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica del algoritmo de FIbonacci Bottom-Up")
plt.show()
