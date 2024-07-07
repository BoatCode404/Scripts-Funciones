# Escribe un algoritmo que ordene una lista de palabras por su longitud.

import funciones

palabras=['hola','julian','eres']

listaOrdenda=sorted(palabras,key=len)
print(listaOrdenda)

palabras.sort(key=len , reverse=True)
print(palabras)

rango=int(input("Cuantas palabras vas a escribir para despues ordenarlas segun su longitud"))
orden=int(input("Como quieres ordenrar la lista\n1.Acendente x Longitud \n2.Decendente x Longitud \nEscriba Aca:"))
print(f"{funciones.OrdenPorLongitud(rango,orden)}")
