itens = []

while True:
    nome = input("Digite o nome de um item (ou 'fim' para encerrar): ").strip().lower()

    if nome == "fim":
        break

    posicao = input("Deseja adicionar no início ou no final? ").strip().lower()

    if posicao == "início" or posicao == "inicio":
        itens.insert(0, nome)
    elif posicao == "final":
        itens.append(nome)
    else:
        print("Posição inválida! Item não adicionado.")

print("\nEstrutura completa:")
print(itens)

if itens:
    print(f"\nPrimeiro item: {itens[0]}")
    print(f"Último item: {itens[-1]}")
else:
    print("\nNenhum item foi adicionado.")

print(f"\nTotal de itens adicionados: {len(itens)}")