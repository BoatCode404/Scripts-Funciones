#Escribe una función que cuente cuántas veces aparece un nombre específico en una lista.

def conteo(n,lista):
    c=0
    for i in lista:
        if i == n:
            c+=1
    return c


if __name__=='__main__':
    nombres=['julian','julian','santiago']
    bus='julian'
    
    cantidad=conteo(bus,nombres)
    print(cantidad)