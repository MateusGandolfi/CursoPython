def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (Opcional) Mostrar ou nao a conta por extenso
    :return: O valor do fatorial do numero escolhido
    """
    f = 1
    # Seguindo a logica de fatorial, seria o valor, ate o 0, pulando de -1
    # Ou seja, seria 5 x 4 x 3... Pulando sempre um a menos para tras
    for c in range(n, 0, -1):
        if show:  # Se o show for True, ele ira mostrar por extenso o Fatorial, nao somente o resultado
            print(c, end='')
            if c > 1:  # Se for maior que 1, ele ira aparecer multiplicando
                print(' x ', end='')
            else:  # Se for menor que 1, ele ira ser o valor final, ou seja ira dar um "="
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
num = int(input('Escreva um numero para ser fatorado: '))
print(fatorial(num, show=True))
ajuda = str(
    input('Deseja visualizar o help da funcao fatorial? [S/N] ')).upper()[0]
if ajuda == 'S':
    help(fatorial)
if ajuda == 'N':
    print('Programa finalizando... Volte sempre!')
