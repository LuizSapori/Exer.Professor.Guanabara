from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1,6),
'Jogador 2': randint(1,6),
'Jogador 3': randint(1,6),
'Jogador 4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k,v in jogo.items(): #ATENÇÃO!!!! ESSE FORMATO É PARA DICIONÁRIO
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True) #Pega chave do dicionário e as converte em tuplas.
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking): #ATENÇÃO!!!! ENUMERATE É PARA LISTA!!
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)