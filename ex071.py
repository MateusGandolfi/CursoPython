print ('='*32)
print ('{:^32}'.format('MARQUINHOS AGIOTA'))
print ('='*32)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd: # SE O TOTAL FOR MAIOR OU IGUAL A CÉDULA 50
        total -= céd # SERÁ TIRADO 50 REAIS DO TOTAL
        totcéd += 1 # TODA VEZ QUE FOR TIRADO 50 REAIS IRÁ AUMENTAR +1 TOTAL DE CÉDULAS
    else:
        if totcéd > 0:
            print (f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print ('='*32)
print ('Volte sempre ao MARQUINHOS AGIOTA! Tenha um Bom dia!')
