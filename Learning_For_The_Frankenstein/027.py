'''Elaborar un algoritmo que solicite 2 números enteros y un operador aritmético y
luego debe de mostrar el resultado de la operación correspondiente.'''
import time,os
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
def calculadora(o,n1,n2):
    if o=='+':
        return(f'El resultado de la suma es {n1+n2}')
    elif o=='-':
        return(f'El resultado de la resta es {n1-n2}')
    elif o=='*':
        return(f'El resultado de la multiplicacion es {n1*n2}')
    elif o=='%':
        return(f'El resultado de la division es {n1/n2:.3f}')
lista=[]
index=1
while True:
    animated_text(f"Registro #{index}\n")
    operador,num1,num2=input("Cual es el operador: "),int(input("Cual es el primero numero: ")),int(input("Cual es el segundo numero: "))   
    resultado=calculadora(operador,num1,num2)
    lista.append(((operador,num1,num2,resultado)))
    index+=1
    os.system('cls')
    print("Quieres ingresar otro Registro ? si o no ")
    r=input("Responda aca: ")
    if r!='si':
        break
