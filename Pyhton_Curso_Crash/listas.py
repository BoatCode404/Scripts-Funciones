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