import random
from time import sleep
numeros = list(range(1,61))
jogo = []
sorteio=numeros[:]
print(50*'-')
print(f'JOGODA MEGA SENA')
print(50*'-')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {quant} jogos.')
for j in range(1, quant+1):
    for n in range(1,7):
        s = random.choice(sorteio)
        jogo.append(s)
        jogo.sort()
        sorteio.remove(s)

    print(f'Jogo {j}: ', end='')
    print(jogo)
    jogo.clear()
    sorteio = numeros[:]
    sleep(0.5)
