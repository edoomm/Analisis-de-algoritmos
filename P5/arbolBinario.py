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

import sys
sys.setrecursionlimit(1500)

import copy

class Nodo:
    def __init__(self, freq, car):
        self.izq = None
        self.der = None
        self.freq = freq
        self.car = car

    # Inserta hojas dependiendo de que valor de frecuencia sea más grande de cada nodo
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

    def obtenerHojaMasDerecha(self, raiz):
        if raiz.izq == raiz.der == None:
            return raiz
        else:
            return self.obtenerHojaMasDerecha(raiz.der)

    # Función que imprime [raices] con sus hojas de izq -> der
    def imprimir(self, raiz):
        if raiz == None:
            return

        if raiz.izq == None and raiz.der == None:
            print(raiz)
            return

        if raiz.izq != None:
            self.imprimir(raiz.izq)
        if raiz.der != None:
            self.imprimir(raiz.der)

        print("[", raiz, "]")

    # Función para recorrer el arbol con etiquetas
    # 0: Izquierda
    # 1: Derecha
    def recorrer(self, raiz):
        if raiz.izq == None and raiz.der == None: # Es hoja
            c = raiz.car
            raiz.car = "-1" # Se coloca un -1 para "invalidar" dicho nodo
            return ":" + c

        if raiz.izq.car != "-1":
            return "0" + self.recorrer(raiz.izq)
        if raiz.der.car != "-1":
            return "1" + self.recorrer(raiz.der)

        if raiz.izq.car == raiz.der.car == "-1":
            raiz.car = "-1"

        return ""

    def obtenerCodificacion(self):
        # Hacemos una copia de nuestro arbol principal para sobreescribirlo
        rz = copy.deepcopy(self.raiz)
        # Obtenemos la hoja más a la derecha, ya que iremos recorriendo el arbol de izq -> der
        ed = self.obtenerHojaMasDerecha(self.raiz).car

        codificacion = {}
        # Mientras que la hoja más a la derecha no este en nuestras llaves de nuestro diccionario seguirá obteniendo los recorridos hasta encontrarlo
        while ed not in codificacion.keys():
            d = self.recorrer(rz)

            # Si no tiene el caracter ':' significa que todavía no es una clave con su valor, ej: "0:a", "100:c", etc.
            if ':' in d:
                codificacion[d[d.index(':') + 1 :]] = d[: d.index(':')]

        return codificacion

    def __str__(self):
        return "(" + str(self.raiz) + ")"










































#~Fin
