def ficha (a= '', b= ''):
    '''

    :param a: Nome do jogador
    :param b: gols do jogados
    :return: resumo
    '''
    if a == '':
        a="desconhecido"

    if b == '':
        b = 0
    elif b.isnumeric() == False:
        b = 0
    else:
        b=b


    resumo = (f'O jogado {a} fez {b} gol(s) no campeonato')
    return resumo

print(50*"-")
jog=input("Qual o nome do jogador? ").capitalize()
gols=input('Quantos gols foram feitos? ')

