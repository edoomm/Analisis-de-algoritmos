"""
        INSTITUTO POLITÉCNICO NACIONAL
        ESCUELA SUPERIOR DE CÓMPUTO

    ANÁLISIS DE ALGORITMOS
    GRUPO: 3CV2
    ALUMNOS:
            - AGUILAR GONZALEZ DANIEL
            - MENDOZA MARTINEZ EDUARDO
    PROFESOR: DR. BENJAMÍN LUNA BENOSO
    PRÁCTICA 5 "DIVIDE Y VENCERAS Y ALGORITMOS VORACES"
"""

import heapq # Nos apoyamos de una libreria ya existente que maneja colas de prioridad de enteros
import arbolbinario as ab

class ColaPrioridad:
    def __init__(self):
        self.listaNodos = []
        self.listaValores = []

    def extraer(self):
        # Se extrae a partir del indice de la lista de frecuencias
        lval = self.listaValores.copy()
        return self.listaNodos.pop(lval.index(heapq.heappop(self.listaValores)))

    def insertar(self, obj):
        if isinstance(obj, ab.Nodo):
            # Insertamos primero a la lista de enteros
            heapq.heappush(self.listaValores, obj.freq)
            self.listaValores.sort()
            # Para después insertar a partir del indice de la última frecuencia ingresada el nodo a ingresar en la lista de nodos
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
