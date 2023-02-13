from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}

print('Valores sorteados:')
for j in range(1,5):
    jogadores[f'jogador {j}'] = randint(1,6)

rank = []

for c, v in jogadores.items():
    print(f'{c} tirou {v} no dado.')
    sleep(0.1)
print('-=' *30)
print('== RANKING DOS JOGADORES ==')

rank =sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i , v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.1)