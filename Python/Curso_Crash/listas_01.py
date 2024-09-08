bicicletas=['   Raptor','B2','cRoSS','BMX']


#* Usamos Metodos En las listas para modificar datos
print(bicicletas[0].lstrip())
print(bicicletas[1].title())
print(bicicletas[2].upper())
print(bicicletas[3].lower())


print('-------------------------')
#* Forma de acceder al ultimo elemento 
print(bicicletas[-1].capitalize()) 
print(bicicletas[-2].lower())
print(bicicletas[-3].upper())
print(bicicletas[-4].strip())


print('-------------------------')
#* Concatenar mensajes con listas f-string
mensaje=f'!hola! mi primera bicicleta fue : {bicicletas[-1].title()}'
print(mensaje.title())


print('-------------------------')
#* Cambimos el valor de un elemento de la lista
bicicletas[0]='Vector Cycla'
print(bicicletas[0])


print('-------------------------')
#* Agregamos un nuevo elemento al final de la lista
bicicletas.append('Raptor')
print(bicicletas)


print('-------------------------')
#* Agregamos un nuevo elemento donde Queramos segun el indice
bicicletas.insert(0,'Xpress')
bicicletas.insert(-1,'GW')
bicicletas.insert(7,'Fina')
print(bicicletas)

print('-------------------------')
#* Eliminar un elemento con su indice Y DEL
del bicicletas[7]
print(bicicletas)

print('-------------------------')
#* Eliminar un elemento con su indice Y trabajar con el con el metodo POP()
bicicleta_dañada=bicicletas.pop()
bicicletas.pop(0) #! eliminados elemento segun el indice
print(bicicletas)
print(f"La bicicleta dañada fue : {bicicleta_dañada.upper()}")

print('-------------------------')
#* Eliminar un elemento con su Valor Remove()
bicicletas.remove('B2') #! Eliminamos el elemnto que dice B2 en la lista
print(bicicletas)

print('-------------------------')
#* Otra Forma de usa El metodo Remove con variables y trabajar con ese dato removido
demasiada_cara='BMX'
bicicletas.remove(demasiada_cara)
print(bicicletas)
print(f'\nLa {demasiada_cara.title()} Es demaciada cara para mi ')

