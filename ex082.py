valores = []
n1 = []
n2 = []
while True:
    n = valores.append(int(input('Digite uma valor: ')))
    continuar = str(input('Deseja continuar S/N: ')).strip().upper()
    if continuar == 'N':
        break
for i,v in enumerate(valores):
    if v % 2 ==0:
        n1.append(v)
    if v % 2 ==1:
        n2.append(v)
print(valores)
print(f'Os valores pares são{n1}')
print(f'Os valores ímpares são {n2}.')
print('Fim')