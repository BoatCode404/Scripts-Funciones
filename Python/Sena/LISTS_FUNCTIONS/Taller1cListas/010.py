#Escribe un algoritmo que divida una lista en dos partes iguales. Si la lista tiene un número impar de elementos, la primera parte debe tener un elemento más que la segunda. 


numeros=[1,2,3,4,5]

mitad=len(numeros)//2

if len(numeros)%2==1:
    mitad+=1
    primeraMitad=numeros[:mitad]
    segundaMitad=numeros[mitad:]
print(f"{primeraMitad}\n{segundaMitad}")