# INSTITUTO POLITÉCNICO NACIONAL
# ESCUELA SUPERIOR DE CÓMPUTO
# ANÁLISIS DE ALGORITMOS
# GRUPO: 3CV2
# ALUMNOS:
#   MENDOZA MARTÍNEZ EDUARDO
#   AGUILAR GONZALES DANIEL
#
# PROFESOR: BENJAMÍN LUNA BENOSO
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# PRÁCTICA NÚMERO: 2
# TÍTULO: FUNCIONES RECURSIVAS VS ITERATIVAS
# DESARROLLO: ANALIZAR ALGORITMOS RECURSIVOS E ITERATIVOS CON EL FIN DE OBSERVAR CUAL ES EL MÁS EFICIENTE
# FECHA: 12/02/19

import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas

def encontrarNumeroPerfecto(c):
    n = 1
    i = 0

    while i < c:
        sum = 0
        divisor = 1
        while divisor < n:
            if not n % divisor:
                sum += divisor
            divisor = divisor + 1
        if sum == n:
            print(n, "es un numero perfecto")
            i += 1
        n += 1

i = 1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
while i <= 5:
    tiempoIniciado = time.time()
    encontrarNumeroPerfecto(i)
    tiempoFinal = time.time() - tiempoIniciado
    print(i, " numeros perfectos encontrados en: ", tiempoFinal, "segundos\n--")
    x.insert(0, i)
    y.insert(0, tiempoFinal)
    i += 1

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
fig.suptitle("Grafica de numeros perfectos encontrados")
plt.show()
