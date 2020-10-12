
def MergeSort(A,p,r):				# (1) DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN MERGESORT QUE RECIBE COMO PARÁMETROS UN ARREGLO DE 'N' ELEMENTOS,
									# (2) EL INICIO DEL ARREGLO Y EL FINAL DE ÉSTE.
    global acum
    if p < r:
    	q = int((p+(r-1))/2)
    	MergeSort(A, p, q)
    	MergeSort(A, q+1, r)
    	Merge(A, p, q, r)

def Merge(A, p, q, r):					# DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN QUE DIVIDE EL ARREGLO ORIGINAL EN DOS SUB ARREGLOS
   	n1 = q - p + 1						# TAMAÑO DEL SUB ARREGLO 1
   	n2 = r- q 							# TAMAÑO DEL SUB ARREGLO 2
   	L = [0] * (n1)						# IMPLEMENTACIÓN DEL SUBARREGLO 'L' CON EL TAMAÑO ANTES DEFINIDO
   	R = [0] * (n2) 						# IMPLEMENTACIÓN DEL SUBARREGLO 'R' CON EL TAMAÑO ANTES DEFINIDO
   	for i in range(0 , n1):				# SE PROCEDE A 'DIVIDIR' EL ARREGLO ORIGINAL EN DOS
   		L[i] = A[p + i]					# LA PRIMERA MITAD ENTERA SE ASIGNA A 'L'
   	for j in range(0 , n2):
   		R[j] = A[q + 1 + j]				# LA SEGUNDA MITAD ENTERA SE ASIGNA A 'R'
   	i = 0     							# SE INICIALIZAN LAS VARIABLES QUE MARCAN EL 'INICIO' DE CADA ARREGLO (CONTANDO AL ORIGINAL)
   	j = 0
   	k = p
   	while i < n1 and j < n2 :
   		if L[i] <= R[j]:				# SI EL ELEMENTO QUE SE ENCUENTRA EN EL SUBARREGLO 1 ES MENOR O IGUAL AL QUE SE ENCUENTRA EN EL SUBARREGLO 2...
   			A[k] = L[i]					# SE INTERCAMBIA EL VALOR DEL ARREGLO ORIGINAL POR ÉSTE
   			i += 1						# SE INCREMENTA UNA POSICIÓN EN EL SUBARREGLO 1
   		else:							# EN CASO CONTRARIO...
   			A[k] = R[j]					# SE INTERCAMBIA EL VALOR DEL ARREGLO ORIGINAL, POR EL VALOR ENCONTRADO EN EL SUBARREGLO 2
   			j += 1							# SE INCREMENTA UNA POSICIÓN EN EL SUBARREGLO 2
   		k += 1							# SE INCREMENTA UNA POSICIÓN EN EL ARREGLO ORIGINAL
   	while i < n1:						# SE ASIGNAN AL ARREGLO ORIGINAL EL RESTO DE LOS VALORES CONTENIDOS EN EL SUBARREGLO 1 (SI QUEDAN AÚN)
   		A[k] = L[i]
   		i += 1
   		k += 1
   	while j < n2:						# SE ASIGNAN AL ARREGLO ORIGINAL EL RESTO DE LOS VALORES CONTENIDOS EN EL SUBARREGLO 2 (SI QUEDAN AÚN)
   		A[k] = R[j]
   		j += 1
   		k += 1


def datos(n):					# DEFINICIÓN E IMPLEMENTACIÓN DE LA FUNCIÓN 'DATOS' EN LA QUE SE PIDEN LOS ELEMENTOS DEL ARREGLO
	A=[0]*n 						# DECLARACIÓN E INICIALIZACIÓN DEL ARREGLO 'A' CON TAMAÑO 'N'
	for i in range(n):
		A[i]=int(input("Ingrese el elemento:"))
	return A 						# SE RETORNA EL ARREGLO 'A'


n=int(input("Número de elementos del arreglo:"))
A=datos(n)
print("El arreglo dado es:")
print(A)						# SE IMPRIME EL CONTENIDO INICIAL DEL ARREGLO
MergeSort(A,0,n-1)				# LLAMADO A LA FUNCIÓN QUE ORDENA DE MENOR A MAYOR EL ARREGLO
print("El arreglo ordenado es:")
for i in range(n):
	print("%d" %A[i]),			# SE IMPRIME EL NUEVO ORDEN DEL ARREGLO
