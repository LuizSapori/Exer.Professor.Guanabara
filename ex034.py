salario = float(input('Qual o seu salário? R$ '))
if salario > 1250.00:
    print('O seu novo salário é: R$ {:.2f} '.format(salario*1.10))
else:
    print('O seu novo salário é: R$ {:.2f} '.format(salario * 1.15))