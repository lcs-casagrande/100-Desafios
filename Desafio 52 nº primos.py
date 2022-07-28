n=int(input('Digite um numero: '))
d=0
for c in range (1,n+1):
    if n%c==0:
        d+=1
        print('\033[33m', end=' ')
        print(c, end=' ')
    else:
        print('\033[31m', end=' ')
        print('{}' .format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.' .format(n,d))
if d==2 or n==1:
    print('{} é primo ' .format(n))
else:
    print('{} não é primo' .format(n))
