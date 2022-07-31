
numeros = ('zero','um','dois','três','quatro','cinco','seis',
           'sete','oito','nove','dez','onze','doze','treze',
           'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    while True:
        num=int(input('Digite um número entre 0 e 20: '))
        if 0<=num<21:
            break
        print('Tente novamente', end='.')
    p = numeros[num]
    print(f'Você digitou o numero {p}.')
    con=str(input('Quer contnuar?'))[0]
    if con in 'Nn':
        break
print('Fim da operação')