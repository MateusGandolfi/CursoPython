def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print ('\033[31mERRO! Por favor, digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print ('\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n
    
    
def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print ('\033[31mERRO! Por favor, digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print ('\033[31mUsuario preferiu nao digitar esse numero.\033[m.')
            return 0
        else:
            return n2
    
# Programa Principal
n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print (f'O valor Inteiro digitado foi {n1} e o real foi {n2}')