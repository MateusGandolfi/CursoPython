pessoa = {}
galera = []
soma = idade = 0

while True:
    pessoa.clear()  # IRA REMOVER AS INFORAMACOES NO DICIONARIO, POIS E UMA PESSOA NOVA
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    # ELE IRA COPIAR O DICIONARIO PESSOA PARA A LISTA GALERA
    galera.append(pessoa.copy())
    while True:
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if escolha == 'N':
        break
print('-='*20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
# A SOMA SERA TODAS AS IDADES, DIVIDO PELO TOTAL DE PESSOAS
media = soma / len(galera)
print(f'B) A media de idade e de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()  # PRINT VAZIO PARA QUEBRAR DE LINHA DEPOIS DO RESULTADO
print(f'D) Lista da pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():  # PARA CADA VALOR E CHAVE NO DICIONARIO P ACIMA, ELE IRA MOSTRAR AS INFORMACOES DA PESSOA
            print(f'{k} = {v}; ', end='')
        print()  # PRINT VAZIO PARA QUEBRAR DE LINHA DEPOIS DO RESULTADO
print('<< ENCERRADO >>')
