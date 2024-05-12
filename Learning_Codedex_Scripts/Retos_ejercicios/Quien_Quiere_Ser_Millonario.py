import os,time

botin = 0

def welcome():
    os.system('cls')
    mensaje="¡Bienvenido a ¿Quién quiere ser millonario?!\n\n"
    print(mensaje.center(60))
    animated_text("Demuestra tus conocimientos y gana 38 mil Dolares.\nContestarás una serie de preguntas de opción múltiple.\n¡Buena suerte!\n\n")
    input("\n\n<---- PRESIONA UNA TECLA PARA CONTINUAR ---->")
def animated_text(text):
    for char in text:
        print(char, end='',flush=True)
        time.sleep(0.03)
def questions():
    global botin
    os.system('cls')
    animated_text("La primera pregunta se jugara  por $1,000. ¡Buena suerte!\n\n")
    animated_text("¿Cual es la capital de francia?\na)Londres\nb)Paris\nc)Madrid\nd)Roma")
    p1=(input("\nEscriba la opcion Aca: ")).lower()
    if p1=="b":
        botin+=1000
        opcion="La Respuesta es ¡Correcta!"
    else:
        opcion="Opcion Incorrecta"
    print(opcion)
    input("<---- Segunda Pregunta (ENTER) ---->")
    os.system('cls')
    animated_text("La segunda pregunta se jugara  por $2,000. ¡Buena suerte!\n\n")
    animated_text("¿Cuál es el río más largo del mundo?\na)Nilo\nb)Amazonas\nc)Yangtsé\nd)Misisipi")
    p2=(input("\nEscriba la opcion Aca: ")).lower()
    if p2=="b":
        botin+=2000
        opcion="La Respuesta es ¡Correcta!"
    else:
        opcion="Opcion Incorrecta"
    print(opcion)
    input("<---- Tercera Pregunta (ENTER) ---->")
    os.system('cls')
    animated_text("La tercer pregunta se jugara  por $5,000. ¡Buena suerte!\n\n")
    animated_text("¿Quién escribió Don Quijote de la Mancha?\na)Miguel de Cervantes\nb)Gabriel García Márquez\nc)William Shakespeare\nd)Pablo Neruda")
    p3=(input("\nEscriba la opcion Aca: ")).lower()
    if p3=="a":
        botin+=5000
        opcion="La Respuesta es ¡Correcta!"
    else:
        opcion="Opcion Incorrecta"
    print(opcion)
    print("\n\n¿Quieres seguir jugando o te quieres retirar?\na)Si\nb)No")
    retiro=input("Responda Aca: ").lower()
    os.system('cls')
    if retiro=="a":
        opcion=animated_text(f"Gracias por jugar te llevas un botin de {botin} ")
    else:
        animated_text("La cuarta pregunta se jugara  por $10,000. ¡Buena suerte!\n\n")
        animated_text("¿Cuál es el símbolo químico del oro?\na)Au\nb)Ag\nc)Fe\nd)Cu")
    p4=(input("\nEscriba la opcion Aca: ")).lower()
    if p4=="a":
        botin+=10000
        opcion="La Respuesta es ¡Correcta!"
    else:
        opcion=("Opcion Incorrecta")
    print(opcion)
    print("\n\n¿Quieres seguir jugando o te quieres retirar?\na)Si\nb)No")
    retiro=input("Responda Aca: ").lower()
    os.system('cls')
    if retiro=="a":
        opcion=animated_text(f"Gracias por jugar te llevas un botin de {botin} ")
    else:
        animated_text("La quinta pregunta se jugara  por $20,000. ¡Buena suerte!\n\n")
        animated_text("¿En qué año llegó Cristóbal Colón a América?\na)1492\nb)1500\nc)1520\nd)1450")
    p4=(input("\nEscriba la opcion Aca: ")).lower()
    if p4=="a":
        botin+=20000
        opcion="La Respuesta es ¡Correcta!"
    else:
        opcion="Opcion Incorrecta"
    print(opcion)

welcome()