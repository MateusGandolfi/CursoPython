from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print (f'Os valores sorteados foram: ', end ='')
for n in num:
    print (f'{n}, ', end ='')
print (f'\nO maior valor sorteado foi {max(num)}') #MAIOR VALOR DENTRO DE UMA TUPLA
print (f'O menor valor sorteado foi {min(num)}') #MENOR VALOR DENTRO DE UMA TUPLA