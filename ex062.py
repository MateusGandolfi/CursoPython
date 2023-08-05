print ('Gerador de PA 3.0')
print ('-='*8)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0 
mais = 10

while mais != 0: # SE A QUANTIDADE DE TERMOS MOSTRADA FOR DIFERENTE DE 0 IRÁ CONTINUAR
    total = total+mais # O TOTAL MOSTRADO SERÁ O TOTAL + A QUANTIDADE QUE ELE IRÁ QUERER
    while cont <= total:
        print (f'{termo} ➝  ', end='')
        termo += razão
        cont += 1
    print ('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print (f'Progresso finalizada, com {total} termos mostrados.')
