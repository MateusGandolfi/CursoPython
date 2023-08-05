números = list()

while True:
    valores = (int(input('Digite um valor: ')))
    if valores not in números: #SE O VALOR JÁ ESTIVER NA LISTAGEM IRÁ ADICIONAR
        números.append(valores)
        print ('Valor adicionado com suceso...')
    else: #SE O VALOR ESTIVER NA LISTAGEM NÃO IRÁ ADICIONAR
        print ('Valor duplicado! Não vou adicionar...')
    escolha = ' '
    while escolha not in 'SN':
        print ('-='*20)
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print ('-='*20)
números.sort() #NÃO PODE COLOCAR O SORT DENTRO DO FORMAT
print (f'Você digitou os valores {números}')
