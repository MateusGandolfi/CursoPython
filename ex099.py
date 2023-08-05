from time import sleep


def maior(*num):  # Funcao despacotamento, usando * pois nao especifica qual a quantidade de argumentos para a funcao def
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...')
    for valor in num:
        # Funcao flush e para nao ter buffering de tela no sleep
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:  # Maneira de achar o maior valor entre os numeros passados
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Programa Princiapl
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
