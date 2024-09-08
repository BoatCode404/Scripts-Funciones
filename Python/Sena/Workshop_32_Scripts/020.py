import os,time
def animated_text(text):
    for caracter in text:
        print(caracter,end='',flush=True)
        time.sleep(0.1)
pago_trabajador=float(48733*30)
animated_text('¿cuantos empleados son?:\n')
empleados=int(input())
for i in range(empleados,0,-1):
    print(f'el sueldo promedio del empleado {i} es : {pago_trabajador:.3F}')