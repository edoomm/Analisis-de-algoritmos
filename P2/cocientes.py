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

import random as rand # Libreria para numeros aleatorios
import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas

def div1(n, div, r):
    # n: numerador
    # div: denominador
    # r: residuo
    q = 0 # Cociente
    while n >= div: # Va restando hasta que numerador < denominador
        n = n - div
        q += 1

    r = n
    return q

def div2(n, div, r):
    # n: numerador
    # div: denominador
    # r: residuo
    dd = div # dd se iguala al denominador
    q = 0 # Cociente
    r = n # residuo se iguala al numerador

    while dd <= n:
        dd *= 2 # Incrementa dd por dos hasta que dd sea mayor al numerador
    while dd > div:
        dd /= 2 # Decrementa por dos hasta que dd sea menor al denominador
        q *= 2 # Incrementa por dos el cociente
        if dd <= r: # dd menor o igual al residuo
            r -= dd # decrementa el residuo en dd
            q += 1 # Incrementa cociente en 1

    return q

def div3(n, div):
    # n: numerador
    # div: denominador
    print("a")
    if div > n:
        return 0
    else:
        return 1 + div3(n - div, div)




# i = 1
# x = [] # Puntos en x de la grafica
# y = [] # Puntos en y de la grafica
# while i != 100:
#     tiempoIniciado = time.time()
#     div2(i, 1, 0)
#     tiempoFinal = time.time() - tiempoIniciado
#     print(i, "/ 1, calculado en: ", tiempoFinal, "segundos --")
#     x.insert(0, i)
#     y.insert(0, tiempoFinal)
#     i += 1
#
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.grid(True, which='both')
# ax.axhline(y=0, color='k')
# ax.axvline(x=0, color='k')
# fig.suptitle("Grafica de cociente de dos enteros positivos")
# plt.show()
