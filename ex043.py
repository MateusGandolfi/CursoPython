peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso/(altura**2)

print (f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print ('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print ('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print ('Você está SOBREPESO!')
elif 30 <= imc < 40:
    print ('Você está em OBESIDADE!')
else:
    print ('Você está em OBESIDADE MÓRBIDA, cuidado!')

