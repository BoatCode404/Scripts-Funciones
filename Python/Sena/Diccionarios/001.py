#Ejercicio 1: Elabore un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano.

romanos={
    1:'I',
    2:'II',
    3:'III',
    4:'IV',
    5:'V',
    6:'VI',
    7:'VII',
    8:'VIII',
    9:'IX',
    10:'X'
}


numero=5
if numero in romanos:
    print(romanos[numero])