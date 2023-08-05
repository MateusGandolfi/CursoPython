# Se em uma funcao, eu adicionar valores aos parametros, eles passam a ser opcionais, e caso
# o nome do jogador ficar vazio, ele ira ganhar o valor '<desconhecido>' e o gol, ira ficar como 0
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():  # Se o gol for numero, ele ira deixar de ser uma string, e passara ser uma int
    g = int(g)
else:
    g = 0  # Se ele nao for numerico, ele estara vazio, sendo assim ira ganhar o valor de 0
if n.strip == '':  # Se o nome do jogador, apos tirar todos os espacos continuar vazio, ele ira apenas ler o gol
    ficha(gol=g)
else:  # Se o nome do jogador nao estiver vazio, ele ira ler o gol e o nome do jogador.
    ficha(n, g)
