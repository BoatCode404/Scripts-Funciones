'''una empresa desea saber cuanto dinero debe pagarle a cada uno de sus empleados por la hora semanal trabajada,teniendo en cuenta que si el empleado trabaja mas de 40 horas estas se consideran extras,y por esllo se pagara el doble de la hora normal hasta las 8 horas extras(despues de 40 horas);si las horas extras exceden de 8 se pagan las primeras 8 al doble de una hora normal y el resto al triple'''

import os
os.system('cls')
horas=int(input("Cuantas Horas trabajo en la semana: "))
valorHora=int(input("Cual es el valor de la hora: "))
salarioBase=valorHora*40


if horas>40:
    os.system('cls')
    cantidadHorasExtras=horas-40
    if cantidadHorasExtras<=8:
        salarioBase+=cantidadHorasExtras * valorHora * 2
        print(f'\nEl empleado Trabajo {horas} Horas semanales\n\nEl valor de la hora es: {valorHora}$\nHoras Extras que realizo: : {cantidadHorasExtras} Horas\nEl salario del empleado es: {salarioBase}\n\n')
    else:
        salarioBase+= 8 * valorHora * 2
        salarioBase+=(cantidadHorasExtras-8)*valorHora*3
        print(f'\nEl empleado Trabajo {horas} Horas semanales\n\nEl valor de la hora es: {valorHora}$\nHoras Extras que realizo: : {cantidadHorasExtras} Horas\nEl salario del empleado es: {salarioBase}\n\n')

else:
    os.system('cls')
    print(f'\nEl empleado Trabajo {horas} Horas semanales\n\nEl valor de la hora es de : {valorHora}$\nEl salario del empleado es: {salarioBase}\nEl empleado no trabajo horas extras\n\n')


