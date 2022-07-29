cont=0
c=0
soma=0
while c != 1:
    num=int(input('Digite um numero [999 para parar]: '))
    if num != 999:
        soma +=num
        cont+=1
    else:
        c = 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))