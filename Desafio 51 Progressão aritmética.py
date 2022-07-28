print('='*10)
print('{}'.format('10 TERMOS DE UMA PA'))
print('='*10)
c=0
p=int(input('Primeiro termo: '))
r=int(input('Razão'))
f=10*r+p
for c in range(p,f,r):
    print(c, end=' > ')
print('Acabou',end='')
