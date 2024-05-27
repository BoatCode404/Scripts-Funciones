import os 
#? Acabas de encontrar una mesa de comedor más grande, por lo que ahora hay más espacio disponible. Piense en tres invitados más para invitar a cenar.

#TODO Comience con su programa del Ejercicio 3-6. Agrega una nueva línea que imprima un mensaje diciendo que solo puedes invitar a dos personas a cenar.

# TODO Utilice pop() para eliminar invitados de su lista de uno en uno hasta que solo queden dos. los nombres permanecen en su lista. Cada vez que seleccione un nombre de su lista, imprima un mensaje para esa persona haciéndole saber que lamenta no poder invitarla a cenar.

# TODO Imprima un mensaje para cada una de las dos personas que todavía están en su lista, haciéndoles saber que todavía están invitados.

# TODO Utilice 'del' para eliminar los dos últimos nombres de su lista, de modo que tenga una lista vacía. Imprima su lista para asegurarse de que realmente tiene una lista vacía al final de su programa.


os.system('cls')

invitados_cena=[
    'PaPa',
    'MaMa',
    'hermano',
    'ABUELA',
    'Santiago'
]

#* Mensaje Para Los invitados de cada lista
print('Invitacion Para la Cena de Fin de año \n')
print(f'Hola {invitados_cena[0].title()}\n\tEres mi ejemplo a seguir\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[1].title()}\n\tEres mi motivacion\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[2].title()}\n\tEres mi compañero\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[3].title()}\n\tTenemos mucho de que hablar TE AMO \n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[4].title()}\n\tEres un idiota lo sabias\n\tTe quiero invitar a Cenar\n')

#  Invitados que no puedes asistir con mensaje 
no_asisten='Santiago'
print(f"\n\n{no_asisten} No puede Asistir a la Cena por que es un idiota")

input()
os.system('cls')


#* Remplazamos a Santiago por Julian
invitados_cena[4]='Julian'

#*  Mensaje Para Los invitados de cada lista (ACTUALIZADO) con julian
print("Bienvenidos Todos a la Cena de Fin de año esta es la lista actualizada \n")
print(f'\n\nHola {invitados_cena[0].title()}\n\tEres mi ejemplo a seguir\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[1].title()}\n\tEres mi motivacion\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[2].title()}\n\tEres mi compañero\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[3].title()}\n\tTenemos mucho de que hablar TE AMO \n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[4].title()}\n\tYa no te enamores ombre \n\tTe quiero invitar a Cenar\n')

input()
os.system('cls')


#* Guardamos nuevos invitados en variables y escribimos un mensaje
invitado1='Pablo'
invitado2='Juanda'
invitado3='Felipe'

os.system
mensaje=f'Hola {invitado1}, {invitado2} & {invitado3}\nBienvenidos a la cena\n\tPor suerte tenemos una mesa mas disponible'
print(mensaje)
input()

#! agregamos los elementos segun lo pide el ejercicio
invitados_cena.insert(0,invitado1)
invitados_cena.insert(2,invitado2)
invitados_cena.append(invitado3)


#*  Mensaje Para Los invitados de cada lista (ACTUALIZADO) con la mesa nueva
os.system('cls')
print("Bienvenidos Todos a la Cena de Fin de año esta es la lista actualizada \n")
print(f'\n\nHola {invitados_cena[1].title()}\n\tEres mi ejemplo a seguir\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[3].title()}\n\tEres mi motivacion\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[4].title()}\n\tEres mi compañero\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[5].title()}\n\tTenemos mucho de que hablar TE AMO \n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[6].title()}\n\tYa no te enamores ombre \n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[0].title()}\n\tUnas Ranked o que?\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[2].title()}\n\tQue se dice el Mompy\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[-1].title()}\n\tFelipasa en la casa \n\tTe quiero invitar a Cenar\n')
input()

#* Eliminamos el invitado de la ultima mesa y escribimos un mensaje
os.system('cls')
invitado_eliminado=invitados_cena.pop(2)
print(f"Lo siento solo podre invitar a dos personas a cenar en la ultima mesa por retrasos de chef\n\n{invitado_eliminado.capitalize()} No puedes asistir a la Cena de fin de año lo lamento ")
input()


#* Personas De la ultima mesa que estan invitados todavia y  con mensaje
os.system('cls')
print(f"Ustedes Amigos {invitados_cena[-1]} & {invitados_cena[0]} de la ultima mesa todavia estan invitados ")
input()



#* Eliminamos por completo a los invitados con del 
print("lista Actualizada elimando con DEL")
del invitados_cena[-1]
del invitados_cena[5]
print(invitados_cena)
input()

#*  Mensaje Para Los invitados de cada lista (ACTUALIZADO) con la mesa nueva
os.system('cls')
print("Bienvenidos Todos a la Cena de Fin de año esta es la lista actualizada \n")
print(f'\n\nHola {invitados_cena[1].title()}\n\tEres mi ejemplo a seguir\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[2].title()}\n\tEres mi motivacion\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[3].title()}\n\tEres mi compañero\n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[4].title()}\n\tTenemos mucho de que hablar TE AMO \n\tTe quiero invitar a Cenar\n')
print(f'Hola {invitados_cena[0].title()}\n\tUnas Ranked o que?\n\tTe quiero invitar a Cenar\n')
input()