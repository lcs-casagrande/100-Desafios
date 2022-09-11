valores = list()
pos_maior = list()
pos_menor = list()
pos=maior = menor = 0
for c in range(0,5):
    novo = int(input(f'Digite o valor da posição {c}:'))
    valores.append(novo)
    if c == 0:
        maior=menor=novo
    elif novo> maior:
        maior=novo
    elif novo<menor:
        menor=novo
posicao = valores[:]
for p in posicao:
    if p == maior:
        pos_maior.append(pos)
    if p == menor:
        pos_menor.append(pos)
    pos+=1
print('-='*20)
print(f'Você digitou os valores: {valores}')

print(f'O maior valor digitado foi {maior}',end=' nas posições ')
for p in pos_maior:
    print(p,end='...')
print()
print(f'O menor valor digitado foi {menor}',end=' nas posições ')
for d in pos_menor:
    print(d,end='...')
