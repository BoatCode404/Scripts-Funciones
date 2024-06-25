
#* Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.
def sumaLista(lista):
    suma=0
    for numero in lista:
        if numero % 2 != 1:
            suma+=numero
    return suma

numeros=[1,2,3,4,5,6,7,8,9,10]

print(f'La suma de los numero es : {sumaLista(numeros)}')