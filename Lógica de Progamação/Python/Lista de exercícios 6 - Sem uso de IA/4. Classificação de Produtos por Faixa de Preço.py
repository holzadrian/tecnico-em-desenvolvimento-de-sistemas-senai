preços = 0
Barato = 0
Acessivel = 0 
Moderado = 0
Caro = 0
resposta = int(input("Digite quantos preços você deseja cadastrar: "))
for i in range(1, resposta + 1):
    preços = float(input(f"Digite o preço do produto {i}: "))
    if preços < 10:
        Barato += 1
    elif preços > 10 and preços < 30:
        Acessivel += 1
    elif preços > 30 and preços <60:
        Moderado += 1
    else:
        Caro += 1
print(f"\n{Barato} preços baratos")
print(f"{Acessivel} preços acessiveis")
print(f"{Moderado} preços moderados")
print(f"{Caro} preços caros")