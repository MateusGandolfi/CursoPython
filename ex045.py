from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('''\033[1;35mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA\033[m''')
jogador = int(input('\033[1;35mQual é a sua jogada?\033[m ')) 
print ('\033[1;36mJO \033[m')
sleep (1)
print ('\033[1;36mKEN \033[m')
sleep (1)
print ('\033[1;36mPO!!! \033[m')
print ('\033[1;34m-=\033[m'*15)
print (f'\033[1;34m O computador escolheu {itens[computador]} \033[m')
print (f'\033[1;34m O jogador escolheu {itens[jogador]} \033[m')
print ('\033[1;34m-=\033[m'*15)
if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print ('\033[0;33mEMPATE!\033[m')
    elif jogador == 1:
        print ('\033[0;32mJOGADOR GANHOU!\033[m')
    elif jogador == 2:
        print ('\033[0;31mCOMPUTADOR GANHOU!\033[m')
    else:
        print ('\033[0;31mOPÇÃO INVÁLIDA, tente novamente!\033[m')
elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print ('\033[0;32mJOGADOR GANHOU!\033[m')
    elif jogador == 1:
        print ('\033[0;33mEMPATE!\033[m')
    elif jogador == 2:
        print ('\033[0;31mCOMPUTADOR GANHOU!\033[m')
    else:
        print ('\033[0;31mOPÇÃO INVÁLIDA, tente novamente!\033[m')
elif computador == 2: # Computador jogou Tesoura
    if jogador == 0:
        print ('\033[0;32mJOGADOR GANHOU!\033[m')
    elif jogador == 1:
        print ('\033[0;31mCOMPUTADOR GANHOU!\033[m')
    elif jogador == 2:
        print ('\033[0;33mEMPATE!\033[m')
    else:
        print ('\033[0;31mOPÇÃO INVÁLIDA, tente novamente!\033[m')
else:
    print ('\033[0;31mOPÇÃO INVÁLIDA, tente novamente!\033[m')
