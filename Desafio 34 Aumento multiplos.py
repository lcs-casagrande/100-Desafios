sal=float(input('Qual o salário do funcionario? '))
if sal > 1250:
    aum=sal*1.10
else:
    aum=sal*1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.' .format(sal,aum))