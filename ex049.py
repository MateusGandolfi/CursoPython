n = int(input('Digite o número que deseja visualizar a tabuada: '))
print ('-='*7)
print (f'Tabuada do número {n}:')
for c in range (1,11):
    print (f'{n} x {c:2} = {n*c}')

print ('-='*7)
