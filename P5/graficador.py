import random
import time                     # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math
from maxSubarreglo import * # Importando funciones de STRASSEN

def crearLista(n):
    return [random.randint(-100, 100) for i in range (0, n)]

i = 1
x = []  # Puntos en x de la grafica
y = []  # Puntos en y de la grafica
# fc = [] # Funcion que cota

x.insert(0, 0)
y.insert(0, 0)
# fc.insert(0, 0)

while i <= 1000:
    tiempoInicial = time.time()
    # maxSubArrayDC(crearLista(i), 0, int((i - 1)/2), i - 1) # Cruzado
    maxSubArrayDC(crearLista(i), 0, i - 1)
    tiempoFinal = time.time() - tiempoInicial
    # print("Maximo subarreglo cruzado de arreglo de tamaño", i, "\n---Encontrado en", tiempoFinal, "segundos") # Cruzado
    print("Maximo subarreglo DC de arreglo de tamaño", i, "\n---Encontrado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    # # fc.insert(i,(1/390000) * i) # Cruzado
    # fc.insert(i,(1/1000000) * i * (math.log(i)/math.log(2)))

    i += 1

fig, ax = plt.subplots()
ax.plot(x, y)
# ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
# fig.suptitle("Grafica del maximo subarreglo cruzado") # Cruzado
fig.suptitle("Grafica del maximo subarreglo DC")
plt.show()
