matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Sao 3 listas com 3 valores, pois uma matriz e constituida por 9 valores

for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print ('-='*20)
for linha in range (0, 3): 
    for coluna in range (0, 3):
        print (f'[{matriz [linha] [coluna]:^5}]', end='')
    print () #PRINT VAZIO COM UMA IDENTAÇÃO PARA FRENTE PARA NÃO FICAR TOTALMENTE NA MESMA LINHA
