totM20 = totH = tot18 = 0

while True:
    print ('-='*12)
    print ('  CADASTRE UMA PESSOA')
    print ('-='*12)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': #IRÁ REPETIR ATÉ QUE SEJA FEITO A ESCOLHA CERTA
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print ('-'*24)
    escolha = ' '
    while escolha not in 'SN': #IRÁ REPETIR ATÉ QUE SEJA FEITO A ESCOLHA CERTA
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if sexo == 'M': #SE FOR DO SEXO MASCULINO IRÁ CONTABILIZAR
            totH +=1
    if sexo == 'F' and idade < 20: #SE FOR MULHER E TER MENOS QUE 20 ANOS, IRÁ CONTABILIZAR
            totM20 +=1
    if idade >= 18: #SE IDADE FOR MAIOR QUE 18 ANOS IRÁ CONTABILIZAR
            tot18 += 1
    if escolha == 'N': #ESCOLHA DE PARADA
        break

print (f'Total de pessoa com mais de 18 anos: {tot18}')
print (f'Ao todo temos {totH} homens cadastrados.')
print (f'E temos {totM20} mulheres com menos de 20 anos')