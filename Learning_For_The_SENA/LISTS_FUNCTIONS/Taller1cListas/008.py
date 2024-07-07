#Escribe un algoritmo que encuentre el segundo mayor número en una lista de números. 

numeros=[1,2,3,4,5,6,7,8,9,10]
mayor=max(numeros)
segundomayor=max([numero for numero in numeros if numero!=mayor])
print(segundomayor)

