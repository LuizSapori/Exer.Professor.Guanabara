from datetime import date
n1 = int(input('Qual o seu ano de nacimento? '))
n2 = date.today().year - n1
if n2 <= 9:
    print('Você nasceu tem {} anos. MIRIM!'.format(n2))
elif n2 > 9 and n2 <= 14:
    print('Você tem {} anos. INFANTIL!'.format(n2))
elif n2 > 14 and n2 <= 19:
    print('Você tem {} anos.JUNIOR!'.format(n2))
elif n2 > 19 and n2 <= 25:
    print('Você tem {} anos.SENIOR!!'.format(n2))
elif n2 > 25:
    print('Você tem {} anos. MASTER!!!!'.format(n2))
