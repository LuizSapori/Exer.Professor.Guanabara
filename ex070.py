soma = 0
produtos = 0
menor = 0
contador = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Preço R$: '))
    soma = soma + preco
    contador = contador + 1
    if preco >= 1000:
        produtos = produtos + 1
    if contador == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    c = ' '
    while c not in 'SN':
        c = input(str('Você deseja continuar SIM [S] ou NÃO [N]? ')).strip().upper()
    if c == 'N':
        print('Operação finalizada')
        print(f'{barato} tem preço mais barato de {menor :.2f}, existe {produtos} produtos mais que R$ 1.000 e o total é {soma} ')
        print('FIM')
        break
    else:
        print('Vamos continuar!')