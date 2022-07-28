totalidade=0
maior=0
mulheres=0
velho=1000
for c in range(1,5):
    print('----{}ª Pesoa ----' .format(c))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).upper()
    totalidade +=idade
    if sexo=='M'and c==1:
        maior=idade
        velho=nome
    if sexo=='M' and idade >maior:
        maior=idade
        velho=nome
    elif sexo=='F' and idade<20:
        mulheres+=1

media= totalidade/c
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
