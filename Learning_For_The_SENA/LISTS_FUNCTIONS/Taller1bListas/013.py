#Escribe un algoritmo que filtre y devuelva solo los números pares de una lista. 

numeros=[numero for numero in range(1,101)]

pares=[pares for pares in numeros if pares % 2 !=1]

print(pares)