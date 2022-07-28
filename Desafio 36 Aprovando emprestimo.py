#Questionario Emprestimo
valor=float(input('Qual o valor da casa?'))
salario=float(input('Qual o salário?'))
anos=float(input('Em quantos anos irá pagar?'))
meses=anos*12
margem=salario*0.3
parcela=valor/meses
print('Para pagar uma casa de {} em {}'.format(valor,anos))
print('A prestação será de R$ {.:2f}'.format(parcela))

if parcela <= margem:
    print('Aprovado')
else:
    print('Reprovado')





