senha_correta = "4321"

tentativas = 3

for tentativa in range(1, tentativas + 1):
    senha = input(f"Tentativa {tentativa} - Digite a senha do cofre: ")

    if senha == senha_correta:
        print("Cofre aberto!")
        break
    else:
        print("Senha incorreta!")

else:
    print("Limite de tentativas atingido!")