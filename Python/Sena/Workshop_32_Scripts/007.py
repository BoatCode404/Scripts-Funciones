def edad_persona(f):
    año_actual=2024
    e=año_actual-f
    return e
añoN=int(input("Cual es su año de nacimiento: "))
edad=edad_persona(añoN)
if edad>=18:
    print("Debe sacar CUIL 😒")
else: print("No debe sacar CUIL 😁")