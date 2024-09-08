# Escribe una función que elimine a un estudiante del diccionario dado su nombre.

def crearDiccionarioNotas():
    calificaciones={
        'julian':5.0,
        'pedro':4.0,
        'santago':1.0
    }
    return calificaciones


def eliminarEstudiante(e,dic):
    if e in dic:
        del dic[e]
    


notas=crearDiccionarioNotas()

eliminarEstudiante('pedro',notas)

print(notas)