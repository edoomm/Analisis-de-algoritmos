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

'''
generarFrecuencias("original.txt")
generarCodificacion("frecuencias.txt")
generarCodificado("original.txt", "codificacion.txt")
generarComprimido("original_codificado.txt")
generarSalida("original_compr.txt", "codificacion.txt")
'''

import random
import math
import arbolbinario as ab
import colaprioridad as cp
import ast # Biblioteca para evaluar strings a dictionaries
import codecs # Biblioteca para leer 'utf-8'

# Función para generar original.txt (0)
def generarOriginal(tam, num):
    # Generando caracteres de manera aleatoria a partir del número de letras que se quiera con num y de tamaño tam
    text = ''
    for i in range(tam):
        text += chr((random.randint(0, num-1) % 1000000) + 97)

    # Escribiendo en el archivo
    with codecs.open("original.txt", encoding="utf-8", mode="w") as file:
        file.write(text)
# num % 27

# Función para generar frecuencias.txt a partir de fileN (i)
def generarFrecuencias(fileN):
    frecuencias = {}
    with codecs.open(fileN, encoding="utf-8", mode="r") as file:
        og = str(file.read())
        lst = list(set(list(og)))
        lst.sort()
        for c in lst:
            frecuencias[c] = og.count(c)

    with codecs.open("frecuencias.txt", encoding="utf-8", mode="w") as file:
        file.write(str(frecuencias))

    return frecuencias

# Función que crea arbol para la codificacion Huffman
def huffman(freq):
    n = len(freq.keys())
    # Acomoda la lista por orden de frecuencias
    CP = [ab.Nodo(v, k) for k, v in freq.items()]
    Q = cp.ColaPrioridad()
    for e in CP:
        Q.insertar(e)

    print(Q)

    for i in range(n - 1):
        x = Q.extraer()
        y = Q.extraer()
        z = ab.Nodo(x.freq + y.freq, "")
        z.insertarHojas(x, y)
        Q.insertar(z)
        print(Q)

    return Q.listaNodos[0]

# Función para generar codificacion.txt (ii)
def generarCodificacion(fileN):
    with codecs.open(fileN, encoding="utf-8", mode="r") as file:
        freq = ast.literal_eval(file.read())

    # Obtenemos la codificacion a partir del algoritmo de Huffman
    arbol = ab.Arbol(huffman(freq))
    codificacion = arbol.obtenerCodificacion()

    with codecs.open("codificacion.txt", encoding="utf-8", mode="w") as file:
        file.write(str(codificacion))

    return arbol

# Función para generar original_codificado.txt (iii)
def generarCodificado(fileOg, fileCod):
    # Generamos el codificado a partir de la codificacion
    with codecs.open(fileCod, encoding="utf-8", mode="r") as file:
        codificacion = ast.literal_eval(file.read())

    codificado = ""
    with codecs.open(fileOg) as file:
        for line in file: # No es O(n^2) ya que solo se tiene una sola linea en todos los casos, sin embargo así hay que ponerlo en Python
            for c in line:
                codificado += codificacion[c]

    with codecs.open("original_codificado.txt", encoding="utf-8", mode="w") as file:
        file.write(codificado)

    return codificado

# Función para generar original_compr.txt (iv)
def generarComprimido(fileN):
    paq = ""
    comprimido = u""

    with codecs.open(fileN) as file:
        for line in file:
            for i in range(len(line)):
                paq += line[i]
                if ((i + 1) % 8) == 0:
                    comprimido += chr(int(paq, 2))
                    print(int(paq, 2), end=" ")
                    paq = ""

    # Leyendo último paquete de 8 bits y colocando cuantos bits se tomaran de este sobrante
    s = "," + str(len(paq) % 8)
    for p in range(len(paq), 8):
        paq += "0"

    print(int(paq, 2))

    comprimido += chr(int(paq, 2)) + s

    # Escribiendo original_compr.txt
    with codecs.open("original_compr.txt", encoding="utf-8", mode="w") as file:
        file.write(comprimido)

    return comprimido

# Función para mostrar salida de un texto codificado y comprimido a partir de su codificacion (v)
def generarSalida(fileComp, fileCod):
    with codecs.open(fileCod, encoding="utf-8", mode="r") as file:
        codificacion = ast.literal_eval(file.read())

    comprimido = ""

    with codecs.open(fileComp, encoding="utf-8") as file:
        for line in file:
            comprimido += line

    codificado = ""
    for i in range(0, len(comprimido) - 2):
        if i != len(comprimido) - 3:
            codificado += "{0:08b}".format(ord(comprimido[i]))
        else:
            codificado += "{0:08b}".format(ord(comprimido[i]))[: int(comprimido[len(comprimido) - 1])]

    val = ""
    salida = ""
    for c in codificado:
        val += c
        if val in codificacion.values():
            salida += list(codificacion.keys())[list(codificacion.values()).index(val)]
            val = ""

    with codecs.open("salida.txt", encoding="utf-8", mode="w") as file:
        file.write(salida)

    return salida

# Función para verificar si dos archivos son iguales
def archivosIguales(file1, file2):
    txt1 = ""
    txt2 = ""

    with codecs.open(file1, encoding="utf-8", mode="r") as file:
        txt1 = file.read()

    with codecs.open(file2, encoding="utf-8", mode="r") as file:
        txt2 = file.read()

    if txt1 == txt2:
        print("Los archivos son iguales(:")
    else:
        print("Los archivos NO son iguales:(")

# Función para generar tabla
def generarTablaComp(num):
    print("\nCantidad de bytes usados por", num, "archivos\n")
    print("\toriginal.txt\t|\toriginal_compr.txt")
    print("------------------------------------------------")
    for i in range(num):
        generarOriginal(random.randint(10, 10 + math.pow(3, i)), random.randint(1, i+5))
        generarFrecuencias("original.txt")
        generarCodificacion("frecuencias.txt")
        generarCodificado("original.txt", "codificacion.txt")
        generarComprimido("original_codificado.txt")

        numbog = 0
        with codecs.open("original.txt", encoding="utf-8", mode="r") as file:
            for line in file:
                for c in line:
                    numbog += 1

        numbcomp = 0
        with codecs.open("original_compr.txt", encoding="utf-8", mode="r") as file:
            for line in file:
                for c in line:
                    numbcomp += 1


        if len(str(numbog)) > 5:
            strnbo = str(numbog) + "\t"
        else:
            strnbo = str(numbog) + "\t\t"


        print("\t  " + strnbo + "|\t\t" + str(numbcomp))
