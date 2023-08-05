expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: #SE A PILHA NÃO ESTIVER SEM NADA, IRÁ RETIRAR O ÚLTIMO
            pilha.pop()
        else: #SE A PILHA TIVER ALGO A MAIS, IRÁ CONSIDERAR O PARENTESES
            pilha.append(')')
            break
if len(pilha) == 0: #SE NÃO SOBRAR NENHUM PARENTESES, OU SEJA TODOS TEREM PARES, A EXPRESSÃO SERÁ CORRETA
    print ('Sua expressão está válida!')
else: #CASO SEJA MAIOR QUE 0, NÃO SERÁ UMA EXPRESSÃO VÁLIDA, POIS NEM TODOS PARENTESES TEM SEUS PARES
    print ('Sua expressão está incorreta!')