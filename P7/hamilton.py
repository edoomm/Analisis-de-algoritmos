"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 7 "VERIFICACION EN TIEMPO POLINOMIAL"
"""

class Grafo:
    def __init__(self, v, e):
        self.vertices = v # Lista normal
        self.aristas = e # Lista de tuplas

    def __str__(self):
        # Formateando string de los vertices del grafo
        strv = "Vertices = {"
        for v in self.vertices:
            if v != self.vertices[len(self.vertices)-1]:
                strv += str(v) + ", "
            else:
                strv += str(v) + "}"
        # Formateando string de las aristas del grafo
        stra = "Aristas = {"
        for a in self.aristas:
            if a != self.aristas[len(self.aristas)-1]:
                stra += str(a) + ", "
            else:
                stra += str(a) + "}"

        return "Grafo con " + str(len(self.vertices)) + " vertices y " + str(len(self.aristas)) + " aristas\n" + strv + "\n" + stra

class Camino:
    def __init__(self, r):
        l = []
        for i in range(len(r)):
            if i == 0:
                t = (r[i], r[i+1])
                l.append(t)
            elif i < len(r)-1:
                t = (r[i], r[i+1])
                l.append(t)

        self.recorrido = l # Lista de tuplas

    def __str__(self):
        strr = ""
        for e in self.recorrido:
            if e != self.recorrido[len(self.recorrido)-1]:
                strr += str(e[0]) + "-"
            else:
                strr += str(e[0]) + "-" + str(e[1])

        return strr

def Verificacion_Hamilton(G, C):
    d = {} # Diccionario para ver si estan todos los vertices del grafo y si estos son recorridos 2 veces
    # d.keys = Vertices
    # d.values = Número de veces que se recorrio el vertice

    # Se recorre el certificado
    for t in C.recorrido:
        # Verifica que el recorrido este en las aristas del grafo
        if t in G.aristas or t[::-1] in G.aristas:
            # Mete los vertices del recorrido a la lista v
            for e in t:
                if e not in d.keys(): # Primera vez que se ingresa al diccionario
                    d[e] = 1
                elif d[e] == 1: # Incrementa en 2 al ser recorrido por segunda vez el vertice
                    d[e] += 1
                else: # Es recorrido más de una vez
                    print("El vertice", e, "es recorrido mas de una vez")
                    return 0
        else:
            print("No existe arista", t)
            return 0

    if len(d.keys()) != len(G.vertices):
        print("No se recorrieron todos los vertices")
        return 0

    for v in d.values():
        if v != 2:
            print("(ERROR) Un vertice no fue recorrido de la manera correcta\n[Posible error en la manera de utilizar crearRecorrido(a)]")
            return 0

    return 1

g = Grafo([1,2,3,4,5], [(1,2),(1,3),(1,5),(2,3),(2,5),(2,4),(3,4),(4,5)])
cert1 = Camino([1,2,3,4,5,1])
cert2 = Camino([1,2,4,3,5,1])
cert3 = Camino([1,3,2,4,3,1])
cert4 = Camino([2,4,3,1,5,2])
cert5 = Camino([5,4,3,2,1,5])
