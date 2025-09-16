import random

def jogar():
    num_secreto = gerar_numero()
    palpite = 0
    while num_secreto != palpite:
        palpite = receber_palpite()
        verificar_palpite(num_secreto, palpite)    

def gerar_numero():
    return random.randint(1, 100)

def receber_palpite():
    return int(input("Qual é o número secreto? "))
    
def verificar_palpite(num_secreto, palpite):
    if palpite > num_secreto:
        print("O número secreto é menor!")
    elif palpite < num_secreto:
        print("O número secreto é maior!")
    else:
        print("Parabéns! Você acertou!")

jogar()