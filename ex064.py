num = cont = soma = 0 #DEFINE TODOS OS VALORES DA VARIAVEIS COMO 0

num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num #SOMA
    cont += 1 #CONTADOR
    num = int(input('Digite um número [999 para parar]: ')) #DESCONSIDERAÇÃO DO FLAG (999)
print (f'Você digitou {cont} números e a soma entre eles foi {soma}.')