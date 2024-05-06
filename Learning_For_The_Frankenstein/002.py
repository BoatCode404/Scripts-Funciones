'#?Se necesita obtener el promedio simple de un estudiante a partir de sus notas parciales. si el promedio es 3 hasta 5 ( Aprobo) de resto ( No aprobo ) '

#// MODIFICADO

listaNotas=[]
cantidadNotas=int(input("¿cuantas notas vas ingresar hoy? : "))
for i in range(cantidadNotas):
    notas=float(input(f"Digite la {i+1} Nota de 1-5 : "))
    listaNotas.append(notas)
promedio=print(f'el promedio de las notas es {sum(listaNotas)/cantidadNotas:.1f}')
promedio=float()
if promedio>=3.0:
    print('No aprobo')
else:
    print('Aprobo')