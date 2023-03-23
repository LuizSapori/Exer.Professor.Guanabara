print('{:=^40}'.format('LOJAS DO CABEÇA '))
pr = float(input('Preço do produto: (R$) '))
sl = float(input('Selecione a forma de pagamento: \n [1] DINHEIRO / CHEQUE \n [2] CARTÃO A VISTA \n [3] CARTÃO 2X \n [4] CARTÂO 3X OU MAIS \n Qual é a opção? '))
if sl == 1:
    print('VALOR DO PRODUTO: R$ {} '.format(pr * 0.90))
elif sl == 2:
    print('VALOR DO PRODUTO: R$ {} '.format(pr * 0.95))
elif sl == 3:
    parcela1 = pr / 2
    print('VALOR DO PRODUTO: R$ {}. TOTAL DE 2 X DE R$ {}.'.format(pr,parcela1))
elif sl == 4:
    print('VALOR DO PRODUTO: R$ {} '.format(pr*1.20))
    parcela2 = float(input('NÚMERO DE PARCELAS: '))
    print('O DE PARCELAS SERÁ DE {} VEZES. TOTALIZANDO {} POR MÊS.'.format(parcela2,(pr*1.20/parcela2)))
else:
    print("OPÇÃO DE PAGAMENTO INEXISTENTE. SELECIONE OUTRA VEZ.")
