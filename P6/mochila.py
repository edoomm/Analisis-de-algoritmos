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

def test(j, c, w, b, P, g):
    if j > 0:
        if c < w[j-1]:
            test(j-1, c, w, b, P, g)
        else:
            if g[j-1][c-w[j-1]] + b[j-1] > g[j-1][c]:
                test(j-1, c-w[j-1], w, b, P, g)
                print("Guardar objeto", j)
            else:
                test(j-1, c, w, b, P, g)

b = [38, 40, 24]
w = [9, 6, 5]
P = 15
g = generarTabla(w, b, P)
