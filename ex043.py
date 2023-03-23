p = float(input('Qual o seu peso?   Kg '))
H = float(input('Qual a sua altura?  metros '))
IMC = p/(H**2)
if IMC < 18.5:
    print('Seu IMC é {:.2f}. ABAIXO DO PESO'.format(IMC))
elif IMC >=18.5 and IMC < 25:
    print('Seu IMC é {:.2f}. PESO IDEAL'.format(IMC))
elif IMC >=25 and IMC < 30:
    print('Seu IMC é {:.2f}. SOBREPESO'.format(IMC))
elif IMC >= 30 and IMC < 40 :
    print('Seu IMC é {:.2f}. OBESIDADE'.format(IMC))
elif IMC >= 40:
    print('Seu IMC é {:.2f}. OBESIDADE MORBIDA')
