import os
while True:
        letra=input('Ingrese letra\n').lower()
        if letra!='a'and letra!='e'and letra!='i'and letra!='o'and letra!='u':
                letra=input('Ingrese letra\n').lower()
        else:
            print('Has escrito una vocal')
            break