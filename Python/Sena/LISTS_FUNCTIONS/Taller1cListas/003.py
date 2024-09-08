#Escribe un algoritmo que encuentre los elementos comunes entre dos listas y los muestre. 

lista1=[1,2,3,4,5,6]
lista2=[2,4,6,8,7,3]

numerosComunes=list(set(lista1) & set(lista2))
print(numerosComunes)