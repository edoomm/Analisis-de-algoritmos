import random as rand # Libreria para numeros aleatorios
import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas

def suma(A, B):
    i = len(A) - 1 # Indice bit menos significativo
    acarreo = 0 # Acarreo que se lleva cuando hay sumas de la forma 1 + 1
    C = [] # Lista C que guarda el resultado de la suma binaria

    # Recorre los numeros de deracha a izquierda
    while i != -1:
        if acarreo == 0:
            if A[i] == 0 and B[i] == 0: # Sumas de la forma 0 + 0 = 0, sin acarreo
                acarreo = 0
                c = 0
            elif A[i] == 1 and B[i] == 1: # Sumas de la forma 1 + 1 = 10, sin acarreo, coloca acarreo
                acarreo = 1
                c = 0
            else: # Sumas de la forma 0 + 1 = 1 o 1 + 0 = 1, sin acarreo
                acarreo = 0
                c = 1
        else: # Existe acarreo, por tanto se realizan sumas de 3 miembros
            if A[i] == 0 and B[i] == 0: # Sumas de la forma 1 + 0 + 0 = 1
                acarreo = 0
                c = 1
            elif A[i] == 1 and B[i] == 1: # Sumas de la forma 1 + 1 + 1 = 11
                acarreo = 1
                c = 1
            else: # Sumas de la forma 1 + 0 + 1 = 10 o 1 + 1 + 0 = 10
                acarreo = 1
                c = 0

        C.insert(0, c) # Inserta el resultado de la suma en C, en la posicion 0
        i -= 1

    if acarreo == 1:
        C.insert(0, acarreo)

    # print(A)
    # print("+")
    # print(B)
    # print(C)

i = 1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
while i != 16:
    A = []
    B = []
    k = 0
    while k < pow(2, i):
        A.append(rand.randint(0, 1))
        B.append(rand.randint(0, 1))
        k += 1

    tiempoIniciado = time.time()
    suma(A, B)
    tiempoFinal = time.time() - tiempoIniciado
    print(i, "-- Suma con dos terminos de", k,"bits, tiempo:", tiempoFinal, "segundos --\n")
    x.insert(0, k)
    y.insert(0, tiempoFinal)

    i += 1

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica de sumas binarias")
plt.show()
