#Escribe una función que añada un estudiante y su calificación al diccionario.

def crearDiccionarioNotas():
    calificaciones={
        'julian':5.0,
        'pedro':4.0,
        'santago':1.0
    }
    return calificaciones



def agregarEstudiante(n,c,dic):
    dic[n]=c
    return dic


notas=crearDiccionarioNotas()

agregarEstudiante('pepito',5.0,notas)
print(notas)



