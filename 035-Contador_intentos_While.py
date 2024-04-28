import random
import os
entrada_usuario=0
intentos=0
numero_secreto=random.randint(1,100)
print(numero_secreto)
while entrada_usuario!=numero_secreto:
    try:   
        entrada_usuario=int(input("Adivina el numero\n"))
        intentos+=1
        os.system('cls')
        if entrada_usuario < numero_secreto:
            print("Estas muy abajo del numero")
        elif entrada_usuario > numero_secreto:
            print("Estas muy alto del numero")
    except ValueError:
        print('Se esperaba un numero entero')
print(f"Adivinaste el numero con un numero de intentos de :  {intentos}")