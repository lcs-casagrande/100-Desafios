matriz = [[0,0,0],[0,0,0],[0,0,0]]

maior = pares = terceira = 0
for x in range (0, 3):
    for y in range (0,3):
        matriz[x][y] = int(input(f'Digite um valor para [{x},{y}] '))

for x in range (0,3):
    for y in range (0,3):
        if x == 1 :
            if y == 0 or matriz[x][y] > maior :
                maior = matriz[x][y]

        if y == 2:
            terceira += matriz[x][y]
        if matriz[x][y] % 2 ==0:
            pares += matriz[x][y]



print('-=' * 50)
for p in matriz:
    print(p)
print(f'A soma dos valores pares é {pares} ')
print(f'A soma do valor da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')

