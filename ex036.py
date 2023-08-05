casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos de financiamento? '))
prestação = casa/(anos*12) # Prestação em meses
minimo = salario*30/100 # Porcentagem de 30%

print (f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestação:.2f}')

if prestação <= minimo:
    print ('Empréstimo pode ser CONCEDIDO')
else:
    print ('Empréstimo NEGADO')