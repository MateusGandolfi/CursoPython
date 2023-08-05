def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        # Ira trocar todas as virgulas por ponto, fazendo com que seja possivel colocar virgulas na parte de centavos do preco
        # Com o strip ira tirar todos os espacos da mensagem, ja tratando erro.
        if entrada.isalpha() or entrada == '':
            # Se ele for alpha numerico, ou seja, haver numero e letra, ou apenas letra, ele nao sera valido
            # Se a entrada estiver vazia, ele tambem ira desconsiderar.
            print(f'\033[0;31mERRO! \"{entrada}\" e um preco invalido.\033[m')
        else:
            valido = True
            return float(entrada)


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