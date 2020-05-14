"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 5 "DIVIDE Y VENCERAS Y ALGORITMOS VORACES"
"""

import random
import heapq # Librearia para cola de prioridad
import arbolBinario as ab
import copy # Para hacer deepcopy de los nodos

#
#   Crear arbol de la diapositiva con la clase Nodo
#   Todos los elementos de la lista serán nodos -> Almacenar en otra lista sus frecuencias y hacer heapify ahí
#

# Función para generar original.txt (i)
def generarOriginal(tam, num):
    # Generando caracteres de manera aleatoria a partir del número de letras que se quiera con num y de tamaño tam
    text = ''
    for i in range(tam):
        text += chr(97 + random.randint(0, num-1))

    # Escribiendo en el archivo
    with open("original.txt", "w") as file:
        file.write(text)

    print("original.txt creado")

# Función para generar frecuencias.txt a partir de fileN (ii)
def generarFrecuencias(fileN):
    frecuencias = {}
    with open(fileN, "r+") as file:
        og = str(file.read())
        lst = list(set(list(og)))
        lst.sort()
        for c in lst:
            frecuencias[c] = og.count(c)

    with open("frecuencias.txt", "w") as file:
        file.write(str(frecuencias))

    print("frecuencias.txt creado")
    return frecuencias

# Función que crea arbol para la codificacion Huffman
def huffman(freq):
    n = len(freq.keys())
    Q = heapq.heapify(freq.values())
    print(Q)

# Función para generar original_codificado.txt (iii)
def generarCodificado(fileN):
    print(generarFrecuencias(fileN))











































#~Fin
