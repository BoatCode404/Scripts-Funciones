# Desarrolla  un  programa  para  registrar  notas de  estudiantes en  múltiples cursos, 
# solicitando primero la cantidad de cursos y estudiantes por curso, y luego las notas individuales para 
# almacenarlas en una matriz.




notasCursos=[]

cantidadCursos=2
estudianteCurso=3


for i in range(cantidadCursos):
    print(f'\nCurso {i + 1}')
    notasCurso=[]
    for  j in range(estudianteCurso):
        nota = float(input(f'Ingrese la nota del estudiante # {j + 1} : '))
        notasCurso.append(nota)
    notasCursos.append(notasCurso)
    print('')


for i in range(cantidadCursos):
    print(f'Curso # {i+1} : ',end='')
    for j in range(estudianteCurso):
        print(f'{notasCursos[i][j]}',end=' ')
    print()




