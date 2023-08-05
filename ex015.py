dias = float(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodado? '))
print (f'O total a ser pago é de R${(dias*60) + (km*0.15):.2f}')