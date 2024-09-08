lego_parts=[8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

print(f'La pieza que mas se esta acabando es : {min(lego_parts)}')
print(f'La pieza que mas esta abastecida es :{max(lego_parts)}')
print(f'La cantidad de elementos que hay en la lista son : {len(lego_parts)}')
print(f'La suma de todas las piezas de la lista es : {sum(lego_parts)}\n\n')
ordenar=(input("Quieres Ordenar la lista de menor a mayor o viceversa Escribe \nMenor\nMayor\nResponda aca : ")).lower()
if ordenar =='menor':
   print(f'La lista quedo asi {sorted(lego_parts)}') 
else:
    print(f'La lista quedo asi {sorted(lego_parts,reverse=True)}') 
