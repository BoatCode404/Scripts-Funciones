import time
def animated_text(text):
    for c in text:
        print(c,end='',flush=True)
        time.sleep(0.1)
votos={
    'candidato_1':0,
    'candidato_2':0,
    'candidato_3':0
}
try:
    votantes=int(input("¿Cuantos votantes son?\n"))
except ValueError:
    animated_text("se esperaba un numero\n")
for i in range(votantes):
    while True:
        animated_text("¿Por cual Candidato vas a Votar?\n\n1)Candidato#1\n2)Candidato#2\n3)Candidato#3\n")
        r=(input())
        try:
            if r == '1':
                votos['candidato_1']+=1
            elif r == '2':
                votos['candidato_2']+=1
            elif r == '3':
                votos['candidato_3']+=1
            else:
                animated_text('ERROR DEBESE SELECCIONAR ENTRE LAS OPCIONES\n1)Candidato#1\n2)Candidato#2\n3)Candidato#3\n')
        except ValueError:
            animated_text("Se esperaba un numero\n")
        else:
            break
animated_text("La tabla de posiciones queda asi \n")
for candidato,suma_votos in votos.items():
    print(f"{candidato} : {suma_votos}")
total_votos=max(votos.values())
animated_text(f"El maximo de votos de esta eleccion fueron {total_votos}\n")
ganador=max(votos,key=votos.get)
animated_text(f"Por lo tanto el ganador es {ganador}")