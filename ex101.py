def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA!'
    # Se a pessoa tiver maior de 16 anos, porem menor de 18 anos, o voto sera opcional
    # E se a pessoa tiver mais de 65 anos, tambem sera opcional, de acordo com as leis do Brasil
    elif idade <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'


# Programa Principal
nasc = int(input('Em qua ano voce nasceu? '))
print(voto(nasc))
