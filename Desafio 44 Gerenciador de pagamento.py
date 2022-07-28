print('{:=^40}'.format( 'LOJAS CASAGRANDE' ))
pn=float(input('Qual o preço normal?'))
cdp=input(''''
Qual a opção de pagamento?
[1] DINHEIRO
[2] CARTÃO A VISTA
[3] CARTÃO 2X
[4] CARTÃOMAIS DE 3X
''')

if cdp =='1':
    pf=pn*0.9
    print('R$:{}'.format(pf))
elif cdp == '2':
    pf=pn*0.95
    print('R$:{}'.format(pf))
elif cdp == '3':
    pf=pn
    print('R$:{}'.format(pf))
elif cdp == '4':
    pf=pn*1.2
    print('R$:{}'.format(pf))
else:
    print('Opção invalida')
