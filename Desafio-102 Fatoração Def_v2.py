def fatorial (n,show = False):
    """
    -> Calcula o fatorial de um numero
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostar a conta.
    :return: valor do fatorial de um numero n

    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end='')
            if c >1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *=c
    return f

#principal
print(fatorial(5,True))
help(fatorial)
