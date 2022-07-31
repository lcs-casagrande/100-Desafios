con = soma = 0
while True:
    val=float(input('Digite um valor [999 para parar]: '))
    if val==999:
        break
    soma+=val
    con+=1
print(f'A soma dos {con} valores foi {soma}!')