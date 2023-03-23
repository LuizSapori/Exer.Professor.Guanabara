valores = list()
maior = 0
menor = 0
for c in range(0,5):
    n = int(input('Digite um valor:'))
    if c == 0:
        valores.append(n)
        print('Adicionado ao final da lista...')
    elif n > valores[len(valores)-1]: #ou valores[-1]
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n<= valores[pos]:
                valores.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos = pos +1
print(f'Os valores digitados em ordem foram {valores}')