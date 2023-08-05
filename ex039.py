from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
idade = atual - nasc
print (f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade < 18:
    saldo = 18 - idade
    print (f'Ainda faltam {atual+saldo} anos para o alistamento')
    print (f'Seu alistamento será em {atual-saldo}')
elif idade > 18:
    saldo = idade - 18
    print (f'Você já deveria ter se alistado há {idade-18} anos!')
    print (f'Seu alistamento foi em {atual-saldo}')
elif idade == 18:
    print ('Você tem que se alistar IMEDIETAMENTE!')
