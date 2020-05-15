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
        if self.car == None:
            return str(self.freq)
        else:
            return "(" + str(self.car) + ", " + str(self.freq) + ")"

    def __int__(self):
        return self.freq

class Arbol:
    def __init__(self):
        self.rt = None

    def setRoot(self, rt):
        self.rt = rt

    def __str__(self):
        return str(self.rt)











































#~Fin
