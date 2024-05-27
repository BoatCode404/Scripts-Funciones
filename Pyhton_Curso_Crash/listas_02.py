
#* <<<<<<Ejemplo para ordenar normal e inversa OJO PERMANENTE>>>>> 
coches = ['bmw','audi','toyota','subaru']
coches.sort() #! ordenamos Menor a mayor
print(coches)
coches.sort(reverse=True) #! ordenamos Mayor a menor
print(coches) 


#* <<<<<<Ejemplo para ordenar Temporalmente no se modifica el orden original>>>>> 
print(f"Esta es la lista Original {coches}")
print(f"Esta es la lista Ordenada Menor a Mayor :  {sorted(coches)}")#! mostramos su orden en Menor a Mayor sin dañar su original
print(f"Esta es la lista Ordenada Mayor a Menor :  {sorted(coches,reverse=True)}") #! mostramos su orden en Mayor a menor sin dañar su original
print(f"Esta es la lista Original {coches}")


#* <<<<<<Ejemplo para Mostrar lista inversa>>>>> 
coches.reverse()
print(coches)


#* Para encontrar la longitud de una lista
print(len(coches))