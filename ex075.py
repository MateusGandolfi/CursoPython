num = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')),) #TUPLA COM INPUT
print (f'Você digitou os valores: {num}')
print (f'O valor 9 apareceu {num.count(9)} vezes') #CONTA QUANTAS VEZES APARECE O VALOR 9 NA TUPLA
if 3 in num:
    print (f'O valor 3 apareceu {num.index(3)+1}° posição') #ACHA QUAL FOI A POSIÇÃO DO VALOR 3
else:
    print ('O valor 3 não foi digitado em nenhuma posição') #CASO NÃO TENHA O VALOR 3 IRÁ APARECER ESSA MENSAGEM
print (f'Os valores pares digitados foram ', end ='')
for n in num:
    if n % 2 == 0: #SE ALGUM VALOR FOR PAR, OU SEJA DIVISIVEL POR 2 IRÁ APARECER
        print (f'{n},', end=' ')