#Crea una lista nueva con los números del 1 al 5, revierte su orden con `reverse()` y muestra el resultado.


numeros=[numero for numero in range(1,6)]

numeros.sort(reverse=True)
print(numeros)