n1 = int(input('Digite seu número: '))
r1 = int(input('Razão da Progressão: '))
c = 1
while c <=10:
    print('{}'.format(n1+r1), end='')
    print(',' if c < 11 else '', end='')
    n1 = n1 + r1
    c = c + 1
print('Fim')