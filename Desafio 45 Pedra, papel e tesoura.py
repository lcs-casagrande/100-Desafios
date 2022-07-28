import random
from time import sleep
vi=input('Pedra, papel ou tesoura?')
v=vi.lower()
c=['pedra', 'papel', 'tesoura']
ce=random.choice(c)
sleep(.5)
print('JO')
sleep(.9)
print('KEN')
sleep(1.5)
print('PO!!!')
sleep(0.3)
print("-="*10)
if v==ce:
    print('Empate')
elif v=='pedra' and ce=='papel':
    print('Computador venceu')
elif v=='papel' and ce =='tesoura':
    print('Computador venceu!')
elif v=='tesoura' and ce=='pedra':
    print('Computador venceu')
else:
    print('Você venceu!')
print('Computador escolheu {} e você {}' .format(ce, v))