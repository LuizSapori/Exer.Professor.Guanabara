import random
import time
c = 0
c1 = 0
print('Jogo do par ou ímpar.')
while True:
    computador = random.randint(0, 10)
    print('--**--' * 20)
    print('Escolha um número de 0 - 10.')
    print('--**--' * 20)
    n = int(input('Escolha um número = '))
    time.sleep(0.5)
    s = str(input('Escolha PAR [P] ou ÍMPAR [I]: ')).strip().upper()
    jogo = computador + n
    c1 = c1 +1
    print(f'Você jogou {n} o computador jogou {computador}. O valor é {jogo}.')
    if jogo % 2 == 0 and s == 'P':
        c = c + 1
        print('Você ganhou!!!')
    if jogo % 2 != 0 and s == 'I':
        c = c + 1
        print('Você ganhou!!!')
    if jogo % 2 == 0 and s == 'I':
        print(f'Você perdeu. Foram {c1} jogos e {c} vitórias!!!')
        break
    if jogo % 2 != 0 and s == 'P':
        print(f'Você perdeu. Foram {c1} jogos e {c} vitórias!!!')
        break
print('FIM!!')
