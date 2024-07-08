"Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros."

numeros=[numero for numero in range(1,20+1)]

sumaPares=[numero for numero in numeros if numero %2!=1]
print(sumaPares)