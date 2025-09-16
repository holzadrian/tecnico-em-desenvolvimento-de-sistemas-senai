from collections import defaultdict

estoque = defaultdict(list)

while True:
    nome = input("Digite o nome do alimento (ou 'fim' para encerrar): ").strip()
    if nome.lower() == "fim":
        break

    categoria = input(f"Digite a categoria de '{nome}' (ex: legume, fruta, grão): ").strip().lower()
    
    try:
        quantidade = int(input(f"Digite a quantidade de '{nome}' em unidades: "))
        if quantidade < 0:
            raise ValueError
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro positivo.")
        continue

    estoque[categoria].append((nome, quantidade))

print("\n--- Estoque Agrupado por Categoria ---")
for categoria, alimentos in estoque.items():
    print(f"\nCategoria: {categoria.capitalize()}")
    for nome, quantidade in alimentos:
        print(f" - {nome}: {quantidade} unidades")

print("\n--- Total de Unidades por Categoria ---")
for categoria, alimentos in estoque.items():
    total = sum(qtd for _, qtd in alimentos)
    print(f"{categoria.capitalize()}: {total} unidades")

maior_alimento = None
maior_qtd = -1
for alimentos in estoque.values():
    for nome, qtd in alimentos:
        if qtd > maior_qtd:
            maior_alimento = nome
            maior_qtd = qtd

if maior_alimento:
    print(f"\nAlimento com maior quantidade: {maior_alimento} ({maior_qtd} unidades)")

print(f"\nTotal de categorias diferentes: {len(estoque)}")