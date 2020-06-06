"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 7 "VERIFICACION EN TIEMPO POLINOMIAL"
"""

import sys                      # Biblioteca para obtener argumentos de la linea de comandos
import time                     # Biblioteca para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Biblioteca para graficas
from hamilton import *          # Biblioteca del programa hamilton.py

def obtenerInstanciaYCertificado(ejemplo):
    if ejemplo == 1:
        return Grafo([1,2,3], [(1,2),(1,3),(2,3)]), [ Camino([1,2,3,2]), Camino([2,3,1,2]), Camino([3,2,3,3]) ]
    elif ejemplo == 2:
        return Grafo([1,2,3,4], [(1,2),(1,4),(1,3),(2,4),(2,3),(3,4)]), [ Camino([3,2,4,1,3]), Camino([1,2,1,4,1]), Camino([1,4,3,4,1]) ]
    elif ejemplo == 3:
        return Grafo([1,2,3,4,5], [(1,2),(1,4),(1,3),(5,3),(5,2),(5,4),(3,4),(3,2)]), [ Camino([1,2,3,1,4,1]), Camino([3,5,2,1,4,3]), Camino([3,2,1,4,2,3]) ]
    elif ejemplo == 4:
    	return Grafo ([1,2,3,4,5,6], [(4,1),(1,3),(1,2),(2,3),(2,5),(4,3),(4,5),(6,4),(5,3),(5,6)]), [Camino([1,2,3,4,5,6,1]), Camino([1,2,3,5,6,4,1]), Camino([2,3,1,4,5,3,2]) ]
    elif ejemplo == 5:
    	return Grafo ([1,2,3,4,5,6,7],[(1,2),(1,3),(5,1),(2,3),(2,4),(4,3),(4,6),(5,3),(7,5),(3,6),(6,7),(7,3)]), [ Camino([1,2,3,4,6,3,7,1]),Camino([3,2,1,5,7,6,4,3]), Camino([5,1,2,4,3,6,7,5]) ]
    elif ejemplo == 6:
    	return Grafo ([1,2,3,4,5,6,7,8],[(1,2),(1,3),(6,1),(1,7),(3,4),(3,2),(3,5),(5,4),(5,2),(2,7),(2,8),(8,7),(7,6),(4,2)]), [ Camino([6,1,3,5,4,2,8,7,6]),Camino([1,2,3,5,4,2,8,7,1]), Camino([4,5,3,2,8,7,6,1,4]) ]
    elif ejemplo == 7:
    	return Grafo ([1,2,3,4,5,6,7,8,9],[(1,2),(4,1),(1,5),(2,4),(3,2),(3,4),(6,3),(4,6),(4,9),(4,8),(4,7),(4,5),(5,7),(9,6),(7,8),(8,9)]), [ Camino([1,5,7,8,9,6,3,2,4,1]),Camino([4,9,6,3,2,1,4,8,7,4]), Camino([1,5,7,8,9,4,6,3,2,1]) ]
    elif ejemplo == 8:
    	return Grafo ([1,2,3,4,5,6,7,8,9,10],[(2,1),(1,3),(1,7),(8,2),(2,4),(7,3),(3,5),(4,8),(6,4),(5,9),(5,6),(10,6),(7,8),(7,9),(8,10),(9,10),(8,9),(7,10)]), [ Camino([1,7,8,10,9,5,3,6,2,4,1]),Camino([7,3,5,9,10,6,4,8,2,1,7]), Camino([2,4,6,5,3,1,10,8,7,9,2]) ]
    elif ejemplo == 9:
    	return Grafo ([1,2,3,4,5,6,7,8,9,10,11],[(2,1),(1,3),(1,8),(2,3),(5,2),(3,4),(3,7),(3,5),(3,8),(4,7),(8,5),(6,7),(6,8),(6,9),(6,10),(7,10),(8,10),(11,8),(9,10),(10,11)]), [ Camino([4,3,1,2,5,8,7,6,9,10,11,4]),Camino([1,3,4,7,6,9,10,11,8,5,2,1]), Camino([6,7,4,3,1,2,5,8,11,9,10,6]) ]
    elif ejemplo == 10:
    	return Grafo ([1,2,3,4,5,6,7,8,9,10,11,12],[(1,2),(1,7),(3,1),(2,8),(2,4),(3,9),(5,3),(4,10),(4,12),(4,6),(11,5),(5,6),(6,12),(8,7),(7,9),(7,12),(10,8),(8,11),(9,10),(9,11),(12,10),(11,12)]), [ Camino([11,5,3,1,2,4,6,12,10,8,7,9,11]),Camino([1,2,4,6,5,3,1,7,9,11,12,10,1]), Camino([10,8,11,12,7,9,10,4,2,1,3,5,10]) ]
    elif ejemplo == 11:
    	return Grafo ([1,2,3,4,5,6,7,8,9,10,11,12,13], [(1,2),(1,5),(2,3),(2,4),(3,6),(3,4),(4,1),(4,8),(5,10),(6,5),(6,7),(6,10),(7,8),(8,9),(8,11),(9,4),(10,7),(10,11),(10,13),(11,12),(11,13),(12,4),(12,9),(13,12)]), [Camino([1,2,3,6,5,10,7,8,9,12,13,14,8,1]), Camino([1,2,3,6,5,10,7,8,11,13,12,9,4,1]), Camino([4,8,9,12,14,13,10,7,6,3,2,1,5,4]) ]
    elif ejemplo == 12:
    	return Grafo ([1,2,3,4,5,6,7,8,9,10,11,12,13,14], [(1,2),(1,3),(2,4),(3,4),(3,14),(4,5),(3,6),(5,3),(5,6),(6,7),(6,8),(7,8),(7,9),(7,11),(7,12),(8,10),(9,11),(10,9),(11,12),(12,13),(12,14),(13,7),(13,14),(13,3),(14,1),(14,1)]), [Camino([3,4,5,6,7,8,10,9,11,12,13,14,1,2,3]), Camino([1,2,4,5,3,6,7,8,10,9,11,12,13,14,1]), Camino([7,8,10,9,11,12,7,6,5,4,3,2,1,14,7]) ]
    elif ejemplo == 13:
    	return Grafo ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [(1,2),(1,3),(1,7),(1,8),(2,3),(2,4),(3,8),(4,5),(4,9),(5,3),(6,1),(6,7),(7,2),(7,9),(8,6),(8,13),(9,10),(9,14),(14,12),(12,7),(12,11),(11,6),(11,13),(13,15),(15,10),(15,14),(10,5),(10,8)]), [Camino([11,13,15,14,12,7,9,10,8,3,5,4,2,1,6,11]), Camino([3,1,2,4,5,10,9,7,6,11,12,14,15,13,8,3]), Camino([2,4,9,14,12,11,13,15,10,5,3,8,6,1,7,2]) ]

    return Grafo([1,2,3,4,5], [(1,2),(1,3),(1,5),(2,3),(2,5),(2,4),(3,4),(4,5)]), [ Camino([1,2,3,4,5,1]), Camino([1,2,4,3,5,1]), Camino([1,3,2,4,3,1]) ]

x = []  # Puntos en x de la grafica
y = []  # Puntos en y de la grafica
# fc = [] # Funcion que cota

x.insert(0, 0)
y.insert(0, 0)
# fc.insert(0, 0)

for i in range(1, 13+1):
    instancia, certificados = obtenerInstanciaYCertificado(i)
    print("")
    print(instancia)

    for certificado in certificados:
        print("Camino:", certificado)
        tiempoInicial = time.time()
        v = Verificacion_Hamilton(instancia, certificado)
        tiempoFinal = time.time() - tiempoInicial
        print("Verificaion Hamiltoniana obtenida:", v, "- Realizado en", tiempoFinal, "segundos")
        if v == 1:
            x.insert(0, len(instancia.vertices))
            y.insert(0, tiempoFinal)
            # fc.insert(i,(1/5000000) * i)

fig, ax = plt.subplots()
ax.plot(x, y)
# ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica del cambio de monedas")
plt.show()
