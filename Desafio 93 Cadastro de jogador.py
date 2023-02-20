jogador = {}
gols = []
soma = cont = 0
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for p in range (1,partidas+1):
    quant = int(input(f'Quantos gols na partida {p}?'))
    gols.append(quant)

jogador['total'] = sum(gols)
jogador['gol'] = gols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, p in enumerate(jogador['gol']):
    print(f'=> Na partida {i+1}, fez {p} gols')
print(f'Foi um total de {jogador["total"]} gols.')

