num = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
       'Transferidor', 4.20, 'Compasso', 9.99,'Mochila', 120.32,
       'Canetas', 22.30,'Livro', 34.90)
itens = 0
preco = 0
print('==='*14)
print('Lista de Produtos e Preços')
print('==='*14)
for c in range(0,len(num),2):
    itens = c
    preco = itens +1
    print(f'{num[itens]:.<30} R$ {num[preco]:>5.2f}')
print('===' * 14)