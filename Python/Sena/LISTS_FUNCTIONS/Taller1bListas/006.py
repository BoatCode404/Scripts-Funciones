#Escribe un algoritmo que intercambie el primer y el último elemento de una lista.

numeros=[numero for numero in range(1,10+1)]

numeros[0],numeros[-1]=numeros[-1],numeros[0]

print(numeros)