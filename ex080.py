lista = []
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #SE O NÚMERO FOR MAIOR QUE O ÚLTIMO, OU FOR O PRIMEIRO, SERÁ ADICIONADO
        lista.append(n)
        print ('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista): #SE A POSIÇÃO FOR MAIOR QUE A LISTA
            if n <= lista[pos]:
                lista.insert(pos, n)
                print (f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print ('-='*25)
print (f'Os valores digitados em ordem foram {lista}')

