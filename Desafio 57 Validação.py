s=str(input('Informe seu sexo: [M/F]'))
while s != 'M' and s != 'F':
    s=str(input('Dados inválidos, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso' .format(s))