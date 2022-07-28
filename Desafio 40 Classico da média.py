n1=float(input('1ª nota?'))
n2=float(input('2ª nota?'))
m=(n1+n2)/2
print(m)
if m>=7:
    print('Aprovado')
elif m<5:
    print('Reprovado')
else:
    print('Recuperação')
