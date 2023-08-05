def area(l, c): #Definindo a funcao area com a largura e comprimento
    a = l * c #Calculando a largura * comprimento
    print (f'A area de um terreno {l}x{c} e de {a}m².') #Fazendo o calculo

#Programa Principal
print ('Controle de Terreno')
print ('-'*15)
largura = float(input('LARGURA (m): ')) #Valor dado de Largura
comprimento = float(input('COMPRIMENTO (m): ')) #Valor dado de Comprimento
area(largura, comprimento) #Eu adicionei dois valores para a definicao Area, logo ele ira sempre pedir no final esses 2 valores