def escreva(msg): #A definicao escreva, recebera a mensagem que for dado a ela
    tam = len(msg) + 4 #O tamanho ira ser o "len" da mensagem + 4, ou seja o tamanho total da mensagem com mais 4
    print ('-'*tam) 
    print (f'  {msg}') #Sera dado um print na mensagem, com mais 2 espacos para acompanhar as linhas
    print ('-'*tam)

# Programa Principal
escreva ('Mateus Gandolfi') #Mensagem dada para a definicao escreva
escreva ('Ola!')