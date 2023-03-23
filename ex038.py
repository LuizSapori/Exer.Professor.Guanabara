n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O maior valor é {} e o menor valor é {}'.format(n1,n2))
elif n2 > n1:
    print('O manior valor é {} e o menor valor é {}'.format(n2,n1))
else:
    print('O valor {} e {} são iguais'.format(n1,n2))
