produtos = 0
total = 0
resposta = int(input("Digite quantos produtos você comprou: "))
for i in range(1, resposta + 1):
    produtos = float(input(f"Digite o preço do produto {i}: "))
    total += (produtos)
print(f"Total da compra: {total}")
if total > 150:
    print("Parabéns! Você ganhou um brinde!")