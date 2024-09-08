#Escribe una función que sume todos los números pares en una lista

def crearListaNumeros(n):
    lista=[x for x in range(n+1)]
    return lista



def sumaParesLista(lista):
    pares=sum([par for par in lista if par%2==0])
    return pares



if __name__=='__main__':
    
    cantidad=100

    numeros=crearListaNumeros(cantidad)

    suma=sumaParesLista(numeros)
    print(suma)