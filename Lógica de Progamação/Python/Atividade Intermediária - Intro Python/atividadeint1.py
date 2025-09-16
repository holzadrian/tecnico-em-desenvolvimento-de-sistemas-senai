senha_digitada = input("Digite a senha: ")

senha_correta = "Adrian123"

while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

    print("Acesso liberado!")