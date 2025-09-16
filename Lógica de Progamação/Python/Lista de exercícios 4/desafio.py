def main():
    filmes_por_pessoa = {}
    notas_por_genero = {}
    contagem_genero = {}
    filme_mais_bem_avaliado = {"filme": "", "nota": -1, "pessoa": "", "genero": ""}

    while True:
        pessoa = input("Nome da pessoa (ou 'fim' para encerrar): ").strip()
        if pessoa.lower() == "fim":
            break

        filme = input("Nome do filme: ").strip()
        genero = input("Gênero do filme: ").strip().lower()

        try:
            nota = float(input("Nota para o filme (0 a 10): "))
            if nota < 0 or nota > 10:
                print("A nota deve estar entre 0 e 10.")
                continue
        except ValueError:
            print("Nota inválida. Use um número de 0 a 10.")
            continue

        if pessoa not in filmes_por_pessoa:
            filmes_por_pessoa[pessoa] = []

        filmes_por_pessoa[pessoa].append({
            "filme": filme,
            "genero": genero,
            "nota": nota
        })

        if genero not in notas_por_genero:
            notas_por_genero[genero] = []
        notas_por_genero[genero].append(nota)

        contagem_genero[genero] = contagem_genero.get(genero, 0) + 1

        # Verificar filme com maior nota
        if nota > filme_mais_bem_avaliado["nota"]:
            filme_mais_bem_avaliado = {
                "filme": filme,
                "nota": nota,
                "pessoa": pessoa,
                "genero": genero
            }

    gerar_relatorio(filmes_por_pessoa, notas_por_genero, filme_mais_bem_avaliado)

def gerar_relatorio(filmes_por_pessoa, notas_por_genero, filme_mais_bem_avaliado):
    print("\nRelatório de Filmes Assistidos")

    for pessoa, filmes in filmes_por_pessoa.items():
        print(f"\n{pessoa} assistiu:")
        for f in filmes:
            print(f"  - {f['filme']} ({f['genero']}) - Nota: {f['nota']}")

    print("\nMédia de notas por gênero:")
    for genero, notas in notas_por_genero.items():
        media = sum(notas) / len(notas)
        print(f"  {genero.capitalize()}: {media:.2f}")

    top = filme_mais_bem_avaliado
    print(f"\nFilme mais bem avaliado: '{top['filme']}' ({top['genero']})")
    print(f"  Nota: {top['nota']} por {top['pessoa']}")

    pessoa_top = max(filmes_por_pessoa.items(), key=lambda item: len(item[1]))
    print(f"\nPessoa que assistiu mais filmes: {pessoa_top[0]} ({len(pessoa_top[1])} filmes)")

    total_generos = len(notas_por_genero)
    print(f"\nGêneros diferentes registrados: {total_generos}")


if __name__ == "__main__":
    main()
