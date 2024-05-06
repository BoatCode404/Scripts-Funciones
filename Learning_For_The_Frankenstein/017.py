'''Escribe un programa que reciba una edad como entrada y clasifique a la persona
en las siguientes categorías:
Niño (menos de 11 años)
Adolescente (12-17 años)
Adulto (18-64 años)
Mayor (65 años o más)
Opcional: preadolescente (11 a 13) y adolescente (14 a 17)'''
import time,os
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacionEdad(e):
    if edad>=65:
        return("Mayor\n")
    elif edad>=18 and edad<65:
        return("Adulto\n")
    elif edad>=14 and edad<18:
        return("Adolecente\n")
    elif edad>=11 and edad<14:
        return("Preadolecente\n")
    else:
        return("Niño\n")
listaEdad=[]
while True:
    try:
        os.system('cls')
        edad=int(input("¿Cual es su edad?: "))
        tipo=clasificacionEdad(edad)
        listaEdad.append((edad,tipo))
        print("¿Quieres ingresar mas edades?: Si ó No\n")
        animated_text("Responda Aca: ")
        r=input().lower()
        if r!='si':
            break
    except ValueError:
        print("❌ Error ❌ se esperaba una numero entero como edad")
os.system('cls')
for i , (edad,tipo) in enumerate(listaEdad,1):
    print(f"El Registro #{i}\nTiene La edad {edad}\nEs un {tipo}")