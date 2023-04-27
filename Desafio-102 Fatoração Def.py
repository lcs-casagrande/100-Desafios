def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return f


print(fatorial(5, True))
