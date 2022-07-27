distancia=float(input('Qual a distancia da sua viagem?'))
print('Você está preste a fazer uma viagem de {}km.' .format(distancia))
'''if viagem <200:
    print('E o preço da sua passagem será de R${}' .format(viagem * 0.5))
else:
    {print('E o preço da sua passagem será de R${}' .format(viagem * 0.45))'''
preco = distancia * 0.5 if distancia <=200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

