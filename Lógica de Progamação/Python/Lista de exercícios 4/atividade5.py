itens = []

while True:
    entrada = input("Digite o nome do item e o preço (ou 'fechar' para encerrar): ").strip()
    
    if entrada.lower() == "fechar":
        break

    partes = entrada.rsplit(maxsplit=1)
    if len(partes) != 2 or not partes[1].isdigit():
        print("Formato inválido. Use: nome_do_item preço (ex: elmo 150)")
        continue

    nome, preco = partes[0], int(partes[1])
    itens.append((nome, preco))

if itens:
    mais_caro = max(itens, key=lambda x: x[1])
    total = sum(preco for _, preco in itens)
    ordenados = sorted(itens, key=lambda x: x[1])
else:
    mais_caro = ("", 0)
    total = 0
    ordenados = []

print("\n🧾 Registro de Vendas - Mercador de Itens")
print(f"💎 Item mais caro: {mais_caro[0]} ({mais_caro[1]} moedas)")
print(f"🪙 Total arrecadado: {total} moedas")
print("📦 Itens do mais barato ao mais caro:")
for nome, preco in ordenados:
    print(f"  - {nome}: {preco} moedas")
