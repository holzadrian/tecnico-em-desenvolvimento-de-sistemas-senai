palavra = "senaizera"

letras_adivinhadas = []

while True:
    exibicao = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra
        else:
            exibicao += "_"
    print("Palavra: ", exibicao)

    if "_" not in exibicao:
        print("Parabéns! Você adinvinhou a palavra!")
        break

    palpite = input("Digite uma letra: ").lower()

    if palpite not in letras_adivinhadas:
        letras_adivinhadas.append(palpite)