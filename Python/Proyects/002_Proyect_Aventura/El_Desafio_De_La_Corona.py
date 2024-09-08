import os,random,time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
'======== Armas ======='
daño_espada=30
daño_arco=20
vara_Magica=40

'======= Defensa ======='
puntos_vida=100
defensa_escudo=25
defensa_armadura=15

'======== Estadisticas reales ========'
daño_personaje=1
defensa_personaje=1
vida=1
mensaje_despesida='''
    
                                    ███╗░░░███╗██╗░░░██╗░█████╗░██╗░░██╗░█████╗░░██████╗  
                                    ████╗░████║██║░░░██║██╔══██╗██║░░██║██╔══██╗██╔════╝  
                                    ██╔████╔██║██║░░░██║██║░░╚═╝███████║███████║╚█████╗░  
                                    ██║╚██╔╝██║██║░░░██║██║░░██╗██╔══██║██╔══██║░╚═══██╗  
                                    ██║░╚═╝░██║╚██████╔╝╚█████╔╝██║░░██║██║░░██║██████╔╝  
                                    ╚═╝░░░░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  

                                    ░██████╗░██████╗░░█████╗░░█████╗░██╗░█████╗░░██████╗
                                    ██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔════╝
                                    ██║░░██╗░██████╔╝███████║██║░░╚═╝██║███████║╚█████╗░
                                    ██║░░╚██╗██╔══██╗██╔══██║██║░░██╗██║██╔══██║░╚═══██╗
                                    ╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║██║░░██║██████╔╝
                                    ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░

                                                ██████╗░░█████╗░██████╗░  
                                                ██╔══██╗██╔══██╗██╔══██╗  
                                                ██████╔╝██║░░██║██████╔╝  
                                                ██╔═══╝░██║░░██║██╔══██╗  
                                                ██║░░░░░╚█████╔╝██║░░██║  
                                                ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝  

                                        ░░░░░██╗██╗░░░██╗░██████╗░░█████╗░██████╗░
                                        ░░░░░██║██║░░░██║██╔════╝░██╔══██╗██╔══██╗
                                        ░░░░░██║██║░░░██║██║░░██╗░███████║██████╔╝
                                        ██╗░░██║██║░░░██║██║░░╚██╗██╔══██║██╔══██╗
                                        ╚█████╔╝╚██████╔╝╚██████╔╝██║░░██║██║░░██║
                                        ░╚════╝░░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
                ⲏⲉⲥⲏⲟ ⲥⲟⲛ ⲁⲙⲟꞅ ⲣⲟꞅ Ⲃⲟⲁⲧ ⲥⲟⲇⲉ


                𝗣𝗲𝗿𝗳𝗶𝗹 𝗱𝗲 𝗰𝗼𝗱𝗲𝗱𝗲𝘅: https://www.codedex.io/@boatcode40411898 
                𝗣𝗲𝗿𝗳𝗶𝗹 𝗱𝗲 𝗚𝗶𝘁𝗵𝘂𝗯 : https://github.com/BoatCode404                              
    '''
'===== Panel de bienvenida ======='
portada='''



                        ███████╗██╗░░░░░  ██████╗░███████╗░██████╗░█████╗░███████╗██╗░█████╗░  ██████╗░███████╗
                        ██╔════╝██║░░░░░  ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██║██╔══██╗  ██╔══██╗██╔════╝
                        █████╗░░██║░░░░░  ██║░░██║█████╗░░╚█████╗░███████║█████╗░░██║██║░░██║  ██║░░██║█████╗░░
                        ██╔══╝░░██║░░░░░  ██║░░██║██╔══╝░░░╚═══██╗██╔══██║██╔══╝░░██║██║░░██║  ██║░░██║██╔══╝░░
                        ███████╗███████╗  ██████╔╝███████╗██████╔╝██║░░██║██║░░░░░██║╚█████╔╝  ██████╔╝███████╗
                        ╚══════╝╚══════╝  ╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░  ╚═════╝░╚══════╝

                                ██╗░░░░░░█████╗░  ░█████╗░░█████╗░██████╗░░█████╗░███╗░░██╗░█████╗░
                                ██║░░░░░██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
                                ██║░░░░░███████║  ██║░░╚═╝██║░░██║██████╔╝██║░░██║██╔██╗██║███████║
                                ██║░░░░░██╔══██║  ██║░░██╗██║░░██║██╔══██╗██║░░██║██║╚████║██╔══██║
                                ███████╗██║░░██║  ╚█████╔╝╚█████╔╝██║░░██║╚█████╔╝██║░╚███║██║░░██║
                                ╚══════╝╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝

                                            ██████╗░███████╗██████╗░██████╗░██╗██████╗░░█████╗░
                                            ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗
                                            ██████╔╝█████╗░░██████╔╝██║░░██║██║██║░░██║███████║
                                            ██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║██║░░██║██╔══██║
                                            ██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝██║░░██║
                                            ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝
                ᴴᵉᶜʰᵒ ᵖᵒʳ ᴮᵒᵃᵗᶜᵒᵈᵉ
    
'''
print(portada)
animated_text('cual es tu nickname?\nEscribe aca: ')
name_player=input()
bienvenida=f'''
¡Bienvenido/a a el Desafío de la Corona Perdida  @{name_player}
En este emocionante juego de rol, te convertirás en un valiente héroe en una misión épica para rescatar a la princesa y derrotar a los malvados NPC que la mantienen prisionera. Tendrás la oportunidad de seleccionar entre tres valientes personajes.

¿Estás listo/a para enfrentar peligros y desafíos? ¡Entonces prepárate para la aventura de tu vida! ¡La princesa te necesita!

Selecciona tu personaje y adéntrate en el mundo de El Rescate de la Princesa. 


¡Que la suerte esté de tu lado, héroe @{name_player}
'''
print("\n\n")
animated_text(bienvenida)
tecla=input('<-------------PRESIONA UNA TECLA PARA CONTINUAR----------------> ')
os.system('cls')

'===== Seleccionar un personaje ============'

animated_text(f'Hola de nuevo  @{name_player}\nRecuerda que basta con escribir el nombre del personaje para elegirlo\n\n')
animated_text('Guerrero\nNombre: Raoul Espada de la Aurora\n')
print('Descripción: Raoul es un guerrero audaz y decidido, conocido por su valentía en el campo de batalla. Con su imponente espada de la aurora, Raoul protege a los indefensos y lucha por la justicia. Su fuerza y determinación son inigualables, y siempre está listo para enfrentarse a cualquier desafío que se le presente.\n\n\n')
animated_text('Arquero\nNombre: Lila Flecha Veloz\n')
print('Descripción: Lila es una arquera ágil y astuta, cuya destreza con el arco es incomparable. Con su rápida puntería y sus flechas certeras, Lila es capaz de derrotar a sus enemigos desde la distancia antes de que se den cuenta de su presencia. Sigilosa y decidida, es una aliada indispensable en cualquier batalla.\n\n\n')
animated_text('Mago\nNombre\nOrion Hechicero del Cielo\n')
print('Descripción:Orion es un poderoso mago cuyo dominio de la magia es legendario.Con su bastón mágico en mano, es capaz de controlar los elementos a su antojo y desatar poderosos hechizos sobre sus enemigos.Sabio y astuto,Orion utiliza su vasto conocimiento de la magia para proteger a sus compañeros y derrotar a cualquier amenaza que se interponga en su camino.\n\n\n')

'=========Control de Flujo con While ============='
select_character=input('Con cual personaje vas a jugar hoy?\nEscriba aca el nombre:').lower()
os.system('cls')

while select_character!='orion' and select_character!='lila' and select_character!='raoul':
    select_character=input('Con cual personaje vas a jugar hoy?\nRaoul,Orion O Lila \nEscriba aca el nombre:').lower()
    os.system('cls')
if select_character=='raoul':
    vida+=puntos_vida-1
    daño_personaje+=daño_espada
    defensa_personaje+=defensa_escudo
    tabla_estadisticas=f'\nHola @{name_player}\nHas escogido a Raoul Espada de la Aurora\n\nSus estadisticas son\n\nDaño:{daño_personaje}\nDefensa:{defensa_personaje}\nPuntos de Vida : {vida}\n'
    print(tabla_estadisticas)
elif select_character=='lila':
    vida+=puntos_vida-1
    daño_personaje+=daño_arco
    defensa_personaje+=defensa_armadura
    tabla_estadisticas=f'\nHola @{name_player}\nHas escogido Lila Flecha Veloz \n\nSus estadisticas son\n\nDaño:{daño_personaje}\nDefensa:{defensa_personaje}\nPuntos de Vida : {vida}\n'
    print(tabla_estadisticas)
elif select_character=='orion':
    vida+=puntos_vida-1
    daño_personaje+=vara_Magica
    tabla_estadisticas=f'\nHola @{name_player}\nHas escogido Orion Hechicero del Cielo \n\nSus estadisticas son\n\nDaño:{daño_personaje}\nDefensa:{defensa_personaje}\nPuntos de Vida : {vida}\n'
    print(tabla_estadisticas)

'==================== INICIO =================================='
dado1=random.randint(2,6)
dado2=random.randint(2,6)
tirada_dado1=input('\n\n\nPara empezar esta emocionante aventura, necesitarás sacar un número par\n\n\n¡Presiona una tecla para lanzar los dados!\n')
print(f'\nLos Dados Marcaron: {dado1} & {dado2}\n')
while dado1!=dado2:
    dado1=random.randint(2,6)
    dado2=random.randint(2,6)
    tirada_dado1=input('Necesitas sacar un numero par\n')
    os.system('cls')
    print(f'\nLos Dados Marcaron: {dado1} & {dado2}\n')
'============Seleccion de caminos============'
caminos='''
!Felicitaciones has podido salir de la base ese es el primer paso para esta gran aventura que te aguarda primero que todo dejame decirte que para llegar al castillo tenemos 3 formas de llegar a continucacion una breve descripcion para que escojas cual de ellas sera tu ruta 




Camino del Bosque Tenebroso:
Este camino te lleva a través de un oscuro y misterioso bosque, lleno de árboles retorcidos y sombras amenazantes. Deberás enfrentarte a criaturas de la oscuridad, como lobos fantasmales y arañas gigantes, mientras te abres paso a través de la maleza espesa y los senderos ocultos. Utiliza antorchas para iluminar tu camino y mantener a raya a las criaturas de la noche mientras te acercas al castillo.



Camino del Lago Pantanoso:
Opta por un camino que te lleva a través de un oscuro y peligroso lago pantanoso. El aire está lleno de niebla espesa y el agua está infestada de criaturas acuáticas, como caimanes y serpientes venenosas. Deberás ser cuidadoso/a al navegar por los pantanos y encontrar el camino seguro a través de la niebla para llegar al castillo.



        
Camino de la Selva Salvaje:
Toma el camino a través de una densa selva tropical, llena de vegetación exuberante y peligros ocultos. Enfrenta desafíos como plantas carnívoras,enredaderas traicioneras y depredadores acechantes mientras te abres camino a través de la jungla.Utiliza tu ingenio para navegar por el laberinto de la selva y llegar al castillo en lo más profundo del bosque.



para continuar escribe la palabra  Bosque,Lago o Selva segun lo que escogiste
'''
bosque_tenebroso_parte1='''

                                                                        ░░░░░░░░▌░░░░░░░▐
                                                                        ░░░░█░░▄▌░░░░▌░░░█░░░▄▄
                                                                        ░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄
                                                                        ░░░░░▐█░░░░░░░▌░▄█▀░░░▀█
                                                                        ░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░
                                                                        ░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░
                                                                        ▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░
                                                                        █░░░▐░░░██░░░░░█░░▄░█▀░░
                                                                        ▐░░░█░░░▐█░░░░░░░░▌▀░░░░   
                                                                        ░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░
                                                                        ▄▄▀▄█░░░░██░▄█▀░█▄▄░▐▄▄░
                                                                        ░░░░▀█▄░▄███░░░░░░░░░░░░
                                                                        ░░░░░░█████░░░░░░░░░░░░░
                                                                        ░░░░░░░▐███░░░░░░░░░░░░░
                                                                        ░░░░░░░▐███░░░░░░░░░░░░░
                                                                        ░░░░░░░▐████░░░░░░░░░░░░
                                                                        ░░▒▒▒▒▒█████▒▒░░░░░░░░░░
                                                                        ▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒
                                                                        ▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒
                                                                        █▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒
                                                                        乃ㄖ丂Ɋㄩ🝗 ㄒ🝗𝓝🝗⻏尺ㄖ丂ㄖ

Adentrarse en el bosque tenebroso era una tarea que solo los más valientes se atrevían a emprender.Los árboles retorcidos y cubiertos de musgo parecían susurrar secretos antiguos mientras el viento susurraba entre las hojas.El suelo estaba cubierto por una densa capa de hojas marchitas que crujían bajo cada paso.

A medida que avanzabas por el bosque, te dabas cuenta de que no estabas solo/a.Ojos brillantes te observaban desde la oscuridad,y los sonidos de la noche te mantenían alerta.Lobos fantasmales acechaban entre los árboles,mientras que arañas gigantes tejían sus telarañas entre las ramas.


Mientras avanzas por el bosque tenebroso,te encuentras cara a cara con una criatura imponente y aterradora.
El Guardián del Bosque. Esta criatura es una fusión oscura de árbol y bestia,con enormes ramas retorcidas que se agitan en el aire y ojos brillantes que te observan con malicia desde la oscuridad.


Solo con valor y determinación podrás derrotar al Guardián del Bosque y continuar tu camino hacia el castillo para rescatar a la princesa.
'''

bosque_tenebroso_parte2='''


                                                            ██╗██╗░░░░░░█████╗░  ██╗░░██╗░█████╗░░██████╗
                                                            ██║██║░░░░░██╔══██╗  ██║░░██║██╔══██╗██╔════╝
                                                            ██║██║░░░░░██║░░██║  ███████║███████║╚█████╗░
                                                            ╚═╝██║░░░░░██║░░██║  ██╔══██║██╔══██║░╚═══██╗
                                                            ██╗███████╗╚█████╔╝  ██║░░██║██║░░██║██████╔╝
                                                            ╚═╝╚══════╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

                                        ░█████╗░░█████╗░███╗░░██╗░██████╗███████╗░██████╗░██╗░░░██╗██╗██████╗░░█████╗░██╗
                                        ██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝██╔════╝░██║░░░██║██║██╔══██╗██╔══██╗██║
                                        ██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░█████╗░░██║░░██╗░██║░░░██║██║██║░░██║██║░░██║██║
                                        ██║░░██╗██║░░██║██║╚████║░╚═══██╗██╔══╝░░██║░░╚██╗██║░░░██║██║██║░░██║██║░░██║╚═╝
                                        ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝███████╗╚██████╔╝╚██████╔╝██║██████╔╝╚█████╔╝██╗
                                        ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝░╚═════╝░░╚═════╝░╚═╝╚═════╝░░╚════╝░╚═╝

¡Felicidades! Has derrotado al Guardián del Bosque!


Con una antorcha en una mano y tu arma en la otra, te adentraste más y más en el bosque, enfrentándote a cada desafío con valentía y determinación. El camino era difícil y peligroso, pero sabías que la princesa te necesitaba, y no dejarías que nada te detuviera.

Finalmente, después de horas de caminar, llegaste al borde del bosque, donde se alzaba imponente el castillo. La luz de la luna brillaba sobre sus torres, y sabías que tu misión estaba a punto de llegar a su fin. Con el corazón lleno de determinación, te preparaste para enfrentarte a los desafíos que te esperaban dentro del castillo, listo/a para rescatar a la princesa y poner fin a la oscuridad que acechaba en el bosque tenebroso.
'''



minijuegos_dados='''
Para vencer a este jefe, tendrás que enfrentarte a un desafío. Consiste en tirar un dado y sacar un número más alto que el enemigo. Si obtienes el número más alto, le quitarás un 15% de su vida, dependiendo de su armadura. Lo mismo te ocurrirá a ti si tu oponente saca un número más alto. ¡Buena suerte!  
'''



minijuegos_adivinazas='''
¡Excelente! Has pasado la primera prueba y tienes al enemigo acorralado, o él a ti, pero aún hay esperanza. Si ese es el caso, ahora rematémoslo. Pero primero, un juego de adivinanzas. Si adivinas el número antes que tu oponente, le quitarás el 50% de su vida. ¡Buena suerte!  
'''


mensaje1_lago='''

                                                                        ─────▄████▀█▄
                                                                        ───▄█████████████████▄
                                                                        ─▄█████.▼.▼.▼.▼.▼.▼▼▼▼
                                                                        ▄███████▄.▲.▲▲▲▲▲▲▲▲
                                                                        ████████████████████▀▀
                                                                        ㇄闩Ꮆㄖ 七🝗𝓝🝗⻏尺ㄖ丂ㄖ


Optas por un camino que te lleva a través de un oscuro y peligroso lago pantanoso. El aire está lleno de niebla espesa y el agua está infestada de criaturas acuáticas, como caimanes y serpientes venenosas. Deberás ser cuidadoso/a al navegar por los pantanos y encontrar el camino seguro a través de la niebla para llegar al castillo.

Adentrarse en el lago pantanoso era una tarea que solo los más valientes se atrevían a emprender. La niebla espesa cubría la superficie del agua, haciendo que la visibilidad fuera casi nula. Criaturas acuáticas acechaban bajo la superficie, listas para atacar en cualquier momento.

A medida que avanzas, el agua se vuelve más profunda y las criaturas más peligrosas. De repente, emergiendo de las aguas turbias, te encuentras cara a cara con una criatura imponente y aterradora. El Azote del Pantano. Esta criatura es una masa oscura y viscosa, con ojos brillantes que te observan con malicia desde la oscuridad del agua.

Solo con valor y determinación podrás derrotar al Azote del Pantano y continuar tu camino hacia el castillo para rescatar a la princesa.
'''



mensaje2_lago='''


                                                            ██╗██╗░░░░░░█████╗░  ██╗░░██╗░█████╗░░██████╗
                                                            ██║██║░░░░░██╔══██╗  ██║░░██║██╔══██╗██╔════╝
                                                            ██║██║░░░░░██║░░██║  ███████║███████║╚█████╗░
                                                            ╚═╝██║░░░░░██║░░██║  ██╔══██║██╔══██║░╚═══██╗
                                                            ██╗███████╗╚█████╔╝  ██║░░██║██║░░██║██████╔╝
                                                            ╚═╝╚══════╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

                                        ░█████╗░░█████╗░███╗░░██╗░██████╗███████╗░██████╗░██╗░░░██╗██╗██████╗░░█████╗░██╗
                                        ██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝██╔════╝░██║░░░██║██║██╔══██╗██╔══██╗██║
                                        ██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░█████╗░░██║░░██╗░██║░░░██║██║██║░░██║██║░░██║██║
                                        ██║░░██╗██║░░██║██║╚████║░╚═══██╗██╔══╝░░██║░░╚██╗██║░░░██║██║██║░░██║██║░░██║╚═╝
                                        ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝███████╗╚██████╔╝╚██████╔╝██║██████╔╝╚█████╔╝██╗
                                        ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝░╚═════╝░░╚═════╝░╚═╝╚═════╝░░╚════╝░╚═╝
¡Felicidades! Has derrotado al Azote del Pantano!

Después de una intensa y ardua batalla, logras derrotar al Azote del Pantano. Con la criatura vencida, continúas tu camino hacia el castillo para rescatar a la princesa.

Finalmente, llegas al castillo justo a tiempo para salvar a la princesa de las garras del malvado hechicero. Con la princesa a salvo, el reino entero te agradece por tu valentía y determinación.

¡Has completado tu misión con éxito y te conviertes en el héroe del reino!
'''



mensaje1_selva='''

                                                                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                                    ░░░░░████░░░░░░░░░░░░░░░████░░░░░
                                                                    ░░░░███░░░░░░░░░░░░░░░░░░░███░░░░
                                                                    ░░░███░░░░░░░░░░░░░░░░░░░░░███░░░
                                                                    ░░███░░░░░░░░░░░░░░░░░░░░░░░███░░
                                                                    ░███░░░░░░░░░░░░░░░░░░░░░░░░░███░
                                                                    ████░░░░░░░░░░░░░░░░░░░░░░░░░████
                                                                    ████░░░░░░░░░░░░░░░░░░░░░░░░░████
                                                                    ██████░░░░░░░███████░░░░░░░██████
                                                                    █████████████████████████████████
                                                                    █████████████████████████████████
                                                                    ░███████████████████████████████░
                                                                    ░░████░███████████████████░████░░
                                                                    ░░░░░░░███▀███████████▀███░░░░░░░
                                                                    ░░░░░░████──▀███████▀──████░░░░░░
                                                                    ░░░░░░█████───█████───█████░░░░░░
                                                                    ░░░░░░███████▄█████▄███████░░░░░░
                                                                    ░░░░░░░███████████████████░░░░░░░
                                                                    ░░░░░░░░█████████████████░░░░░░░░
                                                                    ░░░░░░░░░███████████████░░░░░░░░░
                                                                    ░░░░░░░░░░█████████████░░░░░░░░░░
                                                                    ░░░░░░░░░░░███████████░░░░░░░░░░░
                                                                    ░░░░░░░░░░███──▀▀▀──███░░░░░░░░░░
                                                                    ░░░░░░░░░░███─█████─███░░░░░░░░░░
                                                                    ░░░░░░░░░░░███─███─███░░░░░░░░░░░
                                                                    ░░░░░░░░░░░░█████████░░░░░░░░░░░░
                                                                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                                    丂🝗㇄ᐯ闩 〸🝗𝓝🝗⻏尺ㄖ丂闩

Adentrarse en la selva tropical era una tarea que solo los más valientes se atrevían a emprender. Los árboles gigantes se alzaban sobre ti, bloqueando gran parte de la luz del sol y sumiendo la selva en una penumbra constante. El suelo estaba cubierto por una gruesa capa de hojas y ramas, ocultando peligrosas trampas naturales.

A medida que avanzas, el sonido de la jungla se vuelve más intenso. Los chillidos de los monos y el crujir de las ramas te mantienen alerta, mientras evitas las emboscadas de las serpientes y los depredadores acechantes.

Mientras avanzas por la selva, te encuentras cara a cara con una criatura imponente y aterradora. El Vigía de la Selva. Esta criatura es una masa oscura y viscosa, con ojos brillantes que te observan con malicia desde lo más profundo de la jungla.

Solo con valor y determinación podrás derrotar al Vigía de la Selva y continuar tu camino hacia el castillo para rescatar a la princesa.
'''



mensaje2_selva='''


                                                            ██╗██╗░░░░░░█████╗░  ██╗░░██╗░█████╗░░██████╗
                                                            ██║██║░░░░░██╔══██╗  ██║░░██║██╔══██╗██╔════╝
                                                            ██║██║░░░░░██║░░██║  ███████║███████║╚█████╗░
                                                            ╚═╝██║░░░░░██║░░██║  ██╔══██║██╔══██║░╚═══██╗
                                                            ██╗███████╗╚█████╔╝  ██║░░██║██║░░██║██████╔╝
                                                            ╚═╝╚══════╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

                                        ░█████╗░░█████╗░███╗░░██╗░██████╗███████╗░██████╗░██╗░░░██╗██╗██████╗░░█████╗░██╗
                                        ██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝██╔════╝░██║░░░██║██║██╔══██╗██╔══██╗██║
                                        ██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░█████╗░░██║░░██╗░██║░░░██║██║██║░░██║██║░░██║██║
                                        ██║░░██╗██║░░██║██║╚████║░╚═══██╗██╔══╝░░██║░░╚██╗██║░░░██║██║██║░░██║██║░░██║╚═╝
                                        ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝███████╗╚██████╔╝╚██████╔╝██║██████╔╝╚█████╔╝██╗
                                        ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝░╚═════╝░░╚═════╝░╚═╝╚═════╝░░╚════╝░╚═╝

¡Felicidades! Has derrotado al Vigia de la Selva!

Después de una intensa y ardua batalla, logras derrotar al Vigía de la Selva. Con la criatura vencida, continúas tu camino hacia el castillo para rescatar a la princesa.

Finalmente, llegas al castillo justo a tiempo para salvar a la princesa de las garras del malvado hechicero. Con la princesa a salvo, el reino entero te agradece por tu valentía y determinación.

¡Has completado tu misión con éxito y te conviertes en el héroe del reino!
'''


os.system('cls')
print(caminos)

respuesta_caminos=input('\n\nEscriba El nombre del camino aqui:').lower()
while respuesta_caminos!='bosque' and respuesta_caminos!='lago' and respuesta_caminos!='selva':
    respuesta_caminos=input('\n\nRecuerda escribir Bosque,Lago o Selva\nEscriba El nombre del camino aqui:').lower()
if respuesta_caminos=='bosque':
    os.system('cls')
    print(bosque_tenebroso_parte1)
    daño_guardian_bosque=30
    defensa_guardian_bosque=50
    puntos_vida_guardian=120
    dado_guardian_bosque=random.randint(1,6)
    dado_jugador_bosque=random.randint(1,6)
    animated_text(minijuegos_dados)
    while puntos_vida_guardian>50 and puntos_vida>50:
        dado_guardian_bosque=random.randint(1,6)
        dado_jugador_bosque=random.randint(1,6)
        tirada_dados_bosque=input("\n\n<----------------PRESIONE UNA TECLA PARA TIRAR DADOS------------------>: \n")
        os.system('cls')
        print(f'El dado de : @{name_player}\nMarco : {dado_jugador_bosque}\n\nEl dado del Guardian de bosque\nMarco:{dado_guardian_bosque}')
        if dado_jugador_bosque>dado_guardian_bosque:
            golpe=puntos_vida_guardian*15//100
            vida_final=puntos_vida_guardian-golpe
            puntos_vida_guardian=vida_final
            print(f'\n\n!Excelente! @{name_player} has golpeado al Guardian\nSu vida ahora es: {puntos_vida_guardian}')
        elif dado_guardian_bosque>dado_jugador_bosque:
            golpe=puntos_vida*15//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Guardian del Bosque te ha golpeado\nTu vida ahora es : {puntos_vida}')
        else:
            print(f"\nLos dados muestran numeros iguales\n\n!Es un empate!\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Guardian del Bosque se mantiene en : {puntos_vida_guardian} ")
    os.system('cls')
    print(f'La vida de {name_player} es : {puntos_vida}\nLa vida del Guardian del Bosque es : {puntos_vida_guardian}\n\n')
    animated_text(f'\n{minijuegos_adivinazas}')
    numero_secreto=2
    dado_guardian_bosque=random.randint(1,4)
    dado_jugador_bosque=random.randint(1,4)
    while puntos_vida_guardian>1:
        numero_secreto=2
        dado_guardian_bosque=random.randint(1,4)
        dado_jugador_bosque=random.randint(1,4)
        tirada_dados_bosque=input("\n\n<----------------PRESIONE UNA TECLA PARA TIRAR DADOS------------------>: \n")
        os.system('cls')
        print(f'El dado de : @{name_player}\nMarco : {dado_jugador_bosque}\n\nEl dado del Guardian de bosque\nMarco:{dado_guardian_bosque}')
        if dado_jugador_bosque==numero_secreto and dado_guardian_bosque==numero_secreto:
            print(f'\nLos dados Adivinaron el numero \n\n!Es un empate!\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Guardian del Bosque se mantiene en : {puntos_vida_guardian} ")')
        elif puntos_vida==1:
            os.system('cls')
            print(f"¡Game over! El Guardián del Bosque ha derrotado a @{name_player}.")
            exit()
        elif dado_jugador_bosque==numero_secreto:
            golpe=puntos_vida_guardian*50//100
            vida_final=puntos_vida_guardian-golpe
            puntos_vida_guardian=vida_final
            print(f'\n!Excelente! @{name_player} has golpeado al Guardian\nSu vida ahora es: {puntos_vida_guardian}')
        elif dado_guardian_bosque==numero_secreto:
            golpe=puntos_vida*50//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Guardian del Bosque te ha  golpeado\nTu vida ahora es : {puntos_vida}')
        elif dado_guardian_bosque!=numero_secreto and dado_jugador_bosque!=numero_secreto:
            print(f'\n\nNinguno Adivino el numero\nAsi que {name_player} & El Guardian del Bosque no atacan\n\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Guardian del Bosque se mantiene en : {puntos_vida_guardian} ')
    os.system('cls')
    print(bosque_tenebroso_parte2)
    os.system('cls')
    print(mensaje_despesida)
elif respuesta_caminos=='lago':
    os.system('cls')
    print(mensaje1_lago)
    daño_azote_pantano=30
    defensa_azote_pantano=50
    puntos_vida_azote=150
    dado_azote_pantano=random.randint(4,9)
    dado_jugador_pantano=random.randint(4,9)
    animated_text(minijuegos_dados)
    while puntos_vida_azote>50 and puntos_vida>50:
        dado_azote_pantano=random.randint(4,9)
        dado_jugador_pantano=random.randint(4,9)
        tirada_dados_pantano=input("\n\n<----------------PRESIONE UNA TECLA PARA TIRAR DADOS------------------>: \n")
        os.system('cls')
        print(f'El dado de : @{name_player}\nMarco : {dado_jugador_pantano}\n\nEl dado del Azote del Pantano\nMarco:{dado_azote_pantano}')
        if dado_jugador_pantano>dado_azote_pantano:
            golpe=puntos_vida_azote*15//100
            vida_final=puntos_vida_azote-golpe
            puntos_vida_azote=vida_final
            print(f'\n\n!Excelente! @{name_player} has golpeado al Azote del Pantano \nSu vida ahora es: {puntos_vida_azote}')
        elif dado_azote_pantano>dado_jugador_pantano:
            golpe=puntos_vida*15//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Azote del Pantano te ha golpeado\nTu vida ahora es : {puntos_vida}')
        else:
            print(f"\nLos dados muestran numeros iguales\n\n!Es un empate!\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Azote del Pantano se mantiene en : {puntos_vida_azote} ")
    os.system('cls')
    print(f'La vida de {name_player} es : {puntos_vida}\nLa vida del Azote del Pantano es : {puntos_vida_azote}\n\n')
    animated_text(f'\n{minijuegos_adivinazas}')
    numero_secreto=14
    dado_azote_pantano=random.randint(9,14)
    dado_jugador_pantano=random.randint(9,14)
    while puntos_vida_azote>1:
        numero_secreto=14
        dado_azote_pantano=random.randint(9,14)
        dado_jugador_pantano=random.randint(9,14)
        tirada_dados_pantano=input("\n\n<----------------PRESIONE UNA TECLA PARA TIRAR DADOS------------------>: \n")
        os.system('cls')
        print(f'El dado de : @{name_player}\nMarco : {dado_jugador_pantano}\n\nEl dado del Azote del Pantano\nMarco:{dado_azote_pantano}')
        if dado_jugador_pantano==numero_secreto and dado_azote_pantano==numero_secreto:
            print(f'\nLos dados Adivinaron el numero \n\n!Es un empate!\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Azote del Pantano se mantiene en : {puntos_vida_azote} ")')
        elif puntos_vida==1:
            os.system('cls')
            print(f"¡Game over! El Azote del Pantano ha derrotado a @{name_player}.")
            exit()
        elif dado_jugador_pantano==numero_secreto:
            golpe=puntos_vida_azote*50//100
            vida_final=puntos_vida_azote-golpe
            puntos_vida_azote=vida_final
            print(f'\n!Excelente! @{name_player} has golpeado al Azote del Pantano\nSu vida ahora es: {puntos_vida_azote}')
        elif dado_azote_pantano==numero_secreto:
            golpe=puntos_vida*50//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Guardian del Bosque te ha  golpeado\nTu vida ahora es : {puntos_vida}')
        elif dado_azote_pantano!=numero_secreto and dado_jugador_pantano!=numero_secreto:
            print(f'\n\nNinguno Adivino el numero\nAsi que {name_player} & El Azote del Pantano no atacan\n\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Azote del Pantano se mantiene en : {puntos_vida_azote} ')
    os.system('cls')
    print(mensaje2_lago)
    os.system('cls')
    print(mensaje_despesida)
elif respuesta_caminos=='selva':
    os.system('cls')
    print(mensaje1_selva)
    daño_vigia_selva=30
    defensa_vigia_selva=50
    puntos_vida_vigia=115
    dado_vigia_selva=random.randint(1,6)
    dado_jugador_selva=random.randint(1,6)
    animated_text(minijuegos_dados)
    while puntos_vida_vigia>50 and puntos_vida>50:
        dado_vigia_selva=random.randint(1,6)
        dado_jugador_selva=random.randint(1,6)
        tirada_dados_selva=input("\n\n<----------------PRESIONE UNA TECLA PARA TIRAR DADOS------------------>: \n")
        os.system('cls')
        print(f'El dado de : @{name_player}\nMarco : {dado_jugador_selva}\n\nEl dado del Vigia de la Selva \nMarco:{dado_vigia_selva}')
        if dado_jugador_selva>dado_vigia_selva:
            golpe=puntos_vida_vigia*15//100
            vida_final=puntos_vida_vigia-golpe
            puntos_vida_vigia=vida_final
            print(f'\n\n!Excelente! @{name_player} has golpeado al Vigia de la selva \nSu vida ahora es: {puntos_vida_vigia}')
        elif dado_vigia_selva>dado_jugador_selva:
            golpe=puntos_vida*15//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Vigia de la Selva te ha golpeado\nTu vida ahora es : {puntos_vida}')
        else:
            print(f"\nLos dados muestran numeros iguales\n\n!Es un empate!\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Vigia de la Selva se mantiene en : {puntos_vida_vigia} ")
    os.system('cls')
    print(f'La vida de {name_player} es : {puntos_vida}\nLa vida del Vigia de la Selva es : {puntos_vida_vigia}\n\n')
    animated_text(f'\n{minijuegos_adivinazas}')
    numero_secreto=24
    dado_vigia_selva=random.randint(18,24)
    dado_jugador_selva=random.randint(18,24)
    while puntos_vida_vigia>1:
        numero_secreto=24
        dado_vigia_selva=random.randint(18,24)
        dado_jugador_selva=random.randint(18,24)
        tirada_dados_selva=input("\n\n<----------------PRESIONE UNA TECLA PARA TIRAR DADOS------------------>: \n")
        os.system('cls')
        print(f'El dado de : @{name_player}\nMarco : {dado_jugador_selva}\n\nEl dado del Vigia del Pantano \nMarco:{dado_vigia_selva}')
        if dado_jugador_selva==numero_secreto and dado_vigia_selva==numero_secreto:
            print(f'\nLos dados Adivinaron el numero \n\n!Es un empate!\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del vigia de la Selva se mantiene en : {puntos_vida_vigia} ")')
        elif puntos_vida==1:
            os.system('cls')
            print(f"¡Game over! El Vigia de la Selva ha derrotado a @{name_player}.")
            exit()
        elif dado_jugador_selva==numero_secreto:
            golpe=puntos_vida_vigia*50//100
            vida_final=puntos_vida_vigia-golpe
            puntos_vida_vigia=vida_final
            print(f'\n!Excelente! @{name_player} has golpeado al vigia de la Selva\nSu vida ahora es: {puntos_vida_vigia}')
        elif dado_vigia_selva==numero_secreto:
            golpe=puntos_vida*50//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Vigia de la selva te ha  golpeado\nTu vida ahora es : {puntos_vida}')
        elif dado_vigia_selva!=numero_secreto and dado_jugador_selva!=numero_secreto:
            print(f'\n\nNinguno Adivino el numero\nAsi que {name_player} & El Vigia de la Selva no atacan\n\nLa vida de @{name_player} se mantiene en : {puntos_vida}\nLa vida del Vigia de la Selva se mantiene en : {puntos_vida_vigia} ')
    os.system('cls')
    print(mensaje2_selva)
    input("\n\n\n Presiona una tecla para continuar\n")
    os.system('cls')
    print(mensaje_despesida)