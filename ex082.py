lista = [] #LISTA PRINCIPAL
pares = [] #LISTA DOS PARES
impares = [] #LISTA DOS IMPARES

while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = ''
    if escolha in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0: #ADICIONA PAR
        pares.append(v)
    else: #ADICIONAR IMPAR
        impares.append(v)
print ('-='*20)
print (f'A lista completa é {lista}')
print (f'A lista de pares é {pares}')
print (f'A lista de ímpares é {impares}')
