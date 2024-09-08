import os
import time as t

salida=True
contador=0

IdLibro=[]
tituloLibro=[]
autorLibro=[]
añoLibro=[]
versionLibro=[]
ejemplarLibro=[]

def presionarTecla():
    input("Presiona una Tecla para continuar")
    
def animated_text(tx):
    for c in  tx:
        print(c,end='',flush=True)
        t.sleep(0.02)
    
def menu():
    os.system('clear')
    encabezado='''
        Invenario Biblioteca 
            De Libros
    '''
    print(encabezado.center(40))
    animated_text(''' 
    1. Añadir un nuevo libro.
    2. Buscar un libro por título.
    3. Actualizar los datos de un libro.
    4. Eliminar un libro.
    5. Salir del programa.
    
    ''')

def add_libro():
    global contador
    os.system('clear')
    titulo=input("Cual es el Titulo del libro : ").capitalize()
    autor=input("Caul es el Autor  del libro: ").capitalize()
    año=int(input("Cual es el Año de publicacion del libro : "))
    version=int(input("Cual es la Version del libro: "))
    ejemplar=int(input("Cual es el Ejemplar de este Libro : "))
    
    IdLibro.append(contador)
    tituloLibro.append(titulo)
    autorLibro.append(autor)
    añoLibro.append(año)
    versionLibro.append(version)
    ejemplarLibro.append(ejemplar)
    
    animated_text("\n\nLibro Agregado Correctamente\n")
    presionarTecla()
 
def respuesta_menu(n):
    global salida
    if n==1:
        os.system('clear')
        add_libro() 
    elif n==2:
        os.system('clear')
        r=int(input("Quieres Buscar El libro por:\n1. ID Libro\n2. Titulo Libro\nResponda Aca: "))
        if r==1:
            os.system('clear')
            id=int(input("Cual es el ID del Libro: "))
            buscarId=id in IdLibro
            if buscarId==True:
                os.system('clear')
                index=IdLibro.index(id)
                animated_text("El ID Se Encontro Correctamente\nEstos Son los Datos\n\n")
                print(f'ID: {IdLibro[index]}\nTitulo : {tituloLibro[index]}\nAutor: {autorLibro[index]}\nAño: {añoLibro[index]}\nVersion: {versionLibro[index]}\nEjemplar: {ejemplarLibro[index]}\n\n')
                presionarTecla()
            else:
                os.system('clear')
                animated_text("ERROR NO SE ENCONTRO EL ID DEL LIBRO")
                presionarTecla()
        elif r==2:
            os.system('clear')
            title=input("Cual es el Titulo del Libro : ").capitalize()
            buscarTitle=title in tituloLibro
            if buscarTitle==True:
                os.system('clear')
                index=tituloLibro.index(title)
                animated_text("EL Titulo Se encontro Correctamente\nEstos son los datos\n\n")
                print(f'ID: {IdLibro[index]}\nTitulo : {tituloLibro[index]}\nAutor: {autorLibro[index]}\nAño: {añoLibro[index]}\nVersion: {versionLibro[index]}\nEjemplar: {ejemplarLibro[index]}\n\n')
                presionarTecla()
            else:
                os.system('clear')
                animated_text("ERROR NO SE ENCONTRO EL TITULO DEL LIBRO")
                presionarTecla()
        else:
            os.system('clear')
            animated_text("ERROR OPCION INVALIDA")
            presionarTecla()
    elif n==3:
        os.system('clear')
        r=int(input("Para Actualizar un libro Primero tenemos que buscarlo\n\nQuieres buscarlo por:\n1. ID Libro\n2. Titulo Libro\nResponda Aca: "))
        if r==1:
            id=int(input("Cual es el ID del libro: "))
            buscarId= id in IdLibro
            if buscarId==True:
                
                os.system('clear')
                index=IdLibro.index(id)
                animated_text("EL ID SE ENCONTRO CORRECTAMENTE\n\n")
                
                nuevoTitulo=input("Cual es el nuevo Titulo del Libro: ").capitalize()
                nuevoAutor=input(" Cual es el nuevo Autor de Libro: ").capitalize()
                nuevoAño=int(input("Cual es el nuevo Año del Libro: "))
                nuevaVersion=int(input("Cual es la nueva Version del Libro: "))
                nuevoEjemplar=int(input("Cual es el nuevo ejemplar del libro:  "))
                
                tituloLibro[index]=nuevoTitulo
                autorLibro[index]=nuevoAutor
                añoLibro[index]=nuevoAño
                versionLibro[index]=nuevaVersion
                ejemplarLibro[index]=nuevoEjemplar 
                
                animated_text("\n\nLIBRO ACTUALIZADO CORRECTAMENTE\n")
                presionarTecla()
            else:
                os.system('clear')
                animated_text("ERROR NO SE ENCONTRO EL ID DEL LIBRO\n")
                presionarTecla()
        elif r==2 :
            title=input("Cual es el Titulo del Libro : ").capitalize()
            buscarTitle=title in tituloLibro
            if buscarTitle==True:
                os.system('clear')
                index=tituloLibro.index(title)
                animated_text("ID Encontrado Correctamente\n\n")
                
                nuevoTitulo=input("Cual es el nuevo Titulo del Libro: ").capitalize()
                nuevoAutor=input(" Cual es el nuevo Autor de Libro: ").capitalize()
                nuevoAño=int(input("Cual es el nuevo Año del Libro: "))
                nuevaVersion=int(input("Cual es la nueva Version del Libro: "))
                nuevoEjemplar=int(input("Cual es el nuevo ejemplar del libro:  "))
                
                tituloLibro[index]=nuevoTitulo
                autorLibro[index]=nuevoAutor
                añoLibro[index]=nuevoAño
                versionLibro[index]=nuevaVersion
                ejemplarLibro[index]=nuevoEjemplar
                
                animated_text("\n\nLIBRO ACTUALIZADO CORRECTAMENTE\n")
                presionarTecla()
            else:
                os.system('clear')
                animated_text("ERROR NO SE ENCONTRO EL TITULO DEL LIBRO\n")
                presionarTecla()
        else:
            os.system('clear')
            animated_text("ERROR OPCION INVALIDA\n")
            presionarTecla()
    elif n==4:
        os.system('clear')
        r=int(input("Para eliminar un libro Primero tenemos que buscarlo\n\nQuieres buscarlo por:\n1. ID Libro\n2. Titulo Libro\nResponda Aca: "))
        if r==1:
            os.system('clear')
            id=int(input("Cual es el ID del libro: "))
            buscarId= id in IdLibro
            if buscarId==True:
                os.system('clear')
                index=IdLibro.index(id)
                animated_text("ID ENCONTRADO CORRECTAMENTE\n¿Seguro que quiere Eliminar este Libro? SI / NO ")
                eleccion=input("Responde Aca: ").lower()
                if eleccion!='no':
                    os.system('clear')
                    IdLibro.pop[index]
                    tituloLibro.pop[index]
                    autorLibro.pop[index]
                    añoLibro.pop[index]
                    versionLibro.pop[index]
                    ejemplarLibro.pop[index]
                    
                    animated_text("Libro Eliminado Correctamente\n")
                    presionarTecla()
                else:
                    os.system('clear')
                    animated_text("NO SE ELIMINO EL LIBRO\n")
                    presionarTecla()
            else:
                os.system('clear')
                animated_text("ERROR NO SE ENCONTRO EL ID DEL LIBRO\n")
                presionarTecla()
        elif r==2:
            os.system('clear')
            title=input("Cual es el Titulo del Libro : ").capitalize()
            buscarTitle=title in tituloLibro
            if buscarTitle==True:
                os.system('clear')
                index=tituloLibro.index(title)
                animated_text("Titulo Encontrado Correctamente\n¿Seguro que quiere Eliminar este Libro? SI / NO")
                eleccion=input("Responde Aca: ").lower()
                if eleccion!='no':
                    os.system('clear')
                    IdLibro.pop[index]
                    tituloLibro.pop[index]
                    autorLibro.pop[index]
                    añoLibro.pop[index]
                    versionLibro.pop[index]
                    ejemplarLibro.pop[index]
                    
                    animated_text("Libro Eliminado Correctamente\n")
                    presionarTecla()
                else:
                    os.system('clear')
                    animated_text("NO SE ELIMINO EL LIBRO\n")
                    presionarTecla()
            else:
                os.system('clear')
                animated_text("ERROR NO SE ENCONTRO EL TITULO DEL LIBRO\n")
                presionarTecla()
        else:
            os.system('clear')
            animated_text("ERROR OPCION INVALIDA\n")
            presionarTecla()
    else:
        os.system('clear')
        animated_text("Hasta Pronto\n")
        salida=False
 
            
while salida==True:
    contador+=1
    menu()
    respuesta=int(input("\nResponda Aca: "))
    respuesta_menu(respuesta)