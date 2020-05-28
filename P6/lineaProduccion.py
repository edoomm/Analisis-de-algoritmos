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
    print("linea", Ia, "- estacion", n+1)

a = []
a.append([7,9,3,4,8,4])
a.append([8,5,6,4,5,7])
n = len(a[0])

t = []
t.append([2,3,1,3,4])
t.append([2,1,2,2,1])

e = [2,4]
x = [3,7]
