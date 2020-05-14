class Nodo:
    def __init__(self, f, c):
        self.l = None
        self.r = None
        self.f = f
        self.c = c

    def aniadirHijos(self, nodo1, nodo2):
        if isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
            if nodo1.f < nodo2.f:
                self.l = nodo1
                self.r = nodo2
            else:
                self.l = nodo2
                self.r = nodo1

    def __str__(self):
        if self.c == None:
            return str(self.f)
        else:
            return "(" + str(self.c) + ", " + str(self.f) + ")"

class Arbol:
    def __init__(self):
        self.rt = None

    def setRoot(self, rt):
        self.rt = rt

    def __str__(self):
        return str(self.rt)
