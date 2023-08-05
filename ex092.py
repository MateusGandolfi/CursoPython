from datetime import datetime

cadastro = {}

cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 nao tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contrato'] = int(input('Ano de Contratacao: '))
    cadastro['Salario'] = float(input('Salario R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contrato'] + 35) - datetime.now().year 
    #IDADE + ANO DE CONTRATO+35 ANOS DE TRABALHO - O ANO ATUAL

print ('-='*15)
for k, v in cadastro.items():
    print (f'  - {k} tem o valor: {v}')