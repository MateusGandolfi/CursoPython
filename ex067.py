while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print ('=-'*20)
    for c in range (1,11):
        print (f'{num} x {c:2} = {num*c}')
    print ('=-'*20)
print ('=-'*20)
print ('PROGRAMADA TABUADA ENCERRADO. Volte sempre!')



