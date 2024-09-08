#Escribe un algoritmo que invierta una sublista dentro de una lista más grande.
numeros=[numero for numero in range(1,10+1)]

sublista=numeros[1:4] # indice 1 al 4 

sublista.reverse()

numeros[1:4]=sublista

print(numeros)