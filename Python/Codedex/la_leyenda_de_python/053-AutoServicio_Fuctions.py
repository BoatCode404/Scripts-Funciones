import os,time
menuPrincipal=["Burger Basic","Looping Lettuce Wrap"," Recursive Refill Fries"]
bebidas=["Java Juice","Binary Soda",""]
postres=["Code Cream Sundae","Bit Bites"]
def get_item(num1,num2,num3):
    if 0< num1<=len(menuPrincipal):
        item1=menuPrincipal[num1-1]
    else:
        item1="No se encontro el elemento"
    if 0< num2 <= len(bebidas):
        item2=bebidas[num2-1]
    else:
        item2="No se encontro el elemento"
    if 0<num3<=len(postres):
        item3=postres[num3-1]
    else:
        item3="No se encontro el elemento"
    return item1,item2,item3
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.03)
def welcome():
    os.system('cls')
    animated_text("Bienvenidos a ByteBoat Burgers 🍔\n\n")
    print("¡Navega por el sabor de la innovación!\nEn ByteBoat Burgers, combinamos la pasión por la programación con el amor por la buena comida. Nuestro menú está codificado para satisfacer tus antojos con una selección de hamburguesas gourmet, complementos binarios y refrescos de edición limitada\n\n") 
    
    print("----- Menu Principal ----\n")  
    animated_text("1) Burger Basic\n")
    print(" Una clásica con todos los bits.")
    print("  - Ingredientes: Pan, carne de res, lechuga, tomate, cebolla, queso.")
    print("  - Precio: $8.99\n\n")

    animated_text("2) Looping Lettuce Wrap\n")
    print(" Para los que buscan iterar su dieta.")
    print("  - Ingredientes: Hojas de lechuga, carne de pollo, tomate, cebolla, salsa de yogur.")
    print("  - Precio: $7.99\n\n")

    animated_text("3) Recursive Refill Fries\n")
    print(" ¡Come todo lo que puedas, y vuelve por más!")
    print("  - Ingredientes: Papas, aceite, sal.")
    print("  - Precio: $4.99\n\n")

    print("----- Bebidas ----\n")  
    animated_text("1) Java Juice\n")
    print(" Un café cargado para esos días de debugging.")
    print("  - Ingredientes: Café, agua, opcionalmente leche y azúcar.")
    print("  - Precio: $3.99\n\n")

    animated_text("2) Binary Soda\n")
    print(" Refrescos con solo dos opciones: ¡0 azúcar ò 1 montón de sabor!.")
    print("  - Ingredientes: Agua carbonatada, colorante, saborizante, azúcar o edulcorante.")
    print("  - Precio: $2.99\n\n")

    animated_text("3) Exceptional Water\n")
    print(" Hidratación para continuar codificando.")
    print("  - Ingredientes: Agua purificada.")
    print("  - Precio: $1.99\n\n")

    print("----- Postres ----\n")  
    animated_text("1) Code Cream Sundae\n")
    print(" Un postre que desborda capas de dulzura.")
    print("  - Ingredientes: Helado de vainilla, sirope de chocolate, crema batida, nueces.")
    print("  - Precio: $5.99\n\n")

    animated_text("2) Bit Bites\n")
    print(" Pequeñas delicias para un bocado rápido.")
    print("  - Ingredientes: Galletas, chocolate.")
    print("  - Precio: $3.99\n\n")

welcome()

num1=int(input("Que vas a desear del Menu Principal: "))
num2=int(input("Que vas a querer de Bebida: "))
num3=int(input("Que vas a querer de Postre: "))

os.system()
animated_text("Su pedido es este\n ")
comida,bebida,postre=get_item(num1,num2,num3)
animated_text(f"Del menu principal elejiste {comida}")
animated_text(f"Del menu de bebidas elejiste {bebida}")
(f"Del menu de postres elejiste {postre}")