
# ? acaba de enterarse de que uno de sus invitados no puede asistir a la cena, por lo que debe enviar un nuevo conjunto de invitaciones. Tendrás que pensar en alguien más a quien invitar.

#TODO Comience con su programa del Ejercicio 3-4. Agregue una llamada print() al final de su programa que indique el nombre del invitado que no puede asistir.

#TODO Modifica tu lista, reemplazando el nombre del invitado que no puede asistir con el nombre de la nueva persona que estás invitando.

#TODO Imprima un segundo conjunto de mensajes de invitación, uno para cada persona que todavía está en la lista

invitados_cena=[
    'PaPa',
    'MaMa',
    'hermano',
    'ABUELA',
    'Santiago'
]

#* Mensaje Para Los invitados de cada lista
print('Invitacion Para la Cena de Fin de año \n')
print(f'Hola {invitados_cena[0].title()}\n\tEres mi ejemplo a seguir\n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[1].title()}\n\tEres mi motivacion\n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[2].title()}\n\tEres mi compañero\n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[3].title()}\n\tTenemos mucho de que hablar TE AMO \n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[4].title()}\n\tEres un idiota lo sabias\n\tTe quiero invitar a Cenar')

#* Invitados que no puedes asistir con mensaje 
no_asisten='Santiago'
print(f"\n\n{no_asisten} No puede Asistir a la Cena por que es un idiota")


#* Remplazamos a Santiago por Julian
invitados_cena[4]='Julian'

#*  Mensaje Para Los invitados de cada lista (ACTUALIZADO) con julian
print("Bienvenidos Todos a la Cena de Fin de año esta es la lista actualizada \n")
print(f'\n\nHola {invitados_cena[0].title()}\n\tEres mi ejemplo a seguir\n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[1].title()}\n\tEres mi motivacion\n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[2].title()}\n\tEres mi compañero\n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[3].title()}\n\tTenemos mucho de que hablar TE AMO \n\tTe quiero invitar a Cenar')
print(f'Hola {invitados_cena[4].title()}\n\tYa no te enamores ombre \n\tTe quiero invitar a Cenar')