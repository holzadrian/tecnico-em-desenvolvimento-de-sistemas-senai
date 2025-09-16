import random
tentativas = 0
num_secreto = random.randint(1, 100)
while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 100: "))
    tentativas += 1
    if palpite < num_secreto:
        print("O número secreto é maior!")
    elif palpite > num_secreto:
        print("O número secreto é menor!")
    else:
        print(f"\nParabéns! O número secreto era {num_secreto} e você acertou em {tentativas} tentativas. ")
        break