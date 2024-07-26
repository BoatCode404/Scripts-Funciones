#Escribe una función que elimine los duplicados de una lista.


def sinDuplicados(lista):
    sinD=list(set(lista))
    return sinD


numeros=[1,2,2,3,2,3,2,1,4,5,1,2,3,2,2,6,7,8,8,9,2,1,3]

nueva=sinDuplicados(numeros)
print(nueva)