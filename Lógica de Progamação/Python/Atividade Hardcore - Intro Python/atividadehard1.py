nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
devendo = input("Você está devendo livros? (sim ou não): ").strip().lower()

if idade < 14:
    print("Cadastro negado: idade insuficiente.")
elif devendo == "sim":
    print("Cadastro negado: regularize sua dívida.")
elif len(nome) > 12:
    print("Cadastro negado: nome muito extenso.")
else:
    print(f"✅ Cadastro aprovado para {nome}!")
    if 14 <= idade <= 17:
        print("Cadastro de menor vinculado a um responsável.")