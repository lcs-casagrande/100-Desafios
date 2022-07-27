from random import randint
from time import sleep
r = randint(0,5)
print(10*'-#-')
print('Vou pensar em um numero de 0 à 5. Tente adivinhar')
print(10*'-#-')
print('PROCESSANDO...')
sleep(5)
n=int(input("Em qual numero eu pensei?"))
if n == r:
    print('Parabens, você acertou')
else :
    print('GANHEI!!! Eu pensei no numero {} e não {}.' .format(r,n))


