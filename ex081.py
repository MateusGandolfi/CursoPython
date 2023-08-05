lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = ''
    if escolha in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'N':
            break
print ('-='*15)
print (f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print (f'Os valores digitados em ordem decrescente são {lista}')
if 5 in lista:
    print ('O valor 5 faz parte da lista!')
else:
    print ('O valor 5 não foi encontrado na lista!')
    