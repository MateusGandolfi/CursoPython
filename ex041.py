from datetime import date

atual = date.today().year
nascimento = int(input('Digite o ano que você nasceu: '))
idade = atual-nascimento
print (f'O atleta tem {idade} anos em {atual}')

if idade <= 9:
    print ('Classificação: MIRIM')
elif idade <= 14:
    print ('Classificação: INFANTIL')
elif idade <= 19:
    print ('Classificação: JUNIOR')
elif idade <= 25:
    print ('Classificação: SÊNIOR')
else:
    print ('Classificação: MASTER')