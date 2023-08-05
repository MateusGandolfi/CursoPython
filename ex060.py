n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print (f'Calculando {n}! = ', end ='')

while c > 0:
    print (f'{c}', end ='')
    print (' x ' if c > 1 else ' = ', end ='')
    f *= c #Fatorial
    c -= 1 #Mostrando "1 x 2 x 3"
print (f'{f}')