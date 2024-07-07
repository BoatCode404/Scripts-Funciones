#Escribe un algoritmo que divida una lista en dos partes iguales. Si la lista tiene un número impar de elementos, la primera parte debe tener un elemento más que la segunda.

lista=[1,2,3,4,5]

mitad=len(lista)//2
if len(lista)%2!=0:
    mitad+=1
primeraMitad=lista[:mitad]
segundaMitad=lista[mitad:]

print(primeraMitad)
print(segundaMitad)