def cambio(total,matriz_cambio,matriz_ceros):
    contador=0
    matriz_cambio=matriz_ceros
    for moneda in matriz_cambio:
        while(total/moneda[0]>=1):
            total=total-moneda[0]
            matriz_cambio[contador][1]+=1
        contador+=1
    return matriz_cambio

def obtenerMatriz():
    return [[10,0],[5,0],[2,0],[1,0],[.5,0]]
