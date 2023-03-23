print('--**--'*20)
print('TABUADA DE INTEIROS')
print('--**--'*20)
while True:
    n = int(input('Digite um número:  '))
    if n < 0:
        print('Tente outra vez.')
        break
    for c in range(0,11,1):
        print(f'{n} x {c} = {n*c}')
print('Fim')