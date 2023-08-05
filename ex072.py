cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'doze', 'treze',
    'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
    'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print ('Tente novamente!', end =' ')
        continue
    if 0 <= num <= 20:
        print (f'Você digitou o número {cont[num]}')
        print ('-='*13)
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print ('-='*13)
    if escolha in 'S':
        continue
    if escolha in 'N':
        break
print ('Fim do programa, volte sempre!')
