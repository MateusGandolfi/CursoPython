sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper() [0] #Irá tirar os espaços, colocar em maiúsculo e pegar somente a primeira letra.

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper() [0]
    
print (f'Sexo {sexo} registrado com sucesso!')