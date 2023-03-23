aprovacao = {}
aprovacao['nome'] = str(input('Nome do aluno: '))
aprovacao['nota'] = float(input('Média do aluno: '))
print('=++='*5)
print( '   - O nome do aluno é {}'.format(aprovacao['nome']))
print( f'   - A média da nota é {aprovacao["nota"]}') #dentro de aspas simples você tem que usar aspas duplas
if aprovacao['nota'] >= 7:
    print('   - O aluno está aprovado.')
if aprovacao['nota'] < 7 and aprovacao['nota'] >= 5:
    print('   - O aluno está em recuperação.')
if aprovacao['nota'] < 5:
    print('   - O aluno foi reprovado.')