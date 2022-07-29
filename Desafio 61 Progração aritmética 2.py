print('Gerando uma progressão aritmética')
print('-'*10)
con=10
ter=int(input('Digite o primeiro termo: '))
raz=int(input('Digite a razão da PA: '))
while con !=0:
    print(ter,'>',end=' ')
    ter+=raz
    con -=1
print('fim')
