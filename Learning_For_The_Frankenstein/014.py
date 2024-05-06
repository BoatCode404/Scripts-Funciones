'#? Elabore un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano'
romanos=['I','II','III','IV','V','VI','VII','VII','IX','X']
try:
    numero=int(input("Digite un numero entero: "))
    if numero==1:
        print(romanos[0])
    elif numero==2:
        print(romanos[1])
    elif numero==3:
        print(romanos[2])
    elif numero==4:
        print(romanos[3])
    elif numero==5:
        print(romanos[4])
    elif numero==6:
        print(romanos[5])
    elif numero==7:
        print(romanos[6])
    elif numero==8:
        print(romanos[7])
    elif numero==9:
        print(romanos[8])
    elif numero==10:
        print(romanos[9])
except ValueError:
    print("Se esperaba un numero entero")