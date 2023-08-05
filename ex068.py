from random import randint
vitória = 0

print ('-='*15)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('-='*15)

while True:
    num = int(input('Diga um valor: '))
    bot = randint(0,11)
    total = num+bot
    escolha = ' ' 
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0] #Tira todos os espaços, deixa tudo em maiúsculo e considera apenas primeira letra

    if (num + bot) % 2 == 0: #RESULTADO SE FOR DIVIDO POR 2 = PAR. SE NÃO = IMPAR
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print ('-='*15)
    print (f'Você jogou {num} e o computador {bot}. Total de {total} DEU {resultado}')
    print ('-='*15)

    if escolha == 'P':
        if total % 2 == 0: #VITÓRIA PAR
            print ('VOCÊ GANHOU!')
            vitória += 1
        else:
            print ('VOCÊ PERDEU!')
            print ('-'*30)
            break
    elif escolha == 'I':
        if total % 2 == 1: #VITÓRIA IMPAR
            print ('VOCÊ GANHOU!')
            vitória += 1
        else:
            print ('VOCÊ PERDEU!')
            print ('-'*30)
            break
    print ('Vamos jogar novamente...')
    print ('-='*15)
print (f'GAME OVER! Você venceu {vitória} vezes.')



