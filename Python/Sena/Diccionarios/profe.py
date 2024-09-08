import sys

def crearDicListas():
    notas = { 
        "Matemáticas": [90, 85, 92], 
        "Ciencias": [88, 79, 85], 
        "Historia": [95, 80, 82], 
        "Literatura": [85, 87, 90] 
    } 
    return notas 

def agregarAsignatura(dic,asignatura,nota):
    dic[asignatura]=[nota]

def agregarNota(dic,asignatura,valor):    
    if dic[asignatura]:
       dic[asignatura].append(valor)
    
def borrarAsignatura(dic,asignatura):
    del dic[asignatura]

def borrarNota(dic,asignatura,valor):
    dic[asignatura].remove(valor)
    
def editarNota(dic,asignatura,valorViejo,valorNuevo):
    i=dic[asignatura].index(valorViejo)
    print(f"la posicion a editar {i}")
    dic[asignatura][i]=valorNuevo

def mostrarPromedios(dic):
    promedios={}
    for clave,valor in dic.items():
        promedio=sum(valor)/len(valor)
        promedios[clave]=promedio
    return promedios



if  __name__== 'main_':
    dic= crearDicListas()
    while True:
        print("\n Opciones:")
        print("1. agregar nueva asignatura")
        print("2. agregar nota a una asignatura existente")
        print("3. borrar una asignatura ")
        print("4. borrar una nota de una asignatura ")
        print("5. editar una nota de una asignatura ")
        print("6. mostrar diccionario de notas ")
        print("7. mostrar promedios por asignatura ")
        print("8. salir ")

        opcion=int(input("Selecciona una opcion: "))

        if opcion==1:
            nom=input("Nombre de la nueva asignatura: ")
            nota=float(input("Nota del estudiante: "))
            agregarAsignatura(dic,nom,nota)
            print(dic)
        elif opcion==2:
            nom=input("Nombre de la asignatura del estudiante: ")
            valor=float(input("Nota del estudiante: "))
            agregarNota(dic,nom,valor)
            print(dic)
        elif opcion==3:
            nom=input("Nombre de la asignatura a borrar: ")
            borrarAsignatura(dic,nom)
            print(dic)
        elif opcion==4:
            nom=input("Nombre de la asignatura del estudiante: ")
            valor=float(input("Nota del estudiante: "))
            borrarNota(dic,nom,valor)
            print(dic)
        elif opcion==5:
            nom=input("Nombre de la asignatura del estudiante: ")
            valorV=float(input("Nota vieja del estudiante: "))
            valorN=float(input("Nota nueva del estudiante: "))
            editarNota(dic,nom,valorV,valorN)
            print(dic)
        elif opcion==6:
            print(dic)
        elif opcion==7:
            print(mostrarPromedios(dic))
        elif opcion==8:
            sys.exit("finalizando programa...")