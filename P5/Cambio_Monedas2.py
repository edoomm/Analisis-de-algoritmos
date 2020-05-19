
import time # Libereria para obtener el tiempo de ejecucion
import matplotlib.pyplot as plt # Libreria para graficas
import math
from random import randint

def cambio(total,matriz_cambio,matriz_ceros):
    contador=0
    matriz_cambio=matriz_ceros
    for moneda in matriz_cambio:
        while(total/moneda[0]>=1):
            total=total-moneda[0]
            matriz_cambio[contador][1]+=1
        contador+=1
    return matriz_cambio


matriz_cambio=[[10,0],[5,0],[2,0],[1,0],[.5,0]]
contador_inferior=1
contador_superior=10
i=0

while(i<4):
    #matriz_ceros=[[10,0],[5,0],[2,0],[1,0],[.5,0]]
    total=randint(contador_inferior,contador_superior)
    contador_inferior=contador_inferior*10
    contador_superior=contador_superior*10
    i+=1
    print("**TOTAL:",total,"\n","**Tu cambio es:",cambio(total,matriz_cambio,[[10,0],[5,0],[2,0],[1,0],[.5,0]]),"\n")
