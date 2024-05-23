mensaje_1="pRuBa DE TiTlE"
print(mensaje_1.upper())
print(mensaje_1.lower())

nombre="jUlIAn"
apellido="hOlGuin"
nombre_completo=f'{nombre} {apellido}'
saludo=f'! Hola , {nombre_completo.title()} !' #* mira donde usamos el metodo 'title()'
print(saludo)

print("hola")
print("\tpython")
print("hola\nSoy Julian\nEstudio en el SENA\nItagui\nCalatrava\n2024")

print("Estudiante:\n\tJulian Holguin\nIdiomas:\n\tA duras penas Español")

ejemplo_rstrip='con Espacios al final  ' 
ejemplo_rstrip=ejemplo_rstrip.rstrip()
print(ejemplo_rstrip)


eliminarEspacios='  Hola    '

print(f'{eliminarEspacios.lstrip()}\n{eliminarEspacios.rstrip()}\n{eliminarEspacios.strip()}')


'''eliminarEspacios=eliminarEspacios.lstrip() #* Elimina espacios o caracteres al inicio

eliminarEspacios=eliminarEspacios.rstrip() #* Elimina espacios o caracteres al final

eliminarEspacios=eliminarEspacios.strip()  #* Elimina espacios o caracteres en ambos lados'''

