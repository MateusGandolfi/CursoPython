from ex109 import moeda

p = float(input('Digite o preco: R$'))
# O moeda.moeda(p) seria para formatar usando R$ e ,00.
# O True na segunda parte do programa, segue a mesma formatacao da primeira, porem sem que fique repetindo varias vezes
# A moeda.moeda, sendo assim se voce colocar como "False" nao ira ter a formatacao de Real R$
print(f'A metade de {moeda.moeda(p)} e {(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} e {(moeda.dobro(p, True))}')
print(f'Aumentando 10%, temos {(moeda.aumentar(p, 10, True))}')
print(f'Reduzindo 13%, temos {(moeda.diminuir(p, 13, True))}')

