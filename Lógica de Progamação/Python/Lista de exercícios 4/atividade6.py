def main():
    inventario = {}

    while True:
        nome_item = input("Item (ou 'fim' para encerrar): ").strip().lower()
        if nome_item == "fim":
            break

        regiao = input("Região onde foi encontrado: ").strip().lower()

        try:
            quantidade = int(input("Quantidade coletada: "))
        except ValueError:
            print("Entrada inválida. A quantidade deve ser um número inteiro.")
            continue

        if regiao not in inventario:
            inventario[regiao] = {}

        inventario[regiao][nome_item] = inventario[regiao].get(nome_item, 0) + quantidade

    gerar_relatorio(inventario)


def gerar_relatorio(inventario):
    print("\nRelatório de Itens Coletados")

    total_itens = 0
    regiao_com_mais_itens = None
    maior_total_por_regiao = 0

    for regiao, itens in inventario.items():
        print(f"\nRegião: {regiao.capitalize()}")
        total_na_regiao = 0

        for item, qtd in itens.items():
            print(f"  - {item}: {qtd}")
            total_na_regiao += qtd

        total_itens += total_na_regiao

        if total_na_regiao > maior_total_por_regiao:
            maior_total_por_regiao = total_na_regiao
            regiao_com_mais_itens = regiao

    print("\nResumo Geral")
    print(f"Total de itens coletados: {total_itens}")
    print(f"Região com mais itens: {regiao_com_mais_itens.capitalize()} ({maior_total_por_regiao} itens)")
    print(f"Regiões diferentes visitadas: {len(inventario)}")


if __name__ == "__main__":
    main()