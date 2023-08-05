total = totmil = menor = cont = 0 #DANDO VALOR 0 PARA VARIAVEIS
barato = '' #USANDO STR PARA DAR UM NOME A UM FORMAT

print ('-='*15)
print ('     LOJINHA DO SEU ZÉ')
print ('-='*15)

while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Preço: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor: #SIMPLIFCANDO MOSTRANDO QUE O PRIMEIRO VALOR JÁ SERÁ VALIDADO COMO O MENOR
        barato = produto
        menor = valor 
    print ('-='*15)
    escolha = ' '
    while escolha not in 'SN':  
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print ('-='*15)
    if escolha == 'N':
        break
print ('----------FIM DO PROGRAMA----------')
print (f'O total da compra foi R${total:.2f}')
print (f'Temos {totmil} produtos custando mais de R$1000.00')
print (f'O produto mais barato foi {barato} que custa {menor:.2f}')