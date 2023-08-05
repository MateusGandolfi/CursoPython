from time import sleep


def contador(i, f, p):
    if p < 0:  # Se o passo for menor do que zero
        p *= -1  # Ele ira receber o passo x -1 para que fique um valor positivo
    if p == 0:  # Se o passo for zero, seguindo a logica, ele nao iria contar.
        p = 1  # Sendo assim, o passo ganhara o valor 1, pois nao ha como contar pulando de 0 em 0
    print('-='*20)
    print(f'Contagem de {i} ate {f}, de {p} em {p}')
    sleep(2)

    if i < f:  # Se o inicio, for maior que o final
        cont = i  # Contador comeca do inicio
        while cont <= f:  # Enquanto o contador, for MENOR que o final, ele ira dar um print
            # A funcao flush, ela e usada para nao dar um buffer de tela usando a funcao sleep
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)  # Dando uma pausa apos cada numero
            cont += p  # Como o inicio sera menor que o final, ele ira fazer mais
        print('FIM!')
    else:  # Caso nao seja o contador MENOR que o final, ele ira fazer o inverso
        cont = i  # Contador comeca do inicio
        while cont >= f:  # Enquanto o contador, for MAIOR que o final, ele ira dar um print
            # A funcao flush, ela e usada para nao dar um buffer de tela usando a funcao sleep
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)  # Dando uma pausa apos cada numero
            cont -= p  # Como o inicio sera maior que o final, ele ira fazer o inverso, por isso o menos
        print('FIM!')


# Programa Principal
contador(1, 10, 1)  # Contagem comecando no 1, ate o 10, de 1 em 1
contador(10, 0, 2)  # Contagem comecando no 10, ate o 0, de 2 em 2
print('-='*20)
print('Agora e a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
