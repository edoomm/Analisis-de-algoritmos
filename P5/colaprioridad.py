import heapq
import arbolbinario as ab

class ColaPrioridad:
    def __init__(self):
        self.listaNodos = []
        self.listaValores = []


    def extraer(self):
        lval = self.listaValores.copy()
        return self.listaNodos.pop(lval.index(heapq.heappop(self.listaValores)))

    def insertar(self, obj):
        if isinstance(obj, ab.Nodo):
            heapq.heappush(self.listaValores, obj.freq)
            self.listaValores.sort()
            self.listaNodos.insert(self.listaValores.index(obj.freq), obj)
        else:
            print("Error al insertar en cola de prioridad: Variable a insertar no es de tipo arbolbinario.Nodo")


    def __str__(self):
        string = "["
        for i in range(len(self.listaValores)):
            if self.listaNodos[i].car != None:
                string += str(self.listaNodos[i])
            else:
                string += "(" + str(self.listaValores[i]) + ")"

            if i != len(self.listaValores) - 1:
                string += ", "

        return string + "]"











































#~Fin
