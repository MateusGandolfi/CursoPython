aluno = {}
boletim = []

aluno ['Nome'] = str(input('Nome: '))
aluno ['Media'] = float(input(f'Media de {aluno["Nome"]}: '))

if aluno['Media'] >= 7: #SE FOR MAIOR OU IGUAL A 7 ELE SERA APROVADO
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7: #SE O ALUNO FOR MAIOR OU IGUAL A 5 E MENOR QUE 7, ELE IRA FICAR EM RECUPERACAO
    aluno['Situacao'] = 'Recuperacao'
else: #SE FOR ABAIXO DE 5, ELE IRA SER REPROVADO
    aluno['Situacao'] = 'Reprovado'
print ('-='*15)
for k, v in aluno.items():
    print (f' - {k} e igual a {v}')
