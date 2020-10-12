import random

def maximo(A):
    max = A[0]
    for a in A:
        if a > max:
            max = a

    print("Maximo elemento en el arreglo:", max)

A=[random.randint(0, 10) for i in range(10)]
print(A)
maximo(A)
