num = (int(input( 'Digitie um número: ')),
    int(input('Digitie um número: ')),
    int(input('Digitie um número: ')),
    int(input('Digitie um número: ')))
print(f'Os valores digitador foram {num}')
print(f'O número de vezes que o 9 foi digitado {num.count(9)}.')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3)+1}°')
else:
    print('O número 3 não foi digitado.')
print(f'Os valores pares são:  ', end= ' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
