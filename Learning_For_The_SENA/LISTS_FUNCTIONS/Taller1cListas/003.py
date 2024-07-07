#Escribe un algoritmo que encuentre los elementos comunes entre dos listas y los muestre.
import funciones

lista1=[4,8,3]
lista2=[3,9,8]

comunes=list(set(lista1) & set(lista2))
print(comunes)

comunes2=[numero for numero in lista1 if numero in lista2]
print(comunes2)


