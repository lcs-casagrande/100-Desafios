import math
co=float(input('Qual é o cateto oposto?'))
ca=float(input('Qual o cateto adjacente?'))
hi=math.hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hi))