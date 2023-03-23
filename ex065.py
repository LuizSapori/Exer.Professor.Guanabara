p = 'S' or 's'
count = 0
soma = 0
maior = 0
menor = 0
while p == 'S' or p == 's':
    n = int(input('Digite um número: '))
    p = str(input(('Quer continuar [S]/[N]: ').strip().upper()))
    count = count + 1
    soma = soma + n
    if n == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
if p != 'S' or p != 's':
    med = soma/count
    print('A média dos inteiros é {}'.format(med))
    print('O maior número é {} e o menor é {}.'.format(maior,menor))