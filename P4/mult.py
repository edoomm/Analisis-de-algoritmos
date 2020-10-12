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
# PRÁCTICA NÚMERO: 4
# TÍTULO: DIVIDE Y VENCERAS
# DESARROLLO: IMPLEMENTAR FUNCIONES QUE USAN EL PARADIGMA DE RECURSION MULTI-RAMIFICADA DE DIVIDE Y VENCERÁS
# FECHA: 01/04/2020

import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math
from random import randint

def multiplicacion(a, b):
    p = 1 # Número que indica si se trata de decenas, centenas, etc
    c = 0 # Resultado de la multiplicacion de a*b
    for x in a[::-1]: # Irá recorriendo
        s = 0 # Suma de las multiplicaciones del primer número de b con todo los números de a
        q = 1 # Número que indica si se trata de decenas, centenas, etc
        for y in b[::-1]:
            s += (int(x) * int(y)*q)
            q *= 10
        s *= p
        c += s
        p *= 10
    return c

def karatsuba(a, b):
    if len(a) == 1 or len(b) == 1: #Cuando alguno de los numeros ya tiene longitud de 1 ya
        return int(a)*int(b)
    else:
        m = max(len(a), len(b))
        m2 = m // 2

        a1 = int(a) // 10**(m2)
        b1 = int(a) % 10**(m2)
        c1 = int(b) // 10**(m2)
        d1 = int(b) % 10**(m2)

        z0 = karatsuba(str(b1),str(d1))
        z1 = karatsuba(str((a1+b1)),str((c1+d1)))
        z2 = karatsuba(str(a1),str(c1))

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

i = 1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
fc = [] # Funcion que cota

n = 10 # Factor que ira incrementando el tamaño de los números

while i <= 500:
    tiempoInicial = time.time()
    karatsuba(str(randint(0, n-1)), str(randint(0, n-1)))
    tiempoFinal = time.time() - tiempoInicial
    print("Multiplicacion con números de hasta de tamaño " + str(i) + "\n---Calculado en", tiempoFinal, "segundos")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    fc.insert(i,(1/150000)*math.pow(i,1.58))

    i += 1
    n *= 10


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica del algoritmo de Karatsuba")
plt.show()
