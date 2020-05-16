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

# Ejemplo diapositiva:
# {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}

import random
import arbolbinario as ab
import colaprioridad as cp
import ast

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

# Función que crea arbol para la codificacion Huffman
def huffman(freq):
    n = len(freq.keys())
    # Acomoda la lista por orden de frecuencias
    CP = [ab.Nodo(v, k) for k, v in freq.items()]
    Q = cp.ColaPrioridad()
    for e in CP:
        Q.insertar(e)

    for i in range(n - 1):
        x = Q.extraer()
        y = Q.extraer()
        z = ab.Nodo(x.freq + y.freq, "")
        z.insertarHojas(x, y)
        Q.insertar(z)

    return Q.listaNodos[0]

# Función para generar original_codificado.txt (iii)
def generarCodificado(fileOg, fileFreq):
    with open(fileFreq, "r") as file:
        freq = ast.literal_eval(file.read())

    # Obtenemos la codificacion a partir del algoritmo de Huffman
    arbol = ab.Arbol(huffman(freq))
    codificacion = arbol.obtenerCodificacion()

    # Generamos el codificado a partir de la codificacion
    codificado = ""
    with open(fileOg) as file:
        for line in file: # No es O(n^2) ya que solo se tiene una sola linea en todos los casos, sin embargo así hay que ponerlo en Python
            for c in line:
                codificado += codificacion[c]

    with open("original_codificado.txt", "w") as file:
        file.write(codificado)

    return codificacion

# Función para generar original_compr.txt (iv)
def generarComprimido(fileN):
    return














































#~Fin
