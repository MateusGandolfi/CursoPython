somaidade = 0 #A soma total para calcular média
maioridade = 0 #A idade do homem mais velho
nomevelho = '' #O nome do homem mais velho
totalmulher = 0 #Total de mulheres com menos de 20 anos

for p in range (1, 5):
    print (f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totalmulher += 1

print (f'A média de idade do grupo é de {somaidade/4} anos') #Média = idade/4 pessoas ao todo
print (f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}')
print (f'Ao todo são {totalmulher} mulheres com menos de 20 anos')