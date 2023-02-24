from time import sleep
def maior (* num):
    print('-=' *30)
    print('Analisdando os valores passados...')
    maior = 0
    for n in num:
        if n == num[0]:
            maior = n
        print( n, end=' ')
        sleep(0.5)
        if n > maior:
            maior = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    sleep(0.5)


maior(2, 9, 7, 5, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(-1, -3, -2)