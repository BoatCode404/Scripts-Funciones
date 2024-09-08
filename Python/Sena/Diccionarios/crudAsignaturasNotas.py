
import os , time


def borrar():
    os.system('cls')


def saltar():
    input('\nPRESIONE UNA TECLA PARA CONTINUAR')


def animar_texto(t):
    for c in t:
        print(c,end='',flush=True)
        time.sleep(0.01)


def crearDiccionarioNotas():
    dic={'ciencias':[5.0,4.0,3.0]}
    return dic


def agregarMateria(name,dic,nota):
    dic[name]=[nota]


def agregarNota(name,dic,nota):
    if name in dic:
        dic[name].append(nota)


def borrarMateria(name,dic):
    if name in dic:
        del dic[name]


def borrarNota(name,dic,nota):
    if name in dic:
        dic[name].remove(nota)


def editarNota(name,dic,notaVieja,notaNueva):
    if name in dic:
        index=dic[name].index(notaVieja)
        dic[name][index]=notaNueva


def mostrarPromedios(dic):
    promedios={}
    for clave,valor in dic.items():
        promedio=sum(valor)/len(valor)
        promedios[clave]=promedio
    return promedios


def main():
    dicMaterias=crearDiccionarioNotas()
    salir=False
    while salir == False:
        
        borrar()

        menu='''
        1. Agregar nueva Materia
        2. Agregar nota a una Materia existente
        3. Borrar una Materia 
        4. Borrar una nota de una Materia 
        5. Editar una nota de una Materia 
        6. Mostrar diccionario de notas
        7. Mostrar promedios por Materia 
        8. Salir 
        '''

        
        animar_texto(menu)
        r=int(input('\nResponda Aca:'))

        if r == 1:
            borrar()
            nombre=input('Cual es el nombre de la Materia : ')
            nota=float(input('Cual es la nota del estudiante: '))
            agregarMateria(nombre,dicMaterias,nota)
            saltar()
        elif r == 2:
            borrar()
            nombre=input('Cual es el nombre de la Materia : ')
            nota=float(input('Cual es la nota del estudiante: '))
            agregarNota(nombre,dicMaterias,nota)    
            saltar()
        elif r == 3:
            borrar()
            nombre=input('Cual es el nombre de la Materia : ')
            borrarMateria(nombre,dicMaterias)
        elif r == 4:
            borrar()
            nombre=input('Cual es el nombre de la Materia : ')
            nota=float(input('Cual es la nota del estudiante: '))
            borrarNota(nombre,dicMaterias,nota)
            saltar()
        elif r == 5 :
            borrar()
            nombre=input('Cual es el nombre de la Materia : ')
            notaVieja=float(input('Cual es la nota Vieja del estudiante: '))
            notaNueva=float(input('Cual es la nota Nueva del estudiante: '))
            editarNota(nombre,dicMaterias,notaVieja,notaNueva)
            saltar()
        elif r == 6 : 
            borrar()
            print(dicMaterias)
            saltar()
        elif r == 7:
            borrar()
            print(mostrarPromedios(dicMaterias))
            saltar()
        elif r == 8 :
            borrar()
            salir=True
            print('Hasta Pronto')
        elif r > 8 :
            borrar()
            print('Seleccione una opcion valida del menu ')
            saltar()


            
            
            
if __name__== '__main__':

    main()
