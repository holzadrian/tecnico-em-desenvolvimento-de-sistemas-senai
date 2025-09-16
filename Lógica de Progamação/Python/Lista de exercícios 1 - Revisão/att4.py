import random
numero = random.randint(1, 100)

print("Eu estou pensando em um número aleatório entree 1 e 100. Tente acertar!")

while True:
    palpite = int(input("Digite o seu palpite: "))
    
    if palpite < numero:
        print("O número é maior!")
    elif palpite > numero:
        print("O número é menor!")
    else:
        print(f"Parabéns! Você acertou o número {numero} ")