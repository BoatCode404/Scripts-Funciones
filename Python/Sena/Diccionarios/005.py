# Escribe una función que devuelva los nombres de los estudiantes con calificaciones mayores a un valor dado.


def crearDiccionarioNotas():
    calificaciones={
        'julian':5.0,
        'pedro':4.0,
        'santago':1.0
    }
    return calificaciones


def mayor(dic,v):
    return [nombre for nombre,calificacion in dic.items() if calificacion > v]


if __name__=='__main__':
    notas=crearDiccionarioNotas()
    valor=3.0

    mayores=mayor(notas,valor)
    print(mayores)