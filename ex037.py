n1 = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão: \n [1] Binário \n [2] Octal \n [3] Hexadecimal')
conversao = int(input('Base: '))
if conversao == 1:
    print('{} convertido para binário é {}'.format(n1,bin(n1)))
elif conversao == 2:
    print('{} convertido para Octal é {}'.format(n1, oct(n1)))
elif conversao == 3:
    print('{} convertido para Hexadecimal é {}'.format(n1, hex(n1)))
else:
    print('Opção Invalida!!')
