n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando o fatorial de {}!'.format(n))
while c >0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    f = f * c
    c = c -1
print('{}'.format(f))

#from math import factorial
#n = int(input( 'Digite um número: '))
#f = factorial(n)
#print('O fatorial de n é {}'.format(f))

'''n = int(input('Digite seu fatorial: '))
for c in range(n-1,1,-1):
    n = n*c
    print(n)'''