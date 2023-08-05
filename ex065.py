soma = quant = maior = menor = 0 #TODOS RECEBEM 0
resp = 'S' #RESPOSTA = Ss

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor > num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #CONSIDERA APENAS A PRIMEIRA LETRA

print (f'Você digitou {quant} números e a média foi {soma/quant:.2f}')
print (f'O maior valor foi {maior} e o menor foi {menor}')