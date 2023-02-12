boletim= [[], [], [],[]]
cont = 0
while True:
  cont +=1
  nome = str(input('Nome: ')).capitalize()

  n1 = float(input('Nota 1: '))
  n2 = float(input('Nota 2: '))

  boletim[0].append(nome)
  boletim[1].append(n1)
  boletim[2].append(n2)
  boletim[3].append((n1+n2)/2)
  contiua = str(input('Quer continuar? [S/N]'))
  if contiua in 'nN':
    break
print(f'-=' *30)
print('nº  NOME    MÉDIA')
print('--'*20)
for n in range(0,len(boletim)):
    print(f'{n+1:^5}', end=' ')
    print(f'{boletim[0][n]:^5}' ,end=' ')
    print(f'{boletim[3][n]:^5}')
print('-' * 20)
while True:
  q = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
  if q == 999:
    print('FINALIZANDO...')
    print('<<< VOLTE SEMPRE>>>')
    break
  print(f'Notas do {boletim[0][q-1]} são n1:{boletim[1][q-1]} e n2:{boletim[2][q-1]}')
  print('-' * 20)