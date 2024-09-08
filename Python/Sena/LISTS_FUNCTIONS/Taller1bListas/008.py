#Escribe un algoritmo que cuente cuántos números pares e impares hay en una lista.

numeros=[numero for numero in range(1,11)]
pares=[pares for pares in numeros if pares % 2 != 1 ]
impares=[impares for impares in numeros if impares % 2 !=0]

print(f'La cantidad de pares son :  {len(pares)}\nLa cantidad de impares son :  {len(impares)}')
