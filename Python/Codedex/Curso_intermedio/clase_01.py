genz_slang=['fachero','gotic','2p']

colombian=(41.909050,-87.791420)
usa=(37.090240,-95.712891)
london=(51.507351,-0.127758)


tupla_unida=colombian+usa+london

print(tupla_unida)



# Diccionarios 
laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023,
}

print(laptop['model'])


estudiante_julian={'nombre':'Julian Holguin','edad':23,'grado':'8-D'}
estudiante_andres={'nombre':'Andres Florez','edad':26,'grado':'9-D'}
estudiante_karol={'nombre':'Karol Arenas','edad':30,'grado':'7-D'}

# Para acceder a los elementos
print(f'nombre : {estudiante_julian["nombre"]}')

# Para modificar elementos 

estudiante_julian['edad']=24

print(f'edad actualizada : {estudiante_julian["edad"]}')


print(f'keys : {estudiante_julian.keys()}')
print(f'values : {estudiante_julian.values()}')
print(f'items : {estudiante_julian.items()}')


#.items()devuelve una lista de los pares clave-valor como tuplas.




the_virgin_of_guadalupe={'artista':'Nicolás Enríquez','periodo':'2014.173','fecha': '1773'}


print(f'values : {the_virgin_of_guadalupe.values()}')
print(f'keys : {the_virgin_of_guadalupe.keys()}')


set1={1,2,3,4}
set2={5,2,7,8}

resultado_union=set1.union(set2)

resultado_insersccion=set1.intersection(set2)

resultado_diferencia=set1.difference(set2)


print(resultado_diferencia)
print(resultado_insersccion)
print(resultado_union)



# para agregar elementos usamos '.add' y para eliminar usamos '.remove'

set={1,2,3}
set.add(4)
set.remove(1)
print(set)


