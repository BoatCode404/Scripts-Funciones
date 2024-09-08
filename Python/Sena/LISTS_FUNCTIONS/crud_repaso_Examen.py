'''print ("Ingresar")
print ("1 Crear tarea")
print ("2 Buscar tarea")
print ("3 Actualizar tarea")    
print ("4 Eliminar tarea")
print ("5 Mostrar todas las tareas")
print ("6 Ordenar tareas por nombre Mayor/Menor (Permanente)")
print ("7 Ordenar tareas por nombre Menor/Mayor (Permanente)")
print ("8 Invertir tareas por nombre")
print ("9 Volver a estado Original")
prin  ("10 Marcar una tarea completada)
print ("11 Cantidad de productor registrados")
print ("12 Eliminar todos las tareas")    
print ("13 Salir")
'''
'''Añadir una nueva tarea.
2. Buscar una tarea por título.
3. Actualizar los detalles de una tarea.
4. Marcar una tarea como completada.
5. Eliminar una tarea.
6. Mostrar todas las tareas.
7. Salir del programa
'''

import os 
import time as t

# Definir las listas a usar 
titulos=[]
detalles=[]
fechasI=[]
fechaF= []
estados=[]


#Funcion de presionar tecla 
def saltar():
    input("Pulse cualquier tecla para continuar.")

#Funcion que anima el texto
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        t.sleep(0.03)

#Funcion para repetir el menu
def menu():
    animated_text("1. Crear Producto\n2. Buscar Producto\n3. Actualizar producto\n4. Eliminar Producto\n5. Mostrar todos los productos\n6. Ordenar Producto por nombre Mayor/Menor\n7. Invertir Producto por nombre\n8. Marcar una tarea completada\n9. Ordenar de Menor/Mayor por nombre\n10. Productos Registrados\n11. Agregar un nuevo elemento\n12. Eliminar todos los productos ")

#Funcion principal para elegir opciones del menu
def eleccion(n):
    if n==1:
        # Agregar Tarea nueva
        os.system('cls') 
        titulo_tarea=input("Titulo de la tarea: ").title()
        detalle_tarea=input("Descripcion de la tarea: ")
        fecha_inicio=input("Fecha Inicial M/D/A: ")
        fecha_final=input("Fecha Final M/D/A: ")
        estado_tarea=input("Estado de la tarea: ")
        titulos.append(titulo_tarea)
        detalles.append(detalle_tarea)
        fechasI.append(fecha_inicio)
        fechaF.append(fecha_final)
        estados.append(estado_tarea)
        animated_text("\n\tTarea Agregada Correctamente\n")
        saltar()
    elif n==2:
        # Buscar Tarea
        os.system('cls')
        buscar_titulo=input("¿Cual es el titulo de la tarea?: ")
        if buscar_titulo in titulos:
            index=titulos.index(buscar_titulo)
            os.system('cls')
            animated_text(f"Datos Encontrados con Exito\n\tTitulo De Tarea: {titulos[index].title()}\nDetalle De Tarea: {detalles[index].Capitalize()}\nFecha De Creacion: {fechasI[index]}\nFecha de Finalizacion: {fechaF[index]}\nEstado Tarea: {estados[index].title()}\n")
            saltar()
        else:
            os.system('cls')
            animated_text("ERROR : TITULO NO ENCONTRADO\n")
            saltar()
    elif n==3:
      # Actualizar Tarea
        os.system('cls')
        buscar_titulo=input("¿Cual es el titulo de la tarea?: ")
        if buscar_titulo in titulos:
            index=titulos.index(buscar_titulo)
            os.system('cls')
            animated_text(f"Datos Encontrados con Exito\n\tTitulo De Tarea: {titulos[index].title()}\nDetalle De Tarea: {detalles[index].Capitalize()}\nFecha De Creacion: {fechasI[index]}\nFecha de Finalizacion: {fechaF[index]}\nEstado Tarea: {estados[index].title()}\n\n")
            nuevo_titulo=input("Nuevo Titulo de la tarea: ").title()
            nuevo_detalle=input("Nueva Descripcion de la tarea: ")
            nueva_fechaI=input("Nueva Fecha Inicial M/D/A: ")
            nueva_fechaF=input("Nueva Fecha Final M/D/A: ")
            nuevo_estado=input("Nuevo Estado de la tarea: ")
            os.system('cls')
            animated_text("\n\n Datos Actualizados Correctamente")
            saltar()
        else:
            os.system('cls')
            animated_text("ERROR : TITULO NO ENCONTRADO\n")
            saltar()
    elif n==4:
        # Eliminar Tarea
        os.system('cls')
        buscar_titulo=input("¿Cual es el titulo de la tarea?: ")
        if buscar_titulo in titulos:
            index=titulos.index(buscar_titulo)
            os.system('cls')
            animated_text(f"Datos Encontrados con Exito\n\tTitulo De Tarea: {titulos[index].title()}\nDetalle De Tarea: {detalles[index].Capitalize()}\nFecha De Creacion: {fechasI[index]}\nFecha de Finalizacion: {fechaF[index]}\nEstado Tarea: {estados[index].title()}\n\n¿Seguro Que Quieres Eliminar esta tarea? SI/NO")
            r=input("Responde Aca:").lower
            if r !='No':
                os.system('cls')
                tarea_eliminada=titulos.pop(index)
                del detalles[index]
                del fechasI[index]
                del fechaF[index]
                animated_text(f"Tarea con titulo\n\t{tarea_eliminada.upper()}\nFUE ELIMINADA CON EXITO\n")
                saltar()
            else:  
                os.system('cls')
                animated_text("LA TAREA NO SE ELIMINO\n")
                saltar()
        else:
            os.system('cls')
            animated_text("ERROR : TITULO NO ENCONTRADO\n")
            saltar()
    elif n==5:
        os.system('cls')
        for i ,(titulo,detalle,fecha1,fecha2,estado) in zip(titulos,detalles,fechasI,fechaF,estados):
            animated_text(f"\nRgistro # {i}\n\tTitulo Tarea: {titulo}\nDetalle Tarea: {detalle}\nFecha De Creacion: {fecha1}\nFecha Final: {fecha2}\nEstado Tarea: {estado}\n")
        saltar()
    elif n==6:
        # Ordenar Tareas Mayor / Menor Por titulo
        os.system('cls')
        # Combinar las listas en una lista de tuplas:
        tupla_comprimida=list(zip(titulos,detalles,fechasI,fechaF,estados))
        tupla_comprimida.sort(key=lambda x:x[0])   # podemos cambiar [0] por el valor que queremos filtrar por ejemplo [2] fechasI
        titulo_ordenado,detalle_ordenado,fecha1_ordenada,fecha2_ordenada,estado_ordenado=zip(*tupla_comprimida) # Descomprimimos 
        for i,(titulo,detalle,fecha1,fecha2,estado) in zip(titulo_ordenado,detalle_ordenado,fecha1_ordenada,fecha2_ordenada,estado_ordenado):
            animated_text(f"\nRgistro # {i}\n\tTitulo Tarea: {titulo}\nDetalle Tarea: {detalle}\nFecha De Creacion: {fecha1}\nFecha Final: {fecha2}\nEstado Tarea: {estado}\n")
        saltar()
    elif n==7:
        # Ordenar Tareas Menor / Mayor Por titulo
        os.system('cls')
        # Combinar las listas en una lista de tuplas:
        tupla_comprimida=list(zip(titulos,detalles,fechasI,fechaF,estados))
        tupla_comprimida.sort(key=lambda x:x[0],reverse=True)   # podemos cambiar [0] por el valor que queremos filtrar por ejemplo [2] fechasI
        titulo_ordenado,detalle_ordenado,fecha1_ordenada,fecha2_ordenada,estado_ordenado=zip(*tupla_comprimida) # Descomprimimos 
        for i,(titulo,detalle,fecha1,fecha2,estado) in zip(titulo_ordenado,detalle_ordenado,fecha1_ordenada,fecha2_ordenada,estado_ordenado):
            animated_text(f"\nRgistro # {i}\n\tTitulo Tarea: {titulo}\nDetalle Tarea: {detalle}\nFecha De Creacion: {fecha1}\nFecha Final: {fecha2}\nEstado Tarea: {estado}\n")
        saltar()
    elif n==8:
        # Ordenar Tareas Menor / Mayor Por titulo
        os.system('cls')
        # Combinar las listas en una lista de tuplas:
        tupla_comprimida=list(zip(titulos,detalles,fechasI,fechaF,estados))
        tupla_comprimida.sort(key=lambda x:x[0],reverse=True)   # podemos cambiar [0] por el valor que queremos filtrar por ejemplo [2] fechasI
        titulo_ordenado,detalle_ordenado,fecha1_ordenada,fecha2_ordenada,estado_ordenado=zip(*tupla_comprimida) # Descomprimimos 
        for i,(titulo,detalle,fecha1,fecha2,estado) in zip(titulo_ordenado,detalle_ordenado,fecha1_ordenada,fecha2_ordenada,estado_ordenado):
            animated_text(f"\nRgistro # {i}\n\tTitulo Tarea: {titulo}\nDetalle Tarea: {detalle}\nFecha De Creacion: {fecha1}\nFecha Final: {fecha2}\nEstado Tarea: {estado}\n")
        saltar()