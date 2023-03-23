pessoas = []
peso = []
maior = menor  = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(peso) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas [1]
    peso.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Deseja continuar S/N? ').strip().upper())
    if continuar == 'N':
        print(f'Os dados são {peso}')
        print(f'O número de pessoas cadastradas foi de {len(peso)}')
        break
print(f'O maior peso foi de {maior} Kg.,',end='')
for p in peso:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor} Kg.', end='')
for p in peso:
    if p[1] == menor:
        print(f'{p[0]}')
print('Fim!!!')