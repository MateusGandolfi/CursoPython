ficha = []

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media]) 
    #LISTA COMPOSTA COM DADOS DO ALUNO (ALUNO [0] = NOME, ALUNO[1] = NOTAS, ALUNO[2] = MEDIA)
    escolha = ''
    if escolha in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break

print ('-='*11)
print (f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print ('-'*22)
for indice, aluno in enumerate(ficha):
    print (f'{indice:<3} {aluno[0]:<10} {aluno[2]:>7.1f}') 
    #INDICE INDICA NUMERO, ALUNO NA POSICAO 0 SERIA O NOME, E O ALUNO NA POSICAO 2 SERIA A MEDIA
while True:
    print ('-'*22)
    notas = int(input('Mostrar notas de qual aluno? (999 Interrompe) '))
    if notas == 999:
        print ('FINALIZANDO...')
        break
    if notas <= len(ficha)-1: #SE A NOTA FOR IGUAL OU MENOR QUE O TOTAL DE LISTA EM FICHAS-1, ELE IRÁ MOSTRAR A NOTA
        print (f'Notas de {ficha[notas][0]} sao {ficha[notas][1]}')
print ('<<<< VOLTE SEMPRE >>>>')
