#Escribe un algoritmo que elimine todos los elementos negativos de una lista de números

numeros=[numero for numero in range(-10,0)]
nuevos=[1,2,3,4,5,6,7,8,9,10]
listaUnida=list(numeros+nuevos)

sinNegativos=[numero for numero in listaUnida if not numero<0]
print(sinNegativos)

