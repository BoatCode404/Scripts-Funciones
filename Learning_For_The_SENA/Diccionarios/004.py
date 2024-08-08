#Escribe una función que calcule el promedio de las calificaciones en un diccionario de estudiantes.


def crearDiccionarioNotas():
    calificaciones={
        'julian':5.0,
        'pedro':4.0,
        'santago':1.0
    }

    return calificaciones


def promedioCalificaciones(dic):
    
    return sum(dic.values())//len(dic)





datosEstudiante=crearDiccionarioNotas()
promedio=promedioCalificaciones(datosEstudiante)

print(promedio)