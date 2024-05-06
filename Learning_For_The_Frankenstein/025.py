'''Escribe un programa que reciba el tamaño de una pantalla (en pulgadas) y la
clasifique en:
Pequeña (menos de 15 pulgadas)
Mediana (15-27 pulgadas)
Grande (28-40 pulgadas)
Muy grande (más de 40 pulgadas)'''
import os,time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasifiacionPantalla(p):
    if p >40:
        return("La pantalla es Muy Grande ")
    elif p>=28 and p<41:
        return("La pantalla es Grande")
    elif p>=15 and p<28:
        return("La pantalla es Mediana")
    else:
        return("La pantalla es pequeña")
lista=[]
index=1
while True:
    os.system('cls')
    animated_text(f"Registro #{index}\n")
    marca=input("escribe la marca de la pantalla: ")
    try:
        pulgadas=int(input("Escriba las pulgadas de la pantalla : "))
        clasificacion=clasifiacionPantalla(pulgadas)
        lista.append(((marca,pulgadas,clasificacion)))
        index+=1
        print("\n\n¿Quieres ingresar mas registros?: ")
        animated_text("Responda Aca: ")
        r=input().lower()
        if r!='si':
            break
    except ValueError:
        animated_text("❌ERROR❌ Se esperaba un numero entero como pulgada")
        os.system('cls')
os.system('cls')
for i , (marca,pulgadas,clasificacion) in enumerate(lista,1):
    print(f"Registro #{i}\nMarca: {marca}\nPulgadas:{pulgadas}\n{clasificacion}\n")