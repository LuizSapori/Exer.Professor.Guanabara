import random
itens = ('PEDRA, PAPEL,TESOURA')
computador = random.randint(0,2)
n1 = input('SELECIONE \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA \n QUAL A SUA OPÇÃO? ')
if computador == 0 and n1 == 1:
    print('COMPUTADOR  ESCOLHEU {}. DEU EMPATE!'.format(0))
elif computador == 0 and n1 == 2:
    print('COMPUTADOR  ESCOLHEU {}. VOCÊ GANHOU!'.format(0))
elif computador == 0 and n1 == 3:
    print('COMPUTADOR  ESCOLHEU {}.VOCÊ PERDEU'.format(0))
if n1 == 2 and computador == c1:
    print('COMPUTADOR ESCOLHEU {}. VOCÊ VENCEU!'.format(c1))
elif n1 == 2 and computador == c2:
    print('COMPUTADOR ESCOLHEU {}. DEU EMPATE'.format(c2))
elif n1 == 2 and computador == c3:
    print('COMPUTADOR ESCOLHEU {}. VOCÊ PERDEU!'.format(c3))
if n1 == 3 and computador == c1:
    print('COMPUTADOR ESCOLHEU {}. VOCÊ PERDEU!!'.format(c1))
elif n1 == 3 and computador == c2:
    print('COMPUTADOR ESCOLHEU {}. VOCÊ VENCEU!!'.format(c2))
elif n1 == 3 and computador == c3:
        print('COMPUTADOR ESCOLHEU {}. DEU EMPATE!!'.format(c3))
print('TENTE OUTRA VEZ!!!')