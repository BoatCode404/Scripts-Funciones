import os
import time
import json
def animated_text(text):
    for caracter in text:
        print(caracter,end='',flush=True)
        time.sleep(0.1)
def mostrar_opciones():
    animated_text('1) Iniciar Sesion\n')
    animated_text('2) Registrarse\n')
def limpar_pantalla():
    os.system('cls'if os.name=='nt'else 'clear')
def iniciar_sesion(users):
    limpar_pantalla()
    nombreUsuario=input('Digite Nombre de usuario \n')
    passwordUsuario=input('Digite contraseña \n')
    limpar_pantalla()
    for nombre,datos in users.items():
        if datos['nombre_usuario']==nombreUsuario and datos['password']==passwordUsuario:
            animated_text('¡Bienvenido de nuevo! 🎉\n\n')
            print('Has iniciado sesión correctamente. ¡Es genial tenerte de vuelta!😊\n')
            animated_text('¿En qué podemos ayudarte hoy?\n\n')
            animated_text('Estamos aquí para hacer tu experiencia lo más fácil y agradable posible.')
            return
    animated_text('❌NOMBRE DE USUARIO O CONTRASEÑA INCORRECTOS ❌')
def registrarse(users):
    limpar_pantalla()

    registroUsuario,registrocontraseña,telefono=input("Digite su usuario \n"),input('Digite su contraseña\n'),input('Digite telefono de recuperacion: \n')

    limpar_pantalla()

    nuevo_usuario={}
    nuevo_usuario['nombre_usuario']=registroUsuario
    nuevo_usuario['password']=registrocontraseña
    nuevo_usuario['telefono_recuperacion']=telefono

    nuevo_nombre_usuario=f"user{len(users)+1}"
    users[nuevo_nombre_usuario]=nuevo_usuario

    with open('users.json','w')as archivo_json:
        json.dump(users,archivo_json,indent=4)
        
    animated_text('¡Registro completado con éxito! 🌟🎉\n\n')
    print('¡Enhorabuena! Ahora formas parte de nuestra comunidad. 😊👏\n\n')
    animated_text('¡Bienvenido a bordo! Estamos emocionados de tenerte con nosotros. 🚀✨')
def main():
   
   with open('users.json','r') as archivo_json:
    users = json.load(archivo_json) 

    animated_text("¡Bienvenido al panel de usuario! 🎉\n\n" )
    print("Estamos emocionados de tenerte aquí. \nPor favor, introduce tus credenciales para acceder a tu cuenta y comenzar a disfrutar de nuestros servicios. 🚀✨ \n")
    print('Tu seguridad es nuestra prioridad \nAsí que descansa tranquilo sabiendo que tus datos están protegidos.🔒\n¡Gracias por confiar en nosotros!😊\n¿Que Quieres hacer?\n')
    mostrar_opciones()
    opcion=input()
    
    if opcion=='1':
        iniciar_sesion(users)
    elif opcion=='2':
        registrarse(users)
    else:
        animated_text('Opcion no valida')
if __name__ == '__main__':
    main()
    