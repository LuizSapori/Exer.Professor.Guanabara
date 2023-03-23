numeros = list()
par = list()
impar = list()
for c in range(1,8):
    numeros.append(int(input(f'Digite o {c}° número: ')))
    if numeros[0] % 2 == 0:
        par.append(numeros[:])
        numeros.clear()
    elif numeros[0] % 2 == 1:
        impar.append(numeros[:])
        numeros.clear()
print(f'Os números pares são {sorted(par)}.')
print(f'Os numeros impares são {sorted(impar)}')