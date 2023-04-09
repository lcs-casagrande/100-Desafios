from datetime import date
def voto(idade):
    print('--' * 40)
    if idade < 16:
        sit='não vota'
    elif 17< idade < 70:
        sit='o voto é obrigatório'
    else:
        sit='o voto é opcional'
    return sit

nasc=int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nasc
print(f'Com {idade} anos: {voto(idade)}.')
