import os
import time as t

listaNombreProducto=[]
listaPrecioProducto=[]
listaCantidadProducto=[]
def prsionaTecla():
    animated_text("\nPresiona una tecla para continuar")
    input()
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        t.sleep(0.03)
def menu():
    titulo='Mercados 7 Esquinas'
    print(titulo.center(30))
    animated_text("Bienvenido Que deseas Hacer\n\n1) Agregar Producto Nuevo\n2) Buscar Producto Existente\n3) Actualizar Producto Existente\n4) Eliminar Producto\n5) Salir\n\n\n")

salida=True
while salida==True:
    os.system('cls')
    menu()
    try:
        respuestaMenu=int(input("Responda Aca:"))
        if respuestaMenu==1:
            os.system('cls')
            nombreProducto=input("Cual es el nombre el producto: ").capitalize()
            precioProducto=int(input("Cual es el precio del producto: "))
            cantidadProducto=int(input("Que cantidad vas ingresar: "))
            listaNombreProducto.append(nombreProducto)
            listaPrecioProducto.append(precioProducto)
            listaCantidadProducto.append(cantidadProducto)
            animated_text("\nProducto Agregado Correctamente")
            prsionaTecla()
        elif respuestaMenu==2 :
            os.system('cls')
            buscarProducto=input("Nombre del producto: ").capitalize()
            if buscarProducto in listaNombreProducto:
                indexproducto=listaNombreProducto.index(buscarProducto)
                os.system('cls')
                animated_text("Producto Encontrado\n\n")
                print(f"Nombre Producto: {listaNombreProducto[indexproducto]}\nPrecio Producto: {listaPrecioProducto[indexproducto]}\nCantidad Producto: {listaCantidadProducto[indexproducto]}\n")
                prsionaTecla()
            else:
                animated_text("PRODUCTO NO ENCONTRADO\n")
                prsionaTecla()
        elif respuestaMenu==3:
            os.system('cls')
            buscarProducto=input("Nombre del producto: ").capitalize()
            if buscarProducto in listaNombreProducto:
                animated_text("Producto Encontrado\n")
                print('-------------------------------------')
                indexproducto=listaNombreProducto.index(buscarProducto)
                nuevoNombre=input("Nuevo Nombre Producto: ").capitalize()
                nuevoPrecio=int(input("Nuevo Precio Producto: "))
                nuevaCantidad=int(input("Nueva Cantidad Producto: "))
                listaNombreProducto[indexproducto]=nuevoNombre
                listaPrecioProducto[indexproducto]=nuevoPrecio
                listaCantidadProducto[indexproducto]=nuevaCantidad
                animated_text("\nProducto Actualizado Correctamente")
                prsionaTecla()
            else:
                animated_text("PRODUCTO NO ENCONTRADO\n")
                prsionaTecla()
        elif respuestaMenu==4:
            os.system('cls')
            buscarProducto=input("Nombre del producto: ").capitalize()
            if buscarProducto in listaNombreProducto:
                animated_text("Producto Encontrado\n")
                print('-------------------------------------')
                desicion=input("Estas Seguro que desea eliminar este porducto? Si / No : ").lower()
                if desicion=='si':
                    indexproducto=listaNombreProducto.index(buscarProducto)
                    listaNombreProducto.pop(indexproducto)
                    listaCantidadProducto.pop(indexproducto)
                    listaPrecioProducto.pop(indexproducto)
                    os.system('cls')
                    animated_text("Producto Eliminado Correctamente")
                    prsionaTecla()
                else :
                    os.system('cls')
                    animated_text("No se elimino el poducto")
                    prsionaTecla()
            else:
                animated_text("PRODUCTO NO ENCONTRADO\n")
                prsionaTecla()
        elif respuestaMenu==5:
            os.system('cls')
            animated_text(" Hasta Pronto")
            salida=False
    except ValueError:
        os.system('cls')
        animated_text("Se esperaba un numero Entero")
        prsionaTecla()