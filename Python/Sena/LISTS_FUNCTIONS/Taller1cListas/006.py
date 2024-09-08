#Escribe un algoritmo que ordene una lista de palabras por su longitud.

palabras=["hola","julian","santiago","herrera","zorro"]

listaOrde=sorted(palabras,key=len)
print(listaOrde)