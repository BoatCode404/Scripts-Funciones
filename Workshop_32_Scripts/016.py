import time
def animated_text(text):
    for caracter in text:
        print(caracter,end='',flush=True)
        time.sleep(0.1)
vocales={1:"A",2:"E",3:"I",4:"O",5:"U"}
try:
    r=int(input("seleccione un numero del 1-5 para saber su vocal: "))
    if r ==1:
            animated_text(f'{r} es : {vocales[1]}')
    elif r ==2:
            animated_text(f'{r} es : {vocales[2]}')
    elif r ==3:
            animated_text(f'{r} es : {vocales[3]}')
    elif r ==4:
            animated_text(f'{r} es : {vocales[4]}')
    elif r ==5:
            animated_text(f'{r} es : {vocales[5]}')
    else:
            animated_text('Lo siento solo hay 5 vocales')
except ValueError:
    animated_text('❌ERROR SE ESCRIBIO UNA LETRA ❌')
