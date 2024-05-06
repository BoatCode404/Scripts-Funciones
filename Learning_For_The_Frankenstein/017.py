'''Escribe un programa que reciba una edad como entrada y clasifique a la persona
en las siguientes categorías:
Niño (menos de 11 años)
Adolescente (12-17 años)
Adulto (18-64 años)
Mayor (65 años o más)
Opcional: preadolescente (11 a 13) y adolescente (14 a 17)'''
import time
try:
    def animated_text(text):
        for c in text:
            print(c,end='',flush=True)
            time.sleep(0.1)
    listaEdad=[]
    cantidadEdades=int(input("¿Cuantas personas vas a registrar?: "))
    for i in range(cantidadEdades):
        edad=int(input("¿Cual es su edad?: "))
        listaEdad.append(edad)
        if edad>=65:
            animated_text("Mayor\n")
        elif edad>=18 and edad<65:
            animated_text("Adulto\n")
        elif edad>=14 and edad<18:
            animated_text("Adolecente\n")
        elif edad>=11 and edad<14:
            animated_text("Preadolecente\n")
        else:
            animated_text("Niño\n")
except ValueError:
    animated_text("ERROR ")
animated_text("¿Deseas Conocer cuantas edadades son mayores?: \nSi\nNo\nResponda Aca:")
respuesta=input().lower()
if respuesta=='si':
    mayores=list(filter(lambda x : x>=18))
    for i in mayores:
        print(f'Los mayores que se registraron fueron {len(mayores)}')
elif respuesta=='no':
    exit()