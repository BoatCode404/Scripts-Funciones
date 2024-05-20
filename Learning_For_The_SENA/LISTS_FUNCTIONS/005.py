'#? Se requiere el algoritmo para elaborar la planilla de un empleado. Para ello se dispone de sus horas laboradas en el mes, así como de la tarifa por hora'
import os
cantidadEmpleados=int(input("¿Cuantos trabajadores vas a registrar hoy?: "))
for i in range(cantidadEmpleados):
    nombre=input(f"Cual es el nombre del empleado {i+1}")
    os.system('cls')
    horasSemanales=int(input(f"¿Cuantas horas en la semana realizo {nombre}?: "))
    os.system('cls')
    valorHora=int(input(f"¿Cual es el valor de la hora de {nombre} ?: "))
    os.system('cls')
    print(f"La planilla # {i+1} para {nombre} es {valorHora*horasSemanales}")