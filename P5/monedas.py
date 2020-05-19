import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math
from random import randint

def cambio(total,matriz_cambio,matriz_ceros):
    contador=0
    matriz_cambio=matriz_ceros
    for moneda in matriz_cambio:
        while(total/moneda[0]>=1):
            total=total-moneda[0]
            matriz_cambio[contador][1]+=1
        contador+=1
    return matriz_cambio


matriz_cambio=[[10,0],[5,0],[2,0],[1,0],[.5,0]]
contador_inferior=1
contador_superior=10
i=1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
fc = [] # Funcion que cota
while(i<5000):
    matriz_ceros=[[10,0],[5,0],[2,0],[1,0],[.5,0]]
    tiempoInicial = time.time()
    nf = cambio(i,matriz_cambio,matriz_ceros)
    tiempoFinal = time.time() - tiempoInicial
    print("TOTAL:",i," Cambio:",nf,"\n---Calculado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    # fc.insert(i,(1/20000000)*math.pow(2,i))

    i += 10


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica Cambio de monedas ")
plt.show()
