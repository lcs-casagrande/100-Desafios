import random

soma = []
def sortear():
    numeros = list(range(1, 11))

    print('Sorteando 5 valores da lista: ',end=' ')
    for n in range(1,6):
        s = random.choice(numeros)
        print(s,end=' ')
        soma.append(s)
        numeros.remove(s)

    print('Pronto!')

def somar(lis):
    total = 0
    print(f'Somando os valores pares {lis},',end=' ')
    for n in lis:
        if n % 2 == 0:
            total += n
    print(f'temos {total}')


sortear()
somar(soma)