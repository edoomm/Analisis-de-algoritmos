
"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 5 "ALGORITMO DE STRASSEN"
"""

acum=0
acum1=0

import random
import time                     # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math

def CrearMatriz(fc):                    # DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'CREARMATRIZ' EN LA QUE SE INICIALIZA UNA MATRIZ TAMAÑO FC*FC
    A=[]                                # DECLARACIÓN  DEL ARREGLO 'A' DE TAMAÑO NULO
    for i in range(fc):                 # PARA 'I' DESDE 0 HASTA FC-1
        A.append([0]*fc)                # ANEXAR EN LA ÚLTIMA POSICIÓN, UNA COLUMNA NUEVA
    return A                            # SE RETORNA EL ARREGLO 'A' DE TAMAÑO FC*FC

def RellenarMatriz(fc):                 # DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'RELLENARMATRIZ' EN LA QUE SE INTRODUCEN LOS VALORES DE UNA MATRIZ
    A=CrearMatriz(fc)                   # LLAMADO A LA FUNCIÓN 'CREARMATRIZ'
    for i in range(fc):                 # POR CADA FILA
       for j in range(fc):              # POR CADA COLUMNA
            A[i][j]=random.randrange(0,100,1) 	# EN LA FILA I, COLUMNA J, SE ANEXA EL VALOR DE ESA CELDA, MEDIANTE UN RANDOM
    return A                            # SE REGRESA EL ARREGLO 'A' RELLENO

def ProducM(A, B):          # DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN QUE REALIZA LA MULTIPLICACIÓN DE MATRICES DE LA FORMA TRADICIONAL
    global acum1            # SE INDICA AL SISTEMA EL USO DE UNA VARIABLE GLOBAL
    n=len(A)                # A LA VARIABLE 'N' SE LE ASIGNA EL 'LARGO' DEL ARREGLO 'A' (NÚMERO DE FILAS)
    C=CrearMatriz(n)        # SE CREA UNA MATRIZ DE TAMAÑO N*N
    acum1+=5                # (1) SE AGREGAN 5 UNIDADES A LA VARIABLE QUE LLEVA EL TEMPO DEL ALGORITMO,
    for i in range(n):      # (2) 3 POR LOS FORS QUE NO ENTRAN CUANDO NO SE CUMPLE LA CONDICIÓN PERO SÍ SE EJECUTA LA LÍNEA
        acum1+=1
        for k in range(n):
            acum1+=1
            for j in range(n):
                acum1+=1
                C[i][j] += A[i][k] * B[k][j]    # (1) AL ARREGLO 'C' EN LA FILA 'I', COLUMNA 'J', SE SUMA LOS PRODUCTOS DEL CONTENIDO EN 'A' FILA 'I',COLUMNA 'K'
    acum1+=1                                    # (2) Y 'B' FILA 'K', COLUMNA 'J'
    return C                # SE RETORNA EL ARREGLO FINAL

def sumarA(A, B):           # DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'SUMARA' QUE SE ENCARGA DE SUMAR LOS SUBPRODUCTOS DEL ALGORITMO PRINCIPAL
    n=len(A)
    C=CrearMatriz(n)
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def restarDe(A, B):           # DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'RESTARDE' QUE SE ENCARGA DE RESTAR LOS SUBPRODUCTOS DEL ALGORITMO PRINCIPAL
    n=len(A)
    C=CrearMatriz(n)
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

#
#   Chansón no nos pueden dar las gráficas porque se usa ProducM
#
def strassen(A, B):           # (1) DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'STRASSEN' QUE SE ENCARGA DE DIVIDIR LOS ARREGLOS PRINCIPALES EN 4 SUBARREGLOS C/U
                              # (2) RECURSIVAMENTE, HASTA QUE SE ALCANCE EL TAMAÑO 'LOSUFICIENTEMENTEPEQUEÑITO' PARA EJECUTAR EL ÚLTIMO PRODUCTO MEDIANTE EL
                              # (3) ALGORITMO TRADICIONAL
    fc=len(A)
    global acum               # NOTA: SÓLO SE COLOCÓ EL ACUMULADOR EN LAS LÍNEAS ORIGINALES DEL ALGORITMO DE STRASSEN.CUALQUIER MOVIMIENTO PARA ORDENAR, FUE REMOVIDO
    if fc==2:
        acum+=2
        C=ProducM(A,B)
        return C
    else:
        redimen=int(fc/2)
        A11,A12,A21,A22,B11,B12,B21,B22,A_total,B_total=CrearMatriz(redimen), CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen),CrearMatriz(redimen)
        for i in range(0, redimen):
            for j in range(0, redimen):
                A11[i][j], A12[i][j],A21[i][j],A22[i][j]= A[i][j],A[i][j + redimen], A[i + redimen][j], A[i + redimen][j + redimen]
                B11[i][j],B12[i][j],B21[i][j],B22[i][j]= B[i][j],B[i][j + redimen],B[i + redimen][j],B[i + redimen][j + redimen]
        A_total,B_total = sumarA(A11, A22),sumarA(B11, B22)
        p1 = strassen(A_total, B_total)
        A_total = sumarA(A21, A22)
        p2 = strassen(A_total, B11)
        B_total = restarDe(B12, B22)
        p3 = strassen(A11, B_total)
        B_total = restarDe(B21, B11)
        p4 =strassen(A22, B_total)
        A_total = sumarA(A11, A12)
        p5 = strassen(A_total, B22)
        A_total,B_total = restarDe(A21, A11),sumarA(B11, B12)
        p6 = strassen(A_total, B_total)
        A_total,B_total = restarDe(A12, A22),sumarA(B21, B22)
        p7 = strassen(A_total, B_total)
        C12,C21 = sumarA(p3, p5),sumarA(p2, p4)
        A_total = sumarA(p1, p4)
        B_total = sumarA(A_total, p7)
        C11 = restarDe(B_total, p5)
        A_total = sumarA(p1, p3)
        B_total = sumarA(A_total, p6)
        C22,C = restarDe(B_total, p2),CrearMatriz(fc)
        acum+=20
        for i in range(0, redimen):
            for j in range(0, redimen):
                C[i][j],C[i][j + redimen],C[i + redimen][j],C[i + redimen][j + redimen] = C11[i][j],C12[i][j],C21[i][j],C22[i][j]
        acum+=1
        return C


i = 1
x = []  # Puntos en x de la grafica
y = []  # Puntos en y de la grafica
# fc = [] # Funcion que cota

while i <= 20:
    tiempoInicial = time.time()
    ProducM(RellenarMatriz(int(math.pow(2, i))), RellenarMatriz(int(math.pow(2, i)))) # Normal
    # strassen(RellenarMatriz(int(math.pow(2, i))), RellenarMatriz(int(math.pow(2, i)))) # Strassen
    tiempoFinal = time.time() - tiempoInicial
    print("Multiplicacion de matrices de tamaño", math.pow(2, i) , "a través del método normal\n---Calculado en", tiempoFinal, "segundos") # Normal
    # print("Multiplicacion de matrices de tamaño", math.pow(2, i), "a través del algoritmo de Strassen\n---Calculado en", tiempoFinal, "segundos") # Strassen
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    # fc.insert(i,(1/150000)*math.pow(i,3)) # Normal
    # # fc.insert(i,(1/150000)*math.pow(i,2.8074)) # Strassen

    i += 1

fig, ax = plt.subplots()
ax.plot(x, y)
# ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica del algoritmo de multiplicacion normal de matrices") # Normal
# fig.suptitle("Grafica del algoritmo de multiplicacion normal de matrices") # Strassen
plt.show()
