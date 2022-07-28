#Escreva um programa que leia um número interno qualquer peça para o usuario escolher qual será a base de conversão
num = int(input('Digite um numero inteiro'))
print('''Escolha uma das base para conversã
[1] Binario
[2] Octal
[3] hexadecimal''')
opção=int(input('Sua opção?'))
if opção==1:
    print('{} convertido para binario é igual a {}' .format(num, bin(num)[2:]))
elif opção==2:
    print('{} convertido para octal é igual a {}'.format(num,oct(num)[2:]))
elif opção==3:
    opção==3
    print('{} convertido para hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida')