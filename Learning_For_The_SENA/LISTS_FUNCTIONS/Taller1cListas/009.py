#Escribe un algoritmo que intercale los elementos de dos listas de igual longitud. 

lista1=[1,2,4,5,6]
lista2=[3,7,8,9,10]

listaIntercalada=['Julian']*(len(lista1)+ len(lista2))
listaIntercalada[0::2]=lista1
listaIntercalada[1::2]=lista2
print(listaIntercalada)


