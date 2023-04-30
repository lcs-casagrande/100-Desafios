def fatorial (n,show=False):
    fat=n
    if show == True:
        print(f'{n} x ', end='')
    while n >2:
        n=n-1
        fat=fat*n
        if show == True:
            print(f'{n} X ', end='')
            if n==2:
                print('1 = ', end='')


    print(f'{fat}')


print(fatorial(5,True))
