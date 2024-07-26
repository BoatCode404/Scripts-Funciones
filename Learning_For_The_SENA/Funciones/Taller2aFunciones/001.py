# Crear un array unidimensional de 20 elementos con nombres de personas. Visualizar los elementos de la lista debiendo ir cada uno en una fila distinta

def recorerListas(lista):
    for  x in lista:
        print (x)
    




def crearListaPersonas():
    personas=[]
    for i in range(1,21):
        name=input(f'Cual es el nombre de la persona # {i}: ')
        personas.append(name)
    return personas
    





if __name__=='__main__':
    listaPersonas=crearListaPersonas()
    recorerListas(listaPersonas)


