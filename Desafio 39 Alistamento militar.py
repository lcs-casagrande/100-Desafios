from datetime import date
atual=date.today().year
nac=int(input('Qual seu ano de nacimento?'))
ano=-nac+atual
if ano==18:
    print('Ano de se alistar!')
elif ano>18:
    pra=ano-18
    print('Passou o prazo de se alista em {} anos' .format(pra))
elif ano<18:
    fal=18-ano
    print('Faltam {} anos para se alistar'.format(fal))
