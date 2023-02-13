from datetime import datetime
candidato = {}
candidato['Nome'] = str(input('Nome: '))
candidato['Ano'] = int(input('Ano de nacimento: '))
candidato['idade'] = int(datetime.now().year - candidato['Ano'])
candidato['ctps'] = str(input('Carteira de trabalho (0 não tem):'))
if candidato['ctps'] != '0':
    candidato['Contratação'] = int(input('Ano de contratação: '))
    candidato['Salário'] = int(input('Qual salário: '))
    candidato['Aposentadoria'] = (candidato['Contratação'] - candidato['Ano'] + 35 )
del candidato['Ano']
print('-=' *30)
for k, v in candidato.items():
    print(f'   -{k} tem o valor de {v}')
