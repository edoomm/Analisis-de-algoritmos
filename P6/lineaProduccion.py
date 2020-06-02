"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 6 "PROGRAMACIÓN DINÁMICA"

    IMPLEMENTACIÓN DEL ALGORITMO DE LAS LÍNEAS DE PRODUCCIÓN
"""
import random

def generarTablas(n, a, t, e, x):
    f = [[0 for x in range(n)] for i in range(2)]
    I = [[0 for x in range(n-1)] for i in range(2)]

    f[0][0] = e[0] + a[0][0]
    f[1][0] = e[1] + a[1][0]

    for j in range(1, n):
        if f[0][j-1] + a[0][j] <= f[1][j-1] + t[1][j-1] + a[0][j]:
            f[0][j] = f[0][j-1] + a[0][j]
            I[0][j-1] = 1
        else:
            f[0][j] = f[1][j-1] + t[1][j-1] + a[0][j]
            I[0][j-1] = 2
        if f[1][j-1] + a[1][j] <= f[0][j-1] + t[0][j-1] + a[1][j]:
            f[1][j] = f[1][j-1] + a[1][j]
            I[1][j-1] = 2
        else:
            f[1][j] = f[0][j-1] + t[0][j-1] + a[1][j]
            I[1][j-1] = 1

    if f[0][n-1] + x[0] <= f[1][n-1] + x[1]:
        fa = f[0][n-1] + x[0]
        Ia = 1
    else:
        fa = f[1][n-1] + x[1]
        Ia = 2

    return f, fa, I, Ia

def imprimirLineaProduccion(n, I, Ia):
    if (n == -1):
        return
    imprimirLineaProduccion(n-1, I, I[Ia-1][n-1])
    print("Linea", Ia, "- estacion", n+1)

def crearLista(n, a, b):
    return [random.randint(a, b) for i in range(n)]

def crearMatriz(n, m, a, b):
    return [crearLista(m, a, b) for j in range(n)]

def imprimirFigura(a, t, e, x):
    # Imprime la primera linea
    print("\t", end="")
    for i in a[0]:
        print("--------", end="")
    print("-")
    print("\t| ", end="")
    for i in a[0]:
        print("(" + str(i) + ")\t", end="")
    print("|")
    print("\t", end="")
    for i in a[0]:
        print("--------", end="")
    print("-")

    # Imrpime primer inicio
    print("  (" + str(e[0]) + ")\t ", end="")
    # Imprime primeros tiempos de traslado de linea a linea
    for i in t[0]:
            print("  (" + str(i) + ")\t ", end="")
    # Imprime primer final
    print("\t  (" + str(x[0]) + ")")

    # Imprime segundo inicio
    print("  (" + str(e[1]) + ")\t ", end="")
    # Imprime segundos tiempos de traslado de linea a linea
    for i in t[1]:
            print("  (" + str(i) + ")\t ", end="")
    # Imprime segundo final
    print("\t  (" + str(x[1]) + ")")

    # Imprime segunda linea
    print("\t", end="")
    for i in a[1]:
        print("--------", end="")
    print("-")
    print("\t| ", end="")
    for i in a[1]:
        print("(" + str(i) + ")\t", end="")
    print("|")
    print("\t", end="")
    for i in a[1]:
        print("--------", end="")
    print("-\n")

def imprimirTabla(t, inc, car):
    for i in range(len(t[0])+1):
        print("--------", end="")
    print("-")
    print("|  j  |\t", end="")
    for i in range(len(t[0])):
        print(i+inc, "\t", end="")
    print("|")
    for i in range(len(t[0])+1):
        print("--------", end="")
    print("-")
    c = 1
    for e1 in t:
        print("|" + car + str(c) + "[n]|\t", end="")
        for e2 in e1:
            print(e2, "\t", end="")
        print("|")
        for i in range(len(t[0])+1):
            print("--------", end="")
        print("-")
        c += 1

def lineaprod(n, x, y):
    a = crearMatriz(2, n, x, y)
    t = crearMatriz(2, n-1, x, y)
    e = crearLista(2, x, y)
    x = crearLista(2, x, y)

    imprimirFigura(a, t, e, x)

    f, fa, I, Ia = generarTablas(n, a, t, e, x)
    imprimirTabla(f, 1, 'f')
    print("f* =", fa, "\n")
    imprimirTabla(I, 2, 'I')
    print("I* =", Ia, "\n")

    imprimirLineaProduccion(n-1, I, Ia)

def lineaprod2(n, a, t, e, x):
    imprimirFigura(a, t, e, x)

    f, fa, I, Ia = generarTablas(n, a, t, e, x)
    imprimirTabla(f, 1, 'f')
    print("f* =", fa, "\n")
    imprimirTabla(I, 2, 'I')
    print("I* =", Ia, "\n")

    imprimirLineaProduccion(n-1, I, Ia)

a = []
a.append([7,5,4,6])
a.append([5,8,3,9])
n = len(a[0])

t = []
t.append([2,1,2])
t.append([3,2,1])

e = [2,3]
x = [3,4]

f, fa, I, Ia = generarTablas(len(a[0]), a, t, e, x)
lineaprod2(n, a, t, e, x)
