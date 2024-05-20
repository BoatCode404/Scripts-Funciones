'''Escribe un programa que reciba el Índice de Masa Corporal (IMC) de una persona
y lo clasifique en:
Bajo peso (menos de 18.5)
Normal (18.5-24.9)
Sobrepeso (25-29.9)
Obeso (30 o más)'''
import os,time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacion_imc(p,a):
    im=p/a**2
    if im>=30:
        return (f"{im:.1f} : Usted es un Obeso")
    elif im>=25 and im<30:
        return (f"{im:.1f} : Usted esta en Sobrepeso")
    elif im>=18.5 and im<25:
        return (f"{im:.1f} : Usted esta Normal")
    else:
        return (f"{im:.1f} : Usted esta bajo de peso ")
listaImc=[]
while True:
    os.system('cls')
    print("Esta es la calculadora de IMC automatica \n ")
    animated_text("Primero escribe tu nombre")
    nombre=input("Aca:")
    os.system('cls')
    try:
        animated_text(f"{nombre} ¿Cual es tu peso?: ")
        peso=float(input())
        animated_text(f"{nombre} ¿Cual es tu altura?: ")
        altura=float(input())
    except ValueError:
        animated_text("ERROR SE ESPERABA UN NUMERO")
    imc=clasificacion_imc(peso,altura)
    listaImc.append((nombre,imc))
    animated_text("\n\n¿Quieres ingresar otra persona?\nSi\nNo\nResponda Aca:")
    r=input().lower()
    if r!='si':
        break
os.system('cls')
for i , (nombre,imc) in enumerate(listaImc,1):
    print(f'Registro #{i} Pertenece a : {nombre}\nSu IMC es: {imc}\n')