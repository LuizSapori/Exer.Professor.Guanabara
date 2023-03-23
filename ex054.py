from datetime import date
atual = date.today().year
count = 0
for c in range(0,7):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = atual - nascimento
    if idade >= 18:
        count = count +1
print('Das 7 pessoas matriculadas, {} pessoas possuem a maioridade e {} não possuem.'.format(count,(7 - count)))