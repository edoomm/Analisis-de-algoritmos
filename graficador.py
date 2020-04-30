import random
import time                     # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math

i = 1
x = []  # Puntos en x de la grafica
y = []  # Puntos en y de la grafica
fc = [] # Funcion que cota

fc.insert(0, 0)

while i <= 8:
    tiempoInicial = time.time()
    # ProducM(RellenarMatriz(int(math.pow(2, i))), RellenarMatriz(int(math.pow(2, i)))) # Normal
    strassen(RellenarMatriz(int(math.pow(2, i))), RellenarMatriz(int(math.pow(2, i)))) # Strassen
    tiempoFinal = time.time() - tiempoInicial
    # print("Multiplicacion de matrices de tamaño", math.pow(2, i) , "a través del método normal\n---Calculado en", tiempoFinal, "segundos") # Normal
    print("Multiplicacion de matrices de tamaño", math.pow(2, i), "a través del algoritmo de Strassen\n---Calculado en", tiempoFinal, "segundos") # Strassen
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    # fc.insert(i,(1/150000)*math.pow(i,3)) # Normal
    fc.insert(i,(1/20)*math.pow(i,2.8074)) # Strassen

    i += 1

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
# fig.suptitle("Grafica del algoritmo de multiplicacion normal de matrices") # Normal
fig.suptitle("Grafica del algoritmo de Strassen de multiplicacion normal de matrices") # Strassen
plt.show()
