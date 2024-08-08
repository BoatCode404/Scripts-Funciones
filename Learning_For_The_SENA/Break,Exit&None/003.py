#Escribe una función que reciba un argumento opcional. Si el argumento no es proporcionado, la función debe imprimir "No se proporcionó ningún argumento


def sinArgumento(arg=None):
    if arg is None:
        print('No se proporciono argumento')
    else:
        print('el argumento es ',arg)



sinArgumento(8)
