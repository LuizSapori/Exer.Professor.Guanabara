import random
n1 = str(input(('Primeiro Aluno: ')))
n2 = str(input(('Segundo Aluno: ')))
n3 = str(input(('Terceiro Aluno: ')))
n4 = str(input(('Quarto Aluno: ')))
lista =[n1,n2,n3,4]
random.shuffle(lista)
print('Ordem de apresentação será:')
print(lista)
