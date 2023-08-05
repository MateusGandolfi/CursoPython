valores = []
for cont in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: '))) #ADICIONANDO OS NÚMEROS DIGITADO NA LISTA
print ('-='*20)
print (f'Você digitou os valores {valores}') #MOSTRANDO TODOS OS VALORES
print (f'O maior valor digitado foi {max(valores)} nas posições ', end='') #MOSTRANDO O MAIOR VALOR
for i, v in enumerate(valores):
    if v == max(valores): #SE O VALOR FOR IGUAL AO MAIOR, ELE IRÁ APARECER AS POSIÇÕES
        print (f'{i}...', end='') #MOSTRANDO A POSIÇÃO, COM UM END PARA CASO TENHA OUTRO NÚMERO IGUAL
print () #PRINT PARA NÃO DAR QUEBRA DE LINHA
print (f'O menor valor digitado foi {min(valores)} nas posições ', end='') #MOSTRANDO O MENOR VALOR
for i, v in enumerate(valores):
    if v == min(valores): #SE O VALOR FOR IGUAL AO MENOR, ELE IRÁ APARECER AS POSIÇÕES
        print (f'{i}...', end='') #MOSTRANDO A POSIÇÃO, COM UM END PARA CASO TENHA OUTRO NÚMERO IGUAL
print () #PRINT PARA NÃO DAR QUEBRA DE LINHA