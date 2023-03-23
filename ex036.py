valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
tempo = int(input('Qual o tempo do empréstimo em meses? '))
mensalidade = float(valor/tempo)
if mensalidade > (salario * 0.30):
    print('A sua parcela de R$ {:.2f} mensal excede o limite autorizado, empréstimo recusado.'.format(mensalidade))
else:
    print('A sua parcela de R$ {:.2f} mensal foi aceita, empréstimo aceito. '.format(mensalidade))
print('Luiz Banco agradece a sua preferência')