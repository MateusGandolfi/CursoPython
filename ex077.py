palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print (f'\nNa palavra {p.upper()} temos as vogais: ',end ='') 
    for letra in p:
        if letra.lower() in 'aáãâeéêiíoóôuúû': #SE TIVER AS LETRAS NA PALAVRA IRÁ APARECER
            print (f'{letra},', end=' ')