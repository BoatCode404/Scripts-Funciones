#Escribe un algoritmo que encuentre el segundo mayor número en una lista de números.

numeros=[numero for numero in range(1,21)]

primerMayor=max(numeros)

segundoMayor=max([numero for numero in numeros if numero!=primerMayor])
print(segundoMayor)

