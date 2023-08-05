from random import randint
from time import sleep

def sorteia(lista):
    print ('Sorteando 5 valores da lista: ', end='')
    for cont in range (0,5): #Apenas dando 5 numeros randomizados
        n = randint(1,10) #Randomizando numeros de 0 a 10
        lista.append(n)
        print (f'{n} ', end='', flush=True) #Funcao flush para nao dar buffering na funcao sleep
        sleep (0.3)
    print ('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista: #Para cada valor na lista, ele ira verificar se o numero e par
        if valor % 2 == 0: #Se o numero da lista for par, ele ira somar com os outros que forem par
            soma += valor
    print (f'Somando os valores pares de {lista}, temos {soma}')

#Programa Principal
numeros = list()
sorteia (numeros)
somaPar (numeros)