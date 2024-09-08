'#?Elabore un algoritmo que solicite un número entero y muestre un mensaje indicando la vocal correspondiente, considerando que la vocal A = 1'
import time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
vocales=['A','E','I','O','U']
try:
    numero=int(input("Digite un numero: "))
    if numero==1:
        print(vocales[0])
    elif numero==2:
        print(vocales[1])
    elif numero==3:
        print(vocales[2])
    elif numero==4:
        print(vocales[3])
    elif numero==5:
        print(vocales[4])
except ValueError:
    animated_text("ERROR Se esperaba un numero entero")