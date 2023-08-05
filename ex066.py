soma = cont = 0 #SOMA E CONTADOR RECEBE VALOR DE 0

while True:
    num = int(input('Digite um número [999 PARA PARAR]: '))
    if num == 999: # CÓDIGO PARA DAR PONTO DE PARADA
        break # PONTO DE PARADA
    soma += num # SOMA
    cont += 1 # CONTADOR
print (f'A soma dos {cont} valores foi {soma}!')

