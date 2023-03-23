n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Sua média é {}. REPROVADO!!'.format(media))
elif media > 5 and media < 6.9:
    print(' Sua média é {}. RECUPERAÇÂO'.format(media))
elif media > 6.9:
    print('Sua média é {}. Você foi aprovado!!'.format(media))