d=int(input('Quantos dias usou o carro?'))
k=float(input('Quantos Km rodou com o carro?'))
cd=d*60
ck=(k*0.15)
print('Valor a pagar R${:.2f}.'.format(cd+ck))
