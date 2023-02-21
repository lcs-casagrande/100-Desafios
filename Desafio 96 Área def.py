def area (a,b):
    total = a * b
    print(f'A área de um terreno {a} x {b} é de {total}m²')


print('Controle de terreno')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l,c)
