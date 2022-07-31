hom = mais = gar = 0
print('-'*20)
while True:
    print('   Cadastre uma pessoa   ')
    id=int(input('Idade: '))
    sex=' '
    while sex not in 'MF':
        sex=str(input('Sexo [F/M]: ')).upper()[0]
    if sex=='M':
        hom+=1
    if id >=18:
        mais += 1
    if sex == 'F' and id <20:
        gar+=1
    cad=' '
    while cad not in 'SN':
        cad=str(input('Quer continuar? ')).upper()[0]
    if cad =='N':
        break
print(f'Total de pessoas com mais de 18 anos {mais}')
print(f'Ao todo tem {hom} homens cadastrados')
print(f'e temos {gar} mulheres com menos de 20 anos')

