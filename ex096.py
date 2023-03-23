def area(a,b):
    s = a * b
    print(f'O terreno com Largura {a} e Comprimento {b} tem área de  {s} m². ')


print('    Controle de Terrenos')
print('-=-' *10)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a,b)
