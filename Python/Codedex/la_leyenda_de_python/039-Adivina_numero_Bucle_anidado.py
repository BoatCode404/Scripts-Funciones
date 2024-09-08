import random

lucky_number = random.randint(1, 10)
not_found = True

while not_found:
  for i in range(1, 10):
    if i == lucky_number:
      not_found = False
      '''print(i)''' # Esto es opcional
      break
    else:
      print(i)
print(f"Felicitaciones El numero secreto era {lucky_number}! 🍀")