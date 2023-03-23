n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
s = 0
while s != 5:
    print( ' Selecione a opção: \n [ 1 ] somar \n [ 2 ] multiplicar \n [ 3 ] maior \n [ 4 ] novos números \n [ 5 ] sair do programa')
    s = int(input('Opção: '))
    if s == 1:
        print(n1 + n2)
    elif s == 2:
        print(n1 * n2)
    elif s == 3 and n1 > n2:
        print('O {} é maior que {}.'.format(n1, n2))
    elif s == 3 and n2 > n1:
        print('O {} é maior que {}.'.format(n2, n1))
    elif s == 3 and n1 == n2:
        print('Os número {} e {} são iguais'.format(n1, n2))
    elif s == 4:
        print('Digite os novos número! ')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif s == 5:
        print('Finalizando!!!')
    print('--==--' *20)
print('Volte sempre!!')