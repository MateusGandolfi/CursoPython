def leiaInt(msg):
    ok = False  # Ok, comeca como falso
    valor = 0  # Valor comeca como 0
    while True:
        n = str(input(msg))
        if n.isnumeric():  # Se o numero passado for numerico
            valor = int(n)  # O valor ira ganhar o numero digitado
            ok = True  # Sendo assim, ele ira fazer uma verificacao e o ok ira ficar como verdadeiro, dizendo que esta certo
        else:  # Se nao for um numero inteiro, ira dar uma mensagem de erro
            print('\033[0;31mERRO! digite um numero inteiro valido.\033[m')
        if ok:  # Se estiver tudo certo, ou seja, o ok estiver True, ele ira parar a repeticao "while"
            break
    return valor  # E apos ser digitado um valor certo, ele ira voltar o valor, que seria o numero


# Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
