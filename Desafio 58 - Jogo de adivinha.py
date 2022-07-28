import random
print('Sou seu computador!')
n=int(input('De 0 à 10, adivinha qual numero estou pensando...'))
l=[0,1,2,3,4,5,6,7,8,9,10]
c=random.choice(l)
cont=1
while c!=n:
    if c>n:
        print('Mais... Tente novamente!')
    elif c<n:
        print('Menos... Tente novamente!')
    n=int(input('Qual seu palpite'))
    cont+=1
print('Acertou Miseravel! Com {} tentativas'.format(cont))
