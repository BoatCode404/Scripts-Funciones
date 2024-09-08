import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
total=dado1+dado2
print(total)
r=int(input("What is the total (2-12)?\n"))
while r != total:
    r=int(input("What is the total (2-12)?\n"))
    if r == total:
        print('You got it!')
        break
    