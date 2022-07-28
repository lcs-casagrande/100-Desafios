soma=cont=0
for c in range (1,7):
    num=int(input('Digite um numero:'))
    if num%2==0:
        soma+=num
        cont+=1
print('A soma dos {} numeros pares é {}.' .format(cont,soma))
