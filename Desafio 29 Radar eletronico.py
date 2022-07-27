velocidade = int(input('Qual a velocidade do carro?'))
multa = (velocidade-80)*7
if velocidade >80 :
    print('MULTADO! Você excedeu o limite permitido de 80Km/h. \nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia. Dirija com segurnaça')
