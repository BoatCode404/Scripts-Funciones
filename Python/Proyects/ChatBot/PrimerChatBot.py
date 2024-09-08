import re,random,time,os
pares=[

    (r'(.*?)horario(.*)atencion(.*?)',['Nuestros horarios de atencion son de\nLunes a Jueves de 8am a 5pm ','Normalmente estamos de\n8 a 5 de Lunes a Juves']),
    (r'(.*?)servicios(.*?)',['contamos con spa','contamos con spa, bañera']),
    (r'(.*?)horario(.*?)',['Nuestros horarios de atencion son de\nLunes a Jueves de 8am a 5pm ','Normalmente estamos de\n8 a 5 de Lunes a Juves']),
    (r'(.*?)ubicados(.*?)',['Estamos ubicados en Medellin\Bogota\Manizales','Nuestros hoteles estan ubicados en :\n\nMedellin\nBogota\Manizales']),
    (r'(.*?)ciudad(.*?)',['Estamos ubicados en Medellin\Bogota\Manizales','Nuestros hoteles estan ubicados en Medellin\nBogota\Manizales']),
    (r'(.*?)contactar(.*?)',['Nuestros numeros de Atencion son :\n\nPara Medellin:3117058703 ext 3\nPara Bogota:31020203 ext 2\nPara Manizales:2553030 ext 1']),
    (r'(.*?)numero(.*?)telefono(.*?)',['Nuestros numeros de contacto\nPara Medellin:3117058703 ext 3\nPara Bogota:31020203 ext 2\nPara Manizales:2553030 ext 1']),
    (r'(.*?)numero(.*?)',['Nuestros numeros de Atencion son :\n\nPara Medellin:3117058703 ext 3\nPara Bogota:31020203 ext 2\nPara Manizales:2553030 ext 1']),
    (r'(.*?)estrellas(.*?)',['El Hotel de Medellin cuenta con 4 Estrellas\n\nEl Hotel de Bogota cuenta con 5 Estrellas','Medellin: 4 Estrellas\nBogota: 5 Estrellas\nManizales: 5 Estrellas']),
    (r'(.*?)promocion(.*?)',['Si contamos con promociones para este mes\nTenemos promocion de 2x1 en la Suit De medellin Animate','Tenemos Promociones en Medellin de 2x1 En cualquiera de nuestras Suits']),
    (r'(.*?)precio(.*?)habitacion(.*?)',['Estos son los precios generales que manejamos:\n\nDia con alimentacion incluida : 100.000$\nDia Sin alimentacion : 60.000\nContamos con un servicio completo por persona que inlcluye acceso a todos los servicios incluido alimentacion del hotel por tan solo : 250.000$ la noche']),

]
def animated_text(text):
    for c in text:
        print(c,end="",flush=True)
        time.sleep(0.03)
def responder_pregunta(pregunta):
    for patron,respuesta in pares:
        concidencia=re.search(patron,pregunta)
        if concidencia:
            grupo=concidencia.group(1)
            chatBot=random.choice(respuesta).format(grupo)
            return chatBot
    return "No entendi tu pregunta"

os.system('cls')
animated_text("ChatBot: Hola Binvenido En puedo ayudarte hoy ?")
while True:
    usuario=input("\n\nTu: ").capitalize()
    print(f"\n\nChatBot: {responder_pregunta(usuario)}")