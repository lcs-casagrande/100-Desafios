import moeda
n=float(input('Adicione um numero: '))
print(f'metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobrar(n))}')
print(f'Aumentando 10%: {moeda.moeda(moeda.aumentar(n))}')
print(f'Diminuindo: {moeda.moeda(moeda.diminuir(n))}')

