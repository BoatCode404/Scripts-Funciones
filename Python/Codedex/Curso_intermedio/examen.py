

jugadores=[{
    'nombre':'julian holguin',
    'posicion':'delantero',
    '#_camiseta':99,
    'partidos jugados':15,
    'goles anotados':2
},

{
    'nombre':'santiago herrera',
    'posicion':'defensa',
    '#_camiseta':39,
    'partidos jugados':20,
    'goles anotados':10
},

{
    'nombre':'daniel herrera',
    'posicion':'volante',
    '#_camiseta':10,
    'partidos jugados':50,
    'goles anotados':18
}
]



# Como iterar con 'for' en un diccionario pero solo si esta dentro de una lista 
posiciones= [jugador['posicion']for jugador in jugadores]
print(f'Las posiciones de los jugadores es {posiciones}')


# como modificar los datos de un jugador
jugadores[2]['posicion']='delantero'
jugadores[2]['#_camiseta']=11


# sumar elementos de una lista de diccionarios
total_goles=sum(jugador['goles anotados'] for jugador in jugadores)
total_partidos=sum(jugador['partidos jugados'] for jugador in jugadores)

# promedio de elementos de una lista de dccionarios

promedio_goles=total_goles/len(jugadores)
promedio_partidos=total_partidos/len(jugadores)

print(f'el promedio de goles es : {promedio_goles}\nel promedio de partidos es: {promedio_partidos}')






