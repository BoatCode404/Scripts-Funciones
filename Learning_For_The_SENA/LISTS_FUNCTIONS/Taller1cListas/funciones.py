
import os
#* Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.
def sumaLista(lista):
    suma=0
    for numero in lista:
        if numero % 2 != 1:
            suma+=numero
    return suma

#* Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.
def prductoImpares(lista):
    producto=1
    for numero in lista:
        if numero%2!=0:
            producto*=numero
    return producto

#*Escribe un algoritmo que encuentre los elementos comunes entre dos listas y los muestre.
def comunesListas(lista1,lista2):
    comunes=list(set(lista1) & set(lista2))
    return comunes

#*Escribe un algoritmo que elimine los primeros N elementos de una lista. 
def eliminarElementos(lista):
    rangoLista=len(lista)
    n=int(input(f"Cuantos elementos vas a eliminar en un rango de 1 a  {rangoLista} : "))
    if n < 1 or n > rangoLista:
        print("Elemento fuera del rango de la lista")
    del lista[:n]
    return lista

#*Escribe un algoritmo que genere una lista donde cada elemento sea el cubo de los números del 1 al 10.
def listaCubos(rango):
    if rango <1:
        raise ValueError (" El rango debe ser un valor entero positivo")
    cubos=[num**3 for num in range(1,rango+1)]
    return cubos

#*Escribe un algoritmo que ordene una lista de palabras por su longitud.
def OrdenPorLongitud(r,o):
    os.system('cls')
    lista=[]
    for i in range(1,r+1):
        p=input(f"Palabra #{i} : ")
        lista.append(p)
    if o !=1:
       listaOrdenada= lista.sort(key=len,reverse=True)
       return listaOrdenada
    else:
        listaOrdenada=sorted(lista,key=len)
        return listaOrdenada

