soma=cont=med=maior=menor=0
con='S'
while con == 'S':
    if cont==0:
        num=float(input('Digite um nº: '))
        con=str(input('Quer continuar? [S/N]')).upper()
        soma+=num
        cont+=1
        menor=maior=num
    else:
        num = float(input('Digite um nº: '))
        con = str(input('Quer continuar? [S/N]')).upper()
        soma += num
        cont += 1
        if menor>num:
            menor=num
        elif maior<num:
            maior=num
    med=soma/cont
print('Você digitou {} números e a média foi {}' .format(cont,med))
print('O menor valor foi {} e o maior foi {}' .format(menor,maior))
