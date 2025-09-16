def contar_vogais(frase):
    vogais = 'AEIOUaeiou'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador
print(contar_vogais("Parabens emanuel"))