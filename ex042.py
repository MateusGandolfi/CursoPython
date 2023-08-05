a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if a < b + c and b < a + c and c < a + b:
    print ('Os segmentos acima PODEM FORMAR um triângulo ', end ='')
    if a == b == c:
        print ('EQUILÁTERO')
    elif a != b != c != a:
        print ('ESCALENO')
    else:
        print ('ISÓSCELES')
else:
    print ('Os segmentos acima NÃO PODEM FORMAR um triângulo')