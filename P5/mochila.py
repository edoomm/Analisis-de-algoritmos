def seleccionarMayor(L):
    idx = 0
    max = L[idx]
    for i in range(len(L)):
        if L[i] > max:
            max = L[i]
            idx = i

    L[idx] = -1
    return idx

def seleccionarMenor(L):
    idx = 0
    min = L[idx]
    for i in range(len(L)):
        if (L[i] != -1 and L[i] < min) or (min == -1 and L[i] != -1):
            min = L[i]
            idx = i

    L[idx] = -1
    return idx

def crearListaBenPeso(B, W):
    BP = []
    for i in range(len(B)):
        BP.append(B[i] / W[i])

    return BP

def mochilaFraccionaria(b, w, P, o):
    n = len(b)
    s = 0
    i = 0
    x = [0 for i in range(len(w))]
    ben = 0
    baux = b.copy()
    waux = w.copy()
    bp = crearListaBenPeso(b, w)

    while s < P and i < n:
        if o == 1:
            k = seleccionarMenor(waux)
        elif o == 2:
            k = seleccionarMayor(baux)
        else:
            k = seleccionarMayor(bp)

        i += 1

        if s + w[k] <= P:
            x[k] = 1
            s += w[k]
        else:
            x[k] = (P-s) / w[k]
            s = P

        ben += x[k]*b[k]

    return ben, x

def tsts():
    print("Ejemplo de la diapositiva")
    b = [20, 30, 65, 40, 60]
    w = [10, 20, 30, 40, 50]
    p = 100

    print("Beneficio ($):\t", b)
    print("Peso (kg):\t", w)

    print("\n------Seleccion por menor peso")
    ben, frac = mochilaFraccionaria(b, w, p, 1)
    print("Fracciones:", frac)
    print("Beneficio: $" + str(ben))

    print("\n------Seleccion por mayor beneficio")
    ben, frac = mochilaFraccionaria(b, w, p, 2)
    print("Fracciones:", frac)
    print("Beneficio: $" + str(ben))

    print("\n------Seleccion por mayor valor por unidad de peso")
    ben, frac = mochilaFraccionaria(b, w, p, 3)
    print("Fracciones:", frac)
    print("Beneficio: $" + str(ben))
