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
import ast # Biblioteca para evaluar strings a dictionaries
import codecs # Biblioteca para leer 'utf-8'

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

    print("original_codificado.txt creado")

    # Regresa la codificacion, para traduccion
    return codificacion

# Función para generar original_compr.txt (iv)
def generarComprimido(fileN):
    paq = ""
    comprimido = u""

    with open(fileN) as file:
        for line in file:
            for i in range(len(line)):
                paq += line[i]
                if ((i + 1) % 8) == 0:
                    comprimido += chr(int(paq, 2))
                    paq = ""

    # Leyendo último paquete de 8 bits y colocando cuantos bits se tomaran de este sobrante
    s = "," + str(len(paq) % 8)
    for p in range(len(paq), 8):
        paq += "0"

    comprimido += chr(int(paq, 2)) + s

    # Escribiendo original_compr.txt
    with codecs.open("original_compr.txt", encoding="utf-8", mode="w") as file:
        file.write(comprimido)

    print("original_compr.txt creado")

# Función para mostrar salida de un texto codificado y comprimido a partir de su codificacion (v)
def generarSalida(fileN, cod):
    comprimido = ""

    with codecs.open(fileN, encoding="utf-8") as file:
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
        if val in cod.values():
            salida += list(cod.keys())[list(cod.values()).index(val)]
            val = ""

    with open("salida.txt", "w") as file:
        file.write(salida)

    print("salida.txt creado")

# Función para verificar si dos archivos son iguales
def archivosIguales(file1, file2):
    txt1 = ""
    txt2 = ""

    with open(file1, "r") as file:
        txt1 = file.read()

    with open(file2, "r") as file:
        txt2 = file.read()

    if txt1 == txt2:
        print("Los archivos son iguales(:")
    else:
        print("Los archivos NO son iguales:(")
