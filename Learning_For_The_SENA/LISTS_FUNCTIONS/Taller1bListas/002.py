#Escribe un algoritmo que calcule el producto de todos los elementos de una lista de números enteros.

numeros=[i for i in range(1,11)]

producto=1

for numero in numeros:
    producto*=numero

print(producto)

