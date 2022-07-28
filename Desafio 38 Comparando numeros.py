pri=float(input('Qual o primeiro numero?'))
seg=float(input('Qual o segundo numero?'))
if pri>seg:
    print('Primeiro valor {} é maior!'.format(pri))
elif pri<seg:
    print('Segundo valor {} é maior!'.format(seg))
elif pri == seg:
    print('Os numeros tem os mesmos valores')
