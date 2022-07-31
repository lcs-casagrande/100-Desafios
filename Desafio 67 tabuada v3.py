print('-'*20)
while True:
    num=float(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    for c in range(1,11):
        mult=c*num
        print(f'{num} X {c} = {mult}')
print('PROGRAMA DE TABUADA ENCERRADO')