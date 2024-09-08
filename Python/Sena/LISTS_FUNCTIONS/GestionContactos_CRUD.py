import os as o
import time as t

salida=True
contdadorId=0

idContacto=[]
nombreContacto=[]
apellidoContacto=[]
emailContacto=[]
telefonoContacto=[]
parentezcoContacto=[]

def menu():
    o.system('cls')
    name='''
            Bienvenido a su lista de contacto 
                    Que desea hacer
        '''
    print(name.center(30))
    animated_text('''
    1. Agregar un nuevo contacto.
    2. Buscar un contacto por nombre.
    3. Actualizar los datos de un contacto existente.
    4. Eliminar un contacto.
    5. Salir del programa
    ''')
    #COMIN SOON ( buscar todos los contactos).

def animated_text(tx):
    for c in tx:
        print(c,end='',flush=True)
        t.sleep(0.02)

def presionar_tecla():
    input("\nPresiona una tecla para continuar")

def add_datos_basico():
    o.system('cls')
    global contdadorId
    n=input("Cual es el nombre del contacto: ").capitalize()
    a=input("Cual es el apellido del contacto: ").capitalize()
    e=input("Cual es el email del contacto: ")
    t=int(input("Cual es el telefono del contacto: "))
    p=input("Cual es el parentezco del contacto: ").capitalize()
    idContacto.append(contdadorId)
    nombreContacto.append(n)
    apellidoContacto.append(a)
    emailContacto.append(e)
    telefonoContacto.append(t)
    parentezcoContacto.append(p)
    animated_text("\n\nContacto Agregado correctamente")
    presionar_tecla()

def eleccion_menu(n):
    global salida
    if n==1:
        add_datos_basico()
    elif n==2:
        o.system('cls')
        r=int(input("Quieres buscar por \n1. ID\n2. Nombre\nReponde Aca: "))
        if r==1:
            o.system('cls')
            id=int(input("Cual es el ID : "))
            buscarId=id in idContacto
            if buscarId==True:
                o.system('cls')
                index=idContacto.index(id)
                animated_text("Se encontraron Estos Datos\n\n")
                print(f"Id= {idContacto[index]}\nNombre= {nombreContacto[index]}\nApellido= {apellidoContacto[index]}\nEmail= {emailContacto[index]}\nTelefono= {telefonoContacto[index]}\nParentezco= {parentezcoContacto[index]}")
                presionar_tecla()
            else:
                o.system('cls')
                animated_text("ERROR NO SE ENCONTRO EL ID DEL CONTACTO")
        elif r==2:
            o.system('cls')
            name=input("Cual es el nombre: ").capitalize()
            buscarNombre=name in nombreContacto
            if buscarNombre==True:
                o.system('cls')
                index=nombreContacto.index(name)
                animated_text("Se encontraron Estos Datos\n\n")
                print(f"Id= {idContacto[index]}\nNombre= {nombreContacto[index]}\nApellido= {apellidoContacto[index]}\nEmail= {emailContacto[index]}\nTelefono= {telefonoContacto[index]}\nParentezco= {parentezcoContacto[index]}")
                presionar_tecla()
            else:
                o.system('cls')
                animated_text("ERROR NO SE ENCONTRO EL NOMBRE DEL CONTACTO")
    elif n==3:
        o.system('cls')
        r=int(input("Quieres buscar por \n1. ID\n2. Nombre\nReponde Aca: "))
        if r==1:
            o.system('cls')
            id=int(input("Cual es el ID : ")) 
            buscarId=id in idContacto
            if buscarId == True:
                o.system('cls')
                animated_text("EL ID ES CORRECTO\n\n")
                index=idContacto.index(id)
                nuevoNombre=input("Cual es el nuevo nombre del contacto : ").capitalize()
                nuevoApellido=input("Cual es el nuevo apellido del contacto: ").capitalize()
                nuevoEmail=input("Cual es el nuevo email del contacto: ")
                nuevoNumero=int(input("Cual es el nuevo numero del contacto: "))
                nuevoParentezco=input("Cual es el nuevo parentezco del contacto: ").capitalize()
                
                nombreContacto[index]=nuevoNombre
                apellidoContacto[index]=nuevoApellido
                emailContacto[index]=nuevoEmail
                telefonoContacto[index]=nuevoNumero
                parentezcoContacto[index]=nuevoParentezco
                
                animated_text("\n\nSe actualizo el contacto correctamente")
                presionar_tecla()
            else:
                o.system('cls')
                animated_text("ERROR NO SE ENCONTRO EL ID DEL CONTACTO")
                presionar_tecla()
        elif r==2:
            o.system('cls')
            name=input("Cual es el nombre: ").capitalize()
            buscarNombre=name in nombreContacto
            if buscarNombre==True:
                index=nombreContacto.index(name)
                o.system('cls')
                animated_text("El Nombre es correcto\n\n")
                nuevoNombre=input("Cual es el nuevo nombre del contacto : ").capitalize()
                nuevoApellido=input("Cual es el nuevo apellido del contacto: ").capitalize()
                nuevoEmail=input("Cual es el nuevo email del contacto: ")
                nuevoNumero=int(input("Cual es el nuevo numero del contacto: "))
                nuevoParentezco=input("Cual es el nuevo parentezco del contacto: ").capitalize()
                
                nombreContacto[index]=nuevoNombre
                apellidoContacto[index]=nuevoApellido
                emailContacto[index]=nuevoEmail
                telefonoContacto[index]=nuevoNumero
                parentezcoContacto[index]=nuevoParentezco

                animated_text("\n\nSe actualizo el contacto correctamente")
                presionar_tecla()
            else:
                o.system('cls')
                animated_text("ERROR NO SE ENCONTRO EL NOMBRE DEL CONTACTO")
                presionar_tecla()
    elif n==4:
        o.system('cls')
        r=int(input("Quieres buscar por \n1. ID\n2. Nombre\nReponde Aca: "))
        if r==1:
            id=int(input("Cual es el ID : ")) 
            buscarId=id in idContacto
            if buscarId == True:
                index=idContacto.index(id)
                o.system('cls')
                animated_text("EL ID ES CORRECTO\n\n")
                eleccion=(input("¿Seguro que quieres borrar este contacto? SI / NO \nResponda Aca: ")).lower()
                if eleccion!='no':
                    o.system('cls')
                    idContacto.pop(index)
                    nombreContacto.pop(index)
                    apellidoContacto.pop(index)
                    emailContacto.pop(index)
                    telefonoContacto.pop(index)
                    parentezcoContacto.pop(index)

                    animated_text("CONTACTO ELIMINADO CORRECTAMENTE")
                    presionar_tecla()
                else:
                    o.system('cls')
                    animated_text("EL CONTACTO NO SE ELIMINO")
                    presionar_tecla()
            else:
                o.system('cls')
                animated_text("ERROR NO SE ENCONTRO EL ID DEL CONTACTO")
                presionar_tecla()
        elif r==2:
            o.system('cls')
            name=input("Cual es el nombre: ").capitalize()
            buscarNombre=name in nombreContacto
            if buscarNombre == True:
                index=nombreContacto.index(name)
                animated_text("EL NOMBRE ES CORRECTO\n\n")
                eleccion=(input("¿Seguro que quieres borrar este contacto? SI / NO \nResponda Aca: ")).lower()
                if eleccion!='no':
                    o.system('cls')
                    idContacto.pop(index)
                    nombreContacto.pop(index)
                    apellidoContacto.pop(index)
                    emailContacto.pop(index)
                    telefonoContacto.pop(index)
                    parentezcoContacto.pop(index)

                    animated_text("CONTACTO ELIMINADO CORRECTAMENTE")
                    presionar_tecla()
                else:
                    o.system('cls')
                    animated_text("EL CONTACTO NO SE ELIMINO")
                    presionar_tecla()
    else:
        animated_text("Hasta Pronto")
        salida=False

while salida==True:
    contdadorId+=1
    menu()
    animated_text("\nRsponda Aca : ")
    r=int(input())
    eleccion_menu(r)