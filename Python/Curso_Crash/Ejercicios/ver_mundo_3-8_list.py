import os as clear
clear.system('cls')
#? piensa en al menos cinco lugares del mundo que te gustaría visitar.
#// • Almacenar las ubicaciones en una lista. Asegúrese de que la lista no esté en orden alfabético
#// • Imprima su lista en su orden original. No se preocupe por imprimir la lista ordenadamente, simplemente imprímala como una lista de Python sin formato.
#// • Use sorted() para imprimir su lista en orden alfabético sin modificar el orden de la lista
#// • Muestre que su lista todavía está en su orden original imprimiéndola.
#// • Use sorted() para imprimir su lista en orden alfabético inverso sin cambiar el orden de la lista riginal.
#// • Muestre que su lista todavía está en su orden original imprimiéndola de nuevo.
#// • Utilice reverse() para cambiar el orden de su lista. Imprima la lista para mostrar que su orden ha cambiado.
#// • Use reverse() para cambiar el orden de su lista nuevamente. Imprima la lista para mostrar que ha vuelto a su orden original.
#// • Use sort() para cambiar su lista para que se almacene en orden alfabético. Imprima la lista para mostrar que su orden ha sido cambiado.
#// • Use sort() para cambiar su lista para que se almacene en orden alfabético inverso. Imprima la lista para mostrar que su orden ha cambiado.


#! <<<<<<< Creamos lista y la mostramos >>>>>>>>
lugares=['paris','san andres','usa','nueva zelanda','brazil']
print('Mi lista de lugares para visitar antes de morir:\n')
for i in lugares: # Forma de recorrer  los elementos de una lista 
   print(i)
print(f'{lugares}') # imprimimos la lista original

#! <<<<<<< Mostramos orden de Menor a mayor en lista y comparamos que no se dañara el orden >>>>>>>>
print(f'\nMostrando orden Menor a mayor: {sorted(lugares)}')
print(f'Mostrando orden Original : {lugares}\n')

#! <<<<<<< Mostramos orden de Mayor a Menor en lista y comparamos que no se dañara el orden >>>>>>>>
print(f'Mostrando orden Mayor a menor: {sorted(lugares,reverse=True)}')
print(f'Mostrando orden Original : {lugares}\n')

#! <<<<<<< Mostramos orden inverso en la lista >>>>>>>>
lugares.reverse()
print(f'Mostrando orden inverso : {lugares}')


#! <<<<<<< Mostramos orden inverso en  lista para volver a su orden original y comparamos que no se dañara el orden >>>>>>>>
lugares.reverse()
print(f'Mostrando orden original : {lugares}\n')

#! <<<<<<< ordenamos la lista Permanente de menor a Mayor y la mostramos >>>>>>>>
lugares.sort()
print(f'Lista Ordenada Menor a Mayor de forma Permanente {lugares}')


#! <<<<<<< ordenamos la lista Permanente de mayor a menor y la mostramos >>>>>>>>
lugares.sort(reverse=True)
print(f'Lista Ordenada Mayor a Menor de forma Permanente {lugares}')