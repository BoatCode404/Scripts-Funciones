
#? Comience con la lista que usó en el Ejercicio 3-1, pero en lugar de solo imprimir el nombre de cada persona, imprima un mensaje para ellos. El texto de cada mensaje debe ser el mismo, pero cada mensaje debe estar personalizado con el nombre de la persona.


list_friends=['PABLO','FeLiPe      ','    Andres','DAniEL']

#* Concatenamos el codigo con un mensaje 
print(f'!Hola! \n\t{list_friends[0].capitalize()}\n\t{list_friends[1].rstrip()}\n\t{list_friends[2].lstrip()}\n\t{list_friends[3].title()}')

