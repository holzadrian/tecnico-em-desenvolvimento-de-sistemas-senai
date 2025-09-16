produtos_validos = []
total_compra = 0.0

print("Cadastro de produtos (digite 'sair' para encerrar)\n")

while True:
    nome = input("Digite o nome do produto: ").strip()
    
    if nome.lower() == "sair":
        break

    if nome == "":
        print("Erro: Insira um nome válido. Tente novamente.\n")
        continue

    while True:
        val_quant = input("Digite a quantidade: ")
        
        try:
            quantidade = int(val_quant)
            if quantidade > 0:
                break
            else:
                print("Erro: A quantidade deve ser maior que zero.\n")
        except ValueError:
            print("Erro: Digite um número inteiro válido.\n")

    while True:
        val_preco = input("Digite o preço (use ponto como separador decimal): ")
        
        try:
            preco = float(val_preco)
            if preco > 0:
                break
            else:
                print("Erro: O preço deve ser maior que zero.\n")
        except ValueError:
            print("Erro: Digite um número válido.\n")

    subtotal = quantidade * preco
    total_compra += subtotal

    produtos_validos.append({
        "nome": nome,
        "quantidade": quantidade,
        "preco": round(preco, 2),
        "subtotal": round(subtotal, 2)
    })

    print(f"Produto '{nome}' cadastrado com sucesso! Subtotal: R$ {subtotal:.2f}\n")

print("\nLista dos produtos cadastrados:")
for p in produtos_validos:
    print(f"- {p['nome']}: {p['quantidade']} x R$ {p['preco']:.2f} = R$ {p['subtotal']:.2f}")

print(f"\nTotal da compra: R$ {total_compra:.2f}")