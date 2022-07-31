nota50 = nota20 = nota10 = nota5 = nota1 = 0
print('='*30)
print('{:^30}' .format('Banco Casa'))
print('='*30)
valor=int(input('Qual valor deseja retirar? R$ '))
if valor>= 50:
    while True:
        nota50 += 1
        valor-=50
        if valor < 50:
            break
if valor>=20:
    while True:
        nota20 += 1
        valor-=20
        if valor < 20:
            break
if valor>=10:
    while True:
        nota10 +=1
        valor-=10
        if valor <10:
            break
if valor>=5:
    while True:
        nota5+=1
        valor-=5
        if valor<5:
            break
if valor>=1:
    while True:
        nota1 +=1
        valor -=1
        if valor ==0:
           break
if nota50>0:
    print(f'Total de {nota50} cédulas de R$50,00')
if nota20>0:
    print(f'Total de {nota20} cédulas de R$20,00')
if nota10>0:
    print(f'Total de {nota10} cédulas de R$10,00')
if nota5>0:
    print(f'Total de {nota5} cédulas de R$5,00')
if nota1>0:
    print(f'Total de {nota1} cédulas de R$1,00')
print('='*30)
print('Volte sempre ao banco Casa!')

