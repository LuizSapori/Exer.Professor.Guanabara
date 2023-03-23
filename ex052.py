n = int(input('Digite um número: '))
count = 0
for c in range(1,n+1,1):
    if n % c == 0:
        print('\033[33m', end='')
        count = count +1
    else:
        print('\033[31m', end='')
    print('{}'.format(c))
print('\n\033[m O número {} é divisível {} vezes.'.format(n,count))
if count == 2:
    print('ESSE NÙMERO É PRIMO!!!!')
else:
    print('ESSA MERDA NÂO É PRIMO!!!!')
