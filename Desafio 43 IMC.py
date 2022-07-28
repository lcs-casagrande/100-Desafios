p=float(input('Qual seu peso?'))
a=float(input('Qual sua altura?'))
i=p/a**2
print('{:.1f}'.format(i))
if i<18.5:
    print('Abaixo do peso')
elif 18.5<=i<25:
    print('Peso ideal')
elif 25<=i<30:
    print('Sobrepeso')
elif 30<=i<40:
    print('Obesidade')
elif i>=40:
    print('Obesidade morbida')
