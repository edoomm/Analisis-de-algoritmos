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

    return Grafo([1,2,3,4,5], [(1,2),(1,3),(1,5),(2,3),(2,5),(2,4),(3,4),(4,5)]), [ Camino([1,2,3,4,5,1]), Camino([1,2,4,3,5,1]), Camino([1,3,2,4,3,1]) ]

x = []  # Puntos en x de la grafica
y = []  # Puntos en y de la grafica
# fc = [] # Funcion que cota

x.insert(0, 0)
y.insert(0, 0)
# fc.insert(0, 0)

for i in range(1, 3+1):
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

# fig, ax = plt.subplots()
# ax.plot(x, y)
# # ax.plot(fc)
# ax.grid(True, which='both')
# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')
# fig.suptitle("Grafica del cambio de monedas")
# plt.show()
