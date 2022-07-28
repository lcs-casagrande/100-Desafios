num = int(input('Digite um numero para calcularmos a fatorial! '))
num2 = num
num3 = num
print('----- Modo 1 (import)-----')
from math import factorial
fac = factorial(num)
print('Fatorial de {} é igual a {}' .format(num,fac))
print('----- Modo 2 (while)-----')
fat=num2
print('Calculando {}!='.format(num2), end=(''))
while num2!=1:
    print('{} x' .format(num2),end=' ')
    num2=num2-1
    fat=fat*num2
    #print(fat,end=(' '))
print('1' if num2==1 else "" , end=(''))
print(' = {}'.format(fat))

print('----- Modo 3 (for)-----')
for p in (num3,1,-1):
    print('{} x' .format(num3),end=' ')
    num3-=1
    fat3=fat*num3
print('=',end='')
print(' {}' .format(fat))