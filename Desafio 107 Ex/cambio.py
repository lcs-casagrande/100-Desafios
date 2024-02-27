import moeda
n=float(input('Adicione um numero: '))
print(f'metade: {moeda.metade(n)}')
print(f'dobro: {moeda.dobrar(n)}')
a=int(input(f'Aumentar quanto? '))
print(f'Aumentando: {moeda.aumentar(n,a)}')
d=int(input(f'Diminuir quanto? '))
print(f'Diminuindo: {moeda.diminuir(n,d)}')

