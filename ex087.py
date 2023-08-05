matriz = [[0,0,0],[0,0,0],[0,0,0]] #3 LISTAS COM 3 VALORES, POIS UMA MATRIZ É 3X3
spar = mai = scol = 0 #SOMA PAR, MAIOR, SOMA COLUNA

for linha in range (0,3):
    for coluna in range (0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print ('-='*20)
for linha in range (0,3):
    for coluna in range (0,3):
        print (f'[{matriz [linha] [coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0: #SE A MATRIZ LINHA E COLUNA, FOR DIVISIVEL POR 2, ELA SERÁ ADICIONADO A VARIAVEL SOMA PAR
            spar += matriz [linha][coluna]
    print () #PRINT VAZIO PARA NÃO FICAR TUDO NA MESMA LINHA
print ('-='*20)

print (f'A soma dos valores pares é {spar}') 
for linha in range (0,3):
    scol += matriz[linha][2] #ELE IRÁ FAZER A SOMA DA TERCEIRA COLUNA, OU SEJA LINHA [2] (POIS COMEÇA COM 0,1,2)
print (f'A soma dos valores da tarceira coluna é {scol}')

for coluna in range (0,3):
    if coluna == 0: #SE A COLUNA FOR IGUAL A 0, SERÁ A PRIMEIRA COLUNA
        mai = matriz[1][coluna] #LOGO O MAIOR SERÁ A MATRIZ NA LINHA 2 
    elif matriz[1][coluna] > mai: #SE A MATRIZ FOR MAIOR DO QUE O MAIOR, ELA PASSA A SER O MAIOR
        mai = matriz[1][coluna]
print (f'O maior valor da segunda linha é {mai}')