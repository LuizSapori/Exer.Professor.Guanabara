valores= []
for c in range(0,5):
    valores.append(int(input('Digite um valor:')))
print(f'O menor valor encontrado foi {min(valores)} e o maior valor encontrado {max(valores)}.')
valores.sort()
print(valores)
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei os valores {v}')

# ATENÇÂO: PARA MAIOR E MENOR EXISTE TAMBÈM ESSA OPÇÂO ABAIXO!!!
# maior= 0
# menor = 0
#  If c == 0:
#    maior = menor = valores[c]
# else:
#    if valores[c]>maior:
#       maior = valores[c]
#    If valores [c] < menor:
#       menor = valores[c]