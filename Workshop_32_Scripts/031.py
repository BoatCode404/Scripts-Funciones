import os
meses={
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}
while True:
    num=int(input("Digite un numero\n"))
    if 1<=num<=12:
        print(meses[num])
    else:print("Solo hay 12 meses")
