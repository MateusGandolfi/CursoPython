from time import sleep

cadastro = {}
partidas = []
time = []

while True:
    cadastro.clear()  # DANDO UM CLEAR, POIS IRA ENTRAR UM NOVO JOGADOR E SERA OUTRO DICIONARIO
    cadastro['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {cadastro["Nome"]} jogou? '))
    partidas.clear()  # TIRANDO AS OUTRAS PARTIDAS, PARA NAO FICAR JUNTANDO O TOTAL DE GOL DE UM JOGADOR COM O OUTRO
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    cadastro['Gols'] = partidas[:]
    # O TOTAL E A SOMA QUE ESTA EM PARTIDA, OU SEJA O TOTAL DE GOLS QUE O JOGADOR FEZ
    cadastro['Total'] = sum(partidas)
    # IRA FAZER UMA COPIA, NAO SE USA [:] POIS E UM DICIONARIO E NAO UMA LISTA
    time.append(cadastro.copy())
    while True:
        escolha = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if escolha in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if escolha == 'N':
        break
print('-='*20)
print('Cod. ', end='')
for i in cadastro.keys():  # ELE IRA FAZER O CABECARIO, USANDO OS NOME DOS DICIONARIOS, EX: Nome,Gols,Total
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    for dados in v.values():  # PARA CADA DADOS NO ENUMERATE DE TIME, IRA MOSTRAR.
        print(f'{str(dados):<15}', end='')
    print()  # PRINT VAZIO PARA QUEBRA DE LINHA
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    # NAO E POSSIVEL ACHAR ALGUM JOGADOR QUE SEJA MAIOR DOS NUMEROS QUE EXISTE
    if busca >= len(time):
        print(f'ERRO! Nao existe o jogador com o codigo {busca}!')
    else:
        # O TIME E UMA LISTA, QUE DENTRO EXISTE A BUSCA QUE E UM DICIONARIO
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-'*40)
print('Finalizando programa...')
sleep(1)
print('<< VOLTE SEMPRE! >>')
