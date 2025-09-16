
senha = input("Digite sua senha: ")

if len(senha) >= 8:
    
    senha_forte = False
    for caractere in senha:
        if caractere.isdigit():
            senha_forte = True
            break

    if senha_forte:
        print("Senha forte!")
    else:
        print("Senha fraca.")
else:
    print("Senha fraca.")
