# una persona promedio habla 2 palabras x segundo , cuantos segundos habla x palabra 

# Punto A : Pedirle al usuario una frase que diga cual quier texto real y 
# calcular cuanto tardaria en decir esa frase 
# cuatas palabras dijo 

# Punto B : si se tarda mas de 1 minuto decirle " Parar flaco tampoco te pedi un testamento"

# Punto C : si una persona hablara un 30% mas rapido cuanto se demoraria 


# le pedimos al usuario la frase
frase = input ('Digita una frase maquina : ')

# separamos la frase por "," comas y en una lista para manipularla 
palabras = frase.split(" ")

# contamos cuantas palabras hay en la frase separada por "," comas y dividimos por 2 palabras
tiempo_en_segundos = len(palabras) / 2 # PUNTO A


# Si una persona hablara un 30 % + rapido PUNTO C
#Tiempo original que se demora una persona en decirlo
tiempo_original = tiempo_en_segundos 

# Calcular el 30 % del tiempo original 
reducir_tiempo = tiempo_original * 0.30

# Reducir el tiempo original en un 30% para simular que habla más rápido
tiempo_rapido = tiempo_original - reducir_tiempo 

# cantidad de palabras 
cantidad_palabras= len(palabras)


# mostramos los resultados 
print('----------------------')
print(f'Se demora {tiempo_en_segundos:.2f} segundos en decir esa frase')
print('----------------------')
print(f'La cantidad de palabras : {len(palabras)} palabras')
print('----------------------')
print(f'Si una persona hablara un 30% mas rapido se tardaria {tiempo_rapido:.2f} segundos en decir la frase')


# condicion si tarda mas de 1 minuto en decir la frase si es True muestra el mensaje si es false no muestra nada PUNTO B
if tiempo_en_segundos > 60.0:
    print('----------------------')
    print('Para flaco tampoco te pedi un testamento 📖')



