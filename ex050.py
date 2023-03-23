soma = 0
count = 0
for c in range(0,6,1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma = soma + n
        count = count + 1
print('A SOMA DOS VALORES É {} E EXISTEM {} NÚMEROS'.format(soma,count))