def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param n: Uma ou mais notas dos alunos (Aceita varias)
    :param sit: Valor opcional. Ele informa como esta a situacao do aluno de acordo com a media
    :return: Dicionario com varias informacoes sobre a situacao da turma
    """
    r = dict()
    # Len de N, seria o total de notas passados
    r['total'] = len(n)
    # Max de N, seria o maior valor dos numeros passados
    r['maior'] = max(n)
    # Min de N, seria o menor valor dos numeros passados
    r['menor'] = min(n)
    # Sum de N, dividido pelo Len de N, seria a soma de toda as notas, dividido pelo total de notas
    r['media'] = sum(n) / len(n)
    # Ira retornar o valor de r (O dicionario)
    if sit:  # Se a situacao for "False" ira mostrar a seguinte informacoes:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5, 3.7, 9, 4.5, sit=True)
print(resp)
