viagem = float(input('Qual é a distância da sua viagem? '))
print (f'Você está prestes a começar uma viagem de {viagem:.0f}km')

if viagem < 200:
    print (f'O valor da sua passagem é de R${viagem*0.50:.2f}')
else:
    print (f'O valor da sua passagem é de R${viagem*0.45:.2f}')