palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO',
            'GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
            'MERCADO','PROGRAMADOR','FUTURO')
for c in range (len(palavras)):
    print(f'Na palavra {palavras[c]} temos ' ,end=' ')
    soletra = palavras[c]
    for s in range (len(soletra)):
        vog=soletra[s]
        if vog in 'AEIOU' :
            print(f'{vog}' ,end=' ')
    print()

