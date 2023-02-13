aluno = {}
aluno['nome'] = str(input('Qual o nome do aluno? '))
aluno['Média'] = float(input(f'Média de {aluno["nome"]}? '))
if aluno['Média'] >= 6:
    aluno['Situação'] = str('Aprovado')
else:
    aluno['Situação'] = str('Reprovado')
print('-='*30)
print(f'  --Nome é igual a {aluno["nome"]}')
print(f'  --Média é igual a {aluno["Média"]}')
print(f'  --Situação é igual a {aluno["Situação"]}')
