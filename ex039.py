from datetime import date
n1 = int(input('Qual o seu ano de nacimento? '))
nascimento = date.today().year - n1
if nascimento == 18:
    print('Você tem {} anos e já pode se alistar'.format(nascimento))
elif nascimento < 18:
    print('Você tem {} anos e não pode se alistar. Faltam {} anos para que possa se alistar'.format(nascimento,(18-nascimento)))
elif nascimento > 18:
    print('Você tem {} anos, passou {} anos para se alistar.'.format(nascimento,(nascimento-18)))