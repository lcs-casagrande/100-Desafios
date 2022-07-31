from random import randint
print('=-' *30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' *30)
cont=0
while True:
    comp=randint(1,10)
    v=int(input('Diga um valor: '))
    pi=str(input('Par ou impar [P/I]: ')).upper()[0]
    soma=v+comp
    res=''
    print(f'Você jogou {v} e o computador {comp}. Total {soma} {res}')
    if soma%2==0:
        res='deu par'
        ven='P'
    else:
        res='deu impar'
        ven='I'
    if ven==pi:
        print('Você venceu!!!')
        cont+=1
    else:
        print('Per-de-dor!')
        break
print(f'Game Over, você ganhou {cont} vezes.')