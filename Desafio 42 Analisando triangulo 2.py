r1=float(input('1ª reta?'))
r2=float(input('2ª reta?'))
r3=float(input('3ª reta?'))
t=r1+r2+r3
if r1>=r2+r3 or r2>=r1+r3 or r3>=r1+r2:
    print('Não é possivel fazer um triangulo!')
else:
    print('É possivel fazer um triangulo')
    if r1 == r2 == r3:
        print('É um triangulo equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('É um Triandulo Isóseles')
    elif r1 != r2 != r3:
        print('É um triangulo Escaleno')


