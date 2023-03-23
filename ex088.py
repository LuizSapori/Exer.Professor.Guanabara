import time
from random import randint
from time import sleep
lista = list()
jogos = list()
print('=-=-='*10)
print('       JOGO DA MEGA SENA       ')
print('=-=-='*10)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot =1
while tot <= quant:
    cont=0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont +1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot +1
print('=-=-='*3, f'SORTEANDO {quant}JOGOS','=-=-='*3)
for i,l in enumerate(jogos):
    time.sleep(0.5)
    print(f'Jogo {i+1}: {l} ')