num = [[], []]
valor = 0

for c in range (1, 8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 == 0: #SE O VALOR FOR DIVISIVEL POR 2, OU SEJA SE FOR PAR, ELE IRA ADICIONAR NA PRIMEIRA LISTA DE NUM
        num[0].append(valor) #ADICIONA O VALOR NA LISTA 0
    else:
        num[1].append(valor) #ADICIONA O VALOR NA LISTA 1
print ('-='*20)
num[0].sort() #APENAS IRA ARRUMAR EM FORMA CRESCENTE A LISTA 0
num[1].sort() #APENAS IRA ARRUMAR EM FORMA CRESCENTE A LISTA 1
print (f'Os valores pares digitados foram: {num[0]}')
print (f'Os valores impares digitados foram: {num[1]}')
