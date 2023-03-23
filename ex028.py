import random
import time
computador = random.randint(0, 5) #FAz o computador pensar
print('---'*20)
print('Vou pensar em um número entre 0 e 5.Tente advinhar...')
print('---'*20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
time.sleep(3)
if jogador == computador:
    print('Parabéns! VocÊ conseguiu acertar')
else:
    print('Você perdeu!!')
