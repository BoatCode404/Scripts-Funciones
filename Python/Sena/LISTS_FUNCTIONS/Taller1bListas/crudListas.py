import os 

def borrar():
    os.system('cls')

def saltar():
    input('Presione una tecla para continuar')


def mostrarTareas(lista):
    for x in lista:
        print(x)

def agregarTareas(lista):
    nombre=input('Digite el nombre de la tarea: ')
    lista.append(nombre)


def eliminarTarea(lista):
    global mostrarTareas
    print('La lista de Tareas es la siguiente \n\t')
    mostrarTareas(lista)
    nombre=input('Digite el nombre de la tarea que deseas eliminar: ')
    if nombre in lista:
        indice=lista.index(nombre)
        lista.pop(indice)
        print('Tarea eleminada correctamente')
    else:
        print('Tarea no encontrada')


if __name__=='__main__':

    tareas=['jugar','trabajar']

    while True:   
        borrar()

        print( '''
        1: Mostrar Todas las tareas
        2: Agregar Tarea
        3: Eliminar Tarea
        ''')

        r=int(input('Responda aca : '))
        if r == 1 : 
            mostrarTareas(tareas)
            saltar()
        elif r == 2 : 
            agregarTareas(tareas)
            saltar()
        elif r == 3 :
            eliminarTarea(tareas)
            saltar()

