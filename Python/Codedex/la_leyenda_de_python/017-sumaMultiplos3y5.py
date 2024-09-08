suma=0
for i in range(1,100):
    if i%3==0 and i%5==0:
        suma += i
        print("Los Multiplos de 3 y 5 son:",i)
print(f"la suma es : {suma}")