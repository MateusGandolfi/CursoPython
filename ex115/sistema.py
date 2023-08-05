from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opcao de Listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opcao de Cdastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opcao de sair do programa.
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        # Digitou uma opcao errada no menu.
        print('\033[31mERRO! Digite uma opcao valida.\033[m')
    sleep(2)