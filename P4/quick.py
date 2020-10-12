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
# PRÁCTICA NÚMERO: 4
# TÍTULO: DIVIDE Y VENCERAS
# DESARROLLO: IMPLEMENTAR FUNCIONES QUE USAN EL PARADIGMA DE RECURSION MULTI-RAMIFICADA DE DIVIDE Y VENCERÁS
# FECHA: 01/04/2020

import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math
from random import randint
from random import randrange

def QuickSort(A, inf, sup):				# DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'QUICKSORT' QUE ORDENA UN ARREGLO DE TAMAÑO DE INF HASTA SUP
	if inf<sup:							# SI EL LÍMITE INFERIOR ES MENOR AL SUPERIOR
		piv=randrange(inf,sup+1)		# SE ASIGNA AL PIVOTE, EL VALOR DE UN RANDOM
		pivf=Partition(A,inf,sup,piv)	# SE ASIGNA A 'NUEVO PIVOTE' EL RETORNO DE LA FUNCIÓN 'PARTITION'
		QuickSort(A,inf, pivf-1)		# AUTOLLAMADO DE LA FUNCIÓN, CON PARÁMETROS DESDE EL LÍMITE INFERIOR HASTA EL PIVOTE-1 (PRIMERA MITAD DEL ARREGLO)
		QuickSort(A,pivf+1,sup)			# "" SEGUNDA MITAD DEL ARREGLO

def Partition(A,inf,sup,piv):			# DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'PARTITION' QUE 'PARTE' EN DOS SUB ARREGLOS
	A[piv], A[sup]=A[sup],A[piv]		# INTERCAMBIO DEL ARREGLO
	aux=inf
	for i in range(inf,sup):
		if A[i]<A[sup]:
			A[i],A[aux]=A[aux], A[i]
			aux+=1
	A[aux], A[sup]=A[sup],A[aux]
	return aux

def crearLista(n): # Crea listas aleatorias de tamaño n
	return [randint(0, n) for i in range(n)]

def crearListaDecreciente(n):
	return [i for i in range(n)][::-1]

def crearListaMismosElementos(n):
	return [0 for i in range(n)]

i = 1
x = [] # Puntos en x de la grafica
y = [] # Puntos en y de la grafica
fc = [] # Funcion que cota

while i <= 997:
	tiempoInicial = time.time()
	# Partition(crearLista(i), 0, i-1, randrange(0,i)) # Inciso1
	# QuickSort(crearLista(i), 0, i-1) # Inciso3
	# QuickSort(crearListaDecreciente(i), 0, i-1) # Inciso5
	QuickSort(crearListaMismosElementos(i), 0, i-1) # ProblemaAnexo
	tiempoFinal = time.time() - tiempoInicial

	# print("Partition con arreglo de tamaño " + str(i) + "\n---Ejecutado en", tiempoFinal, "segundos") # Inciso1
	# print("QuickSort con arreglo de tamaño " + str(i) + "\n---Ejecutado en", tiempoFinal, "segundos") # Inciso3
	# print("QuickSort con arreglo de tamaño " + str(i) + " ordenados decrecientemente\n---Ejecutado en", tiempoFinal, "segundos") # Inciso5
	print("QuickSort con arreglo de tamaño " + str(i) + " y con mismos elementos\n---Ejecutado en", tiempoFinal, "segundos") # ProblemaAnexo

	x.insert(0, i)
	y.insert(0, tiempoFinal)

	# # fc.insert(i,(1/150000)*i) # Inciso1
	# # fc.insert(i,(1/150000)*i*math.log(i,2)) # Inciso3
	# # fc.insert(i,(1/150000)*math.pow(i,2)) # Inciso5
	fc.insert(i,(1/11000000)*math.pow(i,2)) # ProblemaAnexo

	i += 1


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(fc)
ax.grid(True, which='both')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# fig.suptitle("Grafica del algoritmo Partition") # Inciso1
# fig.suptitle("Grafica del algoritmo QuickSort") # Inciso3
# fig.suptitle("Grafica del algoritmo QuickSort con arreglos ordenados decrecientemente") # Inciso5
fig.suptitle("Grafica del algoritmo QuickSort con arreglos con mismos elementos") # ProblemaAnexo

plt.show()
