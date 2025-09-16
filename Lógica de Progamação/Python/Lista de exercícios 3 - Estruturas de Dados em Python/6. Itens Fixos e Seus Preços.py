produtos = []

while True:
    nome = input("Digite o nome do produto (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        break

    try:
        preco = float(input(f"Digite o preço de '{nome}': R$ ").replace(",", "."))
        produtos.append((nome, preco))
    except ValueError:
        print("Preço inválido. Tente novamente.")

if produtos:
    mais_caro = max(produtos, key=lambda x: x[1])

    total = sum(preco for _, preco in produtos)

    produtos_ordenados = sorted(produtos, key=lambda x: x[1], reverse=True)

    print(f"\nProduto mais caro: {mais_caro[0]} (R$ {mais_caro[1]:.2f})")
    print(f"Total gasto: R$ {total:.2f}")

    print("\nLista de produtos (do mais caro ao mais barato):")
    for nome, preco in produtos_ordenados:
        print(f"- {nome}: R$ {preco:.2f}")
else:
    print("\nNenhum produto foi adicionado.")