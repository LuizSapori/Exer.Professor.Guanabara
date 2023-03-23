somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1,5,1):
    print('------- {}ª PESSOA-------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M] ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade/4
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem,nomevelho))
print('O número de mulheres com menos de 20 anos é {}'.format(totmulher20))
