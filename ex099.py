from time import sleep


def maior(*núm):
    cont = maior = 0
    print('\n Analisando os valores...')
    print('-=-' * 30)
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print(f' Foram informados {cont} valores ao todos.')
    print(f' O maior valor informado foi {maior}. ')


maior(2,9,4,5,7,1)
maior(4,7,8)
maior()