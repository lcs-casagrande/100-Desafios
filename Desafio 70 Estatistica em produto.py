total = mil = prebara = 0
print('-'*30)
print(('{:-^30}' .format('SUPER BARATÃO')))
print('-'*30)
while True:
    prod = str(input('Nome do produto: '))
    pre = float(input('Preço R$ '))
    if pre >1000:
        mil+=1
    total+=pre
    if prebara == 0 or prebara > pre:
        barato = prod
        prebara = pre
    cont=' '
    while cont not in 'SN':
        cont=str(input('Quer continuar? ')).upper().strip()[0]
    if cont == 'N':
        break
print('{:-^40}' .format('Fim da programação'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de 1.000,00')
print(f'O produto mais barato foi {barato} custando R${prebara:.2f}')
