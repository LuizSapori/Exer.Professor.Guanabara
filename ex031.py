n1 = float(input("Qual a distância da viagem? "))
if n1 <= 200:
    print('O valor da viagem é R$ {}'.format(n1*0.50))
else:
    print('O valor da passagem é R$ {}'.format(n1*0.45))
print('Boa viagem!!!')