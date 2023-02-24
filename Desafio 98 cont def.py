from time import sleep
def contagem (a,b,c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    if a > b :
        c=-c
    if b > 0:
        b+=1
    else:
        b-=1
    for con in range (a,b,c):
        print(con, end=' ')
        sleep(0.5)
    print('FIM!')

#Código principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora sua vez')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i,f,p)