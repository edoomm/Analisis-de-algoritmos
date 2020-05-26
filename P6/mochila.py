import random

def crearLista(n, a, b):
    return [random.randint(a, b) for i in range (n)]

def generarTabla(w, b, P):
    g = [[0 for x in range(P+1)] for y in range(len(w)+1)]

    for j in range(1, len(w)+1):
        for c in range(1, P+1):
            if c < w[j-1]:
                g[j][c] = g[j-1][c]
            else:
                if g[j-1][c] >= g[j-1][c-w[j-1]] + b[j-1]:
                    g[j][c] = g[j-1][c]
                else:
                    g[j][c] = g[j-1][c-w[j-1]] + b[j-1]

    return g

def test(j, c, w, b, P, g, terna):
    if j > 0:
        if c < w[j-1]:
            test(j-1, c, w, b, P, g, terna)
        else:
            if g[j-1][c-w[j-1]] + b[j-1] > g[j-1][c]:
                test(j-1, c-w[j-1], w, b, P, g, terna)
                terna[j-1] = 1
                print("Guardar objeto", j)
            else:
                test(j-1, c, w, b, P, g, terna)

def mochilaEntera(b, w, P):
    print("Beneficios:\t", b)
    print("Pesos:\t\t", w)
    print("Peso mochila:\t", P, "\n")

    terna = [0 for i in range(len(w))]
    test(len(w), P, w, b, P, generarTabla(w, b, P), terna)
    print("Terna:\t\t",terna)

    ben = 0
    peso = 0
    for i in range(len(w)):
        if terna[i] == 1:
            ben += b[i]
            peso += w[i]
    print("\nBeneficios y pesos de los objetos guardados")
    print("Beneficio: \t$", ben)
    print("Peso: \t\t ", peso)


b = [38, 40, 24]
w = [9, 6, 5]
P = 15
g = generarTabla(w, b, P)
