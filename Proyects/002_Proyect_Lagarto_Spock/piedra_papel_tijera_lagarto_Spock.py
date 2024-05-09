
import time,os,random

options=['Papel 📄','Piedra 🗿','Tijeras ✂️','Lagarto 🦎','Spock 🖖']

contadorUser=0
contadorCpu=0
def reglas():
    wlcome='''
██████╗░██╗███████╗██████╗░██████╗░░█████╗░░░░██████╗░░█████╗░██████╗░███████╗██╗░░░░░░░░████████╗██╗░░░░░██╗███████╗██████╗░░█████╗░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░░░░░░╚══██╔══╝██║░░░░░██║██╔════╝██╔══██╗██╔══██╗
██████╔╝██║█████╗░░██║░░██║██████╔╝███████║░░░██████╔╝███████║██████╔╝█████╗░░██║░░░░░░░░░░░██║░░░██║░░░░░██║█████╗░░██████╔╝███████║
██╔═══╝░██║██╔══╝░░██║░░██║██╔══██╗██╔══██║██╗██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██║░░░░░██╗░░░██║░░░██║██╗░░██║██╔══╝░░██╔══██╗██╔══██║
██║░░░░░██║███████╗██████╔╝██║░░██║██║░░██║╚█║██║░░░░░██║░░██║██║░░░░░███████╗███████╗╚█║░░░██║░░░██║╚█████╔╝███████╗██║░░██║██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░╚╝░░░╚═╝░░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

        ██╗░░░░░░█████╗░░██████╗░░█████╗░██████╗░████████╗░█████╗░  ██╗░░░██╗  ░██████╗██████╗░░█████╗░░█████╗░██╗░░██╗
        ██║░░░░░██╔══██╗██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ╚██╗░██╔╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
        ██║░░░░░███████║██║░░██╗░███████║██████╔╝░░░██║░░░██║░░██║  ░╚████╔╝░  ╚█████╗░██████╔╝██║░░██║██║░░╚═╝█████═╝░
        ██║░░░░░██╔══██║██║░░╚██╗██╔══██║██╔══██╗░░░██║░░░██║░░██║  ░░╚██╔╝░░  ░╚═══██╗██╔═══╝░██║░░██║██║░░██╗██╔═██╗░
        ███████╗██║░░██║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╔╝  ░░░██║░░░  ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░╚██╗
        ╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░  ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝
'''
    print(wlcome)
    animated_text("¡Bienvenido al juego de Piedra, Papel, Tijeras, Lagarto, Spock!\n\nInstrucciones:\n- Este juego es una versión extendida del clásico Piedra, Papel, Tijeras.\n- En esta versión, tienes cinco opciones en lugar de tres: Piedra, Papel, Tijeras, Lagarto, Spock.\n- Las reglas son las siguientes:\n- La piedra aplasta las tijeras y aplasta al lagarto.\n- Las tijeras cortan el papel y decapitan al lagarto.\n- El papel envuelve la piedra y desaprueba a Spock.\n- El lagarto come el papel y envenena a Spock.\n- Spock aplasta las tijeras y desintegra la piedra.\n- Tienes tres intentos para jugar.\n- Después de tres intentos fallidos, el juego termina.\n- ¡Que gane el mejor!\n\n¡Buena suerte!")    
def contador():
    global name,contadorUser,contadorCpu
    if contadorUser>contadorCpu:
        winner=f"El ganador es el Jugador {name}"
    elif contadorCpu>contadorUser:
        winner=f"El ganador es la CPU"
    else:
        winner="Es un Empate"
    return winner
def winner(p1,p2):
    global contadorUser,contadorCpu
    if p1=='Tijeras ✂️' and p2=='Papel 📄':
        winner="Las tijeras cortan el papel\nGana jugador "
        contadorUser+=1
    elif p1=='Papel 📄' and p2=='Piedra 🗿':
        winner="El papel envuelve la piedra\nGana jugador  "
        contadorUser+=1 
    elif p1=='Piedra 🗿' and p2=='Lagarto 🦎':
        winner="La piedra aplasta al lagarto\nGana jugador  "
        contadorUser+=1
    elif p1=='Lagarto 🦎' and p2=='Spock 🖖':
        winner="El lagarto envenena a Spock\nGana jugador  "
        contadorUser+=1
    elif p1=='Spock 🖖' and p2=='Tijeras ✂️':
        winner="Spock aplasta las tijeras\nGana jugador  "
        contadorUser+=1
    elif p1=='Tijeras ✂️' and p2=='Lagarto 🦎':
        winner="Las tijeras decapitan al lagarto\nGana jugador  "
        contadorUser+=1
    elif p1=='Lagarto 🦎' and p2=='Papel 📄':
        winner="El lagarto devora el papel\nGana jugador  "
        contadorUser+=1
    elif p1=='Papel 📄' and p2=='Spock 🖖':
        winner="el papel desaprueba a Spock\nGana jugador  "
        contadorUser+=1
    elif p1=='Spock 🖖' and p2=='Piedra 🗿':
        winner="Spock desintegra la piedra\nGana jugador  "
        contadorUser+=1
    elif p1=='Piedra 🗿' and p2=='Tijeras ✂️':
        winner="La piedra aplasta las tijeras\nGana jugador"  
        contadorUser+=1
    elif p2=='Tijeras ✂️' and p1=='Papel 📄':
        winner="Las tijeras cortan el papel\nGana CPU "
        contadorCpu+=1
    elif p2=='Papel 📄' and p1=='Piedra 🗿':
        winner="El papel envuelve la piedra\nGana CPU  "
        contadorCpu+=1
    elif p2=='Piedra 🗿' and p1=='Lagarto 🦎':
        winner="La piedra aplasta al lagarto\nGana CPU  "
        contadorCpu+=1
    elif p2=='Lagarto 🦎' and p1=='Spock 🖖':
        winner="El lagarto envenena a Spock\nGana CPU  "
        contadorCpu+=1
    elif p2=='Spock 🖖' and p1=='Tijeras ✂️':
        winner="Spock aplasta las tijeras\nGana CPU  "
        contadorCpu+=1
    elif p2=='Tijeras ✂️' and p1=='Lagarto 🦎':
        winner="Las tijeras decapitan al lagarto\nGana CPU  "
        contadorCpu+=1
    elif p2=='Lagarto 🦎' and p1=='Papel 📄':
        winner="El lagarto devora el papel\nGana CPU  "
        contadorCpu+=1
    elif p2=='Papel 📄' and p1=='Spock 🖖':
        winner="el papel desaprueba a Spock\nGana CPU  "
        contadorCpu+=1
    elif p2=='Spock 🖖' and p1=='Piedra 🗿':
        winner="Spock desintegra la piedra\nGana CPU  "
        contadorCpu+=1
    elif p2=='Piedra 🗿' and p1=='Tijeras ✂️':
        winner="La piedra aplasta las tijeras\nGana CPU" 
        contadorCpu+=1
    elif p2==p1:
        winner="Es un Empate"
    else:
        winner="OPCION INVALIDA , SELECCIONA LA OPCION INDICADA DEL MENU"
    return winner
def cpu():
    azar=random.randint(0,4)
    selectionCpu=options[azar]
    return selectionCpu
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.01)
def menu(n):
    animated_text(f"Hola @{n}\n👋¡Bienvenido al juego de papel, piedra, tijeras, lagarto, Spock!👋\n\n¿Listo para jugar? Elige una de las siguientes opciones:\n1️⃣ Papel 📄\n2️⃣ Piedra 🗿\n3️⃣ Tijeras ✂️\n4️⃣ Lagarto 🦎\n5️⃣ Spock 🖖\nPara jugar, simplemente escribe el número correspondiente a tu elección. ¡Que gane el mejor!")
def user_selection(select):
    if 0< select <= len(options):
        selection=options[select-1]
    else:
        selection="Option Not Found"
    return selection
def only_options():
    animated_text(f"Elige una de las siguientes opciones:\n1️⃣ Papel 📄\n2️⃣ Piedra 🗿\n3️⃣ Tijeras ✂️\n4️⃣ Lagarto 🦎\n5️⃣ Spock 🖖\nPara jugar")


os.system('cls')
reglas()
name=input("\n\nCual es tu nombre:").capitalize()
os.system('cls')

intentos=3
pase=True
menu(name)
while pase==True:
    print("\n\n")
    userOption=int(input("\nEscriba la opcion :  "))
    os.system('cls')


    animated_text("Usted Ah elegido : ")
    electionUser=user_selection(userOption)
    print(electionUser)


    animated_text("\nCPU Ah elegido : ")
    electionCpu=cpu()
    print(electionCpu)

    print("\n")
    print(winner(electionUser,electionCpu))
    print("\n\n")
    only_options()
    intentos-=1
    if intentos==0:
        pase=False
print("\n\n\n")
print(f"La tabla de puntuaciones quedo asi\n\n{name}:{contadorUser}\nCPU:{contadorCpu}\n\nPor lo tanto {contador()}")











