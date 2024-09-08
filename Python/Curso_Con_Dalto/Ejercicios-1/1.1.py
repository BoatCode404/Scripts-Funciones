# Curso dalto = 1.5 , curso minimo = 2.5 , Cuso maximo = 7 , curso promedio = 4h , crudo_otros_videos = 5h , crudo_dalto= 3.5 el crudo es el material vacio del video lo que se bota despues de editarlo 

# Punto A : Diferencia en porcentaje entre el curso actual(dalto) y el mas rapido de otros cursos, el mas lento de otros cursos y el promedio de los cursos

# Punto B : porcentaje del materal incervible que se reduce en : el promedio de los cursos ,  el curso actual (  dalto )

# Punto C : Ver 10 horas de este curso a cuantas de otros cursos equivale 

# declaramos las variables de los datos de los cursos ( en  horas )
curso_dalto = 1.5 
curso_minimo = 2.5 # esto vendria ser el curso mas rapido antes que el curso de dalto 
curso_maximo = 7 # este es el curso mas lento a comparacion de los otros 
cursos_promedio = 4  # Esto hace referencia a otros cursos


#Duracion de crudos (  video  sin editar ) 
crudo_dalto = 3.5 
crudo_otros = 5 


# Diferencia en porcentajes PUNTO A
diefencia_con_minimo = 100 - (curso_dalto / curso_minimo * 100)
diefencia_con_maximo = 100 - (curso_dalto  * 1000  // curso_maximo / 10 )  # el resultado es : 78.57142857142857 para redondearlo usamos * 1000  y dividimos por 10 en ves de multiplicarlo al final , con esto hacemos que nos de 78.6 % lo redondea y si ponemos dividido en 100 serian dos decimales al final 
diefencia_con_promedio = 100 - (curso_dalto / cursos_promedio * 100)



# calculando el porcentaje de tiempo vacio ( crudos ) PUNTO B
tiempo_vacio_promedio  = 100 - cursos_promedio * 1000 // crudo_otros /  10   # el video de otros cursos dice que dura 4 horas pero que el video completo es de 5 horas vamos hacer esa resta pero en porcentaje 
tiempo_vacio_dalto  = 100 - curso_dalto * 1000 // crudo_dalto /  10


# Calculando cuantas horas equivale de otros cursos PUNTO C
horas_otros = cursos_promedio *1000 // curso_dalto / 100 
horas_dalto = curso_dalto *1000 // cursos_promedio / 100


# Mostrando resultado de diferencias del PUNTO A
print('-------------------------------')
print(f'el curso de dalto dura un {diefencia_con_minimo} % menos que el mas rapido')
print(f'el curso de dalto dura un {diefencia_con_maximo} % menos que el mas lento')
print(f'el curso de dalto dura un {diefencia_con_promedio} % menos a otros cursos')


# Mostrando resultado de diferencias del PUNTO B
print('-------------------------------')
print(f'Un curso promedio elimina el {tiempo_vacio_promedio}% de tiempo vacio ')
print(f'el curso de dalto elimino el  {tiempo_vacio_dalto}% de tiempo vacio ')

# Mostrando resultado si los cursos duran 10 horas PUNTO C
print('-------------------------------')
print(f'Ver 10 horas del curso de dalto equivale a ver {horas_otros} horas de otros cursos')
print(f'Ver 10 horas de otro cursos equivale a ver {horas_dalto} horas del curso de dalto ')