def validar_cpf(cpf):
    # Remove pontos e hífen
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    # Validação do primeiro dígito
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma1 * 10) % 11
    dig1 = 0 if dig1 == 10 else dig1
    # Validação do segundo dígito
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma2 * 10) % 11
    dig2 = 0 if dig2 == 10 else dig2
    return cpf[-2:] == f"{dig1}{dig2}"
print("Seja bem-vindo ao sistema de cadastro UNIMED.\n")
while True:
    val_nome = input("Digite seu nome: ")

    if val_nome.strip() == "":
        print("Erro: Insira um nome válido. Tente novamente.\n")
    elif val_nome != val_nome.strip():
        print("Erro: Não pode haver espaços no início ou no fim. Tente novamente.\n")
    else:
        nome = val_nome
        break
while True:
    val_email = input("Digite seu E-mail: ")

    if val_email.strip() == "":
        print("Erro: Insira um nome válido. Tente novamente.\n")
    elif not "@" in val_email or not "." in val_email:
        print("Erro: Insira um email válido. Tente novamente.\n")
    else:
        email = val_email
        break
while True:
    val_cpf = input("Digite seu CPF (apenas números ou com pontos e hífen): ")

    if validar_cpf(val_cpf):
        cpf = val_cpf
        break
    else:
        print("Erro: Isira um CPF válido. Tente novamente.\n")
print(f"cadastro finalizado com sucesso.\nNome: {nome}\nE-mail: {email}\nCPF: {cpf}")