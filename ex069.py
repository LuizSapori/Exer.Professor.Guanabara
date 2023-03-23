s = 0
i = 0
m = 0
while True:
    nome = str(input("Qual o seu nome completo: "))
    idade = int(input('Digite a sua idade: '))
    if idade >= 18:
        i = i +1
    sexo = ' '
    while sexo not in 'HM':
        sexo = str(input('HOMEM [H] / MULHER [M]? ')).strip().upper()
    if sexo == 'H':
        s = s +1
    if sexo == 'M' and idade <= 20:
        m = m + 1
    c = ' '
    while c not in 'SN':
        c = input(print('Você deseja continuar? SIM [S] ou Não [N]? ')).strip().upper()
    if c == 'N':
        print(f'Você tem {i} pessoas com mais de 18 anos, {s} homens cadastrados e {m} mulheres com menos de 20.')
        print('FIM')
        break
    else:
        print('Vamos continuar!!!!')