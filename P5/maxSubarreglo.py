import sys
sys.setrecursionlimit(1500)

def maxCrossingSubArray(A, bajo, mitad, alto):
    suma_izq = -sys.maxsize
    max_izq = -sys.maxsize
    suma = 0

    for i in range(mitad, bajo-1, -1):
        suma += A[i]
        if suma > suma_izq:
            suma_izq = suma
            max_izq = i

    suma_der = -sys.maxsize
    max_der = -sys.maxsize
    suma = 0

    for i in range(mitad + 1, alto + 1):
        suma += A[i]
        if suma > suma_der:
            suma_der = suma
            max_der = i

    return max_izq, max_der, suma_izq + suma_der

def maxSubArrayDC(A, bajo, alto):
    if alto == bajo:
        return bajo, alto, A[bajo]
    else:
        mitad = int((bajo + alto) / 2)
        bajo_izq, alto_izq, suma_izq = maxSubArrayDC(A, bajo, mitad)
        bajo_der, alto_der, suma_der = maxSubArrayDC(A, mitad + 1, alto)
        cruz_izq, cruz_der, suma_cruz = maxCrossingSubArray(A, bajo, mitad, alto)
        if suma_izq > suma_der and suma_izq > suma_cruz:
            return bajo_izq, alto_izq, suma_izq
        elif suma_der > suma_izq and suma_der > suma_cruz:
            return bajo_der, alto_der, suma_der
        else:
            return cruz_izq, cruz_der, suma_cruz

def tsts():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print("Encontrando maximo subarreglo de A:\n", A)
    l, d, s = maxSubArrayDC(A, 0, len(A) - 1)
    # print(l,d,s)
    print(A[l:d+1], ", suma =", s)

    B = [1, -4, 3, -4]
    print("Encontrando maximo subarreglo de B:\n", B)
    l, d, s = maxSubArrayDC(B, 0, len(B) - 1)
    # print(l,d,s)
    print(B[l:d+1], ", suma =", s)
