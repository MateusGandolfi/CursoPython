frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split() #FAZ UMA LISTA
junto = ''.join(palavras)
inverso = junto[::-1]
print (f'O inverso de {junto} é {inverso}')

if inverso == junto: 
    print ('A frase digitada é um palíndromo!')
else:
    print ('A frase digitada não é um palíndromo!')