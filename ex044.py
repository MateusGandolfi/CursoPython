preço = float(input('Preço das compras: R$'))
print ('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço*10/100)
elif opção == 2:
    total = preço - (preço*5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print (f'Sua compra será parcela em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço*20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print (f'Sua compra será parcela em {totalparc}x de {parcela:.2f} \033[0;31mCOM JUROS\033[m')
else:
    total = preço
    print ('\033[4;31mOPÇÃO INVÁLIDA de pagamento, tente novamente.\033[m')
print (f'Sua compra de \033[0;32mR${preço:.2f}\033[m vai custar \033[0;32mR${total:.2f}\033[m no final.')