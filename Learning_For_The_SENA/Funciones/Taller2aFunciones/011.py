#Escribe una función que genere una lista de factoriales de los números del 1 al 5.

import math as m



def listaConFactorialesN(n):
    lista=[m.factorial(i) for i in range(1,n+1) ]
    print(f'la lista de factoriales de 1 a {n} es : \n')
    return lista





if __name__=='__main__':
    rango=int(input('Cual es el rango de la lista : '))
    listaFactoriales=listaConFactorialesN(rango)
    print(listaFactoriales)





