ano = int(input("Digite um ano: "))
if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {}ão é Bissexto'.format(ano))