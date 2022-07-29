cont=0
max=9
ter=0
pro=1
print('=-'*10)
pri=int(input('Primeiro termo: '))
termo=pri
raz=int(input('Qual a razão: '))
while pro != 0:
    while cont <= max:
        print('{} > '.format(termo), end=" ")
        termo=termo+raz
        cont+=1
        ter+=1
    print('Pausa',end=' ')
    print()
    mais=int(input('Quantos termos você quer mostrar a mais? '))
    max=max+mais
    pro=mais
print('Progressão finalizada com {} termos mostrados'.format(ter))
