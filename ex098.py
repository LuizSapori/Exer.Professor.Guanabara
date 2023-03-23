from time import sleep
def contador(*num):
    print('Contagem de 1 até 10, de 1 em 1... ')
    print('--'*30)
    for c in range(1,11,1):
        print(f'{c } ', end='')
        sleep(0.5)
    print('Fim',end='')
    print()
    print('--' * 30)
    print('Contagem de 10 até 0, de 2 em 2... ')
    print('--' * 30)
    for m in range(10,0,-2):
        print(f'{m } ', end='')
        sleep(0.5)
    print('Fim',end='')
    print()
    print('Agora é a vez de personalizar!')
    a = int(input('Início: '))
    b = int(input('Fim: '))
    c = int(input('Salto: '))
    if c == 0:
        c = 1
    for l in range(a,b+c,c):
        print(f'{l } ', end='')
        sleep(0.5)
    print('Fim', end='')


contador()