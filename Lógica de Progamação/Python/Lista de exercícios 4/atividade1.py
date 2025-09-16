planetas = []

while True:
    planeta = input("Digite o nome do planeta visitado (ou 'parar' para encerrar): ").strip()
    if planeta.lower() == "parar":
        break
    planetas.append(planeta)

quantidade = len(planetas)
mais_longo = max(planetas, key=len) if planetas else ""
alfabetica = sorted(planetas)

print("\n--- Relatório da Missão ---")
print(f"Quantidade de planetas visitados: {quantidade}")
print(f"Planeta com o nome mais longo: {mais_longo}")
print(f"Lista em ordem alfabética: {', '.join(alfabetica)}")