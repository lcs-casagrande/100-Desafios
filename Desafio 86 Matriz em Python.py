matriz = [[[], [], []], [[], [], []], [[], [], []]]

for x in range (0,3):
    for y in range (0,3):
        valor = int(input(f'Digite um valor para [{x},{y}] '))
        matriz[x][y].append(valor)
print('-=' *50)
for p in matriz:
    print(p)


