colocação = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
            'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo', 
            'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 
            'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print (f'Lista de times: {colocação}') #MOSTRA A TUPLA
print ('-='*20)
print (f'Os 5 primeiros colocados são: {colocação[0:5]}') #VAI DO PRIMREIRO ATÉ O 5 (0 CONTA)
print ('-='*20)
print (f'Os 4 últimos colocados são: {colocação[-4:]}') #ACHA O 4 LUGAR DE TRÁS PRA FRENTE
print ('-='*20)
print (f'Os times em ordem alfabética é: {sorted(colocação)}') #ORDEM ALFABÉTICA DA TUPLA
print ('-='*20)
print (f'O time Chapecoense está na {colocação.index("Chapecoense")+1}° posição') #PROCURA A PALAVRA NA TUPLA