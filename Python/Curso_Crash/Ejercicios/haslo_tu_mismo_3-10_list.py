
#* piensa  en  algo  que  podrías  almacenar  en  una  lista.  Por  ejemplo,  podría   hacer  una  lista  de  montañas,  ríos,  países,  ciudades,  idiomas  o  cualquier  otra  cosa  que  desee. Escriba  un  programa  que  cree  una  lista que  contenga  estos  elementos  y  luego  use  cada   función  presentada  en  este  capítulo  al  menos  una  vez.

ciudades=['Medellin','Broklyn','Barrio Chino','Cali','Uraba','Bogota']

#* Mostramos la longitud de la lusta LEN()
print(f'Cantidads ciudades: {len(ciudades)}')

#* Mostrar lista ordenada Menor/Mayor sin dañar orden
print(f'Mostrar lista ordenada Menor/Mayor sin dañar orden\n\t{sorted(ciudades)}')
print(f'Lista Original\n\t{ciudades}\n')

#* Mostrar lista ordenada Mayor/Menor sin dañar orden
print(f'Mostrar lista ordenada Mayor/Menor sin dañar orden\n\t{sorted(ciudades,reverse=True)}')
print(f'Lista Original\n\t{ciudades}\n')

ciudades.reverse() # invertimos la lista
ciudades.reverse() # volvemos a su estado original
ciudades.sort() # ordenamos permanente de menor/mayor
ciudades.sort(reverse=True) # ordenamos permanente de mayor/menor
ciudades.append('Manhatan') # agregamos una nueva ciudad al final 
ciudades.insert(0,'Villa Vicencio') # agregamos una nueva ciudad al incio puede ser en cualquier index
ciudades.pop(7) # eliminamos con el idice 
ciudades.remove('Cali') # eliminamos con el valor 
print(ciudades) # imprimimos los cambios 

print(f'\nCantidads ciudades: {len(ciudades)}\n')
for ciudades in ciudades:
    print(ciudades) # Podemos recorrerla para presentarla mucho mejor 
