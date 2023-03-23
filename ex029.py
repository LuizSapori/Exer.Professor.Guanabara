velocidade = float(input('Qual a velocidade do Carro? '))
if velocidade <= 80:
    print('Velocidade regular {} Km'.format(velocidade))
else:
    print('A sua velocidade foi de {} Km'.format(velocidade))
    print('O valor da multa é R$ {:.2f}'.format((velocidade-80)*7))