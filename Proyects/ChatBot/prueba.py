import nltk
from nltk.chat.util import Chat, reflections
from difflib import SequenceMatcher

# Pares de preguntas y respuestas para el chatbot
pares = [
    (
        r"¿Cuál es el horario de atención\?",
        ["Nuestro horario de atención es de lunes a viernes de 9:00 a 17:00."],
    ),
    (
        r"¿Cómo puedo ponerme en contacto con ustedes\?",
        ["Puedes contactarnos a través de nuestro correo electrónico: info@ejemplo.com."],
    ),
    # Agrega más preguntas frecuentes y respuestas aquí
]

# Función para encontrar la pregunta más similar a la pregunta del usuario
def encontrar_pregunta_similar(pregunta):
    max_ratio = 0
    mejor_respuesta = None
    for patron, respuestas in pares:
        ratio = SequenceMatcher(None, patron, pregunta).ratio()
        if ratio > max_ratio:
            max_ratio = ratio
            mejor_respuesta = respuestas[0]
    return mejor_respuesta

def chatbot():
    print("¡Hola! Soy un chatbot de servicio al cliente. ¿En qué puedo ayudarte hoy?")
    chat = Chat(pares, reflections)
    while True:
        mensaje = input("Tú: ")
        respuesta = chat.respond(mensaje)
        if respuesta:
            print("Chatbot:", respuesta)
        else:
            pregunta_similar = encontrar_pregunta_similar(mensaje)
            if pregunta_similar:
                print("Chatbot: Lo siento, no entendí tu pregunta. ¿Querías preguntar:", pregunta_similar)
            else:
                print("Chatbot: Lo siento, no puedo ayudarte con eso.")

if __name__ == "__main__":
    chatbot()
