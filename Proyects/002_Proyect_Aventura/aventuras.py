import os,random,time
'======== instructions ========='
print('Los magos no llevan armadura pero sus daños son mas fuertes')

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


'===== Panel de bienvenida ======='
name_player=input('cual es tu nickname?\n')
bienvenida=f'''
¡Bienvenido/a a El Rescate de la Princesa @{name_player}
En este emocionante juego de rol, te convertirás en un valiente héroe en una misión épica para rescatar a la princesa y derrotar a los malvados NPC que la mantienen prisionera. Tendrás la oportunidad de seleccionar entre tres valientes personajes.

¿Estás listo/a para enfrentar peligros y desafíos? ¡Entonces prepárate para la aventura de tu vida! ¡La princesa te necesita!

Selecciona tu personaje y adéntrate en el mundo de El Rescate de la Princesa. ¡Que la suerte esté de tu lado, héroe @{name_player}
'''''
print(bienvenida,'\n')
tecla=input('Presiona una tecla para continuar y elegir tu personaje ')
os.system('cls')
'===== Seleccionar un personaje ============'

print(f'hola {name_player} Para escojer el personaje solo escribe su nombre \n')
print('Guerrero:\nNombre: Raoul Espada de la Aurora\n')
print('Descripción: Raoul es un guerrero audaz y decidido, conocido por su valentía en el campo de batalla. Con su imponente espada de la aurora, Raoul protege a los indefensos y lucha por la justicia. Su fuerza y determinación son inigualables, y siempre está listo para enfrentarse a cualquier desafío que se le presente.\n\n\n')
print('Arquero:\nNombre: Lila Flecha Veloz\n')
print('Descripción: Lila es una arquera ágil y astuta, cuya destreza con el arco es incomparable. Con su rápida puntería y sus flechas certeras, Lila es capaz de derrotar a sus enemigos desde la distancia antes de que se den cuenta de su presencia. Sigilosa y decidida, es una aliada indispensable en cualquier batalla.\n\n\n')
print('Mago:Nombre:\n Orion Hechicero del Cielo\n')
print('Descripción: Orion es un poderoso mago cuyo dominio de la magia es legendario. Con su bastón mágico en mano, es capaz de controlar los elementos a su antojo y desatar poderosos hechizos sobre sus enemigos. Sabio y astuto, Orion utiliza su vasto conocimiento de la magia para proteger a sus compañeros y derrotar a cualquier amenaza que se interponga en su camino.\n\n\n')

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
    tabla_estadisticas=f'\nHola Raoul Espada de la Aurora \n\nSus estadisticas para hoy son\n\nDaño:{daño_personaje}\nDefensa:{defensa_personaje}'
    print(tabla_estadisticas)
elif select_character=='lila':
    vida+=puntos_vida-1
    daño_personaje+=daño_arco
    defensa_personaje+=defensa_armadura
    tabla_estadisticas=f'\nHola Lila Flecha Veloz \n\nSus estadisticas para hoy son\n\nDaño:{daño_personaje}\nDefensa:{defensa_personaje}'
    print(tabla_estadisticas)
elif select_character=='orion':
    vida+=puntos_vida-1
    daño_personaje+=vara_Magica
    tabla_estadisticas=f'\nHola Orion Hechicero del Cielo \n\nSus estadisticas para hoy son\n\nDaño:{daño_personaje}\nDefensa:{defensa_personaje}'
    print(tabla_estadisticas)

'========= INICIO =================='
dado1=random.randint(1,6)
dado2=random.randint(1,6)

tecla=input('Presiona una tecla para continuar ')
os.system('cls')
tirada_dado1=input('Esto Empieza muy emeciononante ya que para poder empezar y salir de base necesitaras sacar un numero par\n\nPresiona una tecla para lanzar el primer dado Aqui :')
print(f'\nEl primer dado callo en : {dado1}\n')
tirada_dado2=input('Escribe una tecla aca para lanzar el dado2 Aqui : ')
print(f'\nEl segundo dado callo en : {dado2}')
os.system('cls')
while dado1!=dado2:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    tirada_dado1=input('\n\npara poder empezar y salir de base necesitaras sacar un numero par\n\nPresiona una tecla para lanzar el primer dado  Aqui :')
    print(f'\nEl primer dado callo en : {dado1}\n')
    tirada_dado2=input('Escribe una tecla aca para lanzar el dado2 Aqui : ')
    print(f'\nEl segundo dado callo en : {dado2}')
'============Seleccion de caminos============'
os.system('cls')
caminos='''
    !Felicitaciones has podido salir de la base ese es el primer paso para esta gran aventura que te aguarda primero que todo dejame decirte que para llegar al castillo tenemos 3 formas de llegar a continucacion una breve descripcion para que escojas cual de ellas sera tu ruta 


    Camino del Bosque Tenebroso:
    Este camino te lleva a través de un oscuro y misterioso bosque, lleno de árboles retorcidos y sombras amenazantes. Deberás enfrentarte a criaturas de la oscuridad, como lobos fantasmales y arañas gigantes, mientras te abres paso a través de la maleza espesa y los senderos ocultos. Utiliza antorchas para iluminar tu camino y mantener a raya a las criaturas de la noche mientras te acercas al castillo.

    Camino del Lago Pantanoso:
    Opta por un camino que te lleva a través de un oscuro y peligroso lago pantanoso. El aire está lleno de niebla espesa y el agua está infestada de criaturas acuáticas, como caimanes y serpientes venenosas. Deberás ser cuidadoso/a al navegar por los pantanos y encontrar el camino seguro a través de la niebla para llegar al castillo.
    
    Camino de la Selva Salvaje:
    Toma el camino a través de una densa selva tropical, llena de vegetación exuberante y peligros ocultos. Enfrenta desafíos como plantas carnívoras, enredaderas traicioneras y depredadores acechantes mientras te abres camino a través de la jungla. Utiliza tu ingenio para navegar por el laberinto de la selva y llegar al castillo en lo más profundo del bosque.

    para continuar escribre Bosque , Lago o Selva segun lo que escogiste
    '''''
bosque_tenebroso_parte1=''''
    Adentrarse en el bosque tenebroso era una tarea que solo los más valientes se atrevían a emprender. Los árboles retorcidos y cubiertos de musgo parecían susurrar secretos antiguos mientras el viento susurraba entre las hojas. El suelo estaba cubierto por una densa capa de hojas marchitas que crujían bajo cada paso.

    A medida que avanzabas por el bosque, te dabas cuenta de que no estabas solo/a. Ojos brillantes te observaban desde la oscuridad, y los sonidos de la noche te mantenían alerta. Lobos fantasmales acechaban entre los árboles, mientras que arañas gigantes tejían sus telarañas entre las ramas.



    Mientras avanzas por el bosque tenebroso, te encuentras cara a cara con una criatura imponente y aterradora: El Guardián del Bosque. Esta criatura es una fusión oscura de árbol y bestia, con enormes ramas retorcidas que se agitan en el aire y ojos brillantes que te observan con malicia desde la oscuridad.



    Solo con valor y determinación podrás derrotar al Guardián del Bosque y continuar tu camino hacia el castillo para rescatar a la princesa.


    '''''
bosque_tenebroso_parte2=''''
    Con una antorcha en una mano y tu arma en la otra, te adentraste más y más en el bosque, enfrentándote a cada desafío con valentía y determinación. El camino era difícil y peligroso, pero sabías que la princesa te necesitaba, y no dejarías que nada te detuviera.

    Finalmente, después de horas de caminar, llegaste al borde del bosque, donde se alzaba imponente el castillo. La luz de la luna brillaba sobre sus torres, y sabías que tu misión estaba a punto de llegar a su fin. Con el corazón lleno de determinación, te preparaste para enfrentarte a los desafíos que te esperaban dentro del castillo, listo/a para rescatar a la princesa y poner fin a la oscuridad que acechaba en el bosque tenebroso.
    '''''

minijuegos_dados='Para vencer este Boos tendras que enfrentarte a un desafio consiste en tirar un dado y sacar un numero mas alto que el enemigo , si sacas el numero mas alto le quitaras un 15 porciento de su vida dependiendo de su armadura , lo mismo te pasara a ti si tu oponente saca un numero mas alto suerte  '
minijuegos_adivinazas='Excelente has pasado la primera prueba y lo tenes bajo las cuerdas o el a ti pero todavia hay fe si ese es el caso ahora rematemoslo pero primero un juego de adivinazas si adivinas el numero primero que tu oponente le quitaras 50% de su vida '
print(caminos)

'<---------CAMINO DEL BOSQUE---------->'
respuesta_caminos=input('\n\nEscriba El nombre del camino aqui:').lower()
if respuesta_caminos=='bosque':
    print(bosque_tenebroso_parte1)
    daño_guardian_bosque=30
    defensa_guardian_bosque=50
    puntos_vida_guardian=120
    dado_guardian_bosque=random.randint(1,6)
    dado_jugador_bosque=random.randint(1,6)
    print(minijuegos_dados)
    while puntos_vida_guardian>50 and puntos_vida>50:
        dado_guardian_bosque=random.randint(1,6)
        dado_jugador_bosque=random.randint(1,6)
        tirada_dados_bosque=input("\n\nPRESIONE UNA TECLA PARA TIRAR DADOS: \n")
        os.system('cls')
        print(f'El dado callo en {dado_jugador_bosque} & El Guardian de bosque saco :{dado_guardian_bosque}')
        if dado_jugador_bosque>dado_guardian_bosque:
            golpe=puntos_vida_guardian*15//100
            vida_final=puntos_vida_guardian-golpe
            puntos_vida_guardian=vida_final
            print(f'\n\nExcelente lo has golpeado y esta es su vida {puntos_vida_guardian}')
        elif dado_guardian_bosque>dado_jugador_bosque:
            golpe=puntos_vida*15//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Guardian del bosque te ha  golpeado y esta es tu vida {puntos_vida}')
        else:
            print(f"\nEs un empate y la vida del jugador es : {puntos_vida} \nLa vida del Guardian del bosque es : {puntos_vida_guardian} ")
    print(minijuegos_adivinazas)
    numero_secreto=35
    dado_guardian_bosque=random.randint(1,50)
    dado_jugador_bosque=random.randint(1,50)
    print(puntos_vida_guardian)
    while puntos_vida_guardian>1:
        numero_secreto=7
        dado_guardian_bosque=random.randint(1,7)
        dado_jugador_bosque=random.randint(1,7)
        tirada_dados_bosque=input("\n\nPRESIONE UNA TECLA PARA TIRAR DADOS: \n")
        
        print(f'Usted saco esto {dado_jugador_bosque} y el guardian {dado_guardian_bosque}')
        if dado_jugador_bosque==7:
            golpe=puntos_vida_guardian*50//100
            vida_final=puntos_vida_guardian-golpe
            puntos_vida_guardian=vida_final
            print(f'\nExcelente lo has golpeado y esta es su vida {puntos_vida_guardian}')
        elif dado_guardian_bosque==7:
            golpe=puntos_vida*50//100
            vida_final=puntos_vida-golpe
            puntos_vida=vida_final
            print(f'\nEl Guardian del bosque te ha  golpeado y esta es tu vida {puntos_vida}')
        elif puntos_vida==1:
            print("GAME OVER")
            exit()
    print(bosque_tenebroso_parte2)