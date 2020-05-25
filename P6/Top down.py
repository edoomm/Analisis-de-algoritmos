
#TOP DOWN

import sys
sys.setrecursionlimit(100000)

import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math

fibo = [0]*5000000
for i in range(0,5000000):
    fibo[i]=-1
fibo[0]=0
fibo[1]=1

def fibonacci_desc(n):
    global fibo
    if fibo[n] !=-1:
        return fibo[n]
    fibo[n]= fibonacci_desc(n-2) + fibonacci_desc(n-1)
    return fibo[n]


i = 1
c = 1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
fc = [] # Funcion que cota

fc.insert(0, 0)

while i <= math.pow(10, 4):
    tiempoInicial = time.time()
    nf = fibonacci_desc(int(i))
    tiempoFinal = time.time() - tiempoInicial
    print(i, "numero de la sucesion de fibonacci\n---Calculado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    fc.insert(i, (1/1000000)*i)

    # c+=1
    i*=4
    # i = math.pow(2, c)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica del algoritmo de FIbonacci TOP DOWN")
plt.show()
