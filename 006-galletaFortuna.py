import time
import os
import random
def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
Mensaje=['Recuerda que eres más fuerte de lo que crees y más capaz de lo que imaginas.','El amor y la amistad son los verdaderos tesoros de la vida','La aventura espera fuera de tu zona de confort','Nunca subestimes el poder de una sonrisa sincera','La paciencia es una virtud poderosa; todo llega en su debido tiempo','La paciencia es una virtud poderosa; todo llega en su debido tiempo','Las dificultades son oportunidades disfrazadas','Las dificultades son oportunidades disfrazadas','Confía en tu instinto; te guiará en la dirección correcta','La felicidad se encuentra en los pequeños momentos de la vida','El éxito llegará a tu puerta si perseveras','La suerte favorece a los valientes']
respuesta=input("Digita Por favor: (Galleta) para obtener una galleta de la fortuna🥠\n")
while respuesta.lower()!="galleta":
    respuesta=input("Digita Por favor: (Galleta) para obtener una galleta de la fortuna🥠\n")
frase=random.choice(Mensaje)
animate_text(f"Felicitaciones su galleta de la fortuna contenia esta frase : \n")
animate_text(f'{frase} ')
print('\n')
respuesta=input("Puedes tomar otra galleta ¿La Quieres?: \n")
if respuesta.lower()=='si':
    frase=random.choice(Mensaje)
    animate_text(f"Felicitaciones su segunda galleta de la fortuna contenia esta frase : {frase} 🥠")
else:
    print("Hasta la proxima 👌")