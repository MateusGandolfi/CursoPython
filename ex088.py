from time import sleep
from random import randint
lista = []
jogos = []
print ('-'*30)
print (f'      JOGO NA MEGA SENA')
print ('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1 #ELE IRA COMECAR COM 1 PARA NAO COMECAR DO 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista: #SE O NUMERO NAO ESTIVER NA LISTA, EU ADICIONO ELE, FAZENDO ASSIM COM QUE NAO SE REPITA
            lista.append(num)
            cont += 1
        if cont >= 6: #COMO SAO UMA LISTA DE 6 NUMEROS, ASSIM QUE FOR IGUAL OU MAIOR QUE 6 NUMEROS, IRA QUEBRAR A LISTA
            break
    lista.sort() #ORGANIZA A LISTA EM ORDEM CRESCENTE
    jogos.append(lista[:]) #ADICIONA EM JOGOS A LISTA, POREM FAZENDO UMA COPIA USANDO [:]
    lista.clear() #APOS TER FEITO UMA COPIA DA LISTA, APAGA ELA PARA NAO TER DUPLICAGEM
    tot += 1 #IRA ADICIONAR 1 NO TOTAL PARA NAO TER UM LOOP INFINITO
print ('-='*3, f' SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos): #PARA CADA INDICE DA LISTA NO ENUMERADO DE JOGOS, ELE IRA MOSTRAR
    print (f'Jogo {i+1}: {l}')
    sleep (1)
print ('-='*4, '< BOA SORTE! >', '-='*4)