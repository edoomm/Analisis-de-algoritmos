import sys
sys.setrecursionlimit(1500)

import copy

class Nodo:
    def __init__(self, freq, car):
        self.izq = None
        self.der = None
        self.freq = freq
        self.car = car

    def insertarHojas(self, nodo1, nodo2):
        if isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
            if nodo1.freq < nodo2.freq:
                self.izq = nodo1
                self.der = nodo2
            else:
                self.izq = nodo2
                self.der = nodo1
        else:
            print("Error al insertar hojas de nodo: Hojas a insertar no son de tipo Nodo")

    def __str__(self):
        if self.car == "":
            return str(self.freq)
        else:
            return "(" + str(self.car) + ", " + str(self.freq) + ")"

    def __int__(self):
        return self.freq

class Arbol:
    def __init__(self, raiz):
        if isinstance(raiz, Nodo):
            self.raiz = raiz
        else:
            print("Error al crear el arbol: Variable en el constructor no es de tipo arbolbinario.Nodo")
            self.raiz = None

    def recorrer(self, raiz):
        if raiz.car != "":
            c = raiz.car
            raiz.car = "-1"
            return ":" + c

        if raiz.izq.car != "-1":
            return "0" + self.recorrer(raiz.izq)
        else:
            if raiz.der.car != "": # ERROR: Chance aqui hay
                raiz.car = "-1"
            return "1" + self.recorrer(raiz.der)

    def codificar(self, num):
        rz = copy.deepcopy(self.raiz)
        for n in range(num):
            print(self.recorrer(rz))

    def __str__(self):
        return "(" + str(self.raiz) + ")"










































#~Fin
