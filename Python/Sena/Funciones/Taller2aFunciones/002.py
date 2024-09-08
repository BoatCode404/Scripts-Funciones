#-Hacer un programa que lea las calificaciones de un alumno en 10 asignaturas, las almacene en un vector y calcule e imprima su media

def crearListaNotas():
    notas=[]
    for i in range(1,11):
        nota=float(input(f'Digite la nota # {i} : '))
        notas.append(nota)
    return notas

def promedioListaNotas(lista):
    promedio= sum(lista)/len(lista)
    return promedio
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    