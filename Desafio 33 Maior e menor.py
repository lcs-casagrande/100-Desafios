n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o sugundo numero:'))
n3 = float(input('Digite o terceiro numero:'))
if n1>=n2 and n1>n3:
        maior=n1
if n1<=n2 and n1<n3:
        menor=n1
if n3>n2 and n3>=n1:
    maior=n3
if n3<n2 and n3<=n1:
    menor=n3
if n2>n1 and n2>=n3:
    maior = n2
if n2<n1 and n2<=n3:
    menor=n2
print('O maior vale {}.' .format(maior))
print('O menor vale {}' .format(menor))

