fra=str(input('Digite uma frase:')).strip().lower().replace('ã','a').replace('á','a').replace('à','a')
print('A letra A aparece {} vezes na frase!'.format(fra.lower().count('a')))
print('A primeira letra A apareceu na posição {}' .format(fra.find('a')+1))
print('A última letra A apareceu na posição {}'.format(fra.rfind('a')+1))
