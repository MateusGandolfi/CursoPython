from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0

while escolha != 5:

    print (f'\033[1;34mOque deseja fazer com os valores {n1} e {n2}?\033[m')
    print ('''\033[1;36m[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa\033[m''')
    escolha = int(input('>>>> Digite a sua opção: '))

    if escolha == 1:
            print (f'A soma entre {n1} + {n2} é {n1+n2}')
    elif escolha == 2:
            print (f'O resultado de {n1} x {n2} é {n1*n2}')
    elif escolha == 3:
        if n1 > n2: # Se o primeiro número for maior que o segundo número, o primeiro será o maior.
            print (f'O maior número entre {n1} e {n2} é {n1} ')
        else: # Se o primeiro número for menor que o segundo número, o segundo será o menor.
            print (f'O maior número entre {n1} e {n2} é {n2} ')
    elif escolha == 4:
            print ('Digite os novos números: ')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print ('Saindo do programa...')
    else:
        print ('Opção inválida. Tente novamente!')
    print ('\033[1;32m-=\033[m'*20)
    sleep (1)
print ('\033[1;31mFim do programa, volte sempre!\033[m')