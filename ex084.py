temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1] #O MAIOR E O MENOR SERA A MESMA COISA QUE O PESO (OU SEJA TEMP[1])
    else:
        if temp[1] > mai: #SE O RESULTADO PESO FOR MAIOR DO QUE O MAIOR, ELE PASSA A SER O MAIOR
            mai = temp[1]
        if temp[1] < men: #SE O RESULTADO PESO FOR MENOR DO QUE O MENOR, ELE PASSA A SER O MENOR
            men = temp[1]
    princ.append(temp[:]) #COPIANDO A LISTA TEMPORARIA USANDO [:]
    temp.clear() #LIMPANDO A LISTA TEMPORARIA PARA QUE NAO OCORRA DUPLICAGEM
    escolha = ''
    if escolha in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha in 'N':
        break
     
print ('-='*20)
print (f'Você cadastrou ao todo {len(princ)} pessoas.') #USANDO LEN DA LISTA PRINC, JA IRA FAZER A CONTAGEM
print (f'O maior peso foi de {mai}KG. Peso de ', end='')
for p in princ: 
    if p[1] == mai: #SE O NOME DA PESSOA, FOR IGUAL A PESSOA COM O MAIOR PESO, IRA APARECE-LO
        print (f'[{p[0]}] ', end='')
print () #PRINT PARA NAO TER PULO DE LINHA
print (f'O menor peso foi de {men}KG. Peso de ', end ='') 
for p in princ: 
    if p[1] == men: #SE O NOME DA PESSOA, FOR IGUAL A PESSOA COM O MENOR PESO, IRA APARECE-LO
        print (f'[{p[0]}] ', end='')
print() #PRINT PARA NAO TER PULO DE LINHA
