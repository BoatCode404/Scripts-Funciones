#Crea un diccionario donde las claves sean los nombres de los estudiantes y los valores sean sus calificaciones


def Diccionario():
    calificaciones={
        'julian':5.0,
        'pedro':4.0,
        'santago':1
    }

    return calificaciones


if __name__=='__main__':
    estudiantes=Diccionario()
    print(estudiantes)

