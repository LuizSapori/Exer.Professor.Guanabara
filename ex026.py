nome = str(input('Digite um nome: ')).strip()
n1 = nome.upper()
print('A letra a aparece {} vezes,\n Acontece primeiro em {} \n Acontece por último {}'.format(n1.count('A'),n1.index('A'),n1.rfind('A')))