import re,random

my_tupla = [
    (r"Yo soy(.*)", ["Por que piensas que eres {}?", "Como llegaste hacer {}"]),
    (r"Hola(.*)", ["Hola como estas! ?", "Hola ,Que tal ", "Hola , Mucho gusto!"]),
    (r"Hola(.*)como estas?", ["Hola, muy bien, ¿y tú cómo estás?", "Hola, ¿qué tal?", "¡Hola! ¿Cómo te ha ido?"]),
    (r"Que (.*)hora es?", ["Es la hora de aprender Python.", "No tengo un reloj a mano.", "Es hora de programar."])
]
def responder_pregunta(pregunta):
    for patron,respuestas in my_tupla:
        concidencia=re.search(patron,pregunta)
        if concidencia:
            grupo=concidencia.group(1)
            chatbot=random.choice(respuestas).format(grupo)
            return chatbot
    return "No entiendo lo que dices"


usuario=input().capitalize()
print(responder_pregunta(usuario))