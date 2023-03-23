soma = soma3 = 0
maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número [{l} x{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]
        if c == 2:
            soma3 = soma3 + matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[l][c]
print('==**=='*5)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('==**=='*5)
print(f'A soma dos valores pares da matriz é : {soma}')
print(f'A soma da terceira coluna da matriz é : {soma3}')
print(f'O maior número da segunda linha é: {maior}')
