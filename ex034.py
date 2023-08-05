salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    print (f'O salário de R${salario:.2f} com um aumento de 10% seria R${salario+(salario*10/100):.2f}')
else:
    print (f'O salário de R${salario:.2f} com um aumento de 15% seria R${salario+(salario*15/100):.2f}')