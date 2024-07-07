#escribe un algoritmo que elimine los primeros N elementos de una lista. 
import funciones

lista=['julian',1,2,3,1.5,True,False]
#! Primera Forma

n=int(input(f"Cuantos elementos vas a eliminar en un rango de 1 a  {len(lista)} : "))

print(f"Lista con elementos eliminados : {lista[n:]}")

#! Segunda Forma

'''n=int(input(f"Cuantos elementos vas a eliminar en un rango de 1 a  {len(lista)} : "))

del lista[:n]
print(lista)'''

print(funciones.eliminarElementos(lista))