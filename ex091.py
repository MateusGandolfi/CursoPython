from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
ranking = [] #DEVERA TRATAR O RANKING COMO UMA LISTA

print ('Valores sorteados:')
for k, v in jogo.items():
    print (f'{k} tirou {v} no dado. ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
#SORTED=ORGANIZAR, KEY=ITEMGETTER=PEGA O VALOR, REVERSE=TRUE IRA DO MAIOR PARA O MENOR
#ELE IRA ORGANIZAR OS ITEMS DE JOGO EM ORDEM DO MAIOR PARA O MENOR, E IRA PEGAR OS VALORES OU SEJA, POSICAO 1
print ('-='*15)
print ('  == RANKING DOS JOGADORES ==')
for indice, v in enumerate(ranking):
    print (f'  {indice+1}° lugar: {v[0]} com {v[1]}.') #INDICE = POSICAO, V[0] = NOME, V[1] = VALOR DO DADO
    sleep(1)