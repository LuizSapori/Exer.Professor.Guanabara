def fatorial (n, show=False):
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ',end='')
        f = f * c
    return f

n = int(input('Qual o número você deseja? '))
print(fatorial(n,show=True))