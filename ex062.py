n1 = int(input('Digite seu número: '))
r1 = int(input('Razão da Progressão: '))
t1 = n1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(t1), end='')
        t1 = t1 + r1
        c = c + 1
    print('Pausa!!!!')
    mais = int(input('Quantos termos você quer a mais? '))
print('Fim')