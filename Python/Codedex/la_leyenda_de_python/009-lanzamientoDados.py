def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
import time
import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
animate_text(f'Los dados calleron en {dado1} Y {dado2}')