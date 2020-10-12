import random
import time

def selectSort(A):
    j = 0
    while j <= len(A) - 2:
        k = j
        i = j + 1
        while i <= len(A) - 1:
            if A[i] < A[k]:
                k = i
            i += 1
        A[j], A[k] = A[k], A[j]
        j += 1

    print(A)

A =[]
i = 0
while i < 10:
    # A.append(i) # Ordenados -> Mejor caso
    # A.insert(0, i) # Desordenados -> Peor caso
    A.append(random.randint(0,10)) # Random
    i += 1

# print("Mejor caso")
# print("Peor caso")
# print("Random")
tiempoIniciado = time.time()
selectSort(A)
tiempoFinal = time.time() - tiempoIniciado
print("-- Select sort con", i ,"elementos, tiempo:", tiempoFinal, "segundos --\n")
