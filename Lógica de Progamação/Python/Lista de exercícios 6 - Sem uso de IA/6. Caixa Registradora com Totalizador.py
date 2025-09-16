produtos = 0
total = 0
totala = 0
resposta = int(input("Digite quantos produtos você comprou: "))
for i in range(1, resposta + 1):
    produtos = float(input(f"Digite o preço do produto {i}: "))
    tipo = input("O produto é alimentício (1) ou outro tipo (2)? ")
    if tipo == "1":
        totala += produtos
    total += (produtos)
print(f"Total da compra: {total}")
print(f"Total do alimentícios: {totala}")
print(f"Total dos outros produtos: {total - totala}")