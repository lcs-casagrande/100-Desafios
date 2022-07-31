par=0
a = tuple
a = int(input('Digite o primeior numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))
d = int(input('Digite um ultimo numero: '))
tup = (a,b,c,d)
print(f'Você digitou {tup}.')
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if a == 3 or b == 3 or c == 3 or d == 4:
    print(f'O valor 3 apareceu {tup.index(3)+1}ª Posição.')
else:
    print('valor 3 não digitado')
print(f'Os valores pares foram:' , end=' ')
for cont in range (len(tup)):
    if tup[cont] %2 == 0:
        print(tup[cont] , end=' ')
print()
print('Fim da operação')