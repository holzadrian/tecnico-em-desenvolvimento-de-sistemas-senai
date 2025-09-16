palavra_secreta = "programa"

letras_reveladas = palavra_secreta[0]

while True:
    palpite = input(f"Adivinhe a palavra: {letras_reveladas}_\n")

    if palpite == palavra_secreta:
        print("Você acertou a palavra! Parabéns!\n")
        break
    else:
        letras_reveladas = palavra_secreta[:len(letras_reveladas) + 1]
        print("Errou! Tentando novamente...\n")

    if letras_reveladas == palavra_secreta:
        print("Você errou! A palavra era: \n", palavra_secreta)
        break