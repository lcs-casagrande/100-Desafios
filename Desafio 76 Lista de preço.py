print('-'*40)
print('{:^40}'.format('LISTA DE PREÇO'))
print('-'*40)
materiais=('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,
           'Transferidor',4.2,'Compasso', 9.99,'Mochila',120.32,'Canetas',22.30,
           'Livros',34.90)
quant=len(materiais)
for c in range (0,quant,2):
    print('{:.<30}' .format(materiais[c]),end='')
    print(f'R$ {materiais[c+1]:>6.2f}')

