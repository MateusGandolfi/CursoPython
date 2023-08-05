cadastro = {}
partidas = []

cadastro['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {cadastro["Nome"]} jogou? '))
for c in range (0, tot): 
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
cadastro['gols'] = partidas[:]
cadastro['total'] = sum(partidas) #O TOTAL E A SOMA QUE ESTA EM PARTIDA, OU SEJA O TOTAL DE GOLS QUE O JOGADOR FEZ
print ('-='*20)
print (cadastro)
print ('-='*20)
for k, v in cadastro.items():
    print (f'O campo {k} tem o valor {v}')
print ('-='*20)
print (f'O jogador {cadastro["Nome"]} jogou {len(cadastro["gols"])} partidas') #O LEN DE CADASTRO GOLS, E O TOTAL DE PARTIDAS, POIS GOLS E UMA COPIA DA LISTA PARTIDA
for i, v in enumerate(cadastro['gols']): #PARA CADA INDICE E VALOR EM GOLS, ELE IRA MOSTRAR
    print (f'    => Na partida {i+1}, fez {v} gols.')
print (f'Foi um total de {cadastro["total"]} gols')