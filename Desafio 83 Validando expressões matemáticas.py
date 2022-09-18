abre=[]
fecha=[]
espressao=input('Digite uma expressão:')
for c in espressao:
    if c == '(':
        abre.append(c)
    elif c == ')':
        fecha.append(c)
if len(abre) == len(fecha):
    print('Sua expressão esta valida.')
else:
    print('Sua expressão esta errada.')