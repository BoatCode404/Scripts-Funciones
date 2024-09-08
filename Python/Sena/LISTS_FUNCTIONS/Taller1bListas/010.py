#Escribe un algoritmo que filtre los números mayores a un valor dado de una lista

numeros=[numero for numero in range(1,11)]
valor=5
mayores=[mayor for mayor in numeros if mayor > valor]
print(mayores)