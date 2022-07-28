from time import sleep
pri=float(input('Primeiro valor: '))
seg=float(input('Segundo valor: '))
menu=0
while menu==0:
    print('=-='*10)
    fun=int(input('''    [1] Somar
    [2] multiplicar
    [3] Maior
    [4] novos números
    [5] sair do programa
    Qual sua opção: '''))
    if fun==1:
        res=pri+seg
        print('{} mais {} é igual a {}' .format(pri,seg,res))
    elif fun==2:
        res=pri*seg
        print('{} vezes {} é igual a {}' .format(pri,seg,res))
    elif fun ==3:
        if pri>seg:
            print('{} é o maior' .format(pri))
        elif pri<seg:
            print('{} é o maior' .format(seg))
        else:
            print('Os valores são iguais')
    elif fun==4:
        print('Digite os novos valores!')
        pri=float(input('Primeiro valor: '))
        seg=float(input('Segundo valor: '))
    elif fun ==5:
        print('Encerrando operação')
        menu=1
    else:
        print('Opção invalida')
    sleep(2)
print('Fim da programação')