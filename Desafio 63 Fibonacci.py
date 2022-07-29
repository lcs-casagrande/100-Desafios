print('-'*15)
print('SEQUENCIA DE FIBONACCI')
print('-'*15)
pri=0
seg=1
cont=0
term=0
quant=int(input('Quantos termos você deseja? ' ))
print('{} > {} >'.format(pri,seg),end=" ")
while cont < (quant-2) :
    cont+=1
    ter=pri+seg
    print('{} >'.format(ter), end=' ')
    pri=seg
    seg=ter
print('Fim')
print('~'*40)