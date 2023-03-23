print('--==--'*20)
print('Sequência de Fibonacci')
print('--==--'*20)
f1 = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
count = 3
print('{} -> {} '.format(t1,t2), end='')
while count <= f1:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count = count + 1
print(' FIm!!!')
