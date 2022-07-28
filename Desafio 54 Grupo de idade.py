import date
atual = date.today().year
maior=0
menor=0
ano=0
for c in range (1,8):
    ano=int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    if ano<2:
        maior +=1
    else:
        menor +=1
print('Ao todo tivemos {} pessoas maiores de idade' .format(maior))
print('E também tivemos {} pessoas menores de idade' .format(menor))
