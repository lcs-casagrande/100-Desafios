def dobrar (n=0):
    r = float(n*2)
    return r
def metade(n=0):
    return n/2

def aumentar(n=0,t=10):
    return n+(n*t/100)

def diminuir (n=0,t=10):
    return n-(n*t/100)

def moeda (preco=0,moeda='R$'):
    m = (f'{moeda} {preco:.2f}').replace('.',',')
    return m
