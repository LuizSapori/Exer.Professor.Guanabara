import random
computador = random.randint(1,10)
print('Pensei em um número entre 1 e 10, você sabe qual é?')
contador = 0
acertou = False
while not acertou:
    jogador = int(input('Digite um número: '))
    contador = contador +1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais, tem mais uma vez!!!!')
        elif computador < jogador:
            print ('Menos, tente outra vez!!!!!')
print('Fim do jogo, você acertou em {} tentativas!!!'.format(contador))