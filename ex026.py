frase = str(input('Digite uma frase: ')).strip()
print (f'Sua frase possui {frase.lower().count("a")} letras A')
print (f'A letra A aparece primeiro na posição {frase.lower().find("a")+1}')
print (f'A letra A aparece por último na posição {frase.lower().rfind("a")+1}')