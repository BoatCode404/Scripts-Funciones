# Introducir tantas frases como queramos y contarlas. 




import os 
listaFrases=[]
frase=''
contador=0

'<--- primera_forma --->'

print("NOTA IMPORTANTE : para salir del programa utilice la plabra exit")
while frase!='exit':
    frase=str(input("Escriba una frase para contarla : ")).lower()
    contador+=1
    if contador==1:
        print(f"Ha escrito {contador} Frase")
    else:
        print(f"Ha escrito {contador} Frases")
os.system('cls')
print("Has escrito Exit , Asi que se cerro el programa\n")
print(f"Se ingresaron un tatal de {contador} frases")





'<--- segunda_forma --->'
cantidadFrases=int(input("Cuantas frases vas ingresar : "))
for i in range(cantidadFrases):
    frase=input("Escriba una frase para contarla : ").lower()
    contador+=1
print(f"Se ingresaron un total de {contador} frases")




'<--- tercera_forma --->'
while frase!='exit':
    frase=input("Escriba una frase para contarla : ").lower()
    listaFrases.append(frase)
    print("\n\nRecuerde para contar las frases que ingreso escriba (Exit)\n\n ")
sumaFrases=print(f"usted ingreso {len(listaFrases)} frases" )