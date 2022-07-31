maior = menor = n =0
sorteio = (0,1,2,3,4,5,6,7,8,9,10)
import  random
for c in range (0,5):
    n = random.choice(sorteio)
    print(n,end=' ')
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'\nO maior valor foi {maior}.')
print(f'O menor valor foi {menor}.')