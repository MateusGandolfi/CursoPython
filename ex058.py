from random import randint

n = 1
computador = randint(0, 10)

print ('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

acertou = False #Já irá começar como errado, porém assim que for "True" irá ser considerado vitória.
palpite = 0

while not acertou: #Enquanto não acertar irá continuar.
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1 #Quando der um palpite, irá receber + um palpite na contagem.
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador: #Se o jogador jogou um número MAIOR que o computador.
            print ('Mais... Tente mais uma vez: ')
        elif jogador > computador: #Se o jogador jogou um número MENOR que o computador.
            print ('Menos... Tente mais uma vez: ')

print (f'Você acertou com {palpite} tentativas. Parabéns!')
