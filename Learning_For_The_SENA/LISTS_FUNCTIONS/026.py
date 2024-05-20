'''26. Escribe un programa que reciba el sueldo mensual de una persona y lo clasifique
en:
Bajo (menos de 1000 euros)
Medio (1000-3000 euros)
Alto (3001-5000 euros)
Muy alto (más de 5000 euros)'''
import os,time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
def clasificacionSueldo(s):
    if s> 5000:
        return("Sueldo Muy Alto")
    elif s>=3001 and s<5001:
        return("Sueldo Alto")
    elif s>=1000 and s<3001:
        return("Sueldo Medio")
    else:
        return("Sueldo Bajo")
lista=[]
index=1
while True:
    os.system('cls')
    animated_text("¿Cual es su nombre? :")
    nombre=input()
    animated_text(f"\nRegistro #{index}\n")
    try:
        print('\nEscribe Su sueldo Mensual en euros Para clasificarlo')
        sueldo=int(input("Aca: "))
        tipoSueldo=clasificacionSueldo(sueldo)
        lista.append((nombre,sueldo,tipoSueldo))
        index+=1
        os.system('cls')
        animated_text("¿Quieres Ingresar mas registros? Si ò No : ")
        r=input().lower()
        if r!='si':
            break
    except ValueError:
        print("❌ERROR❌: Se esperaba un Numero entero como sueldo\n\n")
os.system('cls')
for i , (nombre,sueldo,tipoSueldo) in enumerate(lista,1):
    print(f'Registro #{i}\nNombre del Empleado: {nombre}\nSueldo Empleado: {sueldo}\n{tipoSueldo}\n\n')