dados = {}
banco = []
media = total =0
mulheres = []
while True:
    dados['Nome'] = str(input('Nome: ')).capitalize()
    while True:
        dados['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO, responda M ou F!')
    dados['idade'] = int(input('Idade: '))
    total += dados['idade']
    while True:
        para = str(input('Quer continuar? [S/N] '))[0].upper()
        if para in 'SN':
            break
        print('ERRO, responda S ou N!')
    banco.append(dados.copy())
    if para in 'N':
        break

print(f'A) Ao todo temos {len(banco)} pessoas cadastradas.')
media = total/len(banco)
print(f'B) A média de idade é de {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram:', end ='')
for i in banco:
    if i['Sexo'] == "F":
        print(i['Nome'], end='. ')

print()
print(f'D) A lista de pessoas acima da média são:')
for i in banco:
    if i['idade'] > media:
        print(f" Nome = {i['Nome']}; sexo = {i['Sexo']}; idade = {i['idade']}")
print('<< ENCERROU>>')