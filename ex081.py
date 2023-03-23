valores = []
soma = 0
while True:
    n = valores.append(int(input('Digite um número: ')))
    soma = soma + 1
    cont = input(str(('Deseja continuar S/N?'))).strip().upper()
    if cont == 'N':
        print(f'Lista de valores {valores}')
        print(f'Foram digitados {soma} números.')
        valores.sort(reverse=True)
        print(f'A lista em ordem descrescente é {valores}.')
        print(f'O valor 5 foi digitado {valores.count(5)} vezes.')
        break
print('Fim')

#if 5 in valores:
#   print('O valor 5 está na lista')
# else:
#   print('O valor 5 não está na lista.')


