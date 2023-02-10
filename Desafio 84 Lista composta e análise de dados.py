cont = maior = menor =0
pessoas = list()
dados = list()
galera = list()
lmaior = list()
lmenor = list()

while True:
    cont +=1
    nome = str(input('Nome: ')).capitalize()
    dados.append(nome)
    peso = int(input('Peso: '))
    dados.append(peso)
    parar = str(input('Quer continuar ? [S/N}')).upper()
    galera.append(dados[:])
    dados.clear()


    if cont == 1:
        maior = peso
        menor = peso

    if peso == maior:
        lmaior.append(nome)
    if peso > maior:
        maior = peso
        lmaior.clear()
        lmaior.append(nome)

    if peso == menor:
        lmenor.append(nome)
    if peso < menor:
        menor = peso
        lmenor.clear()
        lmenor.append(nome)



    if parar[0] == 'N':
        break

print(100*'-=')
print(f'Ao todo você cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {lmaior}')
print(f'O menor peso foi de {menor}Kg. Peso de {lmenor} ')