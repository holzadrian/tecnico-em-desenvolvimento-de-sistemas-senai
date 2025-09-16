def main():
    inventario = {}

    while True:
        nome_livro = input("Nome do livro (ou 'fim' para encerrar): ").strip()
        if nome_livro.lower() == "fim":
            break

        genero = input("Gênero do livro: ").strip().lower()

        try:
            quantidade = int(input("Quantidade disponível: "))
        except ValueError:
            print("Quantidade inválida. Use um número inteiro.")
            continue

        if genero not in inventario:
            inventario[genero] = {}

        inventario[genero][nome_livro] = inventario[genero].get(nome_livro, 0) + quantidade

    gerar_relatorio(inventario)


def gerar_relatorio(inventario):
    print("\nRelatório da Biblioteca")

    livro_mais_numeroso = None
    maior_quantidade = 0
    total_por_genero = {}

    for genero, livros in inventario.items():
        print(f"\nGênero: {genero.capitalize()}")
        total_genero = 0

        for livro, qtd in livros.items():
            print(f"  - {livro}: {qtd}")
            total_genero += qtd

            if qtd > maior_quantidade:
                maior_quantidade = qtd
                livro_mais_numeroso = (livro, genero)

        total_por_genero[genero] = total_genero

    print("\nResumo Geral")
    for genero, total in total_por_genero.items():
        print(f"Total de livros em {genero}: {total}")

    if livro_mais_numeroso:
        livro, genero = livro_mais_numeroso
        print(f"\nLivro com maior quantidade: '{livro}' ({maior_quantidade} unidades, gênero: {genero})")

    print(f"\nGêneros cadastrados: {len(inventario)}")


if __name__ == "__main__":
    main()