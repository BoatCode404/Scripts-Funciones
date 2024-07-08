#Escribe un algoritmo que genere una lista de los primeros 10 números de Fibonacci.


serieFibonacci=[0,1]

while len(serieFibonacci) < 10:
    serieFibonacci.append(serieFibonacci[-1]+serieFibonacci[-2])

print(serieFibonacci)



