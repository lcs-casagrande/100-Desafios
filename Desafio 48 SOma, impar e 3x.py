r=0
v=0
for n in range(1,501,2):
    if n%2==1 and n%3==0:
        r +=n
        v +=1

print('A soma de todos os {} valores solicitados é {}' .format(v,r))
