from random import randint
from time import sleep

print ('-=-'*17)
print ('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print ('-=-'*17)
n = int(input('Digite o número que eu pensei: '))
print ('PROCESSANDO...')
sleep (2)
r1 = randint(0, 5)

if n == r1:
    print ('PARABÉNS, você conseguiu me vencer!')
else:
    print (f'EU GANHEI, eu pensei no número {r1} e não no {n}!')