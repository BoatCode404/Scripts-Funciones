import nltk,os
from nltk.chat.util import Chat,reflections

questions=[
    ("Hola como estas?",["Hi Bro muy bien y tu? "]),
    ("En que pais de encuentras?",["Estoy en Medellin"]),
    (r"hola(.*)", ["¡Hola! Muy bien, ¿y tú?"])
    (r"en que pais (.*) encuentras?", ["Estoy en Medellín, ¿y tú?"]),
    (r"yo soy (.*)", ["¿Por qué piensas que eres %1?", "¿Cómo llegaste a ser %1?"]),
    (r"me siento (.*)", ["¿Por qué te sientes %2?", "¿Te sientes %1 a menudo?"])
]

def chatbot():
    print("Chat Bot: Hola En que puedo ayudarte hoy?\n ")
    chatbot=Chat(questions,reflections)
    while True:
        mensajeUsuario=input("Tu: ").capitalize()
        respuestaChatbot=chatbot.respond(mensajeUsuario)
        if respuestaChatbot:
            os.system('cls')
            print(f"ChatBot: {respuestaChatbot}")
        else:
            print("No econtre tu pregunta")
os.system('cls')
chatbot()

    