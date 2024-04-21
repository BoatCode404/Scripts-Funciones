import os
while True:
        try:
            num1,num2=int(input("Digite un numero para hacer la operacion : \n")),int(input('Digite otro numero para hacer la operacion:\n'))
            operacion=input('Que operacion va realizar\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n')
            if operacion =='1':
                print(f"la suma es: {num1+num2}")
            elif operacion =='2':
                print(f"La resta es {num1-num2}")
            elif operacion =='3':
                    print(f"La Multiplicacion es : {num1*num2}")
            elif operacion =='4':
                print(f"La Division es : {num1//num2}")
            else:
                print(" es una calculadora simple de suma,resta,multiplicacion y division ; selecciona entre 1-5")
                num1,num2=int(input("Digite un numero para hacer la operacion : \n")),int(input('Digite otro numero para hacer la operacion:\n'))
                operacion=input('Que operacion va realizar\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n')
        except ValueError:
             print("Se esperaba un numero entero")