import os,time
mayores=0
def animated_text(t):
    for c in t:
        print(c,end='',flush=True)
        time.sleep(0.1)
for i in range(1,201):
    animated_text('Cual es tu edad\n')
    edad=input()
    if edad>='18':
        mayores +=1
print(f' La cantidad de mayores son : {mayores}')